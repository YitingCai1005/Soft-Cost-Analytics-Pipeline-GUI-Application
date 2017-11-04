# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(816, 604)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 191, 46))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 10, 150, 46))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 120, 181, 231))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label0 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label0.setObjectName(_fromUtf8("label0"))
        self.verticalLayout.addWidget(self.label0)
        self.label1 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.verticalLayout.addWidget(self.label1)
        self.label2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.verticalLayout.addWidget(self.label2)
        self.label3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label3.setObjectName(_fromUtf8("label3"))
        self.verticalLayout.addWidget(self.label3)
        self.label4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label4.setObjectName(_fromUtf8("label4"))
        self.verticalLayout.addWidget(self.label4)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(230, 120, 331, 231))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.comboBox0 = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox0.setObjectName(_fromUtf8("comboBox0"))
        self.verticalLayout_2.addWidget(self.comboBox0)
        self.comboBox1 = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox1.setObjectName(_fromUtf8("comboBox1"))
        self.verticalLayout_2.addWidget(self.comboBox1)
        self.comboBox2 = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox2.setObjectName(_fromUtf8("comboBox2"))
        self.verticalLayout_2.addWidget(self.comboBox2)
        self.comboBox3 = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox3.setObjectName(_fromUtf8("comboBox3"))
        self.verticalLayout_2.addWidget(self.comboBox3)
        self.comboBox4 = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox4.setObjectName(_fromUtf8("comboBox4"))
        self.verticalLayout_2.addWidget(self.comboBox4)
        self.GetRatio = QtGui.QPushButton(self.centralwidget)
        self.GetRatio.setGeometry(QtCore.QRect(580, 300, 150, 46))
        self.GetRatio.setObjectName(_fromUtf8("GetRatio"))
        self.result = QtGui.QTextEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(70, 370, 651, 140))
        self.result.setObjectName(_fromUtf8("result"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 38))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Load CSV File", None))
        self.pushButton_2.setText(_translate("MainWindow", "Close", None))
        self.label0.setText(_translate("MainWindow", "ColumnName", None))
        self.label1.setText(_translate("MainWindow", "ColumnName", None))
        self.label2.setText(_translate("MainWindow", "ColumnName", None))
        self.label3.setText(_translate("MainWindow", "ColumnName", None))
        self.label4.setText(_translate("MainWindow", "ColumnName", None))
        self.GetRatio.setText(_translate("MainWindow", "Get Ratio", None))

