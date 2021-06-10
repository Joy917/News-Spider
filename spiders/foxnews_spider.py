import threading
import requests
import json
import time
import newspaper as ns

import utils
import entity

TOTALS = 0


def get_header():
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "Connection": "close",
        "cookie": 'usprivacy=1---; _cb_ls=1; seerid=u_330862514524661950; ajs_anonymous_id=%226457ed39-e596-491b-a510-4b180a0381aa%22; _cb=DTIy5MCw4buyBU29lQ; AMCVS_17FC406C5357BA6E0A490D4D%40AdobeOrg=1; s_ecid=MCMID%7C56205972304140705244168792067879714233; s_cc=true; __gads=ID=d6ac16104eb12e3b:T=1618758268:S=ALNI_MZCI-86PCtn9ImKnKZQ-6nMscI4sQ; permutive-id=16dafeec-f928-4c74-aabd-2ce1479a9476; _csrf=sgVKrXMDlinVu-MHLXYPt9YW; _gcl_au=1.1.1620363967.1618762936; _ga=GA1.2.380611042.1618762938; FXN_flk=1; AKA_A2=A; _gid=GA1.2.1486152134.1619014627; seerses=e; AMCV_17FC406C5357BA6E0A490D4D%40AdobeOrg=2121618341%7CMCIDTS%7C18738%7CMCMID%7C56205972304140705244168792067879714233%7CMCAAMLH-1619363066%7C11%7CMCAAMB-1619619429%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1619021829s%7CNONE%7CMCAID%7CNONE; _cb_svref=https%3A%2F%2Fwww.foxnews.com%2Fsearch-results%2Fsearch%3Fq%3Dtokyo%2520china; CUID=N,1619014941848:ALHGLuQAAAAPTiwxNjE5MDE0OTQxODQ4L1Oz0pBeNqqQVkSL1e/u8LgfmKfAa1q+i5kJKHMaoppeMzYjmE5zzecM+cUsON1lxyeh3Bv9ka7o9dX3mn8FNFmyKHHchN21XBUWgOgyLoHSFmPOarc3GYzylbXhRvjT8A8z09acxS7OObGfgHQkSrM3f34FWotmxPo5vgOy0Aod31XME3Ka2h0coISmQR5jAiz7aEWSabcZcviqzfFBLN8dMRjWgYcH/eE+7RZO8qYQL+nUl6UNVp2Eol5T/Hsb+rGUIc2pv3lCfFSJLzyWGDYywhXDiaD+epGAeRbvXCiA6f7U0+IEPIhuUJn8I98TW4yOMP/eGynayW22vrgIVw==; _uetsid=5c190270a05711ebbcc28d72e2baac3e; _uetvid=5c194f10a05711eb8b51f95f366074d4; _Push_NotificationCount=3; s_sq=%5B%5BB%5D%5D; permutive-session=%7B%22session_id%22%3A%229b3c8a85-1a34-4744-949e-b8d35c2fd032%22%2C%22last_updated%22%3A%222021-04-21T14%3A22%3A54.236Z%22%7D; _chartbeat2=.1618758266169.1619014974289.1111.S5yvoCgOZtkDwonEzBFFkG-Bqju9c.4; _chartbeat5=; FCCDCF=[["AKsRol9Vt_Ve7NiQNY1yCOqdr-AUfBOEt2wzPka5iSkliap-EPeSIr2fQai6t5z1zgCBryVnULpfZEK2qyHPhWE0d9QjwOHiySIzevefvDb2ZjusQLynvkRONc_2BjLy_mPg1QHfMF--knA3HexdbznfDcLMry3-Rw=="],null,["[[],[],[],[],null,null,true]",1619014975076]]; s_pers=%20s_ppn%3Dfnc%253Aroot%253Aroot%253Achannel%7C1618764758408%3B%20s_prop45_cvp%3D%255B%255B%2527Other%252520Natural%252520Referrers%2527%252C%25271618941956000%2527%255D%255D%7C1776708355999%3B%20omtr_lv%3D1619014985750%7C1713622985750%3B%20omtr_lv_s%3DLess%2520than%25201%2520day%7C1619016785750%3B%20s_nr%3D1619014985755-Repeat%7C1621606985755%3B; s_sess=%20c_m%3Dundefinedlocalhost%253A8888Other%2520Natural%2520Referrersundefined%3B%20s_ppvl%3Dfnc%25253Asports%25253Afront%25253Achannel%252C8%252C18%252C1672.4000244140625%252C1536%252C722%252C1536%252C864%252C1.25%252CL%3B%20SC_LINKS%3D%3B%20s_ppv%3Dfnc%25253Asports%25253Asubsection%25253Aarticle%252C17%252C23%252C1122%252C1536%252C722%252C1536%252C864%252C1.25%252CL%3B; spotim_visitId={%22visitId%22:%22cf1cf09c-1480-4a23-9cae-8159dc9b38aa%22%2C%22creationDate%22:%222021-04-21T14:17:07.965Z%22%2C%22duration%22:394}; RT="z=1&dm=foxnews.com&si=4e1d5303-83ed-47a6-9615-1cb24dc0e3f7&ss=knrinhaq&sl=3&tt=1fyv&bcn=%2F%2F684d0d3b.akstat.io%2F&ld=10pvn&nu=69h6lopw&cl=11hbu&ul=13ezc"'
    }
    return header


def start_crawl(file_path, keywords, start_time, end_time):
    keywords_str = "%20".join(keywords)
    url = f"https://api.foxnews.com/search/web?q={keywords_str}+-filetype:amp+-filetype:xml+more:pagemap:metatags-prism.section+more:pagemap:metatags-pagetype:article+more:pagemap:metatags-dc.type:Text.Article&siteSearch=foxnews.com&siteSearchFilter=i&sort=date:r:{start_time}:{end_time}"

    r = requests.get(url=url, headers=get_header())
    data = json.loads(r.text)
    total_results = int(data["searchInformation"]["totalResults"])
    item_set = set()

    for start_index in range(1, total_results + 1, 10):
        time.sleep(2)
        url = f"https://api.foxnews.com/search/web?q={keywords}+-filetype:amp+-filetype:xml+more:pagemap:metatags-prism.section+more:pagemap:metatags-pagetype:article+more:pagemap:metatags-dc.type:Text.Article&siteSearch=foxnews.com&siteSearchFilter=i&sort=date:r:{start_time}:{end_time}&start={start_index}"
        try:
            r = requests.get(url=url, headers=get_header())
            data = json.loads(r.text)

            # 每次查询总数会波动
            total_results = int(data["searchInformation"]["totalResults"])
            if start_index > total_results:
                break

            for j in data["items"]:
                item = j["pagemap"]["metatags"][0]
                article = entity.Article()
                article.title = item["dc.title"]
                article.title_cn = utils.translate_with_webdriver(article.title)
                article.date = item["dc.date"]
                article.url = item["og:url"]
                item_set.add(article)
        except Exception as exc:
            continue

    global TOTALS
    TOTALS += len(item_set)
    # 解析链接对应正文
    for item in item_set:
        try:
            time.sleep(1)
            art = ns.Article(item.url, headers=get_header(), language='en')
            art.download()
            art.parse()
            item.text = art.text
            if art.text.strip() == "":
                title, publish_date, content = utils.get_title_time_content(item.url, header=get_header())
                item.text = content
            item.text_cn = utils.translate_with_webdriver(item.text)

        except Exception as exc:
            continue
        finally:
            utils.write_xlsx_apend(file_path, [item, ])


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
        # 创建空Excel并写入表头
        utils.create_xlsx_with_head(file_path=file_path, sheet_name='+'.join(self.keywords))
        start_crawl(file_path, self.keywords, self.start_time, self.end_time)
        end = time.time()
        print(f"{self.name} end, totals:{TOTALS}, used:{round((end - start) / 60, 2)} min")


if __name__ == '__main__':
    keywords = ["China", "Threat"]
    start_time = "20210525"
    end_time = "20210530"
    # 创建空Excel并写入表头
    utils.create_xlsx_with_head("./FoxNews.xlsx", sheet_name='+'.join(keywords))
    start_crawl("./FoxNews.xlsx", keywords=keywords, start_time=start_time, end_time=end_time)
