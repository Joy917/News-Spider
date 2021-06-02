# -*- coding:utf-8 -*-
import os
import re
import datetime

import openpyxl
import requests
from urllib.parse import urlencode

from bs4 import BeautifulSoup
from selenium import webdriver

MONTH_DICT = {"January": "01",
              "February": "02",
              "March": "03",
              "April": "04",
              "May": "05",
              "June": "06",
              "July": "07",
              "August": "08",
              "September": "09",
              "October": "10",
              "November": "11",
              "December": "12"}

support_lauguage = {'afrikaans': 'af',
                    'arabic': 'ar',
                    'belarusian': 'be',
                    'bulgarian': 'bg',
                    'catalan': 'ca',
                    'czech': 'cs',
                    'welsh': 'cy',
                    'danish': 'da',
                    'german': 'de',
                    'greek': 'el',
                    'english': 'en',
                    'esperanto': 'eo',
                    'spanish': 'es',
                    'estonian': 'et',
                    'persian': 'fa',
                    'finnish': 'fi',
                    'french': 'fr',
                    'irish': 'ga',
                    'galician': 'gl',
                    'hindi': 'hi',
                    'croatian': 'hr',
                    'hungarian': 'hu',
                    'indonesian': 'id',
                    'icelandic': 'is',
                    'italian': 'it',
                    'hebrew': 'iw',
                    'japanese': 'ja',
                    'korean': 'ko',
                    'latin': 'la',
                    'lithuanian': 'lt',
                    'latvian': 'lv',
                    'macedonian': 'mk',
                    'malay': 'ms',
                    'maltese': 'mt',
                    'dutch': 'nl',
                    'norwegian': 'no',
                    'polish': 'pl',
                    'portuguese': 'pt',
                    'romanian': 'ro',
                    'russian': 'ru',
                    'slovak': 'sk',
                    'slovenian': 'sl',
                    'albanian': 'sq',
                    'serbian': 'sr',
                    'swedish': 'sv',
                    'swahili': 'sw',
                    'thai': 'th',
                    'filipino': 'tl',
                    'turkish': 'tr',
                    'ukrainian': 'uk',
                    'vietnamese': 'vi',
                    'yiddish': 'yi',
                    'chinese_simplified': 'zh-CN',
                    'chinese_traditional': 'zh-TW',
                    'auto': 'auto'}


def format_date(input_date):
    """ date examples:
    17 April 2017
    17 April = 17 April {currentYear}
    # April 9, 2021 04:06 pm ET
    :param input_date: string
    :return: int
    """
    result = -1
    try:
        date_slice = re.split(r"\s+", input_date.strip())
        day = date_slice[0]
        if len(day) == 1: day = "0" + day
        # 处理脏数据
        month = MONTH_DICT.get(date_slice[1])
        if not month: month = "01"
        year = "2021"
        if len(date_slice) == 2:
            year = datetime.date.today().strftime("%Y")
        elif len(date_slice) == 3:
            year = date_slice[2]
        result = int(f"{year}{month}{day}")
    finally:
        return result


def now_timestamp():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def translate(text, target_language="zh-CN"):
    """
    请求谷歌翻译接口，次数过多会被限制访问，大概在20次左右
    :param text:
    :param target_language: 
    :return:
    """
    result = ""
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": "wsjregion=na,us; gdprApplies=false; ab_uuid=637c98ca-f18f-4518-a47a-9518c59f567d; usr_bkt=ixi4E5ylqa; cX_P=kngcgf1o240dcpev; cX_S=kngcgf1zy97m3k1z; _sp_v1_csv=null; _sp_v1_opt=1:; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbLKK83J0YlRSkVil4AlqmtrlXSoqiwWACMYp9h2AAAA; _sp_v1_uid=1:798:1c2fe67d-ec2d-4dce-92aa-260e10d09019; _sp_v1_lt=1:; djvideovol=1; __gads=ID=9b4582df3b958aab:T=1618337659:S=ALNI_MY_oTx3ymoSrklLAMySQBZT_hvyUA; MicrosoftApplicationsTelemetryDeviceId=6973b8e1-34df-3a2e-cb4c-58e2fa8d98e9; MicrosoftApplicationsTelemetryFirstLaunchTime=1618337660216; cX_G=cx:pgvu3625bth816cyzb3jwhgfb:2kehjb05hoy9x; AMCVS_CB68E4BA55144CAA0A4C98A5@AdobeOrg=1; s_cc=true; _ncg_id_=b22bcf7f-11af-4eae-8bcf-7c73b63884fe; _li_dcdm_c=.wsj.com; _lc2_fpi=7880a1137012--01f3672xf29pq93a2pckahezsz; _fbp=fb.1.1618337698060.946935606; OB-USER-TOKEN=38deeaf5-c504-49c6-b6c3-29fcdec2feee; has_optimizely=true; optimizelyEndUserId=oeu1618337800998r0.08981723274843434; _ncg_g_id_=375d10e9-f063-4931-a6bd-157af07bab41; ki_r=; ResponsiveConditional_initialBreakpoint=lg; djcs_route=ace07236-6631-4caa-a2af-bc35c3dde732; djcs_secid=YzMyYmZjMjktNzJkZS00ZTgyLTk3ZGUtZTMzNjk2ZTk4ZTBm.J8opVMp2kS5CFQ1aye74_GsiHcLQlvIpJF2q-Rsqqos; TR=V2-15e14b982a648ef519cac5532c476bbe86c3fa51ee3e8e779209bd9a8ba7661c; _ntv_uid=3fc25902-f7b9-43c1-946d-ae954e9fecb3; djcs_auto=M1619298224/92y758qyl9S5yL+w/zUpcoVPq+SwXHskzdk6Avf+rkF/16poPfyMUQ+d/6a+N1hQSdtN2E3xSLLLcUIgBMmGwwXn4qpuYKnDrMnjt+tRS48VCQ7nwwt63ApQtUbURrt17u6qyifUJkabLdfABwSl/ZnpNDEA+WteEH8vU+nPgu8L/2ogvUmzULCfzbdJpva92oJqCSXnVhbTPVCRhk3o0KR+wbhXCbB/QLd2p9tXbHu4E1dlR5t+bKrQYIdHqc6KCH+hpTeJPMaadLZI+7Rn5x9t9ZLN+wZqVJjB3awX6ijrL5yzDPEpmsD80GLFeQ3qHPzb0PzhMRn6TYaL1LoOIakixHK+3BgOkkB8B69Ky++I2bem2KtQ3W90LuIlq48DpBaxwpsbr45WA8mrzwAhdw==G; djcs_session=M1619369028/r8AE2KH/yGew+uyw5V82gC2r9D6LLNpD6s0YVL3nIfChLTquAS58c4cJHExzxcyQUHK3R67k85M8eEI8N0cW/wGyzhvJgD/g2zegO7lpfHrVYCZo3lHTFFxcJ1mxYswNrgHHwBvYRww0kvjB2m71I7hNDJvWOdoNKwE7d1SzI2nb0w7tguQYp7H1/o/tw5QHNdEkNryXJovKm1nwX9AYz062flCm/AZmgsC5ZS7XomfINK908SkNGNaUZtw29nzi+giiXdOu1vbc2n19M+z1Ybd5r2TEHyEUX4+h2O+BvN3iUebi9U5G/KpEHtgGTEmcUhO80kmubdFZFAnFVcyfcjyAhjIc3SRgMCXGI9WPBLU4hy0/3ZPc27SRVnAZvP7S+UTx75s/kDGXAM96KDc+64CxMWHmG7HFcDMfSar3hkuuKwem5zvoNFgTJ5N5S6V4LgTabhiZv3bau8WBWb83jZtIaItOqiYETDAuZq1Vf+tFK6cPV043mX0hTGsAjW33G; usr_prof_v2=eyJwIjp7InBzIjowLjksInEiOjAuODF9LCJjcCI6eyJlYyI6IlN0YWJsZSIsInBjIjowLjQ1NDg0LCJwc3IiOjAuMjE5OTEsInRkIjo0MCwiYWQiOjQsInFjIjo5OSwicW8iOjk5LCJzY2VuIjp7ImNoZSI6MC4zMDU3OCwiY2huIjowLjQ4MDk4LCJjaGEiOjAuMjk5MTgsImNocCI6MC40MzE3OH19LCJpYyI6NX0=; AMCV_CB68E4BA55144CAA0A4C98A5@AdobeOrg=1585540135|MCIDTS|18743|MCMID|20248205616545994651665923179814411163|MCAID|NONE|MCOPTOUT-1619378526s|NONE|MCAAMLH-1619976126|11|MCAAMB-1619976126|j8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI|vVersion|4.4.0; DJSESSION=country=us||continent=na||region=ca||city=sanjose||latitude=37.3435||longitude=-121.8887||timezone=pst||zip=95101+95103+95106+95108-95113+95115-95136+95138-95139+95141+95148+95150-95161+95164+95170+95172-95173+95190-95194+95196; ccpaApplies=true; hok_seg=8ljs5iat1cy0,8m5oogcu3a7n; _am_sp_djcsses.1fc3=*; _scid=8e41a298-cd35-440c-b4f9-e613b3dc2ef5; ki_t=1618337814635;1619372253677;1619372283386;4;11; _sp_v1_data=2:306234:1618337657:0:41:0:41:0:0:_:-1; consentUUID=146ea439-5cc1-4b68-8ea1-145f00505ec9; utag_main=v_id:0178cc71527b000370d00be3349a03073001406b00978$_sn:6$_se:5$_ss:0$_st:1619375623302$vapi_domain:wsj.com$ses_id:1619372257684;exp-session$_pn:5;exp-session$_prevpage:;exp-1619377423313; _ncg_sp_ses.5378=*; _ncg_sp_id.5378=b22bcf7f-11af-4eae-8bcf-7c73b63884fe.1618337685.6.1619373826.1618763125.bd148ec8-8f46-4a16-9793-f43e19e763e9; _rdt_uuid=1619373826336.cd4d2f89-300c-44c7-82e2-85aaa7139d29; _tq_id.TV-63639009-1.1fc3=a06c2662c213de7e.1619373827.0.1619373827..; _sctr=1|1619366400000; s_tp=2942; s_ppv=https%3A//www.wsj.com/search%3Fquery%3Dtokyo%2520china%26isToggleOn%3Dtrue%26operator%3DAND%26sort%3Ddate-desc%26duration%3D1y%26startDate%3D2021%252F04%252F01%26endDate%3D2021%252F04%252F10%26source%3Dwsjie%252Cblog%252Cwsjsitesrch%252Cwsjpro%252Cautowire%252Capfeed,25,25,722; _am_sp_djcsid.1fc3=7fc4b535-a670-457d-95df-8430916f26b4.1618337684.6.1619374065.1618764703.b86d3273-218a-419c-98c7-d0338fe3bd99"
    }
    if text and isinstance(text, str) and text.strip() != "":
        url = "https://translate.google.com/translate_a/single?"
        params = {"client": "gtx", "sl": "auto", "tl": target_language, "dt": "t", "ie": "UTF-8", "oe": "UTF-8",
                  "q": text}
        try:
            r = requests.get(url + urlencode(params), headers=header)
            if r.status_code == 200:
                # 拼接语义分割的各部分
                for item in r.json()[0]:
                    result += item[0]
        except:
            pass
    return result


def translate_with_webdriver(text, target_language="zh-CN"):
    result = ""
    if text and isinstance(text, str) and text.strip() != "":
        # 超过5000字符需要多次翻译
        if len(text) > 5000:
            count = len(text) // 5000 + 1
            temp_result = ""
            for i in range(0, count):
                temp_text = text[5000 * i:5000 * (i + 1)]
                temp_result += translate_with_webdriver(temp_text, target_language)
            return temp_result
        url = f"https://translate.google.cn/?"
        params = {"sl": "auto", "tl": target_language, "op": "translate", "text": text}
        try:
            # 模拟浏览器登录
            options = webdriver.ChromeOptions()
            # 关闭可视化
            options.add_argument('--headless')
            # 关闭图片视频加载
            options.add_argument('blink-settings=imagesEnabled=false')
            driver = webdriver.Chrome(r'../chromedriver.exe', options=options)
            driver.get(url + urlencode(params))
            element = driver.find_element_by_xpath(
                "//div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div[1]/div[1]/span[1]/span[1]")
            soup = BeautifulSoup(element.get_attribute('innerHTML'), "html.parser")
            driver.quit()
            result = soup.find_all("span")[0].string
        except Exception as exc:
            pass
    return result


def create_xlsx_with_head(file_path, sheet_name, head_values=None):
    if head_values is None:
        head_values = ["Title", "Title-CN", "Date", "URL", "Text", "Text-CN"]
    if file_path.endswith("xlsx"):
        dir_name = os.path.dirname(file_path)
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        # 新建文件和表格
        wb = openpyxl.Workbook()
        # 删除默认生成的sheet
        wb.remove(wb["Sheet"])
        sheet = wb.create_sheet(sheet_name, index=1)
        # 调整列宽
        sheet.column_dimensions['A'].width = 20.0
        sheet.column_dimensions['B'].width = 20.0
        sheet.column_dimensions['E'].width = 50.0
        sheet.column_dimensions['F'].width = 80.0
        # 添加表头
        if head_values: sheet.append(head_values)
        wb.save(file_path)  # 保存文件，注意以xlsx为文件扩展名


def write_xlsx_apend(file_path, values):
    if os.path.isfile(file_path) and file_path.endswith(".xlsx"):
        wb = openpyxl.load_workbook(file_path)
        # 获取workbook中第一个表格
        sheet = wb[wb.sheetnames[0]]
        for value in values:
            row = [value.title, value.title_cn, value.date, value.url, value.text, value.text_cn]
            sheet.append(row)
        wb.save(file_path)  # 保存文件，注意以xlsx为文件扩展名


def get_title_time_content(url, header=None):
    """
    简单解析 HTML 网页，获取新闻的文章标题、发布时间和内容
    :param url:
    :return:
    """
    title = publish_date = content = ""
    try:
        r = requests.get(url, headers=header)
        if r.status_code != 200:
            return

        soup = BeautifulSoup(r.text, 'html.parser')
        # 获取标题、时间、内容
        title = soup.h1.text + '\n'
        p_list = soup.find_all('p')
        content = ''
        for p in p_list:
            content += p.text + '\n'
        publish_date = soup.time.text
    except Exception as exc:
        pass
    finally:
        return title, publish_date, content


value_title = [["姓名", "性别", "年龄", "城市", "职业"], ]

value1 = [["张三", "男", "19", "杭州", "研发工程师"],
          ["李四", "男", "22", "北京", "医生"],
          ["王五", "女", "33", "珠海", "出租车司机"], ]

value2 = [["Tom", "男", "21", "西安", "测试工程师"],
          ["Jones", "女", "34", "上海", "产品经理"],
          ["Cat", "女", "56", "上海", "教师"], ]

if __name__ == '__main__':
    # print(format_date("17 Aprxil 2017"))
    # write_excel_xls(book_name_xls, sheet_name_xls, value_title)
    # write_excel_xls_append(book_name_xls, value1)
    # write_excel_xls_append(book_name_xls, value2)
    # read_excel_xls(book_name_xls)
    # create_xlsx_with_head(r"D:\projects\Spider\demo.xlsx", "demosheet", value_title[0])
    # write_xlsx_apend(r"D:\projects\Spider\demo.xlsx", value1)
    text ="""
    The Jan. 6 commission's death knell Presented by Altria

with a big assist from Olivia Beavers, Sarah Ferris and Marianne LeVine

THE WORLD’S GREATEST DELIBERATIVE BODY-ODY-ODY-ODY -- The House is usually known for being the chamber of chaos. But yesterday, the Senate said, “Hold my beer.”

With jet fumes wafting in the air and senators anxious to catch flights home for the Memorial Day recess, some eleventh-hour objections from the GOP ground the Senate to a halt last night, dragging the drama into the wee hours of the morning and delaying action on several bills and nominations.

The backstory: Earlier in the day, senators overcame an impasse on a bipartisan bill to counter China. But then Sen. Ron Johnson (R-Wis.) threw another last-minute wrench into the debate, complaining that he didn’t get any amendments, including one on border security, or have time to read a manager’s package of amendments that had been negotiated for weeks. So Johnson refused to allow quick consideration of the bill, and he and others insisted on taking up floor time to deliver late-night speeches.

Some senators, however, were not interested in sticking around until the bitter end. Retiring Sen. Richard Shelby (R-Ala.) was spotted on a flight last evening, spy novel in hand, per Lydia DePillis of ProPublica.

In another surreal moment, Sen. Lisa Murkowski (R-Alaska) gave an impassioned speech to reporters about the need for a bipartisan commission to investigate the Capitol riots — all while Officer Eugene Goodman, who saved many lives in the Senate on Jan. 6, stood within earshot as he guarded the chamber doors. Murkowski later came back and hugged him, per NBC’s Julie Tsirkin.

Oh, and to top it all off, a massive and disgusting cicada crawled up the lapel of CNN’s Manu Raju, who was about to do a liveshot from one of the Senate office buildings. Fun times!

OK, so now what? The Senate will resume its work at 9 a.m. We’re expecting more delay tactics, but lawmakers will wrap up today. There are a few more votes on the China bill before final passage. And then at some point, the Senate will turn to a procedural vote on the Jan. 6 commission bill, which is expected to be blocked by the GOP — a move that is sure to leave Republican moderates fuming. More from Burgess: https://politi.co/3yMRqdq.

To put a finer point on it: This whole mess doesn’t bode well for bipartisanship and is guaranteed to sour the atmosphere ahead of what is expected to be a long and busy summer. However, there are no signs of moving the needle on nuking the filibuster: Sen. Joe Manchin (D-W.Va.), once again, told reporters: “I’m not ready to destroy our government. I’m not ready to destroy our government, no.”

This is also the death knell for the bipartisan Jan. 6 commission. Democratic leaders haven’t shown their cards on a Plan B yet, but their most obvious solution is to just appoint a select committee, although that has its limits. Per Sen. Susan Collins (R-Maine): "The most likely outcome, sadly, is probably the Democratic leaders will appoint a select committee. We’ll have a partisan investigation. It won’t have credibility with people like me, but the press will cover it because that’s what’s going on."

Much more on the late-night drama, from Andrew and Gavin Bade: https://politi.co/3vunDV1.





Related read: “Senate Republicans want to block a Jan. 6 commission. These questions might go unanswered,” via Sarah D. Wire of the Los Angeles Times: https://lat.ms/3uzfayI.

BUT, BUT, BUT ... You didn’t really think the House was gonna let the Senate have all the fun in Crazytown, did you? Take it away, Rep. Matt Gaetz (R-Fla.): “We have a Second Amendment in this country, and I think we have an obligation to use it,” he said at a rally last night to a cheering crowd. “The Second Amendment is about maintaining within the citizenry the ability to maintain an armed rebellion against the government, if that becomes necessary.”

And one more, via Rep. Marjorie Taylor Greene (R-Ga.): “You know, Nazis were the National Socialist Party. Just like the Democrats are now a national socialist party,” she said at the same rally.

Related read: “How Matt Gaetz helped make Ron DeSantis,” by our Matt Dixon: https://politi.co/2QVMtho



A message from Altria: Moving beyond smoking. Altria’s companies are leading the way in moving adult smokers away from cigarettes – by taking action to transition millions toward less harmful choices. We are investing in a diverse mix of businesses to broaden options beyond traditional, combustible cigarettes. See how we’re moving.

SCOOPLET -- During their Hill lobbying blitz yesterday, officers who were injured while defending the Capitol on Jan. 6 were told by Sen. Lindsey Graham (R-S.C.) that he wants the officers to testify publicly about what they went through, two sources told your Huddle host. Graham also promised to put them in touch with the senators on the relevant committees conducting an investigation to make that happen. (The group, however, reiterated it still wants a commission.)

Marianne then caught up with Graham, who confirmed the conversation. Here is what he had to say: “These two officers have incredibly compelling stories. So this narrative that this is some kind of tourist exercise is beyond offensive. … I want to see it from the cops’ point of view, and we haven't really done that yet. But I want to memorialize for history's sake — I want the public to understand what these men and women went through so we can take not only corrective action but really expose how dangerous January the sixth was. Publicly, when you hear the two stories, it's very compelling. And we don't want to sugar coat anything."

Related read: “Sicknick’s family and the police officers who protected lawmakers Jan. 6 plead with GOP senators to back investigation,” by WaPo’s Felicia Sonmez, Karoun Demirjian and Peter Hermann: https://wapo.st/3yMtW8j.

HAPPY FRIYAY! Welcome to Huddle, the play-by-play guide to all things Capitol Hill, on this May 28, when your host is as excited for the three-day weekend as Anthony Rizzo and Justin Steele watching this wild rundown during the Cubs-Pirates game.

THURSDAY’S MOST CLICKED: The National Journal’s story on how Biden’s infrastructure bill is already moving was the big winner.

PROGRAMMING NOTE: Huddle will not publish on Monday, May 31. We'll be back on our normal schedule on Tuesday, June 1.

PRESIDENT PROPOSES, CONGRESS DISPOSES -- Most years, the White House’s budget resolution lands with a thud on Capitol Hill. But this year, many Democrats have been waiting on that precise proposal as their unofficial start date for reconciliation. With Biden’s FY22 budget in hand, Democrats can ditch the GOP and unlock those special budget powers to go it alone on infrastructure. And many in the party, particularly progressives, are more than ready.

The complicating factor? Biden is still talking with a group of Senate Republicans about a bipartisan deal, with more discussions slated for next week. Democratic leaders are not about to cut off those White House talks prematurely by proceeding with a party-line vote to unlock that budget tool. That means, at least for now, reconciliation plans are still on ice, and the time crunch to get a bill to the floor before the August recess is feeling even more real.

Many Dems are hopeful Biden will have an answer either way by the end of the Memorial Day recess: Sen. Chris Coons (D-Del.), a close Biden ally, acknowledged that Democratic patience is running out: “We need to have a pathway towards closing a bipartisan deal or moving ahead on a Democrats-only basis.” In the words of Sen. Bob Casey (D-Pa.): “I think we’re getting real close to the fish or cut bait time.”

The deets from Caitlin Emma, Sarah and Marianne: https://politi.co/34nWmYf.

Related read: “Biden to Propose $6 Trillion Budget to Make U.S. More Competitive,” from NYT’s Jim Tankersley: https://nyti.ms/3fpGxXx.





WOAH, WE’RE HALFWAY THERE -- Senate Republicans unveiled a $928 billion infrastructure counteroffer yesterday morning. But the latest offer includes only $257 billion in new spending, which is a no-go for Democrats whose latest counter ringed in at $1.7 trillion.

It includes: $506 billion for roads and bridges, $98 billion for public transit systems, $46 billion for passenger and freight trail, $21 billion for safety, $22 billion for ports and waterways, $56 billion for airports, among other features.

The clock is ticking. The bipartisan talks are already skidding past the Memorial Day soft deadline and progress in the negotiations appears to be stalling as the two sides remain far apart on several issues, including the total cost, the definition of infrastructure, and how to pay for it.

“We believe this counteroffer delivers on what President Biden told us in the Oval office that day, and that is to try to reach somewhere near $1 trillion over an eight-year period that would include our baseline spending,” said Sen. Shelley Moore Capito of West Virginia, the top GOP negotiator. “We have achieved that goal with this counteroffer.” Meanwhile, Senate Democrats are already scoffing at this GOP proposal.

More here from Marianne: https://politi.co/3usZ0qg

Related read: “Biden to Meet GOP Next Week on Infrastructure as Clock Ticks,” by Bloomberg’s Erik Wasson and Justin Sink: https://bloom.bg/3utQl6U.

FINKENAUER HOUR — Former Rep. Abby Finkenauer (D-Iowa) is prepping a potential Senate bid as Washington waits to see whether 87-year-old Sen. Chuck Grassley (R-Iowa) will run for an eighth term. Finkenauer, who was elected in 2018 as one of Congress’ youngest-ever women in office, is assembling a potential campaign team in Iowa.

Democrats in the state acknowledge Finkenauer would have an uphill battle in a state that Republicans nearly swept in 2020, but some say she could have a shot to retake the Senate seat if Grassley decides to retire this fall. The Iowa Democrat flipped a red seat in 2018, which she lost to GOP Rep. Ashley Hinson in November.

The scoop from Ally Mutnick and James Arkin: https://politi.co/3p0o1bw.

Related read: “Demings raises Democrats' hopes in uphill fight to defeat Rubio,” by The Hill’s Max Greenwood: https://bit.ly/3vyZmgG.

IF YOU CAN’T BEAT ’EM, FUND ’EM — Democrats in Congress know they don’t have the votes to kill the Hyde amendment on abortion funding or the Dickey amendment on gun research.

Instead, they’re hoping for a workaround that involves a lot more cash to programs that can accomplish a similar goal — without drawing the fierce ire of the GOP.

On the Hyde amendment, for instance, Democrats won’t be able to eliminate the ban on federal funding on abortions, which prevents low-income women from paying for the procedure through programs like Medicaid. Democrats will instead look to pour money into grant programs that fund clinics like Planned Parenthood, which they say can increase health care options to those women.

And while the Dickey amendment still bans the CDC from advocating for gun control, Democrats are planning to provide billions of additional dollars across federal agencies to bolster research, gun violence prevention initiatives and background check systems. The story from Caitlin Emma: https://politi.co/3utp7gP.

WHERE ARE THEY NOW? -- “Paul Ryan to Call for GOP to Lessen Reliance on Trump,” from WSJ’s John McCormick: https://on.wsj.com/3us9OoS | “Biden eyes Claire McCaskill for plum Europe ambassadorship,” by Hans Nichols of Axios: https://bit.ly/2SCVEnl.

D.C. PHONE HOME -- It used to be talking about UFOs would torpedo your political career. But Sen. MARCO RUBIO (R-Fla.) is picking up the mantle from former Senate Majority Leader HARRY REID (D-Nev.) — Congress’ granddaddy of this issue and the person responsible for establishing the Pentagon’s $22 million “Advanced Aerospace Threat Identification Program” to study this.

“Anything that enters an airspace that's not supposed to be there is a threat,” Rubio told “60 Minutes” earlier this month. "Some of my colleagues are very interested in this topic and some kinda, you know, giggle when you bring it up. But I don't think we can allow the stigma to keep us from having an answer to a very fundamental question." Now, the Pentagon is set to deliver a long-awaited report next month detailing what they know — and what they don’t. Can we expect our first-ever UFO hearings in Congress? Maybe!

For more, check out today’s episode of Playbook Deep Dive, where Bryan Bender and Rachael Bade dissect how unidentified flying objects have crashed into the Washington discourse (plus: a POLITICO-exclusive interview with Reid).

ALSO, don’t miss this Friday’s cover of POLITICO Magazine: “The Hidden History of How Washington Embraced UFOs,” by Bryan Bender: https://politi.co/3wEt7MX.



TRANSITIONS

Jake Hochberg, known around the Hill as “GOP Jake” and a Talay Thai savant, is the new chief of staff for Rep. Henry Cuellar (D-Texas). He was previously LD for Rep. Raja Krishnamoorthi (D-Ill.).

Kasey Hampton is joining Families USA. Hampton will be the organization’s senior manager of storytelling and engagement communications. She was previously the press secretary for Sen. Tammy Baldwin (D-Wis.).

Mela Louise Norman will be deputy COS for Defense Secretary Lloyd Austin. She previously was COS for Rep. Elissa Slotkin (D-Mich.).

Matt Hennessey will take over as COS for Slotkin. He most recently was campaign manager for Slotkin’s re-election campaign and is founder and principal of Onward Strategies.

TODAY IN CONGRESS

The House is out.

The Senate gavels in at 9 a.m.

AROUND THE HILL

All eyes on the Senate.

TRIVIA

THURSDAY’S WINNER: Bruce Brown was the first person to correctly guess that former Rep. John Dingell (D-Mich.) holds the record as the longest serving member of Congress, breaking the House service record of Rep. Jamie Whitten (D-Miss.) by five — almost six — years.

TODAY’S QUESTION: From Rep. Don Beyer (D-Va.): Who was the first elected African American governor in U.S. History?

The first person to correctly guess gets a mention in the next edition of Huddle. Send your answer to [email protected].

GET HUDDLE emailed to your phone each morning.

Follow Olivia on Twitter: @Olivia_Beavers



A message from Altria: Moving beyond smoking. Altria’s companies are leading the way in moving adult smokers away from cigarettes. Today, we are taking action to transition millions toward less harmful choices. From cigarettes to innovative alternatives. By investing in a diverse mix of businesses, Altria is working to further broaden options. Our companies are encouraging adult smokers to transition to a range of choices that go beyond traditional, combustible cigarettes. From tobacco company to tobacco harm reduction company. And while Altria is moving forward to reduce harm, we are not moving alone. We are working closely with FDA and other regulatory bodies, and will work strictly under their framework. See how we’re moving.
    """

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "Connection": "close",
        "cookie": "wsjregion=na,us; gdprApplies=false; ab_uuid=637c98ca-f18f-4518-a47a-9518c59f567d; usr_bkt=ixi4E5ylqa; cX_P=kngcgf1o240dcpev; cX_S=kngcgf1zy97m3k1z; _sp_v1_csv=null; _sp_v1_opt=1:; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbLKK83J0YlRSkVil4AlqmtrlXSoqiwWACMYp9h2AAAA; _sp_v1_uid=1:798:1c2fe67d-ec2d-4dce-92aa-260e10d09019; _sp_v1_lt=1:; djvideovol=1; __gads=ID=9b4582df3b958aab:T=1618337659:S=ALNI_MY_oTx3ymoSrklLAMySQBZT_hvyUA; MicrosoftApplicationsTelemetryDeviceId=6973b8e1-34df-3a2e-cb4c-58e2fa8d98e9; MicrosoftApplicationsTelemetryFirstLaunchTime=1618337660216; cX_G=cx:pgvu3625bth816cyzb3jwhgfb:2kehjb05hoy9x; AMCVS_CB68E4BA55144CAA0A4C98A5@AdobeOrg=1; s_cc=true; _ncg_id_=b22bcf7f-11af-4eae-8bcf-7c73b63884fe; _li_dcdm_c=.wsj.com; _lc2_fpi=7880a1137012--01f3672xf29pq93a2pckahezsz; _fbp=fb.1.1618337698060.946935606; OB-USER-TOKEN=38deeaf5-c504-49c6-b6c3-29fcdec2feee; has_optimizely=true; optimizelyEndUserId=oeu1618337800998r0.08981723274843434; _ncg_g_id_=375d10e9-f063-4931-a6bd-157af07bab41; ki_r=; ResponsiveConditional_initialBreakpoint=lg; djcs_route=ace07236-6631-4caa-a2af-bc35c3dde732; djcs_secid=YzMyYmZjMjktNzJkZS00ZTgyLTk3ZGUtZTMzNjk2ZTk4ZTBm.J8opVMp2kS5CFQ1aye74_GsiHcLQlvIpJF2q-Rsqqos; TR=V2-15e14b982a648ef519cac5532c476bbe86c3fa51ee3e8e779209bd9a8ba7661c; _ntv_uid=3fc25902-f7b9-43c1-946d-ae954e9fecb3; djcs_auto=M1619298224/92y758qyl9S5yL+w/zUpcoVPq+SwXHskzdk6Avf+rkF/16poPfyMUQ+d/6a+N1hQSdtN2E3xSLLLcUIgBMmGwwXn4qpuYKnDrMnjt+tRS48VCQ7nwwt63ApQtUbURrt17u6qyifUJkabLdfABwSl/ZnpNDEA+WteEH8vU+nPgu8L/2ogvUmzULCfzbdJpva92oJqCSXnVhbTPVCRhk3o0KR+wbhXCbB/QLd2p9tXbHu4E1dlR5t+bKrQYIdHqc6KCH+hpTeJPMaadLZI+7Rn5x9t9ZLN+wZqVJjB3awX6ijrL5yzDPEpmsD80GLFeQ3qHPzb0PzhMRn6TYaL1LoOIakixHK+3BgOkkB8B69Ky++I2bem2KtQ3W90LuIlq48DpBaxwpsbr45WA8mrzwAhdw==G; djcs_session=M1619369028/r8AE2KH/yGew+uyw5V82gC2r9D6LLNpD6s0YVL3nIfChLTquAS58c4cJHExzxcyQUHK3R67k85M8eEI8N0cW/wGyzhvJgD/g2zegO7lpfHrVYCZo3lHTFFxcJ1mxYswNrgHHwBvYRww0kvjB2m71I7hNDJvWOdoNKwE7d1SzI2nb0w7tguQYp7H1/o/tw5QHNdEkNryXJovKm1nwX9AYz062flCm/AZmgsC5ZS7XomfINK908SkNGNaUZtw29nzi+giiXdOu1vbc2n19M+z1Ybd5r2TEHyEUX4+h2O+BvN3iUebi9U5G/KpEHtgGTEmcUhO80kmubdFZFAnFVcyfcjyAhjIc3SRgMCXGI9WPBLU4hy0/3ZPc27SRVnAZvP7S+UTx75s/kDGXAM96KDc+64CxMWHmG7HFcDMfSar3hkuuKwem5zvoNFgTJ5N5S6V4LgTabhiZv3bau8WBWb83jZtIaItOqiYETDAuZq1Vf+tFK6cPV043mX0hTGsAjW33G; usr_prof_v2=eyJwIjp7InBzIjowLjksInEiOjAuODF9LCJjcCI6eyJlYyI6IlN0YWJsZSIsInBjIjowLjQ1NDg0LCJwc3IiOjAuMjE5OTEsInRkIjo0MCwiYWQiOjQsInFjIjo5OSwicW8iOjk5LCJzY2VuIjp7ImNoZSI6MC4zMDU3OCwiY2huIjowLjQ4MDk4LCJjaGEiOjAuMjk5MTgsImNocCI6MC40MzE3OH19LCJpYyI6NX0=; AMCV_CB68E4BA55144CAA0A4C98A5@AdobeOrg=1585540135|MCIDTS|18743|MCMID|20248205616545994651665923179814411163|MCAID|NONE|MCOPTOUT-1619378526s|NONE|MCAAMLH-1619976126|11|MCAAMB-1619976126|j8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI|vVersion|4.4.0; DJSESSION=country=us||continent=na||region=ca||city=sanjose||latitude=37.3435||longitude=-121.8887||timezone=pst||zip=95101+95103+95106+95108-95113+95115-95136+95138-95139+95141+95148+95150-95161+95164+95170+95172-95173+95190-95194+95196; ccpaApplies=true; hok_seg=8ljs5iat1cy0,8m5oogcu3a7n; _am_sp_djcsses.1fc3=*; _scid=8e41a298-cd35-440c-b4f9-e613b3dc2ef5; ki_t=1618337814635;1619372253677;1619372283386;4;11; _sp_v1_data=2:306234:1618337657:0:41:0:41:0:0:_:-1; consentUUID=146ea439-5cc1-4b68-8ea1-145f00505ec9; utag_main=v_id:0178cc71527b000370d00be3349a03073001406b00978$_sn:6$_se:5$_ss:0$_st:1619375623302$vapi_domain:wsj.com$ses_id:1619372257684;exp-session$_pn:5;exp-session$_prevpage:;exp-1619377423313; _ncg_sp_ses.5378=*; _ncg_sp_id.5378=b22bcf7f-11af-4eae-8bcf-7c73b63884fe.1618337685.6.1619373826.1618763125.bd148ec8-8f46-4a16-9793-f43e19e763e9; _rdt_uuid=1619373826336.cd4d2f89-300c-44c7-82e2-85aaa7139d29; _tq_id.TV-63639009-1.1fc3=a06c2662c213de7e.1619373827.0.1619373827..; _sctr=1|1619366400000; s_tp=2942; s_ppv=https%3A//www.wsj.com/search%3Fquery%3Dtokyo%2520china%26isToggleOn%3Dtrue%26operator%3DAND%26sort%3Ddate-desc%26duration%3D1y%26startDate%3D2021%252F04%252F01%26endDate%3D2021%252F04%252F10%26source%3Dwsjie%252Cblog%252Cwsjsitesrch%252Cwsjpro%252Cautowire%252Capfeed,25,25,722; _am_sp_djcsid.1fc3=7fc4b535-a670-457d-95df-8430916f26b4.1618337684.6.1619374065.1618764703.b86d3273-218a-419c-98c7-d0338fe3bd99"
    }

    url = "https://www.wsj.com/articles/russia-rolls-out-covid-19-vaccine-for-animals-11622128581?page=1"
    title, publish_date, content = get_title_time_content(url, header=header)
    print(title)
    print(publish_date)
    print(content)
    print(translate_with_webdriver(content))
