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
        "cookie": "wsjregion=na,us; gdprApplies=false; ab_uuid=637c98ca-f18f-4518-a47a-9518c59f567d; usr_bkt=ixi4E5ylqa; cX_P=kngcgf1o240dcpev; cX_S=kngcgf1zy97m3k1z; _sp_v1_csv=null; _sp_v1_opt=1:; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbLKK83J0YlRSkVil4AlqmtrlXSoqiwWACMYp9h2AAAA; _sp_v1_uid=1:798:1c2fe67d-ec2d-4dce-92aa-260e10d09019; _sp_v1_lt=1:; djvideovol=1; __gads=ID=9b4582df3b958aab:T=1618337659:S=ALNI_MY_oTx3ymoSrklLAMySQBZT_hvyUA; MicrosoftApplicationsTelemetryDeviceId=6973b8e1-34df-3a2e-cb4c-58e2fa8d98e9; MicrosoftApplicationsTelemetryFirstLaunchTime=1618337660216; cX_G=cx:pgvu3625bth816cyzb3jwhgfb:2kehjb05hoy9x; AMCVS_CB68E4BA55144CAA0A4C98A5@AdobeOrg=1; s_cc=true; _ncg_id_=b22bcf7f-11af-4eae-8bcf-7c73b63884fe; _li_dcdm_c=.wsj.com; _lc2_fpi=7880a1137012--01f3672xf29pq93a2pckahezsz; _fbp=fb.1.1618337698060.946935606; OB-USER-TOKEN=38deeaf5-c504-49c6-b6c3-29fcdec2feee; has_optimizely=true; optimizelyEndUserId=oeu1618337800998r0.08981723274843434; _ncg_g_id_=375d10e9-f063-4931-a6bd-157af07bab41; ki_r=; ResponsiveConditional_initialBreakpoint=lg; djcs_route=ace07236-6631-4caa-a2af-bc35c3dde732; djcs_secid=YzMyYmZjMjktNzJkZS00ZTgyLTk3ZGUtZTMzNjk2ZTk4ZTBm.J8opVMp2kS5CFQ1aye74_GsiHcLQlvIpJF2q-Rsqqos; TR=V2-15e14b982a648ef519cac5532c476bbe86c3fa51ee3e8e779209bd9a8ba7661c; _ntv_uid=3fc25902-f7b9-43c1-946d-ae954e9fecb3; djcs_auto=M1619298224/92y758qyl9S5yL+w/zUpcoVPq+SwXHskzdk6Avf+rkF/16poPfyMUQ+d/6a+N1hQSdtN2E3xSLLLcUIgBMmGwwXn4qpuYKnDrMnjt+tRS48VCQ7nwwt63ApQtUbURrt17u6qyifUJkabLdfABwSl/ZnpNDEA+WteEH8vU+nPgu8L/2ogvUmzULCfzbdJpva92oJqCSXnVhbTPVCRhk3o0KR+wbhXCbB/QLd2p9tXbHu4E1dlR5t+bKrQYIdHqc6KCH+hpTeJPMaadLZI+7Rn5x9t9ZLN+wZqVJjB3awX6ijrL5yzDPEpmsD80GLFeQ3qHPzb0PzhMRn6TYaL1LoOIakixHK+3BgOkkB8B69Ky++I2bem2KtQ3W90LuIlq48DpBaxwpsbr45WA8mrzwAhdw==G; djcs_session=M1619369028/r8AE2KH/yGew+uyw5V82gC2r9D6LLNpD6s0YVL3nIfChLTquAS58c4cJHExzxcyQUHK3R67k85M8eEI8N0cW/wGyzhvJgD/g2zegO7lpfHrVYCZo3lHTFFxcJ1mxYswNrgHHwBvYRww0kvjB2m71I7hNDJvWOdoNKwE7d1SzI2nb0w7tguQYp7H1/o/tw5QHNdEkNryXJovKm1nwX9AYz062flCm/AZmgsC5ZS7XomfINK908SkNGNaUZtw29nzi+giiXdOu1vbc2n19M+z1Ybd5r2TEHyEUX4+h2O+BvN3iUebi9U5G/KpEHtgGTEmcUhO80kmubdFZFAnFVcyfcjyAhjIc3SRgMCXGI9WPBLU4hy0/3ZPc27SRVnAZvP7S+UTx75s/kDGXAM96KDc+64CxMWHmG7HFcDMfSar3hkuuKwem5zvoNFgTJ5N5S6V4LgTabhiZv3bau8WBWb83jZtIaItOqiYETDAuZq1Vf+tFK6cPV043mX0hTGsAjW33G; usr_prof_v2=eyJwIjp7InBzIjowLjksInEiOjAuODF9LCJjcCI6eyJlYyI6IlN0YWJsZSIsInBjIjowLjQ1NDg0LCJwc3IiOjAuMjE5OTEsInRkIjo0MCwiYWQiOjQsInFjIjo5OSwicW8iOjk5LCJzY2VuIjp7ImNoZSI6MC4zMDU3OCwiY2huIjowLjQ4MDk4LCJjaGEiOjAuMjk5MTgsImNocCI6MC40MzE3OH19LCJpYyI6NX0=; AMCV_CB68E4BA55144CAA0A4C98A5@AdobeOrg=1585540135|MCIDTS|18743|MCMID|20248205616545994651665923179814411163|MCAID|NONE|MCOPTOUT-1619378526s|NONE|MCAAMLH-1619976126|11|MCAAMB-1619976126|j8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI|vVersion|4.4.0; DJSESSION=country=us||continent=na||region=ca||city=sanjose||latitude=37.3435||longitude=-121.8887||timezone=pst||zip=95101+95103+95106+95108-95113+95115-95136+95138-95139+95141+95148+95150-95161+95164+95170+95172-95173+95190-95194+95196; ccpaApplies=true; hok_seg=8ljs5iat1cy0,8m5oogcu3a7n; _am_sp_djcsses.1fc3=*; _scid=8e41a298-cd35-440c-b4f9-e613b3dc2ef5; ki_t=1618337814635;1619372253677;1619372283386;4;11; _sp_v1_data=2:306234:1618337657:0:41:0:41:0:0:_:-1; consentUUID=146ea439-5cc1-4b68-8ea1-145f00505ec9; utag_main=v_id:0178cc71527b000370d00be3349a03073001406b00978$_sn:6$_se:5$_ss:0$_st:1619375623302$vapi_domain:wsj.com$ses_id:1619372257684;exp-session$_pn:5;exp-session$_prevpage:;exp-1619377423313; _ncg_sp_ses.5378=*; _ncg_sp_id.5378=b22bcf7f-11af-4eae-8bcf-7c73b63884fe.1618337685.6.1619373826.1618763125.bd148ec8-8f46-4a16-9793-f43e19e763e9; _rdt_uuid=1619373826336.cd4d2f89-300c-44c7-82e2-85aaa7139d29; _tq_id.TV-63639009-1.1fc3=a06c2662c213de7e.1619373827.0.1619373827..; _sctr=1|1619366400000; s_tp=2942; s_ppv=https%3A//www.wsj.com/search%3Fquery%3Dtokyo%2520china%26isToggleOn%3Dtrue%26operator%3DAND%26sort%3Ddate-desc%26duration%3D1y%26startDate%3D2021%252F04%252F01%26endDate%3D2021%252F04%252F10%26source%3Dwsjie%252Cblog%252Cwsjsitesrch%252Cwsjpro%252Cautowire%252Capfeed,25,25,722; _am_sp_djcsid.1fc3=7fc4b535-a670-457d-95df-8430916f26b4.1618337684.6.1619374065.1618764703.b86d3273-218a-419c-98c7-d0338fe3bd99"
    }
    return header


def get_driver_with_login():
    driver = None
    for i in range(3):
        try:
            # 模拟浏览器登录
            options = webdriver.ChromeOptions()
            # 关闭可视化
            options.add_argument('--headless')
            # 关闭图片视频加载
            options.add_argument('blink-settings=imagesEnabled=false')
            driver = webdriver.Chrome(utils.DRIVER_PATH, options=options)
            login_url = "https://accounts.wsj.com/login?target=https%3A%2F%2Fwww.wsj.com%2F"
            driver.get(login_url)
            driver.find_element_by_id("username").send_keys("peacebirdth@gmail.com")
            driver.find_element_by_id("password").send_keys("12345678abc")
            driver.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(7)
            driver.find_element_by_class_name("solid-button.reg-rtl-btn").click()
            if driver:
                break
        except:
            continue
    return driver


def start_crawl(file_path, keywords, start_time, end_time):
    keywords_str = "%20".join(keywords)
    start_date = start_time[0: 4] + "%2F" + start_time[4: 6] + "%2F" + start_time[6: 8]
    end_date = end_time[0: 4] + "%2F" + end_time[4: 6] + "%2F" + end_time[6: 8]

    item_set = set()
    driver = get_driver_with_login()
    # 获取不到总数，限定页数上限
    for page in range(1, 30):
        url = f"http://peacebirdth@gmail.com:12345678abc@www.wsj.com/search?query={keywords_str}&isToggleOn=true&operator=AND&sort=date-desc&duration=1y&startDate={start_date}&endDate={end_date}&source=wsjie%2Cblog%2Cwsjsitesrch%2Cwsjpro%2Cautowire%2Capfeed&page={page}"

        driver.get(url)
        div = driver.find_element_by_id("root")
        soup = BeautifulSoup(div.get_attribute('innerHTML'), "html.parser")

        # 添加发布时间和url
        search_result = soup.find_all("div", class_=re.compile("search-result"))
        if len(search_result) > 0:
            for div in search_result:
                article = entity.Article()
                a = div.find_next("a", href=re.compile("https://www.wsj.com/articles/"))
                article.url = a.get("href")

                p = div.find_next("p", class_=re.compile("timestamp"))
                # April 9, 2021 04:06 pm ET
                article.date = p.string
                item_set.add(article)
        else:
            break

    global TOTALS
    TOTALS += len(item_set)
    # 解析正文和标题
    for item in item_set:
        try:
            # 模拟浏览器获取标题和正文
            driver.get(item.url)
            element = driver.find_element_by_id("main")
            soup = BeautifulSoup(element.get_attribute('innerHTML'), "html.parser")
            title = soup.h1.text.replace("\n", "")
            p_list = soup.find_all('p')
            content = ''
            for p in p_list:
                content += p.text.replace("\n", "") + "\n"

            item.title = title
            item.text = content
            item.title_cn = utils.translate(item.title)
            item.text_cn = utils.translate(item.text)
        except Exception as exc:
            pass
        try:
            utils.write_xlsx_apend(file_path, [item, ])
        except:
            pass
        time.sleep(1)

    driver.quit()
    item_set.clear()


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
    utils.create_xlsx_with_head("./WSJ.xlsx", sheet_name='+'.join(keywords))
    start_crawl("./WSJ.xlsx", keywords=keywords, start_time=start_time, end_time=end_time)
