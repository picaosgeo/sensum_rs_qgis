# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/ui_features.ui'
#
# Created: Tue Jun 24 10:39:14 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Features(object):
    def setupUi(self, Features):
        Features.setObjectName(_fromUtf8("Features"))
        Features.resize(465, 604)
        Features.setMinimumSize(QtCore.QSize(465, 604))
        Features.setMaximumSize(QtCore.QSize(465, 604))
        self.buttonBox = QtGui.QDialogButtonBox(Features)
        self.buttonBox.setGeometry(QtCore.QRect(250, 540, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit_input = QtGui.QLineEdit(Features)
        self.lineEdit_input.setGeometry(QtCore.QRect(50, 150, 241, 27))
        self.lineEdit_input.setObjectName(_fromUtf8("lineEdit_input"))
        self.label_input = QtGui.QLabel(Features)
        self.label_input.setGeometry(QtCore.QRect(50, 130, 131, 17))
        self.label_input.setObjectName(_fromUtf8("label_input"))
        self.pushButton_input = QtGui.QPushButton(Features)
        self.pushButton_input.setGeometry(QtCore.QRect(320, 150, 98, 27))
        self.pushButton_input.setObjectName(_fromUtf8("pushButton_input"))
        self.label_training = QtGui.QLabel(Features)
        self.label_training.setGeometry(QtCore.QRect(50, 185, 191, 17))
        self.label_training.setObjectName(_fromUtf8("label_training"))
        self.pushButton_training = QtGui.QPushButton(Features)
        self.pushButton_training.setGeometry(QtCore.QRect(320, 200, 98, 27))
        self.pushButton_training.setObjectName(_fromUtf8("pushButton_training"))
        self.lineEdit_training = QtGui.QLineEdit(Features)
        self.lineEdit_training.setGeometry(QtCore.QRect(50, 203, 241, 27))
        self.lineEdit_training.setObjectName(_fromUtf8("lineEdit_training"))
        self.label_title = QtGui.QLabel(Features)
        self.label_title.setGeometry(QtCore.QRect(190, 100, 111, 21))
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.frame_spectrals = QtGui.QFrame(Features)
        self.frame_spectrals.setGeometry(QtCore.QRect(40, 350, 191, 224))
        self.frame_spectrals.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_spectrals.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_spectrals.setObjectName(_fromUtf8("frame_spectrals"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_spectrals)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox_maxbr = QtGui.QCheckBox(self.frame_spectrals)
        self.checkBox_maxbr.setObjectName(_fromUtf8("checkBox_maxbr"))
        self.verticalLayout.addWidget(self.checkBox_maxbr)
        self.checkBox_mean = QtGui.QCheckBox(self.frame_spectrals)
        self.checkBox_mean.setObjectName(_fromUtf8("checkBox_mean"))
        self.verticalLayout.addWidget(self.checkBox_mean)
        self.checkBox_minbr = QtGui.QCheckBox(self.frame_spectrals)
        self.checkBox_minbr.setObjectName(_fromUtf8("checkBox_minbr"))
        self.verticalLayout.addWidget(self.checkBox_minbr)
        self.checkBox_mode = QtGui.QCheckBox(self.frame_spectrals)
        self.checkBox_mode.setObjectName(_fromUtf8("checkBox_mode"))
        self.verticalLayout.addWidget(self.checkBox_mode)
        self.checkBox_ndivistd = QtGui.QCheckBox(self.frame_spectrals)
        self.checkBox_ndivistd.setObjectName(_fromUtf8("checkBox_ndivistd"))
        self.verticalLayout.addWidget(self.checkBox_ndivistd)
        self.checkBox_ndvimean = QtGui.QCheckBox(self.frame_spectrals)
        self.checkBox_ndvimean.setObjectName(_fromUtf8("checkBox_ndvimean"))
        self.verticalLayout.addWidget(self.checkBox_ndvimean)
        self.checkBox_std = QtGui.QCheckBox(self.frame_spectrals)
        self.checkBox_std.setObjectName(_fromUtf8("checkBox_std"))
        self.verticalLayout.addWidget(self.checkBox_std)
        self.checkBox_weighbr = QtGui.QCheckBox(self.frame_spectrals)
        self.checkBox_weighbr.setObjectName(_fromUtf8("checkBox_weighbr"))
        self.verticalLayout.addWidget(self.checkBox_weighbr)
        self.frame_textures = QtGui.QFrame(Features)
        self.frame_textures.setGeometry(QtCore.QRect(270, 350, 128, 172))
        self.frame_textures.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_textures.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_textures.setObjectName(_fromUtf8("frame_textures"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_textures)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.checkBox_asm = QtGui.QCheckBox(self.frame_textures)
        self.checkBox_asm.setObjectName(_fromUtf8("checkBox_asm"))
        self.verticalLayout_2.addWidget(self.checkBox_asm)
        self.checkBox_contrast = QtGui.QCheckBox(self.frame_textures)
        self.checkBox_contrast.setObjectName(_fromUtf8("checkBox_contrast"))
        self.verticalLayout_2.addWidget(self.checkBox_contrast)
        self.checkBox_correlation = QtGui.QCheckBox(self.frame_textures)
        self.checkBox_correlation.setObjectName(_fromUtf8("checkBox_correlation"))
        self.verticalLayout_2.addWidget(self.checkBox_correlation)
        self.checkBox_dissimilarity = QtGui.QCheckBox(self.frame_textures)
        self.checkBox_dissimilarity.setObjectName(_fromUtf8("checkBox_dissimilarity"))
        self.verticalLayout_2.addWidget(self.checkBox_dissimilarity)
        self.checkBox_energy = QtGui.QCheckBox(self.frame_textures)
        self.checkBox_energy.setObjectName(_fromUtf8("checkBox_energy"))
        self.verticalLayout_2.addWidget(self.checkBox_energy)
        self.checkBox_homogeneity = QtGui.QCheckBox(self.frame_textures)
        self.checkBox_homogeneity.setObjectName(_fromUtf8("checkBox_homogeneity"))
        self.verticalLayout_2.addWidget(self.checkBox_homogeneity)
        self.lineEdit_output = QtGui.QLineEdit(Features)
        self.lineEdit_output.setGeometry(QtCore.QRect(50, 260, 241, 27))
        self.lineEdit_output.setObjectName(_fromUtf8("lineEdit_output"))
        self.pushButton_output = QtGui.QPushButton(Features)
        self.pushButton_output.setGeometry(QtCore.QRect(320, 260, 98, 27))
        self.pushButton_output.setObjectName(_fromUtf8("pushButton_output"))
        self.label_output = QtGui.QLabel(Features)
        self.label_output.setGeometry(QtCore.QRect(50, 240, 191, 17))
        self.label_output.setObjectName(_fromUtf8("label_output"))
        self.lineEdit_field = QtGui.QLineEdit(Features)
        self.lineEdit_field.setGeometry(QtCore.QRect(130, 310, 241, 27))
        self.lineEdit_field.setObjectName(_fromUtf8("lineEdit_field"))
        self.label_id = QtGui.QLabel(Features)
        self.label_id.setGeometry(QtCore.QRect(80, 320, 51, 17))
        self.label_id.setObjectName(_fromUtf8("label_id"))
        self.logo_unipv = QtGui.QLabel(Features)
        self.logo_unipv.setGeometry(QtCore.QRect(360, 20, 61, 61))
        self.logo_unipv.setText(_fromUtf8(""))
        self.logo_unipv.setPixmap(QtGui.QPixmap(_fromUtf8("unipv.png")))
        self.logo_unipv.setObjectName(_fromUtf8("logo_unipv"))
        self.logo_eucentre = QtGui.QLabel(Features)
        self.logo_eucentre.setGeometry(QtCore.QRect(160, 30, 181, 41))
        self.logo_eucentre.setText(_fromUtf8(""))
        self.logo_eucentre.setPixmap(QtGui.QPixmap(_fromUtf8("eucentre.png")))
        self.logo_eucentre.setObjectName(_fromUtf8("logo_eucentre"))
        self.logo_sensum = QtGui.QLabel(Features)
        self.logo_sensum.setGeometry(QtCore.QRect(30, 40, 101, 21))
        self.logo_sensum.setText(_fromUtf8(""))
        self.logo_sensum.setPixmap(QtGui.QPixmap(_fromUtf8("sensum.png")))
        self.logo_sensum.setObjectName(_fromUtf8("logo_sensum"))

        self.retranslateUi(Features)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Features.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Features.reject)
        QtCore.QMetaObject.connectSlotsByName(Features)

    def retranslateUi(self, Features):
        Features.setWindowTitle(_translate("Features", "SensumTools", None))
        self.label_input.setText(_translate("Features", "Input Raster", None))
        self.pushButton_input.setText(_translate("Features", "...", None))
        self.label_training.setText(_translate("Features", "Input Shapefile", None))
        self.pushButton_training.setText(_translate("Features", "...", None))
        self.label_title.setText(_translate("Features", "<html><head/><body><p><span style=\" font-size:16pt;\">FEATURES</span></p></body></html>", None))
        self.checkBox_maxbr.setText(_translate("Features", "Maximum BR", None))
        self.checkBox_mean.setText(_translate("Features", "Mean", None))
        self.checkBox_minbr.setText(_translate("Features", "Minimum BR", None))
        self.checkBox_mode.setText(_translate("Features", "Mode", None))
        self.checkBox_ndivistd.setText(_translate("Features", "NDVI Standard Deviation", None))
        self.checkBox_ndvimean.setText(_translate("Features", "NDIVI Mean", None))
        self.checkBox_std.setText(_translate("Features", "Standard Deviation", None))
        self.checkBox_weighbr.setText(_translate("Features", "Weigh BR", None))
        self.checkBox_asm.setText(_translate("Features", "ASM", None))
        self.checkBox_contrast.setText(_translate("Features", "Contrast", None))
        self.checkBox_correlation.setText(_translate("Features", "Correlation", None))
        self.checkBox_dissimilarity.setText(_translate("Features", "Dissimilarity", None))
        self.checkBox_energy.setText(_translate("Features", "Energy", None))
        self.checkBox_homogeneity.setText(_translate("Features", "Homogeneity", None))
        self.pushButton_output.setText(_translate("Features", "...", None))
        self.label_output.setText(_translate("Features", "Output Shapefile", None))
        self.lineEdit_field.setText(_translate("Features", "DN", None))
        self.label_id.setText(_translate("Features", "Field ID", None))

