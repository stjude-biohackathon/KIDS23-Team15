# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProteinSimilarDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProteinSimilarDialog(object):
    def setupUi(self, ProteinSimilarDialog):
        ProteinSimilarDialog.setObjectName("ProteinSimilarDialog")
        ProteinSimilarDialog.resize(786, 820)
        self.gridLayout_4 = QtWidgets.QGridLayout(ProteinSimilarDialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(ProteinSimilarDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 3)
        self.groupBox_2 = QtWidgets.QGroupBox(ProteinSimilarDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chkHydrophobicity = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkHydrophobicity.setObjectName("chkHydrophobicity")
        self.gridLayout_2.addWidget(self.chkHydrophobicity, 6, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 7)
        self.chkHydrophilicity = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkHydrophilicity.setObjectName("chkHydrophilicity")
        self.gridLayout_2.addWidget(self.chkHydrophilicity, 6, 5, 1, 1)
        self.spnInstability = QtWidgets.QSpinBox(self.groupBox_2)
        self.spnInstability.setMinimumSize(QtCore.QSize(40, 0))
        self.spnInstability.setMaximumSize(QtCore.QSize(40, 16777215))
        self.spnInstability.setMinimum(8)
        self.spnInstability.setMaximum(99)
        self.spnInstability.setProperty("value", 8)
        self.spnInstability.setObjectName("spnInstability")
        self.gridLayout_2.addWidget(self.spnInstability, 7, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.chkInstability = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkInstability.setObjectName("chkInstability")
        self.gridLayout_2.addWidget(self.chkInstability, 7, 5, 1, 1)
        self.spnpI = QtWidgets.QSpinBox(self.groupBox_2)
        self.spnpI.setMinimumSize(QtCore.QSize(40, 0))
        self.spnpI.setMaximumSize(QtCore.QSize(40, 16777215))
        self.spnpI.setMinimum(2)
        self.spnpI.setMaximum(20)
        self.spnpI.setProperty("value", 5)
        self.spnpI.setObjectName("spnpI")
        self.gridLayout_2.addWidget(self.spnpI, 8, 3, 1, 1)
        self.chkSelectAllProt = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkSelectAllProt.setObjectName("chkSelectAllProt")
        self.gridLayout_2.addWidget(self.chkSelectAllProt, 5, 0, 1, 2)
        self.checkBoxCheckRecords = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxCheckRecords.setChecked(True)
        self.checkBoxCheckRecords.setAutoExclusive(True)
        self.checkBoxCheckRecords.setObjectName("checkBoxCheckRecords")
        self.buttonGroup = QtWidgets.QButtonGroup(ProteinSimilarDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.checkBoxCheckRecords)
        self.gridLayout_2.addWidget(self.checkBoxCheckRecords, 0, 1, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 7)
        self.chkSurface = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkSurface.setObjectName("chkSurface")
        self.gridLayout_2.addWidget(self.chkSurface, 8, 5, 1, 1)
        self.spnHydrophobicity = QtWidgets.QSpinBox(self.groupBox_2)
        self.spnHydrophobicity.setMinimumSize(QtCore.QSize(40, 0))
        self.spnHydrophobicity.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spnHydrophobicity.setMinimum(2)
        self.spnHydrophobicity.setMaximum(20)
        self.spnHydrophobicity.setProperty("value", 5)
        self.spnHydrophobicity.setObjectName("spnHydrophobicity")
        self.gridLayout_2.addWidget(self.spnHydrophobicity, 6, 3, 1, 1)
        self.radioButtonIgnoreGap = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonIgnoreGap.setObjectName("radioButtonIgnoreGap")
        self.gridLayout_2.addWidget(self.radioButtonIgnoreGap, 2, 0, 1, 7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 6, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 5, 2, 1, 5)
        self.spnSurface = QtWidgets.QSpinBox(self.groupBox_2)
        self.spnSurface.setMinimumSize(QtCore.QSize(40, 0))
        self.spnSurface.setMaximumSize(QtCore.QSize(40, 16777215))
        self.spnSurface.setMinimum(2)
        self.spnSurface.setMaximum(20)
        self.spnSurface.setProperty("value", 5)
        self.spnSurface.setObjectName("spnSurface")
        self.gridLayout_2.addWidget(self.spnSurface, 8, 6, 1, 1)
        self.spnHydrophilicity = QtWidgets.QSpinBox(self.groupBox_2)
        self.spnHydrophilicity.setMinimumSize(QtCore.QSize(40, 0))
        self.spnHydrophilicity.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spnHydrophilicity.setMinimum(2)
        self.spnHydrophilicity.setMaximum(20)
        self.spnHydrophilicity.setProperty("value", 5)
        self.spnHydrophilicity.setObjectName("spnHydrophilicity")
        self.gridLayout_2.addWidget(self.spnHydrophilicity, 6, 6, 1, 1)
        self.chkpI = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkpI.setObjectName("chkpI")
        self.gridLayout_2.addWidget(self.chkpI, 8, 0, 1, 3)
        self.chkFlexibility = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkFlexibility.setObjectName("chkFlexibility")
        self.gridLayout_2.addWidget(self.chkFlexibility, 7, 0, 1, 1)
        self.spnFlexibility = QtWidgets.QSpinBox(self.groupBox_2)
        self.spnFlexibility.setMinimumSize(QtCore.QSize(40, 0))
        self.spnFlexibility.setMaximumSize(QtCore.QSize(40, 16777215))
        self.spnFlexibility.setMinimum(9)
        self.spnFlexibility.setMaximum(20)
        self.spnFlexibility.setProperty("value", 9)
        self.spnFlexibility.setObjectName("spnFlexibility")
        self.gridLayout_2.addWidget(self.spnFlexibility, 7, 3, 1, 1)
        self.checkBoxAllRecords = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxAllRecords.setObjectName("checkBoxAllRecords")
        self.buttonGroup.addButton(self.checkBoxAllRecords)
        self.gridLayout_2.addWidget(self.checkBoxAllRecords, 0, 5, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 7)
        self.gridLayout_4.addWidget(self.groupBox_2, 2, 0, 1, 3)
        self.pushButtonCancel = QtWidgets.QPushButton(ProteinSimilarDialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout_4.addWidget(self.pushButtonCancel, 4, 1, 1, 1)
        self.pushButtonConfirm = QtWidgets.QPushButton(ProteinSimilarDialog)
        self.pushButtonConfirm.setDefault(True)
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.gridLayout_4.addWidget(self.pushButtonConfirm, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(583, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 4, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(ProteinSimilarDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEditGeneType = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditGeneType.setReadOnly(True)
        self.lineEditGeneType.setObjectName("lineEditGeneType")
        self.gridLayout_3.addWidget(self.lineEditGeneType, 0, 3, 1, 1)
        self.lineEditJgene = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditJgene.setObjectName("lineEditJgene")
        self.gridLayout_3.addWidget(self.lineEditJgene, 1, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEditIsotype = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditIsotype.setReadOnly(True)
        self.lineEditIsotype.setObjectName("lineEditIsotype")
        self.gridLayout_3.addWidget(self.lineEditIsotype, 0, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 4, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 3, 0, 1, 6)
        self.lineEditName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditName.setReadOnly(True)
        self.lineEditName.setObjectName("lineEditName")
        self.gridLayout_3.addWidget(self.lineEditName, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)
        self.lineEditVgene = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditVgene.setObjectName("lineEditVgene")
        self.gridLayout_3.addWidget(self.lineEditVgene, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 4, 1, 1)
        self.lineEditDgene = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditDgene.setObjectName("lineEditDgene")
        self.gridLayout_3.addWidget(self.lineEditDgene, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 3)
        self.groupBox_3 = QtWidgets.QGroupBox(ProteinSimilarDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 1, 5, 1, 1)
        self.lineEditGapExtend = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditGapExtend.setObjectName("lineEditGapExtend")
        self.gridLayout_5.addWidget(self.lineEditGapExtend, 1, 6, 1, 1)
        self.lineEditGapopen = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditGapopen.setObjectName("lineEditGapopen")
        self.gridLayout_5.addWidget(self.lineEditGapopen, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButtonblosum62 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButtonblosum62.setChecked(True)
        self.radioButtonblosum62.setObjectName("radioButtonblosum62")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(ProteinSimilarDialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButtonblosum62)
        self.horizontalLayout.addWidget(self.radioButtonblosum62)
        self.radioButtonpam60 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButtonpam60.setObjectName("radioButtonpam60")
        self.buttonGroup_2.addButton(self.radioButtonpam60)
        self.horizontalLayout.addWidget(self.radioButtonpam60)
        self.radioButtonbenner22 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButtonbenner22.setObjectName("radioButtonbenner22")
        self.buttonGroup_2.addButton(self.radioButtonbenner22)
        self.horizontalLayout.addWidget(self.radioButtonbenner22)
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 2, 1, 5)
        self.gridLayout_4.addWidget(self.groupBox_3, 3, 0, 1, 3)

        self.retranslateUi(ProteinSimilarDialog)
        QtCore.QMetaObject.connectSlotsByName(ProteinSimilarDialog)

    def retranslateUi(self, ProteinSimilarDialog):
        _translate = QtCore.QCoreApplication.translate
        ProteinSimilarDialog.setWindowTitle(_translate("ProteinSimilarDialog", "Identify Similar Proteins"))
        self.label.setText(_translate("ProteinSimilarDialog", "Identify sequences that have similar protein properties"))
        self.groupBox_2.setTitle(_translate("ProteinSimilarDialog", "Searching criteria"))
        self.chkHydrophobicity.setText(_translate("ProteinSimilarDialog", "Hydrophobicity"))
        self.chkHydrophilicity.setText(_translate("ProteinSimilarDialog", "Hydrophilicity"))
        self.label_4.setText(_translate("ProteinSimilarDialog", "Range:"))
        self.chkInstability.setText(_translate("ProteinSimilarDialog", "Instability"))
        self.chkSelectAllProt.setText(_translate("ProteinSimilarDialog", "Select all"))
        self.checkBoxCheckRecords.setText(_translate("ProteinSimilarDialog", "Checked records"))
        self.label_5.setText(_translate("ProteinSimilarDialog", "Protein properties"))
        self.chkSurface.setText(_translate("ProteinSimilarDialog", "Surface liklihood"))
        self.radioButtonIgnoreGap.setText(_translate("ProteinSimilarDialog", "Ignore Alignment Gaps when calculate similarity scores"))
        self.label_10.setText(_translate("ProteinSimilarDialog", "Window size (residues):"))
        self.chkpI.setText(_translate("ProteinSimilarDialog", "Isoelectric point (pI)"))
        self.chkFlexibility.setText(_translate("ProteinSimilarDialog", "Flexibility"))
        self.checkBoxAllRecords.setText(_translate("ProteinSimilarDialog", "All records"))
        self.pushButtonCancel.setText(_translate("ProteinSimilarDialog", "Cancel"))
        self.pushButtonConfirm.setText(_translate("ProteinSimilarDialog", "Confirm"))
        self.groupBox.setTitle(_translate("ProteinSimilarDialog", "Target sequence"))
        self.label_2.setText(_translate("ProteinSimilarDialog", "Name:"))
        self.label_8.setText(_translate("ProteinSimilarDialog", "V gene:"))
        self.label_9.setText(_translate("ProteinSimilarDialog", "D gene:"))
        self.label_6.setText(_translate("ProteinSimilarDialog", "Isotype:"))
        self.label_3.setText(_translate("ProteinSimilarDialog", "Gene Type:"))
        self.label_11.setText(_translate("ProteinSimilarDialog", "J gene:"))
        self.label_7.setText(_translate("ProteinSimilarDialog", "V(D)J Sequence"))
        self.groupBox_3.setTitle(_translate("ProteinSimilarDialog", "Alignment setting"))
        self.label_13.setText(_translate("ProteinSimilarDialog", "Gap open"))
        self.label_12.setText(_translate("ProteinSimilarDialog", "Substitution Matric"))
        self.label_14.setText(_translate("ProteinSimilarDialog", "Gap Extend"))
        self.lineEditGapExtend.setText(_translate("ProteinSimilarDialog", "-0.1"))
        self.lineEditGapopen.setText(_translate("ProteinSimilarDialog", "-3"))
        self.radioButtonblosum62.setText(_translate("ProteinSimilarDialog", "blosum62"))
        self.radioButtonpam60.setText(_translate("ProteinSimilarDialog", "pam60"))
        self.radioButtonbenner22.setText(_translate("ProteinSimilarDialog", "benner22"))
