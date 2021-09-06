import re
import sys
import os

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QThread, Signal

import utils

from ui import MainWindow
from spiders import bbc_spider
from spiders import cnn_spider
from spiders import foxnews_spider
from spiders import wsj_spider
from spiders import olympics_world_spider
from spiders import olympics_tokyo_spider
from spiders import politico_spider
from spiders import thehill_spider


# 爬虫主线程，继承QThread
class Runthread(QThread):
    #  通过类成员对象定义信号对象
    _signal = Signal(str)

    def __init__(self, target_sites, keywords, start_date, end_date):
        super(Runthread, self).__init__()
        self.target_sites = target_sites
        self.keywords = keywords
        self.start_date = start_date
        self.end_date = end_date

    def run(self):
        # 检查关键词目录，不存在则创建
        result_dir = os.path.join(utils.project_dir(), f"spiderResult\\{'+'.join(self.keywords)}")
        if not os.path.isdir(result_dir):
            self.target_sites.clear()
            os.makedirs(result_dir)
        self._signal.emit(f"resultPath:{result_dir}")
        # 开始爬取
        # 批量启动并阻塞线程
        try:
            threading_pool = []
            for id, site in enumerate(self.target_sites, start=1):
                if site == "WSJ":
                    threading_pool.append(
                        wsj_spider.Task(id, site, result_dir, self.keywords, self.start_date, self.end_date,
                                        self._signal))
                elif site == "CNN":
                    threading_pool.append(
                        cnn_spider.Task(id, site, result_dir, self.keywords, self.start_date, self.end_date,
                                        self._signal))
                elif site == "BBC":
                    threading_pool.append(
                        bbc_spider.Task(id, site, result_dir, self.keywords, self.start_date, self.end_date,
                                        self._signal))
                elif site == "FoxNews":
                    threading_pool.append(
                        foxnews_spider.Task(id, site, result_dir, self.keywords, self.start_date, self.end_date,
                                            self._signal))
                elif site == "Olympics_Tokyo":
                    threading_pool.append(
                        olympics_tokyo_spider.Task(id, site, result_dir, self.keywords, self.start_date, self.end_date,
                                                   self._signal))
                elif site == "Olympics_World":
                    threading_pool.append(
                        olympics_world_spider.Task(id, site, result_dir, self.keywords, self.start_date, self.end_date,
                                                   self._signal))
                elif site == "Politico":
                    threading_pool.append(
                        politico_spider.Task(id, site, result_dir, self.keywords, self.start_date, self.end_date,
                                             self._signal))
                elif site == "TheHill":
                    threading_pool.append(
                        thehill_spider.Task(id, site, result_dir, self.keywords, self.start_date, self.end_date,
                                            self._signal))

            for th in threading_pool:
                th.start()
            for th in threading_pool:
                th.join()
        except:
            pass

# 界面主线程
class Window(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        os.putenv("PYTHONUNBUFFERED", "1")

        self.start_date_content = ""
        self.end_date_content = ""
        self.keywords = []
        self.target_sites = []
        self.thread = None

        self.count_down = 0
        # 增加槽链接
        self.pushButton.clicked.connect(self.start_crawl)

    def start_spiders(self):
        self.count_down = 0
        # 运行期间按钮失效，防止多次启动任务
        self.pushButton.setDisabled(True)
        # 创建线程
        self.thread = Runthread(self.target_sites, self.keywords, self.start_date_content, self.end_date_content)
        # 连接信号
        # self.thread.Daemon = True
        self.thread._signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
        # 开始线程
        self.thread.start()

    def log(self, msg):
        self.textBrowser.append(f"{utils.now_timestamp(mode='human')} {msg}")

    def call_backlog(self, msg):
        if msg.__contains__("end"):
            self.count_down += 1
        self.log(msg)
        if self.count_down == len(self.target_sites):
            self.pushButton.setEnabled(True)

    def start_crawl(self):
        self.target_sites.clear()
        # 获取当前输入
        self.start_date_content = self.start_date.text().replace("/", "")
        self.end_date_content = self.end_date.text().replace("/", "")
        line_edit = self.lineEdit.text().strip()
        if line_edit != "": self.keywords = re.split(r"\s+", line_edit)
        if self.checkBox_wsj.isChecked(): self.target_sites.append("WSJ")
        if self.checkBox_cnn.isChecked(): self.target_sites.append("CNN")
        if self.checkBox_bbc.isChecked(): self.target_sites.append("BBC")
        if self.checkBox_foxnews.isChecked(): self.target_sites.append("FoxNews")
        if self.checkBox_olympics_tokyo.isChecked(): self.target_sites.append("Olympics_Tokyo")
        if self.checkBox_olympics_world.isChecked(): self.target_sites.append("Olympics_World")
        if self.checkBox_politico.isChecked(): self.target_sites.append("Politico")
        if self.checkBox_thehill.isChecked(): self.target_sites.append("TheHill")

        # 无效参数
        if len(self.keywords) == 0 or int(self.start_date_content) > int(self.end_date_content) or len(
                self.target_sites) <= 0:
            self.log("input invalid, please check the parameters!")
            return
        self.start_spiders()


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
