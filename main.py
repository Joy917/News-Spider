import re
import sys
import os
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow

from ui.MainWindow import Ui_MainWindow
from spiders import bbc_spider
from spiders import cnn_spider
from spiders import foxnews_spider
from spiders import wsj_spider
from spiders import olympics_world_spider
from spiders import olympics_tokyo_spider
from spiders import politico_spider
from spiders import thehill_spider


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 增加槽链接
        self.pushButton.clicked.connect(self.start_crawl)

    def start_crawl(self):
        # 获取当前输入
        start_date = self.start_date.text().replace("/", "")
        end_date = self.end_date.text().replace("/", "")
        keywords = re.split(r"\s+", self.lineEdit.text().strip())
        target_sites = []
        if self.checkBox_wsj.isChecked(): target_sites.append("wsj")
        if self.checkBox_cnn.isChecked(): target_sites.append("cnn")
        if self.checkBox_bbc.isChecked(): target_sites.append("bbc")
        if self.checkBox_foxnews.isChecked(): target_sites.append("foxnews")
        if self.checkBox_olympics_tokyo.isChecked(): target_sites.append("olympics_tokyo")
        if self.checkBox_olympics_world.isChecked(): target_sites.append("olympics_world")
        if self.checkBox_politico.isChecked(): target_sites.append("politico")
        if self.checkBox_thehill.isChecked(): target_sites.append("thehill")

        # 无效参数
        if len(keywords) == 0 or int(start_date) > int(end_date) or len(target_sites) <= 0:
            self.label_info.setText("input invalid, please check the parameters!")
            return

        # 创建关键词目录
        dir_name = f"D:\\spiderResult\\{'+'.join(keywords)}"
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        # 开始爬取
        print("spiders are running, please wait...")
        self.label_info.setText("spiders are running, please wait...")
        # 批量启动并阻塞线程
        try:
            threading_pool = []
            for id, site in enumerate(target_sites, start=1):
                if site == "wsj":
                    threading_pool.append(wsj_spider.Task(id, site, dir_name, keywords, start_date, end_date))
                if site == "cnn":
                    threading_pool.append(cnn_spider.Task(id, site, dir_name, keywords, start_date, end_date))
                if site == "bbc":
                    threading_pool.append(bbc_spider.Task(id, site, dir_name, keywords, start_date, end_date))
                if site == "foxnews":
                    threading_pool.append(foxnews_spider.Task(id, site, dir_name, keywords, start_date, end_date))
                if site == "olympics_tokyo":
                    threading_pool.append(olympics_tokyo_spider.Task(id, site, dir_name, keywords, start_date, end_date))
                if site == "olympics_world":
                    threading_pool.append(olympics_world_spider.Task(id, site, dir_name, keywords, start_date, end_date))
                if site == "politico":
                    threading_pool.append(politico_spider.Task(id, site, dir_name, keywords, start_date, end_date))
                if site == "thehill":
                    threading_pool.append(thehill_spider.Task(id, site, dir_name, keywords, start_date, end_date))

            for th in threading_pool:
                th.start()
            for th in threading_pool:
                th.join()
        except Exception as exc:
            print(f"Happened an error ! please check")
        finally:
            self.label_info.setText("please check the result in D:\\spiderResult")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
