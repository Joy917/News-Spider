import threading
from bs4 import BeautifulSoup
import re
import newspaper as ns
import time
from selenium import webdriver

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
        "cookie": '_cb_ls=1; usprivacy=1---; s_fid=696C2FAB5043EE96-2EB78ACFE9AE76FC; SC_LINKS=[[B]]; s_cc=true; _cb=B_t9i8CAp7ByCMnm3y; s_vi=[CS]v1|3055E4BA6FA68F41-6000115869ACE9F4[CE]; _cc_id=bad2759b871e3575129d1e6f49a5a158; __pnahc=0; __tbc={jzx}df5WN6cFCXceUHuwuzcALWDCEgSRtviJHWaf8vlAfItUASDh-DaN01MvIp7JMWCNGjkG1OuLTdqF_JwUEBRERFEQAeMsGStbFfezI80niHrmTuee3To_qXRse2Bm93d6oYpVQBcykV0CdrNa7odWZg; __pat=-14400000; _fbp=fb.1.1621870970119.1138196144; __gads=ID=95c6b99edebda9c6:T=1621870966:S=ALNI_MaMxQN3JY3MpZI0ogwP9WbnbGG4pw; __qca=P0-15818413-1621870967902; _mkto_trk=id:966-KHF-533&token:_mch-politico.com-1621870998344-23356; _t_tests=eyJUTDJMcDNMZDNwOThkIjp7ImNob3NlblZhcmlhbnQiOiJBIiwic3BlY2lmaWNMb2NhdGlvbiI6WyJCTkwybkkiXX0sInV1ZzJpTFJvb1ZqTlMiOnsiY2hvc2VuVmFyaWFudCI6IkEiLCJzcGVjaWZpY0xvY2F0aW9uIjpbIkNVX1pKXyJdfSwiSkEzemZxWkFwTXJ4WiI6eyJjaG9zZW5WYXJpYW50IjoiQiIsInNwZWNpZmljTG9jYXRpb24iOlsiQnZrcmJMIl19LCJNaHVsb2l3MlQwMDF0Ijp7ImNob3NlblZhcmlhbnQiOiJBIiwic3BlY2lmaWNMb2NhdGlvbiI6WyJEd0RIWGsiXX0sIjdBdWxBUFRWVXo3TEEiOnsiY2hvc2VuVmFyaWFudCI6IkEiLCJzcGVjaWZpY0xvY2F0aW9uIjpbIkNkNjlZWCJdfSwid0FDRjEyUDF4VnJQdiI6eyJjaG9zZW5WYXJpYW50IjoiQSIsInNwZWNpZmljTG9jYXRpb24iOlsiQ0RseTlyIl19LCJsaWZ0X2V4cCI6Im0ifQ==; utag_invisit=true; utag_vnum=1624462967247&vn=2; _cb_svref=null; utag_dslv_s=Less than 1 day; siteUser=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyMWNlMGQ2OS0yYTZkLTQwMmUtOTVhOC0yZTlkYWMxMTI3OGIiLCJhdWQiOlsibGlzdC5jcnVkIiwic3Vic2NyaXB0aW9uLmNydSIsInN1YnNjcmliZXIuciIsInVzZXItZXZlbnRzLnIiLCJhY2NvdW50LnIiLCJ1c2VyX2dyb3VwLmNydWQiLCJ1c2VyX3ZhbHVlLmNydWQiLCJ0b3BpYy5yIiwiZmF2b3JpdGUuY3J1ZCIsImVudGl0bGVtZW50LnIiLCJmZWF0dXJlLnIiLCJub3RlLmNydWQiLCJhY2NvdW50X21hbmFnZXIuciIsInNhdmVkX3NlYXJjaC5jcnVkIiwiLnVzZXItYXV0aCIsInVzZXIucnUiLCJub3RpZmljYXRpb24uY3J1Il0sInBvbGl0aWNvLmVudiI6InByb2QiLCJpc3MiOiJjaGllZiIsImV4cCI6MTYyMjA1NjI0OSwiaWF0IjoxNjIyMDUyNjQ5LCJhaWQiOiJwb2xpdGljb2JzcC1wcm9kIiwianRpIjoiS3ByOEo3U054SVoxSTd5MU9SZXdfZE9CeDNjIiwidXNlcm5hbWUiOiJwZWFjZWJpcmR0aEBnbWFpbC5jb20ifQ.J5PhBf-wKgnOcEE3rW5ga5hpywj40PWYirQrfN0NvTdC5oXihd0mfFYwSL__hYH7_djuqT7CI7bHV1bFB99gMihxVY0LwERnCqxEJTJ18Ty8qGGuBxLW6ub-zFTHBazLElsCKgvqlZMVmYGyHW9QwqseJsHMt5MS7kearPsJ0C7oXNT7GwSVrfs7D9XwMMazCCbNpJJU2qcLApTK-jmCwVGQ460uU6wNygVWbVfA_0GXzmYdGBxP6k0tsnnI3-GFvRDRKj4fy5Ez5Z0FDQbQ8LciMIrW-X1-jweXkZpqcmBjHXMrIMaqBYYvSNM1SY9mhhdC7EWqPo4pdp-nKIz0Aw; kli=1; _cp_pt=site search; s_sq=[[B]]; utag_vs=28; utag_dslv=1622053664869; utag_main=v_id:01799f0af9c60013ee61b78b2adb03073001906b00978$_sn:2$_se:23$_ss:0$_st:1622055464860$dc_visit:2$ses_id:1622052538567;exp-session$_pn:21;exp-session$_prevpage:site search advanced;exp-1622057264866$as_event_flag:true;exp-session$dc_event:23;exp-session$dc_region:ap-east-1;exp-session; _chartbeat2=.1621870967399.1622053665171.1001.CCTRoQD7CRFUCf812ecXBYMpEiKh.21; OptanonConsent=isIABGlobal=false&datestamp=Thu+May+27+2021+02:27:45+GMT+0800+(中国标准时间)&version=6.15.0&hosts=&consentId=f0564b44-02ae-45a8-b70b-c86b71949303&interactionCount=1&landingPath=NotLandingPage&groups=C0001:1,C0003:1,C0002:1,BG1:1,C0004:1&AwaitingReconsent=false&geolocation=HK;NST; OptanonAlertBoxClosed=2021-05-26T18:27:45.261Z; __pvi={"id":"v-2021-05-27-02-09-00-983-3JFSY4SUSEqIbDeG-7f1a336155544699f6b69977b3fe2253","domain":".politico.com","time":1622053665362}; nol_fpid=ybllh8pnjqyqqhooomp6jd1nf2w5d1621870970|1621870970227|1622053665450|1622053665771; xbc={jzx}5F6N26ucJ0bAs8zICVa3USOY83-TxUnfRr_SR_EGiXdriih_8u-mjWrHdn0C2Ko7Z0qDUX89BIi_Yt6P4of6WCG_KQgEoxXAgoSTnTQXrLYQ2m3xfluSCzxS2QBSw_Ubs0y9AJS_DlU2hydzSkYtiP9vUCmf1IjOlljJ93kGMLJXnHxo9KITBKok9M9FNF5kV0r-SuToq_RklCJnuolvGg; __atuvc=18|21; __atuvs=60ae8f33215dc35500f'
    }
    return header


def driver_url(url):
    # 模拟浏览器登录
    options = webdriver.ChromeOptions()
    # 关闭可视化
    options.add_argument('--headless')
    # 关闭图片视频加载
    options.add_argument('blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(r'D:\projects\Spider\chromedriver.exe', options=options)
    driver.get(url)

    result = driver.find_element_by_xpath(
        "//body/div[@id='globalWrapper']/main[@id='main']/div[2]/div[1]/div[1]/section[1]/div[3]")
    soup = BeautifulSoup(result.get_attribute('innerHTML'), "html.parser")
    driver.quit()
    return soup


def start_crawl(keywords, start_time, end_time):
    keywords_str = "+".join(keywords)
    start_date = start_time[4: 6] + "%2F" + start_time[6: 8] + "%2F" + start_time[0: 4]
    end_date = end_time[4: 6] + "%2F" + end_time[6: 8] + "%2F" + end_time[0: 4]

    item_set = set()
    url = f"https://www.politico.com/search?adv=true&userInitiated=true&s=newest&q={keywords_str}&start={start_date}&end={end_date}"

    try:
        soup = driver_url(url)

        search_result = soup.find_all("article", class_=re.compile("story-frag"))
        if search_result and len(search_result) > 0:
            for li in search_result:
                article = entity.Article()
                a = li.find_next("header").find_next("a")
                article.url = a.get("href")
                article.title = a.string
                article.title_cn = utils.translate_with_webdriver(article.title)
                article.date = li.find_next("time").get("datetime").split("T")[0].replace("-", "")
                # 解析正文
                try:
                    art = ns.Article(article.url, headers=get_header(), language='en')
                    art.download()
                    art.parse()
                    article.text = art.text
                    article.text_cn = utils.translate_with_webdriver(article.text)
                except Exception as exc:
                    pass
                time.sleep(1)
                item_set.add(article)
        else:
            return item_set
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
    keywords = ["tokyo"]
    start_time = "20210501"
    end_time = "20210527"
    item_set = start_crawl(keywords=keywords, start_time=start_time, end_time=end_time)
    print(f"total crawl number:{len(item_set)}")
