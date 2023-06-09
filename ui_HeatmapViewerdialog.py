# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HeatmapViewerdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HeatmapViewerDialog(object):
    def setupUi(self, HeatmapViewerDialog):
        HeatmapViewerDialog.setObjectName("HeatmapViewerDialog")
        HeatmapViewerDialog.resize(1102, 766)
        self.gridLayout = QtWidgets.QGridLayout(HeatmapViewerDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(HeatmapViewerDialog)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 2)
        self.comboBoxColor = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxColor.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBoxColor.setObjectName("comboBoxColor")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxColor, 8, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButtonHC = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonHC.setChecked(True)
        self.radioButtonHC.setAutoExclusive(False)
        self.radioButtonHC.setObjectName("radioButtonHC")
        self.horizontalLayout.addWidget(self.radioButtonHC)
        self.radioButtonLC = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonLC.setAutoExclusive(False)
        self.radioButtonLC.setObjectName("radioButtonLC")
        self.horizontalLayout.addWidget(self.radioButtonLC)
        self.gridLayout_2.addLayout(self.horizontalLayout, 10, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 4, 0, 1, 2)
        self.checkBoxNum = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxNum.setObjectName("checkBoxNum")
        self.gridLayout_2.addWidget(self.checkBoxNum, 5, 1, 1, 1)
        self.lineEditFeature = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditFeature.setObjectName("lineEditFeature")
        self.gridLayout_2.addWidget(self.lineEditFeature, 1, 0, 1, 2)
        self.radioButtonChecked = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonChecked.setAutoExclusive(False)
        self.radioButtonChecked.setObjectName("radioButtonChecked")
        self.gridLayout_2.addWidget(self.radioButtonChecked, 10, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 8, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 7, 0, 1, 2)
        self.lineEditGroup = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditGroup.setObjectName("lineEditGroup")
        self.gridLayout_2.addWidget(self.lineEditGroup, 6, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 3, 0, 1, 2)
        self.labelInfo = QtWidgets.QLabel(self.groupBox)
        self.labelInfo.setObjectName("labelInfo")
        self.gridLayout_2.addWidget(self.labelInfo, 0, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 9, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.PlotVerticalLayout = QtWidgets.QVBoxLayout()
        self.PlotVerticalLayout.setObjectName("PlotVerticalLayout")
        self.gridLayout.addLayout(self.PlotVerticalLayout, 0, 1, 4, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(HeatmapViewerDialog)
        self.groupBox_2.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButtonExport = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonExport.setObjectName("pushButtonExport")
        self.gridLayout_4.addWidget(self.pushButtonExport, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.radioButtonPNG = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonPNG.setChecked(True)
        self.radioButtonPNG.setObjectName("radioButtonPNG")
        self.gridLayout_4.addWidget(self.radioButtonPNG, 0, 2, 1, 1)
        self.radioButtonSVG = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonSVG.setObjectName("radioButtonSVG")
        self.gridLayout_4.addWidget(self.radioButtonSVG, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.pushButtonDraw = QtWidgets.QPushButton(HeatmapViewerDialog)
        self.pushButtonDraw.setObjectName("pushButtonDraw")
        self.gridLayout.addWidget(self.pushButtonDraw, 3, 0, 1, 1)

        self.retranslateUi(HeatmapViewerDialog)
        QtCore.QMetaObject.connectSlotsByName(HeatmapViewerDialog)

    def retranslateUi(self, HeatmapViewerDialog):
        _translate = QtCore.QCoreApplication.translate
        HeatmapViewerDialog.setWindowTitle(_translate("HeatmapViewerDialog", "Dialog"))
        self.groupBox.setTitle(_translate("HeatmapViewerDialog", "Features for plots"))
        self.label.setText(_translate("HeatmapViewerDialog", "Double click feature to remove it:"))
        self.comboBoxColor.setItemText(0, _translate("HeatmapViewerDialog", "viridis"))
        self.comboBoxColor.setItemText(1, _translate("HeatmapViewerDialog", "afmhot"))
        self.comboBoxColor.setItemText(2, _translate("HeatmapViewerDialog", "rainbow"))
        self.comboBoxColor.setItemText(3, _translate("HeatmapViewerDialog", "RdYlBu_r"))
        self.comboBoxColor.setItemText(4, _translate("HeatmapViewerDialog", "RdYlGn_r"))
        self.comboBoxColor.setItemText(5, _translate("HeatmapViewerDialog", "Spectral_r"))
        self.comboBoxColor.setItemText(6, _translate("HeatmapViewerDialog", "turbo"))
        self.comboBoxColor.setItemText(7, _translate("HeatmapViewerDialog", "YlOrRd"))
        self.radioButtonHC.setText(_translate("HeatmapViewerDialog", "HC"))
        self.radioButtonLC.setText(_translate("HeatmapViewerDialog", "LC"))
        self.checkBoxNum.setText(_translate("HeatmapViewerDialog", "Numerical factor"))
        self.radioButtonChecked.setText(_translate("HeatmapViewerDialog", "only plot checked"))
        self.label_3.setText(_translate("HeatmapViewerDialog", "Color"))
        self.label_2.setText(_translate("HeatmapViewerDialog", "Order records by:"))
        self.labelInfo.setText(_translate("HeatmapViewerDialog", "Select features from this input:"))
        self.groupBox_2.setTitle(_translate("HeatmapViewerDialog", "Download Figure"))
        self.pushButtonExport.setText(_translate("HeatmapViewerDialog", "Export"))
        self.radioButtonPNG.setText(_translate("HeatmapViewerDialog", "PNG"))
        self.radioButtonSVG.setText(_translate("HeatmapViewerDialog", "SVG"))
        self.pushButtonDraw.setText(_translate("HeatmapViewerDialog", "Draw"))
