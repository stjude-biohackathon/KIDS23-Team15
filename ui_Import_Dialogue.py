# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Import_Dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogImport(object):
    def setupUi(self, DialogImport):
        DialogImport.setObjectName("DialogImport")
        DialogImport.resize(594, 605)
        DialogImport.setMaximumSize(QtCore.QSize(800, 16777215))
        DialogImport.setFocusPolicy(QtCore.Qt.TabFocus)
        self.gridLayout = QtWidgets.QGridLayout(DialogImport)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(DialogImport)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButFASTA = QtWidgets.QRadioButton(self.groupBox)
        self.radioButFASTA.setChecked(True)
        self.radioButFASTA.setObjectName("radioButFASTA")
        self.verticalLayout.addWidget(self.radioButFASTA)
        self.radioButIndSeq = QtWidgets.QRadioButton(self.groupBox)
        self.radioButIndSeq.setObjectName("radioButIndSeq")
        self.verticalLayout.addWidget(self.radioButIndSeq)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(DialogImport)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButHuman = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButHuman.setChecked(True)
        self.radioButHuman.setObjectName("radioButHuman")
        self.verticalLayout_2.addWidget(self.radioButHuman)
        self.radioButMouse = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButMouse.setObjectName("radioButMouse")
        self.verticalLayout_2.addWidget(self.radioButMouse)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(DialogImport)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rdoAll = QtWidgets.QRadioButton(self.groupBox_4)
        self.rdoAll.setObjectName("rdoAll")
        self.gridLayout_2.addWidget(self.rdoAll, 2, 0, 1, 1)
        self.rdoVandJ = QtWidgets.QRadioButton(self.groupBox_4)
        self.rdoVandJ.setChecked(True)
        self.rdoVandJ.setObjectName("rdoVandJ")
        self.gridLayout_2.addWidget(self.rdoVandJ, 1, 0, 1, 1)
        self.rdoProductive = QtWidgets.QRadioButton(self.groupBox_4)
        self.rdoProductive.setObjectName("rdoProductive")
        self.gridLayout_2.addWidget(self.rdoProductive, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 3)
        self.groupBox_5 = QtWidgets.QGroupBox(DialogImport)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_5.setObjectName("groupBox_5")
        self.rdoChoose = QtWidgets.QRadioButton(self.groupBox_5)
        self.rdoChoose.setGeometry(QtCore.QRect(10, 20, 111, 20))
        self.rdoChoose.setFocusPolicy(QtCore.Qt.TabFocus)
        self.rdoChoose.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rdoChoose.setObjectName("rdoChoose")
        self.checkBoxFileStruc = QtWidgets.QRadioButton(self.groupBox_5)
        self.checkBoxFileStruc.setGeometry(QtCore.QRect(310, 20, 171, 20))
        self.checkBoxFileStruc.setObjectName("checkBoxFileStruc")
        self.rdoFunction = QtWidgets.QRadioButton(self.groupBox_5)
        self.rdoFunction.setGeometry(QtCore.QRect(120, 20, 152, 20))
        self.rdoFunction.setChecked(True)
        self.rdoFunction.setObjectName("rdoFunction")
        self.gridLayout.addWidget(self.groupBox_5, 2, 0, 1, 3)
        self.label = QtWidgets.QLabel(DialogImport)
        self.label.setMinimumSize(QtCore.QSize(75, 0))
        self.label.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.comboBoxProject = QtWidgets.QComboBox(DialogImport)
        self.comboBoxProject.setMinimumSize(QtCore.QSize(280, 0))
        self.comboBoxProject.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBoxProject.setEditable(True)
        self.comboBoxProject.setCurrentText("")
        self.comboBoxProject.setObjectName("comboBoxProject")
        self.comboBoxProject.addItem("")
        self.comboBoxProject.setItemText(0, "")
        self.comboBoxProject.addItem("")
        self.gridLayout.addWidget(self.comboBoxProject, 3, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(DialogImport)
        self.label_2.setMinimumSize(QtCore.QSize(75, 0))
        self.label_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.comboBoxGroup = QtWidgets.QComboBox(DialogImport)
        self.comboBoxGroup.setMinimumSize(QtCore.QSize(280, 0))
        self.comboBoxGroup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBoxGroup.setEditable(True)
        self.comboBoxGroup.setCurrentText("")
        self.comboBoxGroup.setObjectName("comboBoxGroup")
        self.comboBoxGroup.addItem("")
        self.comboBoxGroup.setItemText(0, "")
        self.comboBoxGroup.addItem("")
        self.gridLayout.addWidget(self.comboBoxGroup, 4, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(DialogImport)
        self.label_3.setMinimumSize(QtCore.QSize(75, 0))
        self.label_3.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.comboBoxSubgroup = QtWidgets.QComboBox(DialogImport)
        self.comboBoxSubgroup.setMinimumSize(QtCore.QSize(280, 0))
        self.comboBoxSubgroup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBoxSubgroup.setEditable(True)
        self.comboBoxSubgroup.setCurrentText("")
        self.comboBoxSubgroup.setObjectName("comboBoxSubgroup")
        self.comboBoxSubgroup.addItem("")
        self.comboBoxSubgroup.setItemText(0, "")
        self.comboBoxSubgroup.addItem("")
        self.gridLayout.addWidget(self.comboBoxSubgroup, 5, 1, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(DialogImport)
        self.groupBox_3.setMinimumSize(QtCore.QSize(350, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtComment = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.txtComment.setMaximumSize(QtCore.QSize(350, 16777215))
        self.txtComment.setObjectName("txtComment")
        self.horizontalLayout.addWidget(self.txtComment)
        self.gridLayout.addWidget(self.groupBox_3, 6, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(DialogImport)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.MaxImport = QtWidgets.QSpinBox(DialogImport)
        self.MaxImport.setMinimumSize(QtCore.QSize(200, 0))
        self.MaxImport.setMaximum(100000000)
        self.MaxImport.setSingleStep(100)
        self.MaxImport.setObjectName("MaxImport")
        self.gridLayout.addWidget(self.MaxImport, 7, 1, 1, 2)
        self.labelpct = QtWidgets.QLabel(DialogImport)
        self.labelpct.setEnabled(True)
        self.labelpct.setObjectName("labelpct")
        self.gridLayout.addWidget(self.labelpct, 8, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(DialogImport)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(DialogImport)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(DialogImport)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 9, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogImport)
        self.buttonBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 10, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(DialogImport)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(50, 20))
        self.progressBar.setSizeIncrement(QtCore.QSize(0, 0))
        self.progressBar.setBaseSize(QtCore.QSize(0, 20))
        self.progressBar.setToolTip("")
        self.progressBar.setAutoFillBackground(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 8, 1, 1, 2)

        self.retranslateUi(DialogImport)
        self.comboBoxProject.setCurrentIndex(0)
        self.comboBoxGroup.setCurrentIndex(0)
        self.comboBoxSubgroup.setCurrentIndex(0)
        self.rdoChoose.pressed.connect(self.comboBoxProject.setFocus)
        self.rdoFunction.pressed.connect(self.groupBox_5.setFocus)
        self.checkBoxFileStruc.pressed.connect(self.groupBox_5.setFocus)
        self.rdoChoose.pressed.connect(self.comboBoxProject.setFocus)
        QtCore.QMetaObject.connectSlotsByName(DialogImport)

    def retranslateUi(self, DialogImport):
        _translate = QtCore.QCoreApplication.translate
        DialogImport.setWindowTitle(_translate("DialogImport", "Import Sequence Options"))
        DialogImport.setToolTip(_translate("DialogImport", "Choose options for sequence import"))
        self.groupBox.setTitle(_translate("DialogImport", "File type:"))
        self.radioButFASTA.setText(_translate("DialogImport", "FASTA"))
        self.radioButIndSeq.setText(_translate("DialogImport", "Multiple (.seq, .txt)"))
        self.groupBox_2.setTitle(_translate("DialogImport", "Species:"))
        self.radioButHuman.setText(_translate("DialogImport", "Human"))
        self.radioButMouse.setText(_translate("DialogImport", "Mouse"))
        self.groupBox_4.setTitle(_translate("DialogImport", "Options:"))
        self.rdoAll.setText(_translate("DialogImport", "Import all sequences with any IgBlast hits for V"))
        self.rdoVandJ.setText(_translate("DialogImport", "Import only sequences with V and J genes"))
        self.rdoProductive.setText(_translate("DialogImport", "Import productive rearrangments only"))
        self.groupBox_5.setTitle(_translate("DialogImport", "Choose grouping options:"))
        self.rdoChoose.setToolTip(_translate("DialogImport", "Select grouping from choices below"))
        self.rdoChoose.setText(_translate("DialogImport", "Choose:"))
        self.checkBoxFileStruc.setToolTip(_translate("DialogImport", "use folder structure to group"))
        self.checkBoxFileStruc.setText(_translate("DialogImport", "Group by file structure"))
        self.rdoFunction.setToolTip(_translate("DialogImport", "Will group based on heavy/kappa/lambda, Functional, Reading frame"))
        self.rdoFunction.setText(_translate("DialogImport", "Functional grouping"))
        self.label.setText(_translate("DialogImport", "Project:"))
        self.comboBoxProject.setItemText(1, _translate("DialogImport", "None"))
        self.label_2.setText(_translate("DialogImport", "Group:"))
        self.comboBoxGroup.setItemText(1, _translate("DialogImport", "None"))
        self.label_3.setText(_translate("DialogImport", "Subgroup:"))
        self.comboBoxSubgroup.setItemText(1, _translate("DialogImport", "None"))
        self.groupBox_3.setTitle(_translate("DialogImport", "Global Comments/Notations:"))
        self.label_4.setText(_translate("DialogImport", "Number to import  (0=all):"))
        self.labelpct.setText(_translate("DialogImport", "Loading progress:"))
        self.label_5.setText(_translate("DialogImport", "Path:"))
        self.toolButton.setText(_translate("DialogImport", "Borwse"))
