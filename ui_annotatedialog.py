# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'annotatedialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnnoDialog(object):
    def setupUi(self, AnnoDialog):
        AnnoDialog.setObjectName("AnnoDialog")
        AnnoDialog.resize(885, 652)
        self.gridLayout_2 = QtWidgets.QGridLayout(AnnoDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonOK = QtWidgets.QPushButton(AnnoDialog)
        self.pushButtonOK.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButtonOK.setDefault(True)
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.gridLayout_2.addWidget(self.pushButtonOK, 5, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(AnnoDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 2)
        self.pushButtonCopyName = QtWidgets.QPushButton(AnnoDialog)
        self.pushButtonCopyName.setObjectName("pushButtonCopyName")
        self.gridLayout_2.addWidget(self.pushButtonCopyName, 2, 4, 1, 2)
        self.pushButtonCancel = QtWidgets.QPushButton(AnnoDialog)
        self.pushButtonCancel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout_2.addWidget(self.pushButtonCancel, 5, 4, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(AnnoDialog)
        self.radioButton.setChecked(True)
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 3, 0, 1, 1)
        self.radioButtonUpdateName = QtWidgets.QRadioButton(AnnoDialog)
        self.radioButtonUpdateName.setAutoExclusive(False)
        self.radioButtonUpdateName.setObjectName("radioButtonUpdateName")
        self.gridLayout_2.addWidget(self.radioButtonUpdateName, 3, 1, 1, 1)
        self.frame = QtWidgets.QFrame(AnnoDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.comboBox2 = QtWidgets.QComboBox(self.frame)
        self.comboBox2.setObjectName("comboBox2")
        self.gridLayout.addWidget(self.comboBox2, 0, 3, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(AnnoDialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.radioButtonAll = QtWidgets.QRadioButton(AnnoDialog)
        self.radioButtonAll.setChecked(True)
        self.radioButtonAll.setObjectName("radioButtonAll")
        self.horizontalLayout_2.addWidget(self.radioButtonAll)
        self.radioButtonHC = QtWidgets.QRadioButton(AnnoDialog)
        self.radioButtonHC.setObjectName("radioButtonHC")
        self.horizontalLayout_2.addWidget(self.radioButtonHC)
        self.radioButtonLC = QtWidgets.QRadioButton(AnnoDialog)
        self.radioButtonLC.setObjectName("radioButtonLC")
        self.horizontalLayout_2.addWidget(self.radioButtonLC)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 3, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(384, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(AnnoDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(AnnoDialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 4, 0, 1, 6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 2, 1, 1)

        self.retranslateUi(AnnoDialog)
        QtCore.QMetaObject.connectSlotsByName(AnnoDialog)

    def retranslateUi(self, AnnoDialog):
        _translate = QtCore.QCoreApplication.translate
        AnnoDialog.setWindowTitle(_translate("AnnoDialog", "Import Annotation from CSV"))
        self.pushButtonOK.setText(_translate("AnnoDialog", "OK"))
        self.label_2.setText(_translate("AnnoDialog", "Determine field name for each column (leave blank for columns you don\'t want):"))
        self.pushButtonCopyName.setText(_translate("AnnoDialog", "Use field names in my CSV"))
        self.pushButtonCancel.setText(_translate("AnnoDialog", "Cancel"))
        self.radioButton.setText(_translate("AnnoDialog", "First row of CSV is Column name"))
        self.radioButtonUpdateName.setText(_translate("AnnoDialog", "Update Field Nick name"))
        self.label.setText(_translate("AnnoDialog", "Anchor column:"))
        self.label_3.setText(_translate("AnnoDialog", "link to:"))
        self.label_5.setText(_translate("AnnoDialog", "Annotate:"))
        self.radioButtonAll.setText(_translate("AnnoDialog", "All"))
        self.radioButtonHC.setText(_translate("AnnoDialog", "HC"))
        self.radioButtonLC.setText(_translate("AnnoDialog", "LC"))
        self.label_4.setText(_translate("AnnoDialog", "If you want import data into a new field, just type your field name:"))
