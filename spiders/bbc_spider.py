import requests
import re

from bs4 import BeautifulSoup
import time
import json
import jsonpath
import threading

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
        "cookie": 'ckns_explicit=0; ckns_policy=111; ckns_sylphid=7AK8ugF8WnglTzcfis4KjAjpIf3NmHWlpUug8q44i68; ckpf_sylphid=7AK8ugF8WnglTzcfis4KjAjpIf3NmHWlpUug8q44i68; ckns_nonce=8qLrRDSmTjplfS-UP25uLhdF; ckns_id=eyJhYiI6Im8xOCIsImVwIjp0cnVlLCJldiI6ZmFsc2UsInBsIjpmYWxzZSwicHMiOiJ1dlk4amdQTnFHNThhbHo1NlY5SFlqcDRoaFdnXzBKQTRVVDVZZ3EzekdVIiwiY2wiOmZhbHNlLCJjYyI6InNnIiwicmVhbG0iOiIvIiwic2VzLWV4cCI6MTYyNDc5ODEyMzAwMCwiand0LWV4cCI6MTY4Nzg2OTIyMzAwMCwicnRrbi1leHAiOjE2ODc4NjkyMjMwMDAsInRrbi1leHAiOjE2MjQ4MDA4MzAwMDB9; ckns_atkn=eyJ0eXAiOiJKV1QiLCJraWQiOiJFZ1VVKzhOaGFBWUtjNnlsb0NCcm5LUFRjZTg9IiwiYWxnIjoiRVMyNTYifQ.eyJzdWIiOiIwNDYzOTQ2NS1hOWUzLTQ4MGUtYTBkYi0xOGQyMDMwY2Q1NDMiLCJjdHMiOiJPQVVUSDJfU1RBVEVMRVNTX0dSQU5UIiwiYXV0aF9sZXZlbCI6MCwiYXVkaXRUcmFja2luZ0lkIjoiNzY3M2NlN2YtYzdiMS00ZDdmLWIzMzAtOTI3YWFiMTlhYzNmLTQ0NDA1NjY0IiwiaXNzIjoiaHR0cHM6Ly9hY2Nlc3MuYXBpLmJiYy5jb20vYmJjaWR2NS9vYXV0aDIiLCJ0b2tlbk5hbWUiOiJhY2Nlc3NfdG9rZW4iLCJ0b2tlbl90eXBlIjoiQmVhcmVyIiwiYXV0aEdyYW50SWQiOiI2NHJkM0puOEQ2SGRROU1rSzlFVDQzQjQySVkiLCJhdWQiOiJBY2NvdW50IiwibmJmIjoxNjI0Nzk3MjMwLCJncmFudF90eXBlIjoicmVmcmVzaF90b2tlbiIsInNjb3BlIjpbImV4cGxpY2l0IiwidWlkIiwiaW1wbGljaXQiLCJwaWkiLCJjb3JlIiwib3BlbmlkIl0sImF1dGhfdGltZSI6MTYyNDc5NzIyMywicmVhbG0iOiIvIiwiZXhwIjoxNjI0ODA0NDMwLCJpYXQiOjE2MjQ3OTcyMzAsImV4cGlyZXNfaW4iOjcyMDAsImp0aSI6ImE4Z1JqX2V4dERrYi1nQXQ2R2ZlTnN2cGtkayJ9.6k-MQBiCWQyfdVVduu8PqYtemS2yAIeYM2kPwO5dv1thJFoBzeZ9Zzyp3Pyd0R74vv7Kn62Ec7ZDPc9cNAZL9w; ckns_idtkn=eyJ0eXAiOiJKV1QiLCJraWQiOiJIa2d0WDBJd3RDOStSVGQvOWdYdFN0bk9VaU09IiwiYWxnIjoiUlMyNTYifQ.eyJhdF9oYXNoIjoiOC1oSXBMODBlYlluOHNzTTViR2ViUSIsInN1YiI6IjA0NjM5NDY1LWE5ZTMtNDgwZS1hMGRiLTE4ZDIwMzBjZDU0MyIsInVzZXJBdHRyaWJ1dGVzIjp7ImNjIjoic2ciLCJldiI6ZmFsc2UsImFiIjoibzE4IiwicHMiOiJ1dlk4amdQTnFHNThhbHo1NlY5SFlqcDRoaFdnXzBKQTRVVDVZZ3EzekdVIiwic3kiOiI3QUs4dWdGOFduZ2xUemNmaXM0S2pBanBJZjNObUhXbHBVdWc4cTQ0aTY4IiwiY2wiOmZhbHNlLCJlcCI6dHJ1ZSwicGwiOmZhbHNlfSwiYXVkaXRUcmFja2luZ0lkIjoiNzY3M2NlN2YtYzdiMS00ZDdmLWIzMzAtOTI3YWFiMTlhYzNmLTQ0NDA1NjY4IiwiaXNzIjoiaHR0cHM6Ly9hY2Nlc3MuYXBpLmJiYy5jb20vYmJjaWR2NS9vYXV0aDIiLCJ0b2tlbk5hbWUiOiJpZF90b2tlbiIsImF1ZCI6IkFjY291bnQiLCJhY3IiOiIwIiwiYXpwIjoiQWNjb3VudCIsImF1dGhfdGltZSI6MTYyNDc5NzIyMywicmVhbG0iOiIvIiwiZXhwIjoxNjI0ODA0NDMwLCJ0b2tlblR5cGUiOiJKV1RUb2tlbiIsImlhdCI6MTYyNDc5NzIzMH0.GDXbMZOFJU2KqQTc47dZKRITi4QvsMkyAC8p9PiRTpDjeTmDPtQbTknl21-J1XLnw_Br2DNGM5ptKxlkbZde9SD5tzpNN2Q9pq-EMLbrRX9nzIusMvBi_m4HM2uWXetVkHFIZXQPdwvtWq7EVlJrK2eST7yE8LES79q6aRkmhfktGS0-bU7nJMyrxIPH0cmu5w2FcsXUNdjHfF4GV4VmlOg3deMEzerj3SdrY0mCnaDewCQIQYUx9kV0q8bLJXUggaJBHMIKA7uFVSRvJgH2EUs1qy6d-x7PrNCDfoUpBY97-EiLnKyXGdSpb_3JCwyattRnVl_lFbw2Y2pNzfY_7A; atuserid={"name":"atuserid","val":"79e79765-f39c-4281-9011-a714843f1077","options":{"end":"2022-07-29T12:34:24.595Z","path":"/"}}'
    }
    return header


def start_crawl(file_path, keywords, start_time, end_time):
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

        for page in range(1, totals // 10):
            # 结果太多，限制条数
            if page == 10:
                break
            try:
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
                        # 8 hours ago
                        origin_date = utils.format_date(item["metadataStripItems"][0]["text"])

                        if origin_date != -1 and int(start_time) <= int(origin_date) <= int(end_time):
                            article = entity.Article()
                            article.title = item["headline"]

                            article.title_cn = utils.translate(article.title)
                            article.url = item["url"]
                            article.date = str(origin_date)
                            try:
                                time.sleep(1)
                                title, publish_date, content = utils.get_title_time_content(item["url"],
                                                                                            header=get_header())
                                article.text = content
                                article.text_cn = utils.translate(article.text)
                            except Exception as exc:
                                continue

                            item_set.add(article)
            except Exception as exc:
                continue
            finally:
                try:
                    global TOTALS
                    TOTALS += len(item_set)
                    utils.write_xlsx_apend(file_path, item_set)
                    item_set.clear()
                except:
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
        except:
            self._signal.emit(f"{self.name} failed end")


if __name__ == '__main__':
    keywords = ["G7"]
    start_time = "20210611"
    end_time = "20210618"
    # 创建空Excel并写入表头
    utils.create_xlsx_with_head("./BBC.xlsx", sheet_name='+'.join(keywords))
    start_crawl("./BBC.xlsx", keywords=keywords, start_time=start_time, end_time=end_time)
