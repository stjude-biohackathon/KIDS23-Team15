# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HistGramdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HistGramDialog(object):
    def setupUi(self, HistGramDialog):
        HistGramDialog.setObjectName("HistGramDialog")
        HistGramDialog.resize(1095, 844)
        self.gridLayout = QtWidgets.QGridLayout(HistGramDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(HistGramDialog)
        self.groupBox_2.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButtonExport = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonExport.setObjectName("pushButtonExport")
        self.gridLayout_3.addWidget(self.pushButtonExport, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.radioButtonPNG = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonPNG.setChecked(True)
        self.radioButtonPNG.setObjectName("radioButtonPNG")
        self.gridLayout_3.addWidget(self.radioButtonPNG, 0, 2, 1, 1)
        self.radioButtonSVG = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonSVG.setObjectName("radioButtonSVG")
        self.gridLayout_3.addWidget(self.radioButtonSVG, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.PlotVerticalLayout = QtWidgets.QVBoxLayout()
        self.PlotVerticalLayout.setObjectName("PlotVerticalLayout")
        self.gridLayout.addLayout(self.PlotVerticalLayout, 0, 1, 4, 1)
        self.groupBox = QtWidgets.QGroupBox(HistGramDialog)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonAddMore = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonAddMore.setFlat(False)
        self.pushButtonAddMore.setObjectName("pushButtonAddMore")
        self.gridLayout_2.addWidget(self.pushButtonAddMore, 0, 0, 1, 1)
        self.radioButtonChecked = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonChecked.setObjectName("radioButtonChecked")
        self.gridLayout_2.addWidget(self.radioButtonChecked, 1, 0, 1, 1)
        self.FeatureLayout = QtWidgets.QVBoxLayout()
        self.FeatureLayout.setObjectName("FeatureLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.FeatureLayout.addWidget(self.lineEdit)
        self.gridLayout_2.addLayout(self.FeatureLayout, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.pushButtonDraw = QtWidgets.QPushButton(HistGramDialog)
        self.pushButtonDraw.setObjectName("pushButtonDraw")
        self.gridLayout.addWidget(self.pushButtonDraw, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)

        self.retranslateUi(HistGramDialog)
        QtCore.QMetaObject.connectSlotsByName(HistGramDialog)

    def retranslateUi(self, HistGramDialog):
        _translate = QtCore.QCoreApplication.translate
        HistGramDialog.setWindowTitle(_translate("HistGramDialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("HistGramDialog", "Download Figure"))
        self.pushButtonExport.setText(_translate("HistGramDialog", "Export"))
        self.radioButtonPNG.setText(_translate("HistGramDialog", "PNG"))
        self.radioButtonSVG.setText(_translate("HistGramDialog", "SVG"))
        self.groupBox.setTitle(_translate("HistGramDialog", "Features for plots"))
        self.pushButtonAddMore.setText(_translate("HistGramDialog", "Add 1 more feature"))
        self.radioButtonChecked.setText(_translate("HistGramDialog", "only plot my checked records"))
        self.pushButtonDraw.setText(_translate("HistGramDialog", "Draw"))