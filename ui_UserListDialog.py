# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserListdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserListDialog(object):
    def setupUi(self, UserListDialog):
        UserListDialog.setObjectName("UserListDialog")
        UserListDialog.resize(506, 735)
        self.gridLayout = QtWidgets.QGridLayout(UserListDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(UserListDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(UserListDialog)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 2)
        self.pushButtonLocate = QtWidgets.QPushButton(UserListDialog)
        self.pushButtonLocate.setObjectName("pushButtonLocate")
        self.gridLayout.addWidget(self.pushButtonLocate, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.pushButtonCancel = QtWidgets.QPushButton(UserListDialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout.addWidget(self.pushButtonCancel, 3, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(UserListDialog)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(UserListDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)

        self.retranslateUi(UserListDialog)
        QtCore.QMetaObject.connectSlotsByName(UserListDialog)

    def retranslateUi(self, UserListDialog):
        _translate = QtCore.QCoreApplication.translate
        UserListDialog.setWindowTitle(_translate("UserListDialog", "Dialog"))
        self.label.setText(_translate("UserListDialog", "Field Name:"))
        self.pushButtonLocate.setText(_translate("UserListDialog", "Locate records"))
        self.pushButtonCancel.setText(_translate("UserListDialog", "Cancel"))
        self.label_2.setText(_translate("UserListDialog", "Please type or paste all values below (one value in each line):"))
