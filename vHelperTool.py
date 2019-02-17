from vHelperToolUI import Ui_vHelperTool
from vHelperToolDB import *
from PyQt5 import QtWidgets, QtCore
import sys, os, ctypes, webbrowser


class MyApp(QtWidgets.QDialog):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_vHelperTool()
        self.ui.setupUi(self)

        # Fill the combobox with all Registry keys
        x = 0
        while x < len(RegKeyList):
            strRegKeyList = str(RegKeyList[x].name)
            self.ui.registrylist_comboBox.addItem(strRegKeyList)
            x += 1

        # call method to update all form values and check safety
        self.refresh()
        self.overridesafety()

        # Actions:
        self.ui.registrylist_comboBox.currentIndexChanged.connect(self.refresh)
        self.ui.set_reg_button.clicked.connect(self.setbuttonclick)
        self.ui.reset_reg_buton.clicked.connect(self.resetbuttonclick)
        self.ui.delete_reg_button.clicked.connect(self.deletebuttonclick)
        self.ui.safety_check.clicked.connect(self.overridesafety)
        self.ui.kburl_pushbutton.clicked.connect(self.clickkburl)

    def setbuttonclick(self):
        currentitem = self.ui.registrylist_comboBox.currentIndex()
        key = RegKeyList[currentitem]
        if key.registry_type is 4:
            value, ok = QtWidgets.QInputDialog.getInt(self, key.name, "New registry value")
            if self.warning():
                if value < 0:
                    value = 0
                if value > 65535:
                    value = 65535
                key.set_reg(value)
        if key.registry_type is 1:
            path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Please select a new path:',
                                                              'C:\\', QtWidgets.QFileDialog.ShowDirsOnly)
            path = QtCore.QDir.toNativeSeparators(path)
            if self.warning():
                key.set_reg(path)
        self.refresh()

    def resetbuttonclick(self):
        currentitem = self.ui.registrylist_comboBox.currentIndex()
        key = RegKeyList[currentitem]
        if self.warning():
            key.reset_reg()
        self.refresh()

    def deletebuttonclick(self):
        currentitem = self.ui.registrylist_comboBox.currentIndex()
        key = RegKeyList[currentitem]
        if self.warning():
            key.deletevalue_reg()
        self.refresh()

    def clickkburl(self):
        currentitem = self.ui.registrylist_comboBox.currentIndex()
        kb_number = str(RegKeyList[currentitem].kb)
        base_url = 'http://veeam.com/'
        url = base_url + kb_number
        webbrowser.get().open(url)

    def overridesafety(self):
        checkbox = str(self.ui.safety_check.isChecked())
        if checkbox == "False":
            self.ui.set_reg_button.setEnabled(False)
            self.ui.reset_reg_buton.setEnabled(False)
            self.ui.delete_reg_button.setEnabled(False)
        else:
            self.ui.set_reg_button.setEnabled(True)
            self.ui.reset_reg_buton.setEnabled(True)
            self.ui.delete_reg_button.setEnabled(True)

    def warning(self):
        answer = QtWidgets.QMessageBox.warning(self, 'WARNING', 'Are you sure you want to change the registry value?\n'
                                                     'As it can lead to unwanted results',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if answer == 16384:  # 16384 == TRUE
            return True
        else:
            return False

    def refresh(self):
        currentitem = self.ui.registrylist_comboBox.currentIndex()
        currentvalue = str(RegKeyList[currentitem].get_reg())
        regkeydiscription_label_text = RegKeyList[currentitem].description

        # If the current registry has no KB article value determined, the button disables
        if RegKeyList[currentitem].kb is "None":
            self.ui.kburl_pushbutton.setEnabled(False)
            kb_number = "Unknown kb article"
        else:
            self.ui.kburl_pushbutton.setEnabled(True)
            kb_number = str(RegKeyList[currentitem].kb)

        # If the current registry has no default value determined, the default buttons disables
        self.ui.safety_check.setChecked(False)
        self.overridesafety()
        if RegKeyList[currentitem].defaultvalue is None:
            self.ui.reset_reg_buton.setEnabled(False)

        # Draw label text
        self.ui.regkeydiscription_label.setText(regkeydiscription_label_text)
        self.ui.regkeyvalue_label.setText(currentvalue)
        self.ui.kburl_pushbutton.setText(kb_number)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    msg = 0
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    while is_admin is False and msg == 0:
        QtWidgets.QMessageBox.information(window, 'Information', 'vHelperTool started without administrative '
                                                                 'permissions \n and therefore cannot make changes '
                                                                 'to the registry.')
        msg = 1
    window.show()
    sys.exit(app.exec_())
