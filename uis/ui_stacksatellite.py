# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stacksatellite.ui'
#
# Created: Tue Oct 21 16:00:40 2014
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_StackSatellite(object):
    def setupUi(self, StackSatellite):
        StackSatellite.setObjectName(_fromUtf8("StackSatellite"))
        StackSatellite.resize(483, 575)
        self.buttonBox = QtGui.QDialogButtonBox(StackSatellite)
        self.buttonBox.setGeometry(QtCore.QRect(240, 520, 171, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox_pixel = QtGui.QGroupBox(StackSatellite)
        self.groupBox_pixel.setGeometry(QtCore.QRect(60, 420, 151, 111))
        self.groupBox_pixel.setObjectName(_fromUtf8("groupBox_pixel"))
        self.checkBox_builtup_index = QtGui.QCheckBox(self.groupBox_pixel)
        self.checkBox_builtup_index.setGeometry(QtCore.QRect(10, 20, 101, 20))
        self.checkBox_builtup_index.setObjectName(_fromUtf8("checkBox_builtup_index"))
        self.checkBox_pca_index = QtGui.QCheckBox(self.groupBox_pixel)
        self.checkBox_pca_index.setGeometry(QtCore.QRect(10, 50, 85, 20))
        self.checkBox_pca_index.setObjectName(_fromUtf8("checkBox_pca_index"))
        self.checkBox_pca_classification = QtGui.QCheckBox(self.groupBox_pixel)
        self.checkBox_pca_classification.setGeometry(QtCore.QRect(10, 80, 131, 20))
        self.checkBox_pca_classification.setObjectName(_fromUtf8("checkBox_pca_classification"))
        self.checkBox_reference_diretory = QtGui.QCheckBox(StackSatellite)
        self.checkBox_reference_diretory.setEnabled(True)
        self.checkBox_reference_diretory.setGeometry(QtCore.QRect(40, 420, 141, 20))
        self.checkBox_reference_diretory.setChecked(False)
        self.checkBox_reference_diretory.setObjectName(_fromUtf8("checkBox_reference_diretory"))
        self.groupBox_options = QtGui.QGroupBox(StackSatellite)
        self.groupBox_options.setGeometry(QtCore.QRect(330, 250, 111, 111))
        self.groupBox_options.setObjectName(_fromUtf8("groupBox_options"))
        self.checkBox_coregistration = QtGui.QCheckBox(self.groupBox_options)
        self.checkBox_coregistration.setGeometry(QtCore.QRect(10, 20, 111, 20))
        self.checkBox_coregistration.setObjectName(_fromUtf8("checkBox_coregistration"))
        self.pushButton_satellite_folder = QtGui.QPushButton(StackSatellite)
        self.pushButton_satellite_folder.setGeometry(QtCore.QRect(350, 150, 98, 27))
        self.pushButton_satellite_folder.setObjectName(_fromUtf8("pushButton_satellite_folder"))
        self.pushButton_reference_directory = QtGui.QPushButton(StackSatellite)
        self.pushButton_reference_directory.setGeometry(QtCore.QRect(250, 440, 41, 27))
        self.pushButton_reference_directory.setObjectName(_fromUtf8("pushButton_reference_directory"))
        self.lineEdit_reference_directory = QtGui.QLineEdit(StackSatellite)
        self.lineEdit_reference_directory.setEnabled(True)
        self.lineEdit_reference_directory.setGeometry(QtCore.QRect(40, 440, 201, 27))
        self.lineEdit_reference_directory.setObjectName(_fromUtf8("lineEdit_reference_directory"))
        self.label_segmentation = QtGui.QLabel(StackSatellite)
        self.label_segmentation.setGeometry(QtCore.QRect(40, 250, 191, 17))
        self.label_segmentation.setObjectName(_fromUtf8("label_segmentation"))
        self.groupBox_object = QtGui.QGroupBox(StackSatellite)
        self.groupBox_object.setGeometry(QtCore.QRect(250, 420, 181, 81))
        self.groupBox_object.setObjectName(_fromUtf8("groupBox_object"))
        self.checkBox_dissimilarity = QtGui.QCheckBox(self.groupBox_object)
        self.checkBox_dissimilarity.setGeometry(QtCore.QRect(10, 20, 161, 20))
        self.checkBox_dissimilarity.setObjectName(_fromUtf8("checkBox_dissimilarity"))
        self.checkBox_pca_ob = QtGui.QCheckBox(self.groupBox_object)
        self.checkBox_pca_ob.setGeometry(QtCore.QRect(10, 50, 141, 20))
        self.checkBox_pca_ob.setObjectName(_fromUtf8("checkBox_pca_ob"))
        self.label_satellite_folder = QtGui.QLabel(StackSatellite)
        self.label_satellite_folder.setGeometry(QtCore.QRect(40, 132, 191, 17))
        self.label_satellite_folder.setObjectName(_fromUtf8("label_satellite_folder"))
        self.logo_unipv = QtGui.QLabel(StackSatellite)
        self.logo_unipv.setGeometry(QtCore.QRect(380, 10, 91, 81))
        self.logo_unipv.setText(_fromUtf8(""))
        self.logo_unipv.setPixmap(QtGui.QPixmap(_fromUtf8(".sensum/unipv.png")))
        self.logo_unipv.setObjectName(_fromUtf8("logo_unipv"))
        self.logo_sensum = QtGui.QLabel(StackSatellite)
        self.logo_sensum.setGeometry(QtCore.QRect(10, 20, 241, 61))
        self.logo_sensum.setText(_fromUtf8(""))
        self.logo_sensum.setPixmap(QtGui.QPixmap(_fromUtf8(".sensum/sensum.png")))
        self.logo_sensum.setObjectName(_fromUtf8("logo_sensum"))
        self.label_title = QtGui.QLabel(StackSatellite)
        self.label_title.setGeometry(QtCore.QRect(160, 100, 201, 21))
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.lineEdit_satellite_folder = QtGui.QLineEdit(StackSatellite)
        self.lineEdit_satellite_folder.setGeometry(QtCore.QRect(40, 150, 291, 27))
        self.lineEdit_satellite_folder.setObjectName(_fromUtf8("lineEdit_satellite_folder"))
        self.comboBox_segmentation = QtGui.QComboBox(StackSatellite)
        self.comboBox_segmentation.setGeometry(QtCore.QRect(40, 270, 280, 21))
        self.comboBox_segmentation.setObjectName(_fromUtf8("comboBox_segmentation"))
        self.comboBox_segmentation.addItem(_fromUtf8(""))
        self.comboBox_segmentation.addItem(_fromUtf8(""))
        self.logo_eucentre = QtGui.QLabel(StackSatellite)
        self.logo_eucentre.setGeometry(QtCore.QRect(280, 10, 71, 81))
        self.logo_eucentre.setText(_fromUtf8(""))
        self.logo_eucentre.setPixmap(QtGui.QPixmap(_fromUtf8(".sensum/eucentre.png")))
        self.logo_eucentre.setObjectName(_fromUtf8("logo_eucentre"))
        self.checkBox_restrict_to_city = QtGui.QCheckBox(StackSatellite)
        self.checkBox_restrict_to_city.setGeometry(QtCore.QRect(40, 190, 171, 20))
        self.checkBox_restrict_to_city.setChecked(True)
        self.checkBox_restrict_to_city.setObjectName(_fromUtf8("checkBox_restrict_to_city"))
        self.comboBox_input_shapefile = QtGui.QComboBox(StackSatellite)
        self.comboBox_input_shapefile.setGeometry(QtCore.QRect(40, 220, 401, 20))
        self.comboBox_input_shapefile.setObjectName(_fromUtf8("comboBox_input_shapefile"))
        self.comboBox_input_shapefile.addItem(_fromUtf8(""))
        self.label_nclasses = QtGui.QLabel(StackSatellite)
        self.label_nclasses.setGeometry(QtCore.QRect(340, 310, 91, 16))
        self.label_nclasses.setObjectName(_fromUtf8("label_nclasses"))
        self.spinBox_nclasses = QtGui.QSpinBox(StackSatellite)
        self.spinBox_nclasses.setGeometry(QtCore.QRect(360, 330, 53, 18))
        self.spinBox_nclasses.setObjectName(_fromUtf8("spinBox_nclasses"))
        self.groupBox_edison = QtGui.QGroupBox(StackSatellite)
        self.groupBox_edison.setGeometry(QtCore.QRect(40, 300, 271, 80))
        self.groupBox_edison.setObjectName(_fromUtf8("groupBox_edison"))
        self.lineEdit_edison_radius = QtGui.QLineEdit(self.groupBox_edison)
        self.lineEdit_edison_radius.setGeometry(QtCore.QRect(90, 24, 31, 20))
        self.lineEdit_edison_radius.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_edison_radius.setObjectName(_fromUtf8("lineEdit_edison_radius"))
        self.label_edison_size_2 = QtGui.QLabel(self.groupBox_edison)
        self.label_edison_size_2.setGeometry(QtCore.QRect(17, 50, 67, 20))
        self.label_edison_size_2.setObjectName(_fromUtf8("label_edison_size_2"))
        self.label_edison_scale_2 = QtGui.QLabel(self.groupBox_edison)
        self.label_edison_scale_2.setGeometry(QtCore.QRect(150, 50, 51, 20))
        self.label_edison_scale_2.setObjectName(_fromUtf8("label_edison_scale_2"))
        self.lineEdit_edison_scale = QtGui.QLineEdit(self.groupBox_edison)
        self.lineEdit_edison_scale.setGeometry(QtCore.QRect(210, 50, 41, 20))
        self.lineEdit_edison_scale.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_edison_scale.setObjectName(_fromUtf8("lineEdit_edison_scale"))
        self.label_edison_radius_2 = QtGui.QLabel(self.groupBox_edison)
        self.label_edison_radius_2.setGeometry(QtCore.QRect(17, 24, 67, 20))
        self.label_edison_radius_2.setObjectName(_fromUtf8("label_edison_radius_2"))
        self.label_edison_range_2 = QtGui.QLabel(self.groupBox_edison)
        self.label_edison_range_2.setGeometry(QtCore.QRect(140, 24, 66, 20))
        self.label_edison_range_2.setObjectName(_fromUtf8("label_edison_range_2"))
        self.lineEdit_edison_range = QtGui.QLineEdit(self.groupBox_edison)
        self.lineEdit_edison_range.setGeometry(QtCore.QRect(210, 20, 41, 20))
        self.lineEdit_edison_range.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_edison_range.setObjectName(_fromUtf8("lineEdit_edison_range"))
        self.lineEdit_edison_size = QtGui.QLineEdit(self.groupBox_edison)
        self.lineEdit_edison_size.setGeometry(QtCore.QRect(90, 50, 31, 20))
        self.lineEdit_edison_size.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_edison_size.setObjectName(_fromUtf8("lineEdit_edison_size"))
        self.groupBox_meanshift = QtGui.QGroupBox(StackSatellite)
        self.groupBox_meanshift.setGeometry(QtCore.QRect(40, 300, 271, 111))
        self.groupBox_meanshift.setObjectName(_fromUtf8("groupBox_meanshift"))
        self.label_meanshift_range = QtGui.QLabel(self.groupBox_meanshift)
        self.label_meanshift_range.setGeometry(QtCore.QRect(130, 24, 70, 20))
        self.label_meanshift_range.setObjectName(_fromUtf8("label_meanshift_range"))
        self.lineEdit_meanshift_range = QtGui.QLineEdit(self.groupBox_meanshift)
        self.lineEdit_meanshift_range.setGeometry(QtCore.QRect(210, 20, 41, 20))
        self.lineEdit_meanshift_range.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_meanshift_range.setObjectName(_fromUtf8("lineEdit_meanshift_range"))
        self.label_meanshift_spatial = QtGui.QLabel(self.groupBox_meanshift)
        self.label_meanshift_spatial.setGeometry(QtCore.QRect(20, 24, 64, 20))
        self.label_meanshift_spatial.setObjectName(_fromUtf8("label_meanshift_spatial"))
        self.label_meanshift_threshold = QtGui.QLabel(self.groupBox_meanshift)
        self.label_meanshift_threshold.setGeometry(QtCore.QRect(20, 50, 64, 20))
        self.label_meanshift_threshold.setObjectName(_fromUtf8("label_meanshift_threshold"))
        self.lineEdit_meanshift_radius = QtGui.QLineEdit(self.groupBox_meanshift)
        self.lineEdit_meanshift_radius.setGeometry(QtCore.QRect(90, 24, 31, 20))
        self.lineEdit_meanshift_radius.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_meanshift_radius.setObjectName(_fromUtf8("lineEdit_meanshift_radius"))
        self.lineEdit_meanshift_iterations = QtGui.QLineEdit(self.groupBox_meanshift)
        self.lineEdit_meanshift_iterations.setGeometry(QtCore.QRect(210, 50, 41, 20))
        self.lineEdit_meanshift_iterations.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_meanshift_iterations.setObjectName(_fromUtf8("lineEdit_meanshift_iterations"))
        self.label_meanshift_iterations = QtGui.QLabel(self.groupBox_meanshift)
        self.label_meanshift_iterations.setGeometry(QtCore.QRect(130, 50, 70, 20))
        self.label_meanshift_iterations.setObjectName(_fromUtf8("label_meanshift_iterations"))
        self.lineEdit_meanshift_threshold = QtGui.QLineEdit(self.groupBox_meanshift)
        self.lineEdit_meanshift_threshold.setGeometry(QtCore.QRect(90, 50, 31, 20))
        self.lineEdit_meanshift_threshold.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_meanshift_threshold.setObjectName(_fromUtf8("lineEdit_meanshift_threshold"))
        self.label_meanshift_minsize = QtGui.QLabel(self.groupBox_meanshift)
        self.label_meanshift_minsize.setGeometry(QtCore.QRect(20, 80, 64, 20))
        self.label_meanshift_minsize.setObjectName(_fromUtf8("label_meanshift_minsize"))
        self.lineEdit_meanshift_minsize = QtGui.QLineEdit(self.groupBox_meanshift)
        self.lineEdit_meanshift_minsize.setGeometry(QtCore.QRect(90, 80, 31, 20))
        self.lineEdit_meanshift_minsize.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_meanshift_minsize.setObjectName(_fromUtf8("lineEdit_meanshift_minsize"))

        self.retranslateUi(StackSatellite)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), StackSatellite.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), StackSatellite.accept)
        QtCore.QMetaObject.connectSlotsByName(StackSatellite)

    def retranslateUi(self, StackSatellite):
        StackSatellite.setWindowTitle(_translate("StackSatellite", "SensumTools", None))
        self.groupBox_pixel.setTitle(_translate("StackSatellite", "Pixel Based Method", None))
        self.checkBox_builtup_index.setText(_translate("StackSatellite", "Buit-up Index", None))
        self.checkBox_pca_index.setText(_translate("StackSatellite", "PCA Index", None))
        self.checkBox_pca_classification.setText(_translate("StackSatellite", "PCA classification", None))
        self.checkBox_reference_diretory.setText(_translate("StackSatellite", "Reference Directory", None))
        self.groupBox_options.setTitle(_translate("StackSatellite", "Options", None))
        self.checkBox_coregistration.setText(_translate("StackSatellite", "Coregistration", None))
        self.pushButton_satellite_folder.setText(_translate("StackSatellite", "...", None))
        self.pushButton_reference_directory.setText(_translate("StackSatellite", "...", None))
        self.label_segmentation.setText(_translate("StackSatellite", "Segmentation", None))
        self.groupBox_object.setTitle(_translate("StackSatellite", "Object Based Method", None))
        self.checkBox_dissimilarity.setText(_translate("StackSatellite", "Dissimilarity-based", None))
        self.checkBox_pca_ob.setText(_translate("StackSatellite", "PCA-based", None))
        self.label_satellite_folder.setText(_translate("StackSatellite", "Satellite Folder", None))
        self.label_title.setText(_translate("StackSatellite", "<html><head/><body><p><span style=\" font-size:16pt;\">STACK SATELLITE</span></p></body></html>", None))
        self.comboBox_segmentation.setItemText(0, _translate("StackSatellite", "Edison", None))
        self.comboBox_segmentation.setItemText(1, _translate("StackSatellite", "Meanshift", None))
        self.checkBox_restrict_to_city.setText(_translate("StackSatellite", "Restrict to City Shapefile", None))
        self.comboBox_input_shapefile.setItemText(0, _translate("StackSatellite", "[Choose from a file..]", "Click to select File"))
        self.label_nclasses.setText(_translate("StackSatellite", "Number of classes", None))
        self.groupBox_edison.setTitle(_translate("StackSatellite", "Edison Paramaters", None))
        self.lineEdit_edison_radius.setText(_translate("StackSatellite", "5", None))
        self.label_edison_size_2.setText(_translate("StackSatellite", "Minimum size", None))
        self.label_edison_scale_2.setText(_translate("StackSatellite", "Scale", None))
        self.lineEdit_edison_scale.setText(_translate("StackSatellite", "1", None))
        self.label_edison_radius_2.setText(_translate("StackSatellite", "Spatial radius ", None))
        self.label_edison_range_2.setText(_translate("StackSatellite", "Range Radius", None))
        self.lineEdit_edison_range.setText(_translate("StackSatellite", "15", None))
        self.lineEdit_edison_size.setText(_translate("StackSatellite", "100", None))
        self.groupBox_meanshift.setTitle(_translate("StackSatellite", "Meanshift Paramaters", None))
        self.label_meanshift_range.setText(_translate("StackSatellite", "Range", None))
        self.lineEdit_meanshift_range.setText(_translate("StackSatellite", "15", None))
        self.label_meanshift_spatial.setText(_translate("StackSatellite", "Spatial radius", None))
        self.label_meanshift_threshold.setText(_translate("StackSatellite", "Threshold", None))
        self.lineEdit_meanshift_radius.setText(_translate("StackSatellite", "5", None))
        self.lineEdit_meanshift_iterations.setText(_translate("StackSatellite", "100", None))
        self.label_meanshift_iterations.setText(_translate("StackSatellite", "Max Iterations", None))
        self.lineEdit_meanshift_threshold.setText(_translate("StackSatellite", "0.1", None))
        self.label_meanshift_minsize.setText(_translate("StackSatellite", "Minimum size", None))
        self.lineEdit_meanshift_minsize.setText(_translate("StackSatellite", "100", None))

