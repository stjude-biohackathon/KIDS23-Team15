# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MarkRecordsdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MarkRecordsDialog(object):
    def setupUi(self, MarkRecordsDialog):
        MarkRecordsDialog.setObjectName("MarkRecordsDialog")
        MarkRecordsDialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(MarkRecordsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonConfirm = QtWidgets.QPushButton(MarkRecordsDialog)
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.gridLayout.addWidget(self.pushButtonConfirm, 6, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(MarkRecordsDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(MarkRecordsDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 2)
        self.label = QtWidgets.QLabel(MarkRecordsDialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 89, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.pushButtonCancel = QtWidgets.QPushButton(MarkRecordsDialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout.addWidget(self.pushButtonCancel, 6, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(MarkRecordsDialog)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 3)
        self.lcdNumber = QtWidgets.QLCDNumber(MarkRecordsDialog)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 2, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(MarkRecordsDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(MarkRecordsDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.line = QtWidgets.QFrame(MarkRecordsDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 4)

        self.retranslateUi(MarkRecordsDialog)
        QtCore.QMetaObject.connectSlotsByName(MarkRecordsDialog)

    def retranslateUi(self, MarkRecordsDialog):
        _translate = QtCore.QCoreApplication.translate
        MarkRecordsDialog.setWindowTitle(_translate("MarkRecordsDialog", "Dialog"))
        self.pushButtonConfirm.setText(_translate("MarkRecordsDialog", "Quick Mark"))
        self.label_2.setText(_translate("MarkRecordsDialog", "Field name:"))
        self.label.setText(_translate("MarkRecordsDialog", "Quick mark of checked records"))
        self.pushButtonCancel.setText(_translate("MarkRecordsDialog", "Cancel"))
        self.label_4.setText(_translate("MarkRecordsDialog", "Number of checked records::"))
        self.label_3.setText(_translate("MarkRecordsDialog", "Value:"))
