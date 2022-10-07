from PyQt5 import QtWidgets, QtGui, QtCore
from inhonor import Ui_Form
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        MainWindow.setWindowIcon(self,QtGui.QIcon("ZhaoCake.ico"))
        self.setupUi(self)
        self.a = 0
        self.pushButton.clicked.connect(lambda :self.queding())



    # 此处编辑业务逻辑代码
    def getfunc(self):
        if self.randompic.isChecked() == True:
            self.a=1
        elif self.iw233.isChecked() == True:
            self.a=2
        elif self.xing.isChecked() == True:
            self.a=3
        elif self.yin.isChecked() == True:
            self.a=4
        elif self.cat.isChecked() == True:
            self.a=5
        elif self.mp.isChecked() == True:
            self.a=6
        elif self.pc.isChecked() == True:
            self.a=7
        elif self.top.isChecked() == True:
            self.a=8
        return self.a

    def getPics(self):
        founction = self.getfunc()
        if founction == 1:
            url = "https://iw233.cn/api.php?sort=random"
            root = ".//随机壁纸全部图//"
            for i in range(int(self.num)):
                th = threading.Thread(target=self.Getpics, args=(url, root))
                th.start()
                th.join()
        elif founction == 2:
            url = "https://iw233.cn/api.php?sort=iw233"
            root = ".//随机壁纸无色图//"
            for i in range(int(self.num)):
                th = threading.Thread(target=self.Getpics, args=(url, root))
                th.start()
                th.join()
        elif founction == 3:
            url = "https://iw233.cn/api.php?sort=xing"
            root = ".//正常的星空//"
            for i in range(int(self.num)):
                th = threading.Thread(target=self.Getpics, args=(url, root))
                th.start()
                th.join()
        elif founction == 4:
            url = "https://iw233.cn/api.php?sort=yin"
            root = ".//银发控//"
            for i in range(int(self.num)):
                th = threading.Thread(target=self.Getpics, args=(url, root))
                th.start()
                th.join()
        elif founction == 5:
            url = "https://iw233.cn/api.php?sort=cat"
            root = ".//兽耳控//"
            for i in range(int(self.num)):
                th = threading.Thread(target=self.Getpics, args=(url, root))
                th.start()
                th.join()
        elif founction == 6:
            url = "https://iw233.cn/api.php?sort=mp"
            root = ".//竖屏壁纸//"
            for i in range(int(self.num)):
                th = threading.Thread(target=self.Getpics, args=(url, root))
                th.start()
                th.join()
        elif founction == 7:
            url = "https://iw233.cn/api.php?sort=pc"
            root = ".//横屏壁纸//"
            for i in range(int(self.num)):
                th = threading.Thread(target=self.Getpics, args=(url, root))
                th.start()
                th.join()
        elif founction == 8:
            url = "https://iw233.cn/api.php?sort=top"
            root = ".//壁纸推荐//"
            for i in range(int(self.num)):
                th = threading.Thread(target=self.Getpics, args=(url, root))
                th.start()
                th.join()

    def Getpics(self, url, root):
        r = requests.get(url)
        path = root + r.headers['Content-Length'] + ".jpg"
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                    with open(path, 'wb') as f:
                        f.write(r.content)
                        f.close()
            else:
                pass
        except:
            QMessageBox.warning(self,"哦豁，出问题了","图片下载失败了欸！要不再试一次？",QMessageBox.Yes|QMessageBox.No)


    def queding(self):
        try:
            self.nums = self.lineEdit.text()
            self.num = int(self.nums)
            QMessageBox.information(self, "正在努力下载", "下载完毕后将会提示您的哦~", QMessageBox.Yes)
            self.getPics()
            QMessageBox.information(self,"下载完毕","本下载器再次肯定绝对绝对绝对不会有任何一张涩图！！！")
        except:
            QMessageBox.warning(self, "哦豁，出问题了", "图片下载失败了欸！要不再试一次？",QMessageBox.Yes | QMessageBox.No)


if __name__ == "__main__":
    import sys
    import requests
    import os
    import threading

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())