# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Bart\SkyDrive\Documenten\Prive\Python\vHelperToolv2\vHelperToolv2\vHelperToolUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_vHelperTool(object):
    def setupUi(self, vHelperTool):
        vHelperTool.setObjectName("vHelperTool")
        vHelperTool.resize(392, 558)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(vHelperTool.sizePolicy().hasHeightForWidth())
        vHelperTool.setSizePolicy(sizePolicy)
        vHelperTool.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        vHelperTool.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        vHelperTool.setWindowIcon(icon)
        self.regkeyname_label = QtWidgets.QLabel(vHelperTool)
        self.regkeyname_label.setGeometry(QtCore.QRect(20, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.regkeyname_label.setFont(font)
        self.regkeyname_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.regkeyname_label.setOpenExternalLinks(False)
        self.regkeyname_label.setObjectName("regkeyname_label")
        self.regkeyvalue_label = QtWidgets.QLabel(vHelperTool)
        self.regkeyvalue_label.setGeometry(QtCore.QRect(20, 350, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.regkeyvalue_label.setFont(font)
        self.regkeyvalue_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.regkeyvalue_label.setWordWrap(True)
        self.regkeyvalue_label.setOpenExternalLinks(False)
        self.regkeyvalue_label.setObjectName("regkeyvalue_label")
        self.regkeydiscription_label = QtWidgets.QLabel(vHelperTool)
        self.regkeydiscription_label.setGeometry(QtCore.QRect(20, 90, 351, 191))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.regkeydiscription_label.setFont(font)
        self.regkeydiscription_label.setAutoFillBackground(False)
        self.regkeydiscription_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.regkeydiscription_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.regkeydiscription_label.setText("")
        self.regkeydiscription_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.regkeydiscription_label.setWordWrap(True)
        self.regkeydiscription_label.setObjectName("regkeydiscription_label")
        self.groupBox = QtWidgets.QGroupBox(vHelperTool)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.registrylist_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.registrylist_comboBox.setGeometry(QtCore.QRect(10, 20, 351, 22))
        self.registrylist_comboBox.setObjectName("registrylist_comboBox")
        self.currentsetting_label = QtWidgets.QLabel(vHelperTool)
        self.currentsetting_label.setGeometry(QtCore.QRect(20, 330, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.currentsetting_label.setFont(font)
        self.currentsetting_label.setObjectName("currentsetting_label")
        self.set_reg_button = QtWidgets.QPushButton(vHelperTool)
        self.set_reg_button.setEnabled(True)
        self.set_reg_button.setGeometry(QtCore.QRect(20, 410, 201, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.set_reg_button.setFont(font)
        self.set_reg_button.setAcceptDrops(False)
        self.set_reg_button.setFlat(False)
        self.set_reg_button.setObjectName("set_reg_button")
        self.reset_reg_buton = QtWidgets.QPushButton(vHelperTool)
        self.reset_reg_buton.setGeometry(QtCore.QRect(20, 440, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.reset_reg_buton.setFont(font)
        self.reset_reg_buton.setObjectName("reset_reg_buton")
        self.delete_reg_button = QtWidgets.QPushButton(vHelperTool)
        self.delete_reg_button.setGeometry(QtCore.QRect(150, 440, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.delete_reg_button.setFont(font)
        self.delete_reg_button.setObjectName("delete_reg_button")
        self.safety_check = QtWidgets.QCheckBox(vHelperTool)
        self.safety_check.setEnabled(True)
        self.safety_check.setGeometry(QtCore.QRect(260, 450, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.safety_check.setFont(font)
        self.safety_check.setChecked(False)
        self.safety_check.setObjectName("safety_check")
        self.label = QtWidgets.QLabel(vHelperTool)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 490, 381, 61))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(vHelperTool)
        self.label_2.setGeometry(QtCore.QRect(10, 540, 71, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.kburl_pushbutton = QtWidgets.QPushButton(vHelperTool)
        self.kburl_pushbutton.setGeometry(QtCore.QRect(230, 60, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kburl_pushbutton.sizePolicy().hasHeightForWidth())
        self.kburl_pushbutton.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.kburl_pushbutton.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.kburl_pushbutton.setFont(font)
        self.kburl_pushbutton.setFlat(True)
        self.kburl_pushbutton.setObjectName("kburl_pushbutton")
        self.groupBox.raise_()
        self.regkeyname_label.raise_()
        self.regkeyvalue_label.raise_()
        self.regkeydiscription_label.raise_()
        self.currentsetting_label.raise_()
        self.set_reg_button.raise_()
        self.reset_reg_buton.raise_()
        self.delete_reg_button.raise_()
        self.safety_check.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.kburl_pushbutton.raise_()

        self.retranslateUi(vHelperTool)
        QtCore.QMetaObject.connectSlotsByName(vHelperTool)

    def retranslateUi(self, vHelperTool):
        _translate = QtCore.QCoreApplication.translate
        vHelperTool.setWindowTitle(_translate("vHelperTool", "vHelperTool v0.2"))
        self.regkeyname_label.setText(_translate("vHelperTool", "Description"))
        self.regkeyvalue_label.setText(_translate("vHelperTool", "registry_value"))
        self.groupBox.setTitle(_translate("vHelperTool", "Select registry value to edit"))
        self.currentsetting_label.setText(_translate("vHelperTool", "Current Setting:"))
        self.set_reg_button.setText(_translate("vHelperTool", "Set registry value"))
        self.reset_reg_buton.setText(_translate("vHelperTool", "set  default value"))
        self.delete_reg_button.setText(_translate("vHelperTool", "Delete"))
        self.safety_check.setText(_translate("vHelperTool", "Override Safety"))
        self.label_2.setText(_translate("vHelperTool", "Powered by"))
        self.kburl_pushbutton.setText(_translate("vHelperTool", "Registry KB Article"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vHelperTool = QtWidgets.QWidget()
    ui = Ui_vHelperTool()
    ui.setupUi(vHelperTool)
    vHelperTool.show()
    sys.exit(app.exec_())
