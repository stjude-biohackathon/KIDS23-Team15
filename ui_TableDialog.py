# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tabledialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ColorTableDialog(object):
    def setupUi(self, ColorTableDialog):
        ColorTableDialog.setObjectName("ColorTableDialog")
        ColorTableDialog.resize(399, 534)
        self.gridLayout = QtWidgets.QGridLayout(ColorTableDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonConfirm = QtWidgets.QPushButton(ColorTableDialog)
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.gridLayout.addWidget(self.pushButtonConfirm, 3, 1, 1, 1)
        self.pushButtonCancel = QtWidgets.QPushButton(ColorTableDialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout.addWidget(self.pushButtonCancel, 3, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(ColorTableDialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(196, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(ColorTableDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.radioButton = QtWidgets.QRadioButton(ColorTableDialog)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 3)

        self.retranslateUi(ColorTableDialog)
        QtCore.QMetaObject.connectSlotsByName(ColorTableDialog)

    def retranslateUi(self, ColorTableDialog):
        _translate = QtCore.QCoreApplication.translate
        ColorTableDialog.setWindowTitle(_translate("ColorTableDialog", "Dialog"))
        self.pushButtonConfirm.setText(_translate("ColorTableDialog", "Confirm"))
        self.pushButtonCancel.setText(_translate("ColorTableDialog", "Cancel"))
        self.label.setText(_translate("ColorTableDialog", "Please uncheck all groups that you want to ignore"))
        self.radioButton.setText(_translate("ColorTableDialog", "Check all"))
