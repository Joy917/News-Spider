import re
import sys
import os
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow

import utils
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
        if self.checkBox_wsj.isChecked(): target_sites.append("WSJ")
        if self.checkBox_cnn.isChecked(): target_sites.append("CNN")
        if self.checkBox_bbc.isChecked(): target_sites.append("BBC")
        if self.checkBox_foxnews.isChecked(): target_sites.append("FoxNews")
        if self.checkBox_olympics_tokyo.isChecked(): target_sites.append("Olympics_Tokyo")
        if self.checkBox_olympics_world.isChecked(): target_sites.append("Olympics_World")
        if self.checkBox_politico.isChecked(): target_sites.append("Politico")
        if self.checkBox_thehill.isChecked(): target_sites.append("TheHill")

        # 无效参数
        if len(keywords) == 0 or int(start_date) > int(end_date) or len(target_sites) <= 0:
            self.label_info.setText("input invalid, please check the parameters!")
            return

        # 创建关键词目录
        result_dir = os.path.join(utils.project_dir(), f"spiderResult\\{'+'.join(keywords)}")
        if not os.path.isdir(result_dir):
            os.makedirs(result_dir)
        # 开始爬取
        print("spiders are running, please wait...")
        # 批量启动并阻塞线程
        try:
            threading_pool = []
            for id, site in enumerate(target_sites, start=1):
                if site == "WSJ":
                    threading_pool.append(wsj_spider.Task(id, site, result_dir, keywords, start_date, end_date))
                if site == "CNN":
                    threading_pool.append(cnn_spider.Task(id, site, result_dir, keywords, start_date, end_date))
                if site == "BBC":
                    threading_pool.append(bbc_spider.Task(id, site, result_dir, keywords, start_date, end_date))
                if site == "FoxNews":
                    threading_pool.append(foxnews_spider.Task(id, site, result_dir, keywords, start_date, end_date))
                if site == "Olympics_Tokyo":
                    threading_pool.append(
                        olympics_tokyo_spider.Task(id, site, result_dir, keywords, start_date, end_date))
                if site == "Olympics_World":
                    threading_pool.append(
                        olympics_world_spider.Task(id, site, result_dir, keywords, start_date, end_date))
                if site == "Politico":
                    threading_pool.append(politico_spider.Task(id, site, result_dir, keywords, start_date, end_date))
                if site == "TheHill":
                    threading_pool.append(thehill_spider.Task(id, site, result_dir, keywords, start_date, end_date))

            for th in threading_pool:
                th.start()
            for th in threading_pool:
                th.join()
        except:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
