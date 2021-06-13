import threading

from bs4 import BeautifulSoup
import re
import time

import utils
import entity

TOTALS = 0


def get_header():
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "Connection": "close",
        "cookie": 'kppid=1a4aac943d4; has_js=1; _ga=GA1.2.2070443439.1621870819; _cb_ls=1; _cb=m_5H0BiRoPOB2AREW; _ntv_uid=3fc25902-f7b9-43c1-946d-ae954e9fecb3; __gads=ID=612340c38c6544d5:T=1621870819:S=ALNI_Mb3_tCo_FRQqwxu6qrFGkd2s5TS0A; ccpaUUID=dd3c619b-abd7-4f46-9c47-de11bb7d07c3; dnsDisplayed=true; ccpaApplies=false; signedLspa=false; ntv_as_us_privacy=1---; cuid=8d4cc250f5752790244f1621870826449_1624462826449; OB-USER-TOKEN=38deeaf5-c504-49c6-b6c3-29fcdec2feee; _pbjs_userid_consent_data=3524755945110770; _gid=GA1.2.168308596.1622039723; _cb_svref=null; FCCDCF=[["AKsRol-ZKv6t0etmo82AvoaLk6FwDVpokWNEqGYDvA2L75tLooCbsghZe48_jP6JwW7qPBK4rU4lQSnJR-eMnq4YBnx_aXRHxGvXN7-psMi0dcYtLf6V3EFzmG7MGGGsiq7W0WOK5r4IkHQGCEjwXRGJymbRm4Aqdg=="],null,["[[],[],[],[],null,null,true]",1622039970296]]; _gat=1; _chartbeat2=.1621870822200.1622040648167.101.BPo3cED3o9ufDVEs-9B1aCjJBDC-pN.8'
    }
    return header


def driver_url(driver, url):
    driver.get(url)

    result = driver.find_element_by_xpath("//body/div[@id='page']/div[@id='main']/div[@id='content']/ol[1]")
    soup = BeautifulSoup(result.get_attribute('innerHTML'), "html.parser")
    driver.quit()
    return soup


def start_crawl(file_path, keywords, start_time, end_time):
    keywords_str = "%20".join(keywords)

    driver = utils.get_webdriver()
    item_set = set()
    for page in range(0, 10):
        url = f"https://thehill.com/search/query/{keywords_str}?page={page}"

        try:
            soup = driver_url(driver, url)

            search_result = soup.find_all("li", class_=re.compile("search-result"))
            if search_result and len(search_result) > 0:
                # 筛选添加文章时间和url title
                for li in search_result:
                    origin_date = li.find_next("p", class_="date").string.strip()
                    date_list = origin_date.split("/")
                    date = date_list[2] + date_list[0] + date_list[1]
                    if int(date) < int(start_time):
                        return item_set
                    if int(date) > int(end_time):
                        continue
                    article = entity.Article()
                    a = li.find_next("h3", class_="title").find_next("a")
                    href = a.get("href")
                    if not href.startswith("https://thehill.com/"):
                        href = "https://thehill.com" + href
                    article.url = href
                    article.title = a.string
                    article.title_cn = utils.translate(article.title)
                    article.date = date
                    # 解析正文
                    try:
                        title, publish_date, content = utils.get_title_time_content(href, header=get_header())
                        article.text = content
                        article.text_cn = utils.translate(article.text)
                    except Exception as exc:
                        pass
                    time.sleep(1)
                    item_set.add(article)
            else:
                return item_set
        except:
            return item_set

        try:
            global TOTALS
            TOTALS += len(item_set)
            utils.write_xlsx_apend(file_path, item_set)
            item_set.clear()
        except:
            pass
    driver.quit()


def save_to_excel(file_path, keywords, item_set):
    # 写入数据
    utils.write_xlsx_apend(file_path, item_set)


class Task(threading.Thread):
    def __init__(self, thread_id, name, dir_name, keywords, start_time, end_time, signal):
        super().__init__()
        self.thread_id = thread_id
        self.name = name
        self.dir_name = dir_name
        self.keywords = keywords
        self.start_time = start_time
        self.end_time = end_time
        self._signal = signal

    def run(self):
        try:
            self._signal.emit(f"{self.name} start...")
            start = time.time()
            file_path = f"{self.dir_name}\\{utils.now_timestamp()}-{self.name}.xlsx"
            # 创建空Excel并写入表头
            utils.create_xlsx_with_head(file_path=file_path, sheet_name='+'.join(self.keywords))
            start_crawl(file_path, self.keywords, self.start_time, self.end_time)
            end = time.time()
            used_time = round((end - start) / 60, 2)
            msg = f"{self.name} end, totals:{TOTALS}, used:{used_time} min"
            self._signal.emit(msg)
        except:
            self._signal.emit(f"{self.name} failed end")

if __name__ == '__main__':
    keywords = ["China", "Threat"]
    start_time = "20210525"
    end_time = "20210530"
    # 创建空Excel并写入表头
    utils.create_xlsx_with_head("./TheHill.xlsx", sheet_name='+'.join(keywords))
    item_set = start_crawl("./TheHill.xlsx", keywords=keywords, start_time=start_time, end_time=end_time)
