# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inhonor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1119, 631)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1121, 651))
        self.label.setStyleSheet("background-image: url(:/setu1/ziyuan/231.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1410, 112))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setStyleSheet("font: 26pt \"隶书\";\n"
"color:rgb(194, 255, 52);\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 170, 371, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.randompic = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.randompic.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 24pt \"楷体\";\n"
"background-color: rgb(85, 255, 255);\n"
";")
        self.randompic.setObjectName("randompic")
        self.verticalLayout.addWidget(self.randompic)
        self.iw233 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.iw233.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 24pt \"楷体\";\n"
"background-color: rgb(85, 255, 255);")
        self.iw233.setObjectName("iw233")
        self.verticalLayout.addWidget(self.iw233)
        self.xing = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.xing.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 24pt \"楷体\";\n"
"background-color: rgb(85, 255, 255);")
        self.xing.setObjectName("xing")
        self.verticalLayout.addWidget(self.xing)
        self.yin = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.yin.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 24pt \"楷体\";\n"
"background-color: rgb(85, 255, 255);")
        self.yin.setObjectName("yin")
        self.verticalLayout.addWidget(self.yin)
        self.cat = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cat.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 24pt \"楷体\";\n"
"background-color: rgb(85, 255, 255);")
        self.cat.setObjectName("cat")
        self.verticalLayout.addWidget(self.cat)
        self.mp = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.mp.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 24pt \"楷体\";\n"
"background-color: rgb(85, 255, 255);")
        self.mp.setObjectName("mp")
        self.verticalLayout.addWidget(self.mp)
        self.pc = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.pc.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 24pt \"楷体\";\n"
"background-color: rgb(85, 255, 255);")
        self.pc.setObjectName("pc")
        self.verticalLayout.addWidget(self.pc)
        self.top = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.top.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 24pt \"楷体\";\n"
"background-color: rgb(85, 255, 255);")
        self.top.setObjectName("top")
        self.verticalLayout.addWidget(self.top)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 115, 331, 60))
        self.label_3.setStyleSheet("font: 25 14pt \"等线 Light\";\n"
"text-decoration: underline;\n"
"color:rgb(255, 255, 0)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(830, 110, 261, 121))
        self.label_4.setStyleSheet("font: 22pt \"隶书\";\n"
"color:rgb(255, 255, 0)")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(820, 230, 281, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(870, 350, 191, 271))
        self.pushButton.setStyleSheet("background-image: url(:/setu1/ziyuan/d5177cc8c9de103428d4e09c41ca08fb.jpg);\n"
"color: rgb(0, 255, 255);\n"
"font: 26pt \"方正舒体\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "壁纸下载器纪念版"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>欢迎使用“二次元图片下载器最终纪念版本”！</p><p>祝你下载图片过得愉快！</p></body></html>"))
        self.randompic.setText(_translate("Form", "随机壁纸全部图"))
        self.iw233.setText(_translate("Form", "随即壁纸无色图"))
        self.xing.setText(_translate("Form", "正常的星空"))
        self.yin.setText(_translate("Form", "白毛控"))
        self.cat.setText(_translate("Form", "兽耳娘"))
        self.mp.setText(_translate("Form", "竖屏壁纸"))
        self.pc.setText(_translate("Form", "横屏壁纸"))
        self.top.setText(_translate("Form", "壁纸推荐"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\">作者：scu机工  赵某</p><p>QQ(小号)3439912523，欢迎交流</p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p>请输入你所期望</p><p>的图片的张数</p></body></html>"))
        self.lineEdit.setText(_translate("Form",""))
        self.pushButton.setText(_translate("Form", "确定成图"))
import setu_rc
