import requests
import re
from bs4 import BeautifulSoup
import newspaper as ns
import time
import json
import jsonpath
import threading

import entity
import utils


def get_header():
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "Connection": "close",
        "cookie": '_cb_ls=1; _cb=CzO6DqKp_6bBXBaTU; ckns_explicit=0; ckns_policy=111; ckns_policy_exp=1652201145357; BBC-UID=8680d9e906b3967fc6e71e58918b9787999571467030e580e5b63846f9808b2f0Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36; _chartbeat2=.1620577822052.1621349966926.100000011.B33yPjYq-pEDm0OlpC7i1RQDBEvQi.1; _cb_svref=https://www.bbc.com/; atuserid={"name":"atuserid","val":"79e79765-f39c-4281-9011-a714843f1077","options":{"end":"2022-06-19T14:59:26.958Z","path":"/"}}'
    }
    return header


def start_crawl(keywords, start_time, end_time):
    keywords_str = "+".join(keywords)
    item_set = set()

    url = f"https://www.bbc.co.uk/search?q={keywords_str}&page=1"
    r = requests.get(url=url, headers=get_header())

    html_content = r.text
    soup = BeautifulSoup(html_content, "html.parser")
    match = re.search(">window.__INITIAL_DATA__=(.+);</script>", str(soup.find_all("script")[3]))
    if match:
        data = json.loads(match[1])
        initial_results = jsonpath.jsonpath(data, "$..initialResults")[0]
        totals = initial_results["count"]

        try:
            for page in range(1, totals // 10):
                time.sleep(1)
                url = f"https://www.bbc.co.uk/search?q={keywords_str}&page={page}"
                r = requests.get(url=url, headers=get_header())

                html_content = r.text
                soup = BeautifulSoup(html_content, "html.parser")
                match = re.search(">window.__INITIAL_DATA__=(.+);</script>", str(soup.find_all("script")[3]))
                if match:
                    data = json.loads(match[1])
                    initial_results = jsonpath.jsonpath(data, "$..initialResults")[0]
                    for item in initial_results["items"]:
                        # 17 April 2017
                        origin_date = utils.format_date(item["metadataStripItems"][0]["text"])

                        if origin_date != -1 and int(start_time) <= origin_date <= int(end_time):
                            article = entity.Article()
                            article.title = item["headline"]
                            article.title_cn = utils.translate_with_webdriver(article.title)
                            article.url = item["url"]
                            article.date = str(origin_date)
                            try:
                                time.sleep(1)
                                art = ns.Article(item["url"], headers=get_header())
                                art.download()
                                art.parse()
                                article.text = art.text
                                article.text_cn = utils.translate_with_webdriver(article.text)
                            except Exception as exc:
                                # logging.exception(exc)
                                continue

                            item_set.add(article)
        except:
            return item_set

    return item_set


def save_to_excel(file_path, keywords, item_set):
    # 创建空Excel并写入表头
    utils.create_xlsx_with_head(file_path=file_path, sheet_name='+'.join(keywords))
    # 写入数据
    utils.write_xlsx_apend(file_path, item_set)


class Task(threading.Thread):
    def __init__(self, thread_id, name, dir_name, keywords, start_time, end_time):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.dir_name = dir_name
        self.keywords = keywords
        self.start_time = start_time
        self.end_time = end_time

    def run(self):
        print(f"{self.name} start...")
        start = time.time()
        file_path = f"{self.dir_name}\\{utils.now_timestamp()}-{self.name}.xlsx"
        item_set = start_crawl(self.keywords, self.start_time, self.end_time)
        save_to_excel(file_path, self.keywords, item_set)
        end = time.time()
        print(f"{self.name} end, totals:{len(item_set)}, used:{round((end - start) / 60, 2)} min")


if __name__ == '__main__':
    keywords = ["tokyo", "china"]
    start_time = "20210301"
    end_time = "20210312"
    item_set = start_crawl(keywords=keywords, start_time=start_time, end_time=end_time)
    print(f"total crawl number:{len(item_set)}")
