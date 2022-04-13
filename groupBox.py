


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(295, 402)
        self.showList = QtWidgets.QListWidget(Form)
        self.showList.setGeometry(QtCore.QRect(-5, 0, 321, 411))
        self.showList.setStyleSheet("QListWidget{    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    margin-top:20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QListWidget::item{\n"
"    border-color: rgb(255, 255, 255);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QListWidget::item:selected{\n"
"    background-color: rgb(170, 170, 255);\n"
"}\n"
"\n"
"QListWidget::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QListWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QListWidget::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QListWidget::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.showList.setObjectName("showList")
        self.btn_minimize = QtWidgets.QPushButton(Form)
        self.btn_minimize.setGeometry(QtCore.QRect(220, 0, 40, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(29, 29, 29);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(85, 0, 0);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-window-minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setObjectName("btn_minimize")
        self.btn_close = QtWidgets.QPushButton(Form)
        self.btn_close.setGeometry(QtCore.QRect(260, 0, 40, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(29, 29, 29);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_close.setIcon(icon)
        self.btn_close.setObjectName("btn_close")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Show Recently", "Show Recently"))
        self.btn_minimize.setToolTip(_translate("Form", "Minimize"))
        self.btn_minimize.setText(_translate("Form", "-"))
        self.btn_close.setToolTip(_translate("Form", "Close"))
        self.btn_close.setText(_translate("Form", "X"))
