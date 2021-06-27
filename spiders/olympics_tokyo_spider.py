import threading

from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver

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
        "cookie": '__gads=ID=7e28525a08005aa6:T=1621871299:S=ALNI_MZfjx2EW8yqsxEmelx4SPK7JLsg5A; _gcl_au=1.1.71240405.1621871303; gig_canary=false; ajs_anonymous_id="8055b1f8-96d5-4ac9-9f33-f30a7b94e0dc"; _scid=3505d351-a7da-4014-90d9-c259aaa2d9fa; _ga=GA1.2.1077322175.1621871303; _gid=GA1.2.1124115102.1621871305; _fbp=fb.1.1621871304662.1193155257; _sctr=1|1621785600000; gig_bootstrap_3_0-C5fmAFNYLmRECBReEdIiy3GrU6r29UMMqR5ej2AF3EiMrp2XiSJ-W3qWQ76Bsf=olympicid_ver4; gig_bootstrap_3_7WJn6CjEnxdOrHeLCAVMtjFPreS-UvLv4U1zutZ-XN5B70ESJDbRis9UIxFrk01w=_gigya_ver4; OptanonAlertBoxClosed=2021-05-24T16:04:32.519Z; gig_canary_ver=12088-3-27032610; _gat_segmentGATracker=1; glt_3_0-C5fmAFNYLmRECBReEdIiy3GrU6r29UMMqR5ej2AF3EiMrp2XiSJ-W3qWQ76Bsf=st2.s.AcbHzdm-Zg.rD95By5n5RAnhc8TN1kvjdMEcsYzYn6n9jBkRoyuboT7S6QIS8KqP5ksRlUHDOwjFy60bTMUtipIlk4GMgjs2u4jPqOiktoHkTZ_oD435Ac.huLWkGKCxGFT3fcZBUfABu-oMLzvvmPLEU9vrActtDcTS1uFielHyrNDtn3AtkpDxXg5QNzEcwidXOysdi0IYQ.sc3; ocsUserID=cc02fc036c2145389dd14a6d4c213b4e; ajs_user_id="cc02fc036c2145389dd14a6d4c213b4e"; RT="z=1&dm=olympics.com&si=9c38a2d7-56e5-4568-866f-8032899eb7b6&ss=kp49enbu&sl=1&tt=1xk&bcn=//684fc536.akstat.io/&ld=abq&ul=26je&hd=26mo"; ABTasty=uid=gryp2v0q0ejk649y&fst=1621871303478&pst=1621878849856&cst=1621960459822&ns=3&pvt=38&pvis=5&th=; ABTastySession=mrasn=&lp=https%3A%2F%2Folympics.com%2Fen%2F&sen=4; OptanonConsent=isIABGlobal=false&datestamp=Wed+May+26+2021+00:36:49+GMT+0800+(中国标准时间)&version=6.17.0&hosts=&consentId=adb0e663-ccbd-4c19-9ee5-c2aaff6c2e09&interactionCount=2&landingPath=NotLandingPage&groups=C0001:1,C0002:1,C0003:1,C0004:1,C0005:1&geolocation=HK;NST&AwaitingReconsent=false'.encode(
            "utf-8").decode("latin1")
    }
    return header


def start_crawl(file_path, keywords, start_time, end_time):
    keywords_str = "+".join(keywords)

    item_set = set()
    url = f"https://olympics.com/tokyo-2020/en/search/?q={keywords_str}"

    try:
        # 模拟浏览器登录
        options = webdriver.ChromeOptions()
        # 关闭可视化
        options.add_argument('--headless')
        # 关闭图片视频加载
        options.add_argument('blink-settings=imagesEnabled=false')
        driver = webdriver.Chrome(utils.DRIVER_PATH, options=options)
        driver.get(url)

        div = driver.find_element_by_xpath(
            "//body/main[@id='tk-main-content']/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]")
        soup = BeautifulSoup(div.get_attribute('innerHTML'), "html.parser")
    except Exception as exc:
        pass
    finally:
        driver.quit()

    # 添加发布时间和url
    search_result = soup.find_all("li", class_=re.compile("tk-cardsgroup"))
    if len(search_result) > 0:
        for li in search_result:
            article = entity.Article()
            a = li.find_next("a", href=re.compile("https://olympics.com/tokyo-2020/en/news/"))
            article.url = a.get("href")
            h3 = li.find_next("h3", class_="tk-card__title")
            article.title = h3.get("title")
            origin_date = li.find_next("time", class_="tk-card__pubdate").get("datetime")
            # 解析正文
            try:
                article.date = origin_date[0:11].replace("-", "")
                if int(start_time) <= int(article.date) <= int(end_time):
                    title, publish_date, content = utils.get_title_time_content(article.url, header=get_header())
                    article.text = content
                    article.text_cn = utils.translate(article.text)
                    time.sleep(1)
                    article.title_cn = utils.translate(article.title)
                else:
                    continue
            except Exception as exc:
                pass

            item_set.add(article)
    try:
        global TOTALS
        TOTALS += len(item_set)
        utils.write_xlsx_apend(file_path, item_set)
        item_set.clear()
    except Exception as exc:
        pass


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
        except Exception as exc:
            self._signal.emit(f"{self.name} failed end")

if __name__ == '__main__':
    keywords = ["Iran"]
    start_time = "20210608"
    end_time = "20210615"
    # 创建空Excel并写入表头
    utils.create_xlsx_with_head("./Tokyo.xlsx", sheet_name='+'.join(keywords))
    start_crawl("./Tokyo.xlsx", keywords=keywords, start_time=start_time, end_time=end_time)
