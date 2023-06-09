# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BeesWarmPlotdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BeesWarmPlotDialog(object):
    def setupUi(self, BeesWarmPlotDialog):
        BeesWarmPlotDialog.setObjectName("BeesWarmPlotDialog")
        BeesWarmPlotDialog.resize(1059, 777)
        self.gridLayout = QtWidgets.QGridLayout(BeesWarmPlotDialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 274, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(BeesWarmPlotDialog)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalSliderRange = QtWidgets.QSlider(self.groupBox)
        self.horizontalSliderRange.setMinimum(1)
        self.horizontalSliderRange.setMaximum(5)
        self.horizontalSliderRange.setPageStep(1)
        self.horizontalSliderRange.setProperty("value", 3)
        self.horizontalSliderRange.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderRange.setObjectName("horizontalSliderRange")
        self.gridLayout_2.addWidget(self.horizontalSliderRange, 8, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalSliderSize = QtWidgets.QSlider(self.groupBox)
        self.horizontalSliderSize.setMinimum(1)
        self.horizontalSliderSize.setMaximum(5)
        self.horizontalSliderSize.setPageStep(1)
        self.horizontalSliderSize.setProperty("value", 3)
        self.horizontalSliderSize.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSize.setObjectName("horizontalSliderSize")
        self.gridLayout_2.addWidget(self.horizontalSliderSize, 7, 1, 1, 1)
        self.comboBoxColor = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxColor.setObjectName("comboBoxColor")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxColor, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 9, 0, 1, 2)
        self.lineEditGroup = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditGroup.setObjectName("lineEditGroup")
        self.gridLayout_2.addWidget(self.lineEditGroup, 1, 1, 1, 1)
        self.radioButtonChecked = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonChecked.setAutoExclusive(False)
        self.radioButtonChecked.setObjectName("radioButtonChecked")
        self.gridLayout_2.addWidget(self.radioButtonChecked, 6, 0, 1, 2)
        self.lineEditData = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditData.setObjectName("lineEditData")
        self.gridLayout_2.addWidget(self.lineEditData, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 8, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButtonBox = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonBox.setChecked(True)
        self.radioButtonBox.setObjectName("radioButtonBox")
        self.horizontalLayout.addWidget(self.radioButtonBox)
        self.radioButtonMean = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonMean.setObjectName("radioButtonMean")
        self.horizontalLayout.addWidget(self.radioButtonMean)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.checkBoxDisplayScatter = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxDisplayScatter.setChecked(True)
        self.checkBoxDisplayScatter.setObjectName("checkBoxDisplayScatter")
        self.gridLayout_2.addWidget(self.checkBoxDisplayScatter, 4, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.PlotVerticalLayout = QtWidgets.QVBoxLayout()
        self.PlotVerticalLayout.setObjectName("PlotVerticalLayout")
        self.gridLayout.addLayout(self.PlotVerticalLayout, 0, 1, 4, 1)
        self.pushButtonDraw = QtWidgets.QPushButton(BeesWarmPlotDialog)
        self.pushButtonDraw.setObjectName("pushButtonDraw")
        self.gridLayout.addWidget(self.pushButtonDraw, 3, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(BeesWarmPlotDialog)
        self.groupBox_2.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButtonExport_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonExport_2.setObjectName("pushButtonExport_2")
        self.gridLayout_4.addWidget(self.pushButtonExport_2, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 1, 1, 1)
        self.radioButtonPNG_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonPNG_2.setChecked(True)
        self.radioButtonPNG_2.setObjectName("radioButtonPNG_2")
        self.gridLayout_4.addWidget(self.radioButtonPNG_2, 0, 2, 1, 1)
        self.radioButtonSVG_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonSVG_2.setObjectName("radioButtonSVG_2")
        self.gridLayout_4.addWidget(self.radioButtonSVG_2, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.retranslateUi(BeesWarmPlotDialog)
        QtCore.QMetaObject.connectSlotsByName(BeesWarmPlotDialog)

    def retranslateUi(self, BeesWarmPlotDialog):
        _translate = QtCore.QCoreApplication.translate
        BeesWarmPlotDialog.setWindowTitle(_translate("BeesWarmPlotDialog", "Dialog"))
        self.groupBox.setTitle(_translate("BeesWarmPlotDialog", "Features for plots"))
        self.label_2.setText(_translate("BeesWarmPlotDialog", "Group"))
        self.comboBoxColor.setItemText(0, _translate("BeesWarmPlotDialog", "Paired"))
        self.comboBoxColor.setItemText(1, _translate("BeesWarmPlotDialog", "Set2"))
        self.comboBoxColor.setItemText(2, _translate("BeesWarmPlotDialog", "Dark2"))
        self.comboBoxColor.setItemText(3, _translate("BeesWarmPlotDialog", "hls"))
        self.comboBoxColor.setItemText(4, _translate("BeesWarmPlotDialog", "rainbow"))
        self.comboBoxColor.setItemText(5, _translate("BeesWarmPlotDialog", "turbo"))
        self.comboBoxColor.setItemText(6, _translate("BeesWarmPlotDialog", "ManyColor1"))
        self.comboBoxColor.setItemText(7, _translate("BeesWarmPlotDialog", "ManyColor2"))
        self.label.setText(_translate("BeesWarmPlotDialog", "Data"))
        self.radioButtonChecked.setText(_translate("BeesWarmPlotDialog", "only plot my checked records"))
        self.label_5.setText(_translate("BeesWarmPlotDialog", "Range"))
        self.label_4.setText(_translate("BeesWarmPlotDialog", "Size"))
        self.label_3.setText(_translate("BeesWarmPlotDialog", "Color"))
        self.radioButtonBox.setText(_translate("BeesWarmPlotDialog", "Boxplot"))
        self.radioButtonMean.setText(_translate("BeesWarmPlotDialog", "Mean+SD"))
        self.checkBoxDisplayScatter.setText(_translate("BeesWarmPlotDialog", "Display Scatter"))
        self.pushButtonDraw.setText(_translate("BeesWarmPlotDialog", "Draw"))
        self.groupBox_2.setTitle(_translate("BeesWarmPlotDialog", "Download Figure"))
        self.pushButtonExport_2.setText(_translate("BeesWarmPlotDialog", "Export"))
        self.radioButtonPNG_2.setText(_translate("BeesWarmPlotDialog", "PNG"))
        self.radioButtonSVG_2.setText(_translate("BeesWarmPlotDialog", "SVG"))
