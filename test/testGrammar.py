# -*- coding:utf-8 -*-
# for i in range(1, 22, 10):
#     print("current index=" + i)

# a = set(["wsj", "cnn", "foxnes"])
#
# for item in a:
#     if item=="wsj":
#         a.remove(item)
#
# print(a)


# print("+".join(["a","b"]))

# import re
#
# src_text = """[[["你好，世界","hello world",null,null,1]
# ]
# ,null,"en",null,null,null,null,[]
# ]"""
# print(re.search("\"(.+?)\"", src_text)[1])

# text = [['自2000年代中期美国房地产繁荣以来，大流行的一年中全球房价涨幅最大。', 'The year of the pandemic saw the largest increase in global house prices since the U.S. housing boom of the mid-2000s.', None, None, 3, None, None, [[]], [[['10557117644f7a91d109812a56f5d3fe', 'en_zh_2021q1.md']]]], ['并且没有迹象表明涨势即将结束。\n\n', 'And there is no sign the rally is coming to an end.\n\n', None, None, 3, None, None, [[]], [[['10557117644f7a91d109812a56f5d3fe', 'en_zh_2021q1.md']], [None, True]]], ['这为全球从 Covid-19 复苏提供了直接的经济支持，但长期的房价上涨将意味着金融稳定面临新的重大问题。', 'That provides immediate economic support for the global recovery from Covid-19  But a prolonged house price upswing would mean big new problems for financial stability.', None, None, 3, None, None, [[]], [[['10557117644f7a91d109812a56f5d3fe', 'en_zh_2021q1.md']]]], ['如果习惯了单向住\u200b\u200b房押注的中产阶级公民突然发现地毯从他们的下方拉出，这可能会导致经济冲突。\n\n', 'And it could result in economic strife if middle-class citizens accustomed to a one-way housing bet suddenly find the rug pulled out from beneath them down the line.\n\n', None, None, 3, None, None, [[]], [[['b3ad15e7a0073e77814019b341d18493', 'en_zh_2019q3.md']], [None, True]]], ['去年，达拉斯联邦储备银行监测的 16 个经济体的房价上涨了 4.91%，这是自 2006 年以来的最大涨幅。按照正常年份的标准来看，涨幅很大——但在全球经济收缩约', 'House prices rose by 4.91% across 16 economies monitored by the Federal Reserve Bank of Dallas last year, the sharpest increase since 2006. The move was large by the standards of a normal year—but explosive in the context of a global economic contraction of around', None, None, 3, None, None, [[]], [[['10557117644f7a91d109812a56f5d3fe', 'en_zh_2021q1.md']]]], ['3.3%。\n\n', '3.3%.\n\n', None, None, 3, None, None, [[]], [[['10557117644f7a91d109812a56f5d3fe', 'en_zh_2021q1.md']], [None, True]]], ['而且这一趋势几乎没有减弱的迹象。', 'And the trend shows little sign of abating.', None, None, 3, None, None, [[]], [[['10557117644f7a91d109812a56f5d3fe', 'en_zh_2021q1.md']]]], ['美国住房市场缺少买家需求的数百万套房屋。', 'The U.S. housing market is millions of homes short of buyer demand.', None, None, 3, None, None, [[]], [[['b3ad15e7a0073e77814019b341d18493', 'en_zh_2019q3.md']]]], ['欧元区、韩国、澳大利亚、新西兰和加拿大等地的价格都在攀升。\n\n', 'Prices have climbed in places as varied as the eurozone, South Korea, Australia, New Zealand and Canada.\n\n', None, None, 3, None, None, [[]], [[['10557117644f7a91d109812a56f5d3fe', 'en_zh_2021q1.md']], [None, True]]], ['物价飞涨反映了从2008年金融危机爆发以来与大流行后的新生热潮之间的重大区别。', 'Booming prices reflect a major difference between the liftoff from the financial crisis of 2008 and the nascent post-pandemic boom.', None, None, 3, None, None, [[]], [[['b3ad15e7a0073e77814019b341d18493', 'en_zh_2019q3.md']]]], ['金融危机源于脆弱的，资本不足的银行业：危机后的明显反应是更为保守地放贷。', 'The financial crisis emanated from a fragile, undercapitalized banking sector: The obvious postcrisis response was to lend much more conservatively.', None, None, 3, None, None, [[]], [[['b3ad15e7a0073e77814019b341d18493', 'en_zh_2019q3.md']]]], ['但是，从去年初开始，银行的扩张程度就大大降低了，在政府的大力支持下，银行能够更快地将降息转嫁给借款人。', 'But at the beginning of last year, banks were far less overextended and, with greater government support, were much more rapidly able to pass on interest rate cuts to borrowers.', None, None, 3, None, None, [[]], [[['b3ad15e7a0073e77814019b341d18493', 'en_zh_2019q3.md']]]]]
# for item in text:
#     print(item[0])

import datetime, re
#
# now = datetime.datetime.now()
# print(now.strftime("%Y%m%d"))
#
# str1 = "June 11, 2021 04:43 pm ET"
# str2 = "30 minutes ago"
# print(datetime.datetime.strptime(str1, "%Y%m%d"))
# hours_match = re.match(r"(\d+)\s+hours.+ago", str1)
# # minutes_match = re.match(r"(\d+)\s+minutes.+ago", str2)
# if hours_match:
#     print(int(hours_match.group(1)))
#     n_hours_before = now - datetime.timedelta(hours=int(hours_match.group(1)))
#     print(n_hours_before.strftime("%Y%m%d"))
# if minutes_match:
#     print(int(minutes_match.group(1)))
#     n_minutes_before = now - datetime.timedelta(minutes=int(minutes_match.group(1)))
#     print(n_minutes_before.strftime("%Y%m%d"))
# str3 = "{'a':'a','b':2}"
# name = "nnnnn"
# str4 = f"{'name':{name}}"
# print(str4)
# d = dict(eval(str3))
# print(type(d.get("b")))

print(re.split(r"\s+", "a  b".strip()))