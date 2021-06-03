import newspaper as ns
import requests
#
# # 配置
# cookies = "wsjregion=na%2Cus; gdprApplies=false; ccpaApplies=true; ab_uuid=637c98ca-f18f-4518-a47a-9518c59f567d; usr_bkt=ixi4E5ylqa; cX_P=kngcgf1o240dcpev; cX_S=kngcgf1zy97m3k1z; __gads=ID=9b4582df3b958aab:T=1618337659:S=ALNI_MY_oTx3ymoSrklLAMySQBZT_hvyUA; cX_G=cx%3Apgvu3625bth816cyzb3jwhgfb%3A2kehjb05hoy9x; AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1; s_cc=true; _ncg_id_=b22bcf7f-11af-4eae-8bcf-7c73b63884fe; _li_dcdm_c=.wsj.com; _lc2_fpi=7880a1137012--01f3672xf29pq93a2pckahezsz; _fbp=fb.1.1618337698060.946935606; OB-USER-TOKEN=38deeaf5-c504-49c6-b6c3-29fcdec2feee; has_optimizely=true; optimizelyEndUserId=oeu1618337800998r0.08981723274843434; _ncg_g_id_=375d10e9-f063-4931-a6bd-157af07bab41; djcs_route=ace07236-6631-4caa-a2af-bc35c3dde732; djcs_secid=YzMyYmZjMjktNzJkZS00ZTgyLTk3ZGUtZTMzNjk2ZTk4ZTBm.J8opVMp2kS5CFQ1aye74_GsiHcLQlvIpJF2q-Rsqqos; TR=V2-15e14b982a648ef519cac5532c476bbe86c3fa51ee3e8e779209bd9a8ba7661c; DJSESSION=country%3Dus%7C%7Ccontinent%3Dna%7C%7Cregion%3Dca%7C%7Ccity%3Dsanjose%7C%7Clatitude%3D37.3435%7C%7Clongitude%3D-121.8887%7C%7Ctimezone%3Dpst%7C%7Czip%3D95101%2B95103%2B95106%2B95108-95113%2B95115-95136%2B95138-95139%2B95141%2B95148%2B95150-95161%2B95164%2B95170%2B95172-95173%2B95190-95194%2B95196; usr_prof_v2=eyJwIjp7InBzIjowLjk4LCJxIjowLjg0fSwiY3AiOnsiZWMiOiJHcm93aW5nIiwicGMiOjAuMDkxNzQsInBzciI6MC4yNjUwNCwidGQiOjMxLCJhZCI6NCwicWMiOjgzLCJxbyI6OTEsInNjZW4iOnsiY2hlIjowLjA4NDgyLCJjaG4iOjAuMDcxMzYsImNoYSI6MC4wODY5NiwiY2hwIjowLjExMTAzfX0sImljIjo1fQ%3D%3D; AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1585540135%7CMCIDTS%7C18733%7CMCMID%7C20248205616545994651665923179814411163%7CMCAID%7CNONE%7CMCOPTOUT-1618518284s%7CNONE%7CMCAAMLH-1619115884%7C9%7CMCAAMB-1619115884%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C4.4.0; hok_seg=none; _ncg_sp_ses.5378=*; _rdt_uuid=1618512606809.742ff3ac-8dd5-40eb-9feb-c90b95e9fb5d; consentUUID=ac2fc6ec-9693-426d-889a-c645a20d4c66; _ncg_sp_id.5378=b22bcf7f-11af-4eae-8bcf-7c73b63884fe.1618337685.3.1618512625.1618423349.c9805901-4fb2-4ff4-b925-b0503f8df1ba; _scid=d6b56e40-e2a5-4c76-b33d-ccbe613b5817; _sctr=1|1618502400000; s_tp=7694; s_ppv=WSJ_Article_Politics_Biden%2520Signs%2520Executive%2520Order%2520Targeting%2520%25u2018Harmful%2520Foreign%2520Activities%25u2019%2520by%2520Russian%2520Government%2C13%2C9%2C1022; s_sq=djglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253DWSJ_Article_Politics_Biden%252520Signs%252520Executive%252520Order%252520Targeting%252520%2525E2%252580%252598Harmful%252520Foreign%252520Activities%2525E2%252580%252599%252520by%252520Russian%252520Government%2526link%253DCustomer%252520Center%2526region%253Dcustomer-nav%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c; reese84=3:41AoCuKvWMh6OHlT7kGksg==:rUvNEr66sLdjjTBpkTBxu2Shyo9CkbH16cAjM96ooiNxX3hER1DBdQbcujhDgcLeFCDl9GUViiL8wNBkvHMgMorFXVWJwPgSSEnmueIHlTcFNGczPpk3lkTB/x/WeX4caIo9eBKJUhRI2QQudZ5SanGVAVRrQ8pK1qDDFQNoL52Kt4Cj0PZ3LSgnrEA61w62mLAfDMuEvnEbIxgfO4HwvCvbWHJ5/ZceQP009BHig3Nx2fX5ln6TJl/GBIK+LwEjJHThvkb4S5NFRFZM+wAt+198cdsHrEKlSrK5fTG+ML0X4fpZyM0tEMV5lx48d3yP8ETuipPh5kPoFFMU3fLcgCy8MmLQ62oI9nMq6H+RI9MXfhUYZPUUxPTHhGbhL5L0vzIOIcJmHdBH60cTaQxVPoGqB1kKX+UinVBLIRZrNVy94hfT3MpbqlznLtCW+nHCpUlo5jy71/uf04RJ2dv73VYrKKY5hh31qPA6rzRPJ2E=:fiTtTmUETzfHBSDaAlipoZOk0HAvnesodZO/clyeQGk=; run-sso=true; djcs_auto=M1618434224%2FNTRuYODUTxLnWdcohhi4d0CjIrLiZ6Od16RJgVdcs4qbZqjQYRm1ctBO9fApzxgckCKuCuLYAeu58hY%2FvduEbYl%2BCMzz97mIbqcjgbE9fyehEgEqGU2CJv1WL0CQRo3oqmzocFyQKHh%2BAx5Lfr%2FeWJU%2BNdtw1lKek3Ee5%2FiGXF9qkCSzKOu%2Bi6hC79kLmpc%2FTmK5eekcGnUj3vfrhTvwvDcBj%2BkIwAmV64ScdeSYE%2Fx0nT5T%2FRZbfcKOIXFNLxK7DG79Mi4qSv5Tyxfd%2Bu6pIq4W3Dfe4ecQOyYlIS9JiaBBLdI%2F2G5ZYeP%2BvabZkQbdt%2FPkaKir8zgwZoKzJGi193DClmO%2Bpum%2FbkMxa9ZkC3ESYnEbzkYbAn1CWfWtdIJnOqbqiBJLlcO0sv4eUJjNiA%3D%3DG; djcs_session=M1618512228%2Fg%2F6uL4uUjwJAIRY0WsTONiM%2FflEhZ5tmjn3PFmyt88IMB01Zt%2FUo0h%2BSh0gWBUprlsBDhTbTgI%2FqNq%2BFsFDEh42VY9rOrk%2Fh%2FY7ycHmrXBaXfzS3Pt3TiOaEjusgBBpdbxEuCyMI%2F34mSs3OEkR%2FKLudlnfCBLR9EEx%2BbQCaD5A%2BJWxJi2tJWdmN8TN0JBamnmpG2l6fikMTe%2BDTViAGT%2Fn9%2B54HUesSJKHED52qNlxpfcjvwUFBTAlykIuB3rNbft7ohZFHw3inhXGkshkJACml5gFhf3nrt6EPUKgHr9gto7V%2FgtiLK9eMn4XO5pxeNC7aF%2B7LM1uLW6AR9XkSzWOaS5DBdWtYbYjmpmOZf%2B%2FUtp7eVeK6vNCXzF0ye5gGRpMv64QqmLC0SqpptdIAK9WrFKcLPZunZrpGHugV4jabx9Po0ktdlKLEBaB4h1iBMtH278LX8WfDutmfM%2BGmgENE%2Fpixrvh55hX9J3Fa%2Bsc%3DG; utag_main=v_id:0178cc71527b000370d00be3349a03073001406b00978$_sn:3$_se:5$_ss:0$_st:1618514525711$vapi_domain:wsj.com$ses_id:1618511093342%3Bexp-session$_pn:6%3Bexp-session$_prevpage:WSJ_Article_Politics_Biden%20Signs%20Executive%20Order%20Targeting%20%E2%80%98Harmful%20Foreign%20Activities%E2%80%99%20by%20Russian%20Government%3Bexp-1618516222333"
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
# headers = {
#     "user-agent": user_agent}
# site_url = "https://www.wsj.com/search?query=tokyo&mod=searchresults_viewallresults"
# # r = requests.get(url=site_url, headers=headers)
# # r.raise_for_status()
# # print(r.text)
#
# washingtonpost_paper = ns.build('https://www.washingtonpost.com')
#
# # 所有文章的url
# for article in washingtonpost_paper.articles:
#     print(article.url)
#
# # 文章分裂
# for category in washingtonpost_paper.category_urls():
#     print(category)

from bs4 import BeautifulSoup
import re

# with open(r"D:\projects\Spider\html.txt", "r", encoding="utf-8") as fr:
#     html_content = fr.read()
#     soup = BeautifulSoup(html_content, "html.parser")
#     for a in soup.find_all(href=re.compile("https://www.wsj.com/articles")):
#         print(a.get("href"))
#
#
# url = "https://www.wsj.com/articles/japanese-stocks-are-back-on-u-s-investors-radar-11617462000?mod=searchresults_pos6&page=1"
#
# header = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
#     "accept": "*/*",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "cookie": "wsjregion=na,us; gdprApplies=false; ab_uuid=637c98ca-f18f-4518-a47a-9518c59f567d; usr_bkt=ixi4E5ylqa; cX_P=kngcgf1o240dcpev; cX_S=kngcgf1zy97m3k1z; _sp_v1_csv=null; _sp_v1_opt=1:; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbLKK83J0YlRSkVil4AlqmtrlXSoqiwWACMYp9h2AAAA; _sp_v1_uid=1:798:1c2fe67d-ec2d-4dce-92aa-260e10d09019; _sp_v1_lt=1:; djvideovol=1; __gads=ID=9b4582df3b958aab:T=1618337659:S=ALNI_MY_oTx3ymoSrklLAMySQBZT_hvyUA; MicrosoftApplicationsTelemetryDeviceId=6973b8e1-34df-3a2e-cb4c-58e2fa8d98e9; MicrosoftApplicationsTelemetryFirstLaunchTime=1618337660216; cX_G=cx:pgvu3625bth816cyzb3jwhgfb:2kehjb05hoy9x; AMCVS_CB68E4BA55144CAA0A4C98A5@AdobeOrg=1; s_cc=true; _ncg_id_=b22bcf7f-11af-4eae-8bcf-7c73b63884fe; _li_dcdm_c=.wsj.com; _lc2_fpi=7880a1137012--01f3672xf29pq93a2pckahezsz; _fbp=fb.1.1618337698060.946935606; OB-USER-TOKEN=38deeaf5-c504-49c6-b6c3-29fcdec2feee; has_optimizely=true; optimizelyEndUserId=oeu1618337800998r0.08981723274843434; _ncg_g_id_=375d10e9-f063-4931-a6bd-157af07bab41; ki_r=; ResponsiveConditional_initialBreakpoint=lg; djcs_route=ace07236-6631-4caa-a2af-bc35c3dde732; djcs_secid=YzMyYmZjMjktNzJkZS00ZTgyLTk3ZGUtZTMzNjk2ZTk4ZTBm.J8opVMp2kS5CFQ1aye74_GsiHcLQlvIpJF2q-Rsqqos; TR=V2-15e14b982a648ef519cac5532c476bbe86c3fa51ee3e8e779209bd9a8ba7661c; _ntv_uid=3fc25902-f7b9-43c1-946d-ae954e9fecb3; djcs_auto=M1619298224/92y758qyl9S5yL+w/zUpcoVPq+SwXHskzdk6Avf+rkF/16poPfyMUQ+d/6a+N1hQSdtN2E3xSLLLcUIgBMmGwwXn4qpuYKnDrMnjt+tRS48VCQ7nwwt63ApQtUbURrt17u6qyifUJkabLdfABwSl/ZnpNDEA+WteEH8vU+nPgu8L/2ogvUmzULCfzbdJpva92oJqCSXnVhbTPVCRhk3o0KR+wbhXCbB/QLd2p9tXbHu4E1dlR5t+bKrQYIdHqc6KCH+hpTeJPMaadLZI+7Rn5x9t9ZLN+wZqVJjB3awX6ijrL5yzDPEpmsD80GLFeQ3qHPzb0PzhMRn6TYaL1LoOIakixHK+3BgOkkB8B69Ky++I2bem2KtQ3W90LuIlq48DpBaxwpsbr45WA8mrzwAhdw==G; djcs_session=M1619369028/r8AE2KH/yGew+uyw5V82gC2r9D6LLNpD6s0YVL3nIfChLTquAS58c4cJHExzxcyQUHK3R67k85M8eEI8N0cW/wGyzhvJgD/g2zegO7lpfHrVYCZo3lHTFFxcJ1mxYswNrgHHwBvYRww0kvjB2m71I7hNDJvWOdoNKwE7d1SzI2nb0w7tguQYp7H1/o/tw5QHNdEkNryXJovKm1nwX9AYz062flCm/AZmgsC5ZS7XomfINK908SkNGNaUZtw29nzi+giiXdOu1vbc2n19M+z1Ybd5r2TEHyEUX4+h2O+BvN3iUebi9U5G/KpEHtgGTEmcUhO80kmubdFZFAnFVcyfcjyAhjIc3SRgMCXGI9WPBLU4hy0/3ZPc27SRVnAZvP7S+UTx75s/kDGXAM96KDc+64CxMWHmG7HFcDMfSar3hkuuKwem5zvoNFgTJ5N5S6V4LgTabhiZv3bau8WBWb83jZtIaItOqiYETDAuZq1Vf+tFK6cPV043mX0hTGsAjW33G; usr_prof_v2=eyJwIjp7InBzIjowLjksInEiOjAuODF9LCJjcCI6eyJlYyI6IlN0YWJsZSIsInBjIjowLjQ1NDg0LCJwc3IiOjAuMjE5OTEsInRkIjo0MCwiYWQiOjQsInFjIjo5OSwicW8iOjk5LCJzY2VuIjp7ImNoZSI6MC4zMDU3OCwiY2huIjowLjQ4MDk4LCJjaGEiOjAuMjk5MTgsImNocCI6MC40MzE3OH19LCJpYyI6NX0=; AMCV_CB68E4BA55144CAA0A4C98A5@AdobeOrg=1585540135|MCIDTS|18743|MCMID|20248205616545994651665923179814411163|MCAID|NONE|MCOPTOUT-1619378526s|NONE|MCAAMLH-1619976126|11|MCAAMB-1619976126|j8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI|vVersion|4.4.0; DJSESSION=country=us||continent=na||region=ca||city=sanjose||latitude=37.3435||longitude=-121.8887||timezone=pst||zip=95101+95103+95106+95108-95113+95115-95136+95138-95139+95141+95148+95150-95161+95164+95170+95172-95173+95190-95194+95196; ccpaApplies=true; hok_seg=8ljs5iat1cy0,8m5oogcu3a7n; _am_sp_djcsses.1fc3=*; _scid=8e41a298-cd35-440c-b4f9-e613b3dc2ef5; ki_t=1618337814635;1619372253677;1619372283386;4;11; _sp_v1_data=2:306234:1618337657:0:41:0:41:0:0:_:-1; consentUUID=146ea439-5cc1-4b68-8ea1-145f00505ec9; utag_main=v_id:0178cc71527b000370d00be3349a03073001406b00978$_sn:6$_se:5$_ss:0$_st:1619375623302$vapi_domain:wsj.com$ses_id:1619372257684;exp-session$_pn:5;exp-session$_prevpage:;exp-1619377423313; _ncg_sp_ses.5378=*; _ncg_sp_id.5378=b22bcf7f-11af-4eae-8bcf-7c73b63884fe.1618337685.6.1619373826.1618763125.bd148ec8-8f46-4a16-9793-f43e19e763e9; _rdt_uuid=1619373826336.cd4d2f89-300c-44c7-82e2-85aaa7139d29; _tq_id.TV-63639009-1.1fc3=a06c2662c213de7e.1619373827.0.1619373827..; _sctr=1|1619366400000; s_tp=2942; s_ppv=https%3A//www.wsj.com/search%3Fquery%3Dtokyo%2520china%26isToggleOn%3Dtrue%26operator%3DAND%26sort%3Ddate-desc%26duration%3D1y%26startDate%3D2021%252F04%252F01%26endDate%3D2021%252F04%252F10%26source%3Dwsjie%252Cblog%252Cwsjsitesrch%252Cwsjpro%252Cautowire%252Capfeed,25,25,722; _am_sp_djcsid.1fc3=7fc4b535-a670-457d-95df-8430916f26b4.1618337684.6.1619374065.1618764703.b86d3273-218a-419c-98c7-d0338fe3bd99"
# }
# art = ns.Article(url, headers=header, language='en')
# art.download()
# art.parse()
# print(art.text)
# print(art.publish_date)

# import jsonpath
#
# date_str = "2021-04-22T06:13:25Z"
# print(date_str[0:4] + date_str[5:7] + date_str[8:10])
# dict = {
#     "a": {},
#     "b": {
#         "c": "haha"
#     }
# }
# print(jsonpath.jsonpath(dict, "$..d"))

# import datetime
# import time
import dateutil.tz as du
# print(datetime.date.today().strftime("%Y"))

import time
import datetime

# print(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
#
# import os
#
# dir = f"D:\\spiderResult"
# if os.path.isdir(dir):
#     print("ok")
# else:
#     os.makedirs(dir)

# print(len(set()))

# import time
#
# start = time.time()
# time.sleep(2)
# end = time.time()
#
# print((end-start).__floor__())

# import utils
# print(utils.now_timestamp())
#
# text = """
# the third wave,” said Dr. Theresa Tam, Canada’s chief public health officer, said during a news conference Friday in Ottawa, pointing to reductions in new daily cases, hospitalizations and intensive care unit admissions. However, Tam said the rate of transmission and the level of infection in Canada remains too high to allow for any loosening of restrictions any time soon.  Tam called the goal of 75% of eligible Canadians getting fully vaccinated as an "aspirational target."  As of Friday, the federal government said more than 42% of Canadians have now received at least one dose. That represents more than half of all eligible adults.  However, less than 4% of Canadians are fully vaccinated and that number is not expected to rise substantially until summer as Canada continues to delay second shots for up to four months. The lack of vaccine supply makes Canada continue to ration vaccine doses, although the government says more vaccines, especially from Pfizer, will continue to ramp up through the end of June. Health Canada guidance indicates that even outdoor activities like barbecues and small outdoor gatherings should only resume in the coming weeks if and when about 75% of eligible Canadians receive at least one vaccine dose and 20% are fully vaccinated. Public health officials also say mask mandates should be one of the last restrictions to be lifted.  “I think masks might be the last layer of that multi-layer protection that we would advise for people to remove. I think we have to slowly and surely ease the more restrictive measures, those shutdowns and those stay-at-home orders,” said Tam.  Canada’s Health Minister Patty Hajdu said her government has discussed the new guidance with all the provinces and territories, and the final word on when and how to relax public health measures will ultimately rest with local officials.  It will take some time and effort to make sure coronavirus vaccines are given to 12-to-15-year-olds in an equitable way, vaccine advisers to the US Centers for Disease Control and Prevention said Friday. The CDC’s Advisory Committee on Immunization Practices (ACIP) voted Wednesday to recommend use of Pfizer/BioNTech’s vaccine in younger teens and CDC Director Dr. Rochelle Walensky signed off on it immediately. Vaccination of the younger age group began right away in some places, but work is required to make sure all the young teens and older children who need the vaccine get it, ACIP said. “Providing rapid and equitable access to COVID-19 vaccine for adolescents will require a stepwise approach, including augmenting existing infrastructure for vaccination, increasing enrollment of providers caring for adolescents into the COVID-19 vaccination program, and applying school-focused strategies to ensure vaccination opportunities for a diverse population,” they wrote in a report distributed by the CDC in its weekly MMWR release. “Some aspects of the Pfizer-BioNTech COVID-19 vaccine (e.g., cold-chain storage requirements or large minimum order sizes) might limit access to the vaccine among some populations, which could negatively affect health equity. Advancing health equity, particularly in populations that experience disproportionate COVID-19 morbidity and mortality, requires engagement with community leaders, adolescent health care providers, and parents to identify and remove barriers to COVID-19 vaccination,” they added. The committee will continue to review safety and effectiveness data on the vaccine and noted that the 12-15-year-olds are eligible to enroll in vaccine safety monitoring programs such as CDC’s cellphone-based v-safe system. “The ACIP COVID-19 Vaccines Work Group, comprising experts in infectious diseases, vaccinology, vaccine safety, public health, and ethics, has held weekly meetings to review COVID-19 surveillance data, evidence for vaccine efficacy and safety, and implementation considerations for COVID-19 vaccines,” the report noted. ##Vaccines## It will take some time to implement new mask guidance from the US Centers for Disease Control and Prevention across the government, the White House said Friday, but changes in masking rules on federal property could be coming soon. “The CDC guidelines were just put out, as you all know, yesterday,” White House press secretary Jen Psaki told reporters during a press briefing. She reiterated the guidelines were “by the CDC, not by us, not by the White House, not by the President, to be very clear.” She said the masking guidelines were immediately adopted as policy at the White House for staffers and reporters. “We're working to implement it,” Psaki said of the new rules, but she added it “may take a couple of days. But certainly I would expect on federal lands, federal properties that the guidelines will be a guide.” President Biden’s first executive order upon taking office was to require masks on federal property. As CNN’s Maggie Fox reported at the time, the "100 Days Masking Challenge," symbolized the administration's
# acking breakthroughs involving people who were hospitalized or who died,” a CDC spokesperson told CNN in an email on Friday. The definition of a breakthrough case — a confirmed Covid-19 case at least two weeks post a second dose of Pfizer or Moderna’s vaccines or a single dose of  Johnson & Johnson vaccine — hasn’t changed. What is being updated is the data CDC collects and provides online. “This was done in order to focus on the cases of greatest clinical and public health importance,” the CDC spokesperson told CNN. Previously, states reported all cases of breakthrough infection, regardless of severity, to the CDC. States will continue to report all positive cases of Covid-19 to the CDC — including any mild or asymptomatic breakthrough cases — but the agency will not differentiate between mild or symptom-free cases in vaccinated versus unvaccinated people. It is unclear if states will continue to collect mild or asymptomatic breakthrough case data. The CDC spokesperson told CNN that the change in breakthrough case reporting would not affect the understanding of vaccine efficacy. “CDC is still doing studies on mild breakthrough infections, so people should not be worried that we are going to miss important data related to mild vaccine breakthrough infections,” the spokesperson said. As of April 26, the CDC reported 9,245 cases of breakthrough infections among the 95 million people vaccinated against coronavirus, though the case count is believed to be higher. Health officials have expressed concern that new variants or the virus could reduce vaccine effectiveness. As effectiveness goes down, more breakthrough cases can be expected. ##Vaccines## Nepal is reporting more than 8,000 new coronavirus cases on Friday, for the 10th straight day, according to data released by the Nepal Ministry of Health.  There have been a total of 439,658 cases and 4,669 deaths in Nepal. About 20% of Nepal's total cases were reported in the last 10 days, as well as 1/4 of its coronavirus-related deaths. International assistance: The country is expecting a second batch of oxygen cylinders from China, part of the 20,000 cylinders China pledged to support Nepal. According to a photo tweeted by the Chinese ambassador to Nepal, the second batch should be arriving in Kathmandu in the next few days. On Wednesday, the head of the United States Agency for International Development Covid-19 task force Jeremy Konyndyk told a Senate Foreign Relations Committee hearing that Nepal, alongside with India, is "the highest priority right now." "Recently we put another $10 million in, just in the past few weeks and we plan on additional aid deliveries and any kind of assistance that will be transported in, particularly on diagnostics and testing," Konyndyk said. More than 155 million people in the United States have received at least one dose of Covid-19 vaccine, including about 2.4 million children under 18, according to data published Friday by the US Centers for Disease Control and Prevention. Overall, 268,438,666 total doses have been reported administered, about 79% of the 341,865,945 doses delivered. That’s about 1.8 million more doses reported administered since Thursday, for a seven-day average of just under 2 million doses per day. Nearly 47% of the US population has received at least one dose of Covid-19 vaccine and about 36% of the US population is fully vaccinated. Among those age 12 and older — younger children are not yet eligible for any coronavirus vaccines — about 55% have received at least one dose and about 43% are fully vaccinated, CDC data shows. The US Food and Drug Administration extended its emergency use authorization for Pfizer/BioNTech's coronavirus vaccine in 12-to-15-year-olds on Monday. CDC Director Dr. Rochelle Walensky said Wednesday the agency now recommends the use of this vaccine for that age range after the CDC's Advisory Committee on Immunization Practices' (ACIP) voted unanimously to recommend giving that vaccine to kids as young as 12. Note: Data published by the CDC may be delayed, and doses may not have been given on the day reported. ##Vaccines## Cuban health officials reported 1,277 new cases of coronavirus on Friday, the highest daily increase since the beginning of the pandemic. Health officials also reported at least seven new coronavirus-related deaths, bringing the total number of deaths to 785.  Cuba had managed to keep the spread of Covid-19 under control, but after reopening its borders near the end of 2020, the island has seen a surge in cases. Cuban officials have begun to distribute the island’s homegrown vaccine candidates more widely in an attempt to lessen the impact of the virus. Mask mandates and social distancing in Canada should be kept in place for months, and indoor gatherings will not be recommended until at least the fall when more than 75% of Canadians will be fully vaccinated, health officials said Friday. “On a national level we’re seeing hopeful signs that we’ve passed the peak of
# """
#
# print(len(text))
# count = 1
# if len(text) > 5000:
#     count = len(text) // 5000 + 1
#
# print(count)
# for i in range(0, count):
#     print(i)
#     temp_text = text[5000 * i:5000 * (i + 1)]
#     print(len(temp_text))

# import os, sys
#
# root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# print(root_path)

