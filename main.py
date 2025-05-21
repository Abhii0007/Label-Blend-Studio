import os
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--log-level=3"
import sys,io

import shutil
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout,
    QWidget, QSpinBox, QHBoxLayout, QLineEdit, QMessageBox
)
from PySide6.QtGui import QPixmap, QImage,QPainter
from PySide6.QtCore import Qt,QUrl
from PIL import Image, ImageQt
from concurrent.futures import ThreadPoolExecutor

import numpy as np
from PIL import ImageDraw
from PySide6.QtWidgets import QPushButton
import cv2
from PySide6.QtGui import QDesktopServices

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog,
    QGraphicsView, QGraphicsScene, QGraphicsPixmapItem,
    QWidget, QHBoxLayout
)
from natsort import natsorted

from PySide6.QtWebEngineWidgets import QWebEngineView 
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEngineSettings




from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFrame, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QTabWidget, QToolButton, QWidget)


class Ui_Form(QWidget):
    def __init__(self,Form):
        super().__init__()
        
        self.widget_8 = QWidget(self)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 0, 1920, 951))
        self.widget_8.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(5, 50, 1910, 891))
        self.widget_9.setStyleSheet(u"background-color: rgb(44, 44, 85);")
        self.label = QLabel(self.widget_9)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 5, 1600, 880))
        font = QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet(u"#label {\n"
    "   \n"
    "	background-color: #140827;\n"
    "    border: 1px solid #7f67d5;\n"
    "    border-radius: 10px;\n"
    "	\n"
    "	color: rgb(56, 48, 86);\n"
    "}\n"
    "\n"
    "#label:hover {\n"
    "    border: 2px solid #5424a7; /* red border on hover */\n"
    "    border-radius: 15px;\n"
    "}\n"
    "")
        self.label.setPixmap(QPixmap(u"banner.jpg"))
        self.label.setScaledContents(True)
        self.label.setMargin(7)
        self.label.setIndent(0)
        self.widget = QWidget(self.widget_9)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(1612, 7, 292, 100))
        self.widget.setStyleSheet(u"#widget {\n"
    "   \n"
    "	background-color: rgb(39, 39, 39);\n"
    "    border: 1px solid #7f67d5;\n"
    "    border-radius: 15px;\n"
    "}\n"
    "\n"
    "#widget:hover {\n"
    "    border: 1px solid #1abc9c; /* red border on hover */\n"
    "    border-radius: 15px;\n"
    "}\n"
    "")
        self.pushButton_generate_single_btn = QPushButton(self.widget)
        self.pushButton_generate_single_btn.setObjectName(u"pushButton_generate_single_btn")
        self.pushButton_generate_single_btn.setGeometry(QRect(5, 63, 281, 25))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton_generate_single_btn.setFont(font1)
        self.pushButton_generate_single_btn.setStyleSheet(u"#pushButton_generate_single_btn{\n"
    "    color: rgb(0, 0, 0);\n"
    "    background-color: #62dfb9;\n"
    "    font: 11pt \"Segoe UI\";\n"
    "    border: none;\n"
    "    border-radius: 12px;\n"
    "\n"
    "\n"
    "}\n"
    "\n"
    "#pushButton_generate_single_btn:hover {\n"
    "    background-color: rgb(134, 255, 215);\n"
    "}\n"
    "\n"
    "#pushButton_generate_single_btn:pressed {\n"
    "    background-color: #ad98ff;\n"
    "    padding-left: 3px;\n"
    "	padding-top: 2px;\n"
    "  \n"
    "\n"
    "}\n"
    "\n"
    "#pushButton_generate_single_btn:disabled {\n"
    "    background-color: rgb(180, 180, 180);\n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "")
        self.pushButton_select_cutouts_btn = QPushButton(self.widget)
        self.pushButton_select_cutouts_btn.setObjectName(u"pushButton_select_cutouts_btn")
        self.pushButton_select_cutouts_btn.setGeometry(QRect(145, 30, 139, 25))
        self.pushButton_select_cutouts_btn.setFont(font1)
        self.pushButton_select_cutouts_btn.setStyleSheet(u"#pushButton_select_cutouts_btn {\n"
    "    color: rgb(0, 0, 0);\n"
    "    background-color: #eab88f;\n"
    "    font: 11pt \"Segoe UI\";\n"
    "    border: none;\n"
    "    border-radius: 5px;\n"
    "\n"
    "\n"
    "}\n"
    "\n"
    "#pushButton_select_cutouts_btn:hover {\n"
    "    background-color: #ffd7a7;\n"
    "}\n"
    "\n"
    "#pushButton_select_cutouts_btn:pressed {\n"
    "    background-color: #ad98ff;\n"
    "    padding-left: 3px;\n"
    "	padding-top: 2px;\n"
    "  \n"
    "\n"
    "}\n"
    "\n"
    "#pushButton_select_cutouts_btn:disabled {\n"
    "    background-color: rgb(180, 180, 180);\n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "")
        self.pushButton_select_background_btn = QPushButton(self.widget)
        self.pushButton_select_background_btn.setObjectName(u"pushButton_select_background_btn")
        self.pushButton_select_background_btn.setGeometry(QRect(7, 30, 132, 25))
        self.pushButton_select_background_btn.setFont(font1)
        self.pushButton_select_background_btn.setStyleSheet(u"#pushButton_select_background_btn {\n"
    "    color: rgb(0, 0, 0);\n"
    "    background-color: #8ac8ef;\n"
    "    font: 11pt \"Segoe UI\";\n"
    "    border: none;\n"
    "    border-radius: 5px;\n"
    "\n"
    "}\n"
    "\n"
    "#pushButton_select_background_btn:hover {\n"
    "    background-color: #b4f9ff;\n"
    "}\n"
    "\n"
    "#pushButton_select_background_btn:pressed {\n"
    "    background-color: #ad98ff;\n"
    "    padding-left: 3px;\n"
    "	padding-top: 2px;\n"
    "  \n"
    "\n"
    "}\n"
    "\n"
    "#pushButton_select_background_btn:disabled {\n"
    "    background-color: rgb(180, 180, 180);\n"
    "    color: rgb(100, 100, 100);\n"
    "}\n"
    "")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(2, 2, 288, 24))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"#label_6 {\n"
    "    color: rgb(180, 161, 255);\n"
    "    background-color: rgb(20, 8, 39);\n"
    "    border-top-left-radius: 12px;\n"
    "    border-top-right-radius: 12px;\n"
    "    border-bottom-left-radius: 0px;\n"
    "    border-bottom-right-radius: 0px;\n"
    "}\n"
    "")
        self.widget_2 = QWidget(self.widget_9)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(1612, 495, 292, 100))
        self.widget_2.setStyleSheet(u"#widget_2 {\n"
    "   \n"
    "	background-color: #433048;\n"
    "    border: 1px solid #7f67d5;\n"
    "    border-radius: 15px;\n"
    "}\n"
    "\n"
    "#widget_2:hover {\n"
    "    border: 1px solid #1abc9c; /* red border on hover */\n"
    "    border-radius: 15px;\n"
    "}\n"
    "")
        self.pushButton_generate_btn = QPushButton(self.widget_2)
        self.pushButton_generate_btn.setObjectName(u"pushButton_generate_btn")
        self.pushButton_generate_btn.setGeometry(QRect(5, 68, 281, 25))
        self.pushButton_generate_btn.setFont(font1)
        self.pushButton_generate_btn.setStyleSheet(u"#pushButton_generate_btn{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #d9b8ff;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"\n"
"}\n"
"\n"
"#pushButton_generate_btn:hover {\n"
"    background-color: #edd3ff;\n"
"}\n"
"\n"
"#pushButton_generate_btn:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_open_folder:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.toolButton_open_box_folder = QToolButton(self.widget_2)
        self.toolButton_open_box_folder.setObjectName(u"toolButton_open_box_folder")
        self.toolButton_open_box_folder.setGeometry(QRect(258, 33, 25, 25))
        self.toolButton_open_box_folder.setStyleSheet(u"background-color: rgb(255, 214, 180);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_box_location = QLineEdit(self.widget_2)
        self.lineEdit_box_location.setObjectName(u"lineEdit_box_location")
        self.lineEdit_box_location.setGeometry(QRect(77, 33, 174, 26))
        self.lineEdit_box_location.setStyleSheet(u"#lineEdit_box_location {\n"
"    background-color: #1e1e2f;\n"
"    color: #ffffff;\n"
"    border: 1px solid #56458f;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"#lineEdit_box_location:focus {\n"
"    border: 1px solid #8ae6c3;\n"
"    background-color: #2a2a40;\n"
"    color: #ffffff;\n"
"}\n"
"")
        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(9, 28, 66, 31))
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: #433048")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(2, 2, 288, 24))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"#label_5 {\n"
"    color: rgb(180, 161, 255);\n"
"    background-color: rgb(20, 8, 39);\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.widget_3 = QWidget(self.widget_9)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(1612, 606, 292, 140))
        self.widget_3.setStyleSheet(u"#widget_3 {\n"
"   \n"
"	background-color: #22313f;\n"
"    border: 1px solid #7f67d5;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#widget_3:hover {\n"
"    border: 1px solid #1abc9c; /* red border on hover */\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.pushButton_segmentation_button = QPushButton(self.widget_3)
        self.pushButton_segmentation_button.setObjectName(u"pushButton_segmentation_button")
        self.pushButton_segmentation_button.setGeometry(QRect(5, 105, 281, 25))
        self.pushButton_segmentation_button.setFont(font1)
        self.pushButton_segmentation_button.setStyleSheet(u"#pushButton_segmentation_button {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #8ac8ef;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"\n"
"}\n"
"\n"
"#pushButton_segmentation_button:hover {\n"
"    background-color: #b4f9ff;\n"
"}\n"
"\n"
"#pushButton_segmentation_button:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_segmentation_button:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.toolButton_toolButton_open_segment_folder = QToolButton(self.widget_3)
        self.toolButton_toolButton_open_segment_folder.setObjectName(u"toolButton_toolButton_open_segment_folder")
        self.toolButton_toolButton_open_segment_folder.setGeometry(QRect(258, 68, 25, 25))
        self.toolButton_toolButton_open_segment_folder.setStyleSheet(u"background-color: rgb(255, 214, 180);\n"
"color: rgb(0, 0, 0);")
        self.spinBox_resolution_epsilon = QSpinBox(self.widget_3)
        self.spinBox_resolution_epsilon.setObjectName(u"spinBox_resolution_epsilon")
        self.spinBox_resolution_epsilon.setGeometry(QRect(130, 34, 91, 26))
        self.spinBox_resolution_epsilon.setStyleSheet(u"background-color: rgb(86, 69, 143);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";")
        self.spinBox_resolution_epsilon.setMinimum(1)
        self.spinBox_resolution_epsilon.setMaximum(100)
        self.spinBox_resolution_epsilon.setSingleStep(5)
        self.spinBox_resolution_epsilon.setValue(10)
        self.spinBox_resolution_epsilon.setDisplayIntegerBase(10)
        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(7, 31, 121, 31))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: #22313f")
        self.pushButton_default_res = QPushButton(self.widget_3)
        self.pushButton_default_res.setObjectName(u"pushButton_default_res")
        self.pushButton_default_res.setGeometry(QRect(225, 34, 61, 26))
        self.pushButton_default_res.setFont(font2)
        self.pushButton_default_res.setStyleSheet(u"background-color: rgb(255, 174, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 65, 77, 31))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: #22313f")
        self.lineEdit_segment_location = QLineEdit(self.widget_3)
        self.lineEdit_segment_location.setObjectName(u"lineEdit_segment_location")
        self.lineEdit_segment_location.setGeometry(QRect(77, 68, 174, 26))
        self.lineEdit_segment_location.setStyleSheet(u"#lineEdit_segment_location {\n"
"    background-color: #1e1e2f;\n"
"    color: #ffffff;\n"
"    border: 1px solid #56458f;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"#lineEdit_segment_location:focus {\n"
"    border: 1px solid #8ae6c3;\n"
"    background-color: #2a2a40;\n"
"    color: #ffffff;\n"
"}\n"
"")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(2, 2, 288, 24))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"#label_7 {\n"
"    color: rgb(180, 161, 255);\n"
"    background-color: rgb(20, 8, 39);\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.widget_4 = QWidget(self.widget_9)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(1612, 343, 292, 140))
        self.widget_4.setStyleSheet(u"#widget_4 {\n"
"   \n"
"	background-color: rgb(39, 39, 39);\n"
"    border: 1px solid #7f67d5;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#widget_4:hover {\n"
"    border: 1px solid #1abc9c; /* red border on hover */\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(2, 2, 288, 24))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"#label_9 {\n"
"    color: rgb(180, 161, 255);\n"
"    background-color: rgb(20, 8, 39);\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.spinBox_height = QSpinBox(self.widget_4)
        self.spinBox_height.setObjectName(u"spinBox_height")
        self.spinBox_height.setGeometry(QRect(174, 35, 107, 26))
        self.spinBox_height.setStyleSheet(u"background-color: rgb(86, 69, 143);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";")
        self.spinBox_height.setMinimum(200)
        self.spinBox_height.setMaximum(3840)
        self.spinBox_height.setSingleStep(40)
        self.spinBox_height.setValue(1024)
        self.spinBox_height.setDisplayIntegerBase(10)
        self.spinBox_width = QSpinBox(self.widget_4)
        self.spinBox_width.setObjectName(u"spinBox_width")
        self.spinBox_width.setGeometry(QRect(62, 35, 107, 26))
        self.spinBox_width.setStyleSheet(u"background-color: rgb(86, 69, 143);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";")
        self.spinBox_width.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox_width.setMinimum(200)
        self.spinBox_width.setMaximum(3840)
        self.spinBox_width.setSingleStep(40)
        self.spinBox_width.setValue(1024)
        self.spinBox_width.setDisplayIntegerBase(10)
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(15, 35, 38, 21))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: rgb(39, 39, 39);")
        self.pushButton_default = QPushButton(self.widget_4)
        self.pushButton_default.setObjectName(u"pushButton_default")
        self.pushButton_default.setGeometry(QRect(208, 104, 73, 26))
        self.pushButton_default.setFont(font2)
        self.pushButton_default.setStyleSheet(u"background-color: rgb(255, 174, 193);\n"
"color: rgb(0, 0, 0);")
        self.horizontalSlider_quality = QSlider(self.widget_4)
        self.horizontalSlider_quality.setObjectName(u"horizontalSlider_quality")
        self.horizontalSlider_quality.setGeometry(QRect(74, 75, 110, 18))
        self.horizontalSlider_quality.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.horizontalSlider_quality.setMinimum(10)
        self.horizontalSlider_quality.setMaximum(100)
        self.horizontalSlider_quality.setSingleStep(5)
        self.horizontalSlider_quality.setValue(90)
        self.horizontalSlider_quality.setSliderPosition(90)
        self.horizontalSlider_quality.setOrientation(Qt.Orientation.Horizontal)
        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(16, 65, 56, 31))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: rgb(39, 39, 39);")
        self.spinBox_num_quality = QSpinBox(self.widget_4)
        self.spinBox_num_quality.setObjectName(u"spinBox_num_quality")
        self.spinBox_num_quality.setGeometry(QRect(190, 70, 90, 26))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.spinBox_num_quality.setFont(font3)
        self.spinBox_num_quality.setStyleSheet(u"background-color: rgb(86, 69, 143);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";")
        self.spinBox_num_quality.setMinimum(10)
        self.spinBox_num_quality.setMaximum(100)
        self.spinBox_num_quality.setSingleStep(5)
        self.spinBox_num_quality.setValue(90)
        self.checkBox = QCheckBox(self.widget_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 104, 201, 24))
        self.checkBox.setFont(font2)
        self.checkBox.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: rgb(39, 39, 39);")
        self.checkBox.setChecked(True)
        self.widget_5 = QWidget(self.widget_9)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(1612, 758, 292, 126))
        self.widget_5.setStyleSheet(u"#widget_5 {\n"
"   \n"
"	background-color: rgb(39, 39, 39);\n"
"    border: 1px solid #7f67d5;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#widget_5:hover {\n"
"    border: 1px solid #1abc9c; /* red border on hover */\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.label_19 = QLabel(self.widget_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 61, 141, 22))
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: rgb(39, 39, 39);")
        self.toolButton_Select_image_folder = QToolButton(self.widget_5)
        self.toolButton_Select_image_folder.setObjectName(u"toolButton_Select_image_folder")
        self.toolButton_Select_image_folder.setGeometry(QRect(150, 61, 25, 25))
        self.toolButton_Select_image_folder.setStyleSheet(u"background-color: rgb(255, 214, 180);\n"
"color: rgb(0, 0, 0);")
        self.toolButton_Select_label_folder = QToolButton(self.widget_5)
        self.toolButton_Select_label_folder.setObjectName(u"toolButton_Select_label_folder")
        self.toolButton_Select_label_folder.setGeometry(QRect(150, 89, 25, 25))
        self.toolButton_Select_label_folder.setStyleSheet(u"background-color: rgb(255, 214, 180);\n"
"color: rgb(0, 0, 0);")
        self.label_20 = QLabel(self.widget_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 89, 141, 22))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: rgb(39, 39, 39);")
        self.pushButton_force_split = QPushButton(self.widget_5)
        self.pushButton_force_split.setObjectName(u"pushButton_force_split")
        self.pushButton_force_split.setGeometry(QRect(186, 90, 102, 25))
        self.pushButton_force_split.setFont(font1)
        self.pushButton_force_split.setStyleSheet(u"#pushButton_force_split{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #62dfb9;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"\n"
"\n"
"}\n"
"\n"
"#pushButton_force_split:hover {\n"
"    background-color: rgb(134, 255, 215);\n"
"}\n"
"\n"
"#pushButton_force_split:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_generate_single_btn:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.label_17 = QLabel(self.widget_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 32, 81, 22))
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: rgb(39, 39, 39);")
        self.comboBox_split = QComboBox(self.widget_5)
        self.comboBox_split.addItem("")
        self.comboBox_split.addItem("")
        self.comboBox_split.addItem("")
        self.comboBox_split.addItem("")
        self.comboBox_split.addItem("")
        self.comboBox_split.addItem("")
        self.comboBox_split.setObjectName(u"comboBox_split")
        self.comboBox_split.setGeometry(QRect(90, 31, 193, 24))
        self.comboBox_split.setStyleSheet(u"background-color: rgb(86, 69, 143);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";")
        self.pushButton_splitter_default = QPushButton(self.widget_5)
        self.pushButton_splitter_default.setObjectName(u"pushButton_splitter_default")
        self.pushButton_splitter_default.setGeometry(QRect(223, 58, 61, 26))
        self.pushButton_splitter_default.setFont(font2)
        self.pushButton_splitter_default.setStyleSheet(u"background-color: rgb(255, 174, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_11 = QLabel(self.widget_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(2, 2, 288, 24))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"#label_11 {\n"
"    color: rgb(180, 161, 255);\n"
"    background-color: rgb(20, 8, 39);\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.listWidget = QListWidget(self.widget_9)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(1612, 118, 292, 215))
        self.listWidget.setStyleSheet(u"#listWidget {\n"
"    font: 12pt \"Segoe UI\";\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid #7f67d5;\n"
"    border-radius: 15px;\n"
"    padding: 5px;\n"
"    outline: none;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Hover effect for the entire list widget */\n"
"#listWidget:hover {\n"
"    border: 1px solid #1abc9c;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"/* Style for each item inside the list */\n"
"#listWidget::item {\n"
"    border-radius: 10px;\n"
"    padding: 4px 6px;\n"
"    margin: 2px 0;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Hover effect for each individual list item */\n"
"#listWidget::item:hover {\n"
"    background-color: #1abc9c;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Selected item style */\n"
"#listWidget::item:selected {\n"
"    background-color: #7f67d5;\n"
"    color: white;\n"
"}\n"
"")
        self.listWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.listWidget.setLineWidth(1)
        self.listWidget.setMidLineWidth(-3)
        self.listWidget.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.listWidget.setSortingEnabled(True)
        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(5, 5, 1910, 40))
        self.widget_10.setStyleSheet(u"#widget_10 {\n"
"   \n"
"	background-color: #56458f;\n"
"    border: 1px solid #140827;\n"
"	color: rgb(121, 98, 203);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.label_1 = QLabel(self.widget_10)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(19, 8, 113, 21))
        font4 = QFont()
        font4.setPointSize(11)
        self.label_1.setFont(font4)
        self.label_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(86, 69, 143);")
        self.label_2 = QLabel(self.widget_10)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(244, 8, 115, 21))
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(86, 69, 143);")
        self.label_3 = QLabel(self.widget_10)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(715, 8, 182, 21))
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(86, 69, 143);")
        self.pushButton_open_folder = QPushButton(self.widget_10)
        self.pushButton_open_folder.setObjectName(u"pushButton_open_folder")
        self.pushButton_open_folder.setGeometry(QRect(1688, 7, 115, 25))
        self.pushButton_open_folder.setFont(font1)
        self.pushButton_open_folder.setStyleSheet(u"#pushButton_open_folder{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #8ac8ef;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"#pushButton_open_folder:hover {\n"
"    background-color: #edd3ff;\n"
"}\n"
"\n"
"#pushButton_open_folder:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_open_folder:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.spinBox_min_size_input = QSpinBox(self.widget_10)
        self.spinBox_min_size_input.setObjectName(u"spinBox_min_size_input")
        self.spinBox_min_size_input.setGeometry(QRect(132, 7, 100, 26))
        self.spinBox_min_size_input.setStyleSheet(u"background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.spinBox_min_size_input.setMaximum(1000)
        self.spinBox_min_size_input.setValue(50)
        self.spinBox_max_size_input = QSpinBox(self.widget_10)
        self.spinBox_max_size_input.setObjectName(u"spinBox_max_size_input")
        self.spinBox_max_size_input.setGeometry(QRect(360, 7, 100, 26))
        self.spinBox_max_size_input.setStyleSheet(u"background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.spinBox_max_size_input.setMaximum(1000)
        self.spinBox_max_size_input.setValue(150)
        self.spinBox_num_images_input = QSpinBox(self.widget_10)
        self.spinBox_num_images_input.setObjectName(u"spinBox_num_images_input")
        self.spinBox_num_images_input.setGeometry(QRect(895, 7, 100, 26))
        self.spinBox_num_images_input.setStyleSheet(u"background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.spinBox_num_images_input.setMaximum(10000)
        self.spinBox_num_images_input.setValue(10)
        self.spinBox_starting_image_input = QSpinBox(self.widget_10)
        self.spinBox_starting_image_input.setObjectName(u"spinBox_starting_image_input")
        self.spinBox_starting_image_input.setGeometry(QRect(600, 7, 100, 26))
        self.spinBox_starting_image_input.setStyleSheet(u"background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.spinBox_starting_image_input.setMaximum(10000)
        self.spinBox_starting_image_input.setValue(1)
        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(474, 8, 127, 21))
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(86, 69, 143);")
        self.toolButton_prev = QToolButton(self.widget_10)
        self.toolButton_prev.setObjectName(u"toolButton_prev")
        self.toolButton_prev.setGeometry(QRect(1809, 5, 45, 30))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.toolButton_prev.setFont(font5)
        self.toolButton_next = QToolButton(self.widget_10)
        self.toolButton_next.setObjectName(u"toolButton_next")
        self.toolButton_next.setGeometry(QRect(1858, 5, 45, 30))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setItalic(False)
        self.toolButton_next.setFont(font6)
        self.toolButton_next.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_background_src = QLabel(self.widget_10)
        self.label_background_src.setObjectName(u"label_background_src")
        self.label_background_src.setGeometry(QRect(1009, 8, 111, 21))
        self.label_background_src.setFont(font4)
        self.label_background_src.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(86, 69, 143);")
        self.lineEdit_background_src = QLineEdit(self.widget_10)
        self.lineEdit_background_src.setObjectName(u"lineEdit_background_src")
        self.lineEdit_background_src.setGeometry(QRect(1120, 5, 281, 30))
        self.lineEdit_background_src.setStyleSheet(u"#lineEdit_background_src {\n"
"    background-color: #140827;\n"
"    color: #ffffff;\n"
"    border: 1px solid #56458f;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"#lineEdit_background_src:focus {\n"
"    border: 1px solid #8ae6c3;\n"
"    background-color: #2a2a40;\n"
"    color: #ffffff;\n"
"}\n"
"")
        self.lineEdit_background_src.setReadOnly(True)
        self.comboBox_profile = QComboBox(self.widget_10)
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.setObjectName(u"comboBox_profile")
        self.comboBox_profile.setGeometry(QRect(1459, 7, 215, 25))
        self.comboBox_profile.setStyleSheet(u"#comboBox_profile {\n"
"    color: #000000;\n"
"    background-color: #d9b8ff;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"#comboBox_profile::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 5px;\n"
"    border-left: 1px solid rgba(0, 0, 0, 0.1);\n"
"    background-color: rgb(180, 161, 255);\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#comboBox_profile:hover {\n"
"    background-color: #7feccc;\n"
"}\n"
"\n"
"\n"
"#comboBox_profile:disabled {\n"
"    background-color: #cccccc;\n"
"    color: #666666;\n"
"}\n"
"\n"
"\n"
"\n"
"#comboBox_profile::down-arrow {\n"
"    width: 8px;\n"
"    height: 12px;\n"
"    image: url(:/icons/down-arrow.png); /* Optional: replace or remove */\n"
"}\n"
"\n"
"/* Dropdown list view */\n"
"#comboBox_profile QAbstractItemView {\n"
"    color: #b7a9ff;\n"
"    background-color: #140827;\n"
"    border: "
                        "1px solid #dddddd;\n"
"    selection-background-color: #5c2d91; /* Optional: active selection color */\n"
"    selection-color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* Red background on hover inside dropdown items */\n"
"#comboBox_profile QAbstractItemView::item:hover {\n"
"    background-color: #d9b8ff;\n"
"    color: black;\n"
"}\n"
"")
        self.label_background_src_2 = QLabel(self.widget_10)
        self.label_background_src_2.setObjectName(u"label_background_src_2")
        self.label_background_src_2.setGeometry(QRect(1409, 8, 51, 21))
        self.label_background_src_2.setFont(font4)
        self.label_background_src_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(86, 69, 143);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Label-Blend v1.1 Synthetic image studio", None))
        self.label.setText("")
        self.pushButton_generate_single_btn.setText(QCoreApplication.translate("Form", u"Random Roll", None))
#if QT_CONFIG(shortcut)
        self.pushButton_generate_single_btn.setShortcut(QCoreApplication.translate("Form", u"Shift+G", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButton_select_cutouts_btn.setToolTip(QCoreApplication.translate("Form", u"Add Object to environment", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_select_cutouts_btn.setText(QCoreApplication.translate("Form", u"Add PNG Cutouts", None))
#if QT_CONFIG(shortcut)
        self.pushButton_select_cutouts_btn.setShortcut(QCoreApplication.translate("Form", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButton_select_background_btn.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Select Environment</p><p>ShortCut: Ctrl+O</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_select_background_btn.setText(QCoreApplication.translate("Form", u"Add Backgrounds", None))
#if QT_CONFIG(shortcut)
        self.pushButton_select_background_btn.setShortcut(QCoreApplication.translate("Form", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.label_6.setText(QCoreApplication.translate("Form", u"                   Image Settings", None))
        self.pushButton_generate_btn.setText(QCoreApplication.translate("Form", u"Save Bounding Box Dataset", None))
#if QT_CONFIG(shortcut)
        self.pushButton_generate_btn.setShortcut(QCoreApplication.translate("Form", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.toolButton_open_box_folder.setToolTip(QCoreApplication.translate("Form", u"Open Box Folder", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_open_box_folder.setText(QCoreApplication.translate("Form", u"...", None))
        self.lineEdit_box_location.setText("")
        self.lineEdit_box_location.setPlaceholderText(QCoreApplication.translate("Form", u"Location...", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Location:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"            Bounding Box Annotation", None))
        self.pushButton_segmentation_button.setText(QCoreApplication.translate("Form", u"Save Mask Segment Dataset", None))
#if QT_CONFIG(shortcut)
        self.pushButton_segmentation_button.setShortcut(QCoreApplication.translate("Form", u"Shift+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.toolButton_toolButton_open_segment_folder.setToolTip(QCoreApplication.translate("Form", u"Open Segment folder", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_toolButton_open_segment_folder.setText(QCoreApplication.translate("Form", u"...", None))
#if QT_CONFIG(tooltip)
        self.spinBox_resolution_epsilon.setToolTip(QCoreApplication.translate("Form", u"Polygon Vertices Epsilon Value", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Form", u"Vertices Distance:", None))
        self.pushButton_default_res.setText(QCoreApplication.translate("Form", u"Default", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Location:", None))
        self.lineEdit_segment_location.setText("")
        self.lineEdit_segment_location.setPlaceholderText(QCoreApplication.translate("Form", u"Location...", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"            Mask Polygons Annotation", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"                   Image Settings", None))
#if QT_CONFIG(tooltip)
        self.spinBox_height.setToolTip(QCoreApplication.translate("Form", u"Polygon Vertices Epsilon Value", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_height.setSuffix(QCoreApplication.translate("Form", u" px", None))
        self.spinBox_height.setPrefix("")
#if QT_CONFIG(tooltip)
        self.spinBox_width.setToolTip(QCoreApplication.translate("Form", u"Polygon Vertices Epsilon Value", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_width.setSuffix(QCoreApplication.translate("Form", u" px", None))
        self.spinBox_width.setPrefix("")
        self.label_10.setText(QCoreApplication.translate("Form", u"Size:", None))
        self.pushButton_default.setText(QCoreApplication.translate("Form", u"Default", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Quality:", None))
        self.spinBox_num_quality.setSuffix(QCoreApplication.translate("Form", u" %", None))
        self.spinBox_num_quality.setPrefix("")
        self.checkBox.setText(QCoreApplication.translate("Form", u"Data Splitting Train / Val", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Select Image Folder", None))
#if QT_CONFIG(tooltip)
        self.toolButton_Select_image_folder.setToolTip(QCoreApplication.translate("Form", u"Open Box Folder", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_Select_image_folder.setText(QCoreApplication.translate("Form", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolButton_Select_label_folder.setToolTip(QCoreApplication.translate("Form", u"Open Box Folder", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_Select_label_folder.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Select Label Folder", None))
        self.pushButton_force_split.setText(QCoreApplication.translate("Form", u"Force Split", None))
#if QT_CONFIG(shortcut)
        self.pushButton_force_split.setShortcut(QCoreApplication.translate("Form", u"Shift+G", None))
#endif // QT_CONFIG(shortcut)
        self.label_17.setText(QCoreApplication.translate("Form", u"Train / Val", None))
        self.comboBox_split.setItemText(0, QCoreApplication.translate("Form", u"95 : 15 OverFit", None))
        self.comboBox_split.setItemText(1, QCoreApplication.translate("Form", u"90 : 10 Biased", None))
        self.comboBox_split.setItemText(2, QCoreApplication.translate("Form", u"80 : 20 Recommended", None))
        self.comboBox_split.setItemText(3, QCoreApplication.translate("Form", u"70 : 30 Standard", None))
        self.comboBox_split.setItemText(4, QCoreApplication.translate("Form", u"50 : 50 Scarcity", None))
        self.comboBox_split.setItemText(5, QCoreApplication.translate("Form", u"30 : 70 UnderFit", None))

        self.pushButton_splitter_default.setText(QCoreApplication.translate("Form", u"Default", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"    Manual Dataset Splitter   <Optional>", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"No Backgrounds Added", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_1.setText(QCoreApplication.translate("Form", u"Min Cutout Size:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Max Cutout Size:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"No. of Images to Generate:", None))
        self.pushButton_open_folder.setText(QCoreApplication.translate("Form", u"Open Folder", None))
#if QT_CONFIG(shortcut)
        self.pushButton_open_folder.setShortcut(QCoreApplication.translate("Form", u"Shift+O", None))
#endif // QT_CONFIG(shortcut)
        self.spinBox_min_size_input.setSuffix(QCoreApplication.translate("Form", u" px", None))
        self.spinBox_max_size_input.setSuffix(QCoreApplication.translate("Form", u" px", None))
        self.spinBox_max_size_input.setPrefix("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Starting Image No:", None))
        self.toolButton_prev.setText(QCoreApplication.translate("Form", u"<--", None))
        self.toolButton_next.setText(QCoreApplication.translate("Form", u"-->", None))
        self.label_background_src.setText(QCoreApplication.translate("Form", u"Background Src:", None))
        self.lineEdit_background_src.setText("")
        self.lineEdit_background_src.setPlaceholderText(QCoreApplication.translate("Form", u"No background selected", None))
        self.comboBox_profile.setItemText(0, QCoreApplication.translate("Form", u"1024 x 1024   Default", None))
        self.comboBox_profile.setItemText(1, QCoreApplication.translate("Form", u"3840 x 2160   SAM", None))
        self.comboBox_profile.setItemText(2, QCoreApplication.translate("Form", u"1920 x 1920   Yolo v11", None))
        self.comboBox_profile.setItemText(3, QCoreApplication.translate("Form", u"1280 x 1280   Yolo v8 Seg", None))
        self.comboBox_profile.setItemText(4, QCoreApplication.translate("Form", u"640 x 640       Yolo v8", None))
        self.comboBox_profile.setItemText(5, QCoreApplication.translate("Form", u"512 x 512       Yolo v5", None))
        self.comboBox_profile.setItemText(6, QCoreApplication.translate("Form", u"256 x 256       ResNet", None))
        self.comboBox_profile.setItemText(7, QCoreApplication.translate("Form", u"224 x 224       ResNet", None))

        self.label_background_src_2.setText(QCoreApplication.translate("Form", u"Profile:", None))
    # retranslateUi


      
        
    # retranslateUi
        self.cutout_images = []
        self.background_images = []
        
        
        
        self.pushButton_select_cutouts_btn.clicked.connect(self.select_cutouts)
        self.pushButton_select_background_btn.clicked.connect(self.select_background)
        self.pushButton_generate_btn.clicked.connect(self.generate_and_save_images)
        self.pushButton_generate_single_btn.clicked.connect(self.generate_image_no_save)
        self.pushButton_segmentation_button.clicked.connect(self.generate_and_save_segmentations)
        
        self.pushButton_open_folder.clicked.connect(self.open_folder)
        self.toolButton_open_box_folder.clicked.connect(self.select_box_folder)
        self.toolButton_toolButton_open_segment_folder.clicked.connect(self.select_segment_folder)
        
        self.bounding_boxes = []
        
        #-------------------Box Viewer------------------\
        self.cv_img = None
        self.label_path = None
        self.image = None
        
        
        self.pushButton_default.clicked.connect(self.reset_res)
       
        #-------------------End------------------/

        #-------------------Segment Viewer------------------\
        self.image = None
        self.image_path = None
        self.pushButton_default_res.clicked.connect(lambda: self.spinBox_resolution_epsilon.setValue(10))
        self.lineEdit_box_location.setText(os.getcwd())
        self.lineEdit_segment_location.setText(os.getcwd())
       
        #-------------------End------------------/
        #--------------------Mannual Data Splitter--------------------\
        self.image_folder = ""
        self.label_folder = ""
        self.comboBox_split.setCurrentIndex(2) #default train/val
        self.toolButton_Select_image_folder.clicked.connect(self.select_images_folder)
        self.toolButton_Select_label_folder.clicked.connect(self.select_labels_folder)
        self.pushButton_force_split.clicked.connect(self.divide_dataset)
        self.pushButton_splitter_default.clicked.connect(lambda: self.comboBox_split.setCurrentIndex(2))
        #-------------------End--------------------------------------/

        
        
        
        
        self.horizontalSlider_quality.valueChanged.connect(self.update_quality_label)
        self.spinBox_num_quality.valueChanged.connect(self.update_quality_slider)
        self.comboBox_profile.currentIndexChanged.connect(self.update_image_settings)
        
        
        
      
        
        #---------------------------New Features------------------------\
        self.listWidget.currentRowChanged.connect(self.on_list_item_selected)
        self.toolButton_next.setText("\u2190")
        self.toolButton_prev.setText("\u2190")
        
        self.toolButton_next.clicked.connect(self.show_next_image)
        self.toolButton_prev.clicked.connect(self.show_prev_image)
        
        
    def select_images_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Images Folder")
        if folder:
            self.image_folder = folder
            

    def select_labels_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Labels Folder")
        if folder:
            self.label_folder = folder

    def divide_dataset(self,checks = False):
        
        train_combobox_index = self.comboBox_split.currentIndex()
        split_percent = 80
        
        
        if train_combobox_index == 0:
            split_percent = 95
        elif train_combobox_index == 1:
            split_percent = 90
        
        elif train_combobox_index == 3:
            split_percent = 70
        elif train_combobox_index == 4:
            split_percent = 50
        elif train_combobox_index == 5:
            split_percent = 30
        
        else:
            split_percent = 80

        
        
        if not self.image_folder or not self.label_folder:
            QMessageBox.warning(self, "Warning", "Please select both folders.")
            return

       
        images = natsorted([
            f for f in os.listdir(self.image_folder)
            if f.lower().endswith(('.jpg', '.jpeg', '.png'))
        ])

      
        split_index = int(len(images) * (split_percent / 100.0))

        train_images = images[:split_index]
        val_images = images[split_index:]

        for subfolder in ['train', 'val']:
            os.makedirs(os.path.join(self.image_folder, subfolder), exist_ok=True)
            os.makedirs(os.path.join(self.label_folder, subfolder), exist_ok=True)

        def move_files(image_list, subfolder):
            for img_file in image_list:
                base_name = os.path.splitext(img_file)[0]
                label_file = base_name + ".txt"

                src_img = os.path.join(self.image_folder, img_file)
                dst_img = os.path.join(self.image_folder, subfolder, img_file)
                if os.path.exists(src_img):
                    shutil.move(src_img, dst_img)

                src_label = os.path.join(self.label_folder, label_file)
                dst_label = os.path.join(self.label_folder, subfolder, label_file)
                if os.path.exists(src_label):
                    shutil.move(src_label, dst_label)

        move_files(train_images, "train")
        move_files(val_images, "val")

        if checks==False:
            
            QMessageBox.information(self, "Success", "Dataset successfully divided!")


    
    def on_list_item_selected(self, index):
        if 0 <= index < len(self.background_images):
            self.current_index = index
            
            self.show_image(self.background_images[self.current_index][1])  # PIL Image
            
            print("Background path:", self.background_images[self.current_index][0])
            self.lineEdit_background_src.setText(self.background_images[self.current_index][0])
        
        
            self.generate_image_no_save()

    def show_next_image(self):
        if self.background_images and self.current_index < len(self.background_images) - 1:
            self.current_index += 1
            self.listWidget.setCurrentRow(self.current_index)  # Update selection

    def show_prev_image(self):
        if self.background_images and self.current_index > 0:
            self.current_index -= 1
            self.listWidget.setCurrentRow(self.current_index)  # Update selection
    # Update selection














            

        
        
    def update_image_settings(self, index):
        if index == 1:
            self.spinBox_width.setValue(3840)
            self.spinBox_height.setValue(2160)
        elif index == 2:
            self.spinBox_width.setValue(1920)
            self.spinBox_height.setValue(1920)
        elif index == 3:
            self.spinBox_width.setValue(1280)
            self.spinBox_height.setValue(1280)
        elif index == 4:
            self.spinBox_width.setValue(640)
            self.spinBox_height.setValue(640)
        elif index == 5:
            self.spinBox_width.setValue(512)
            self.spinBox_height.setValue(512)
        elif index == 6:
            self.spinBox_width.setValue(256)
            self.spinBox_height.setValue(256)
        elif index == 7:
            self.spinBox_width.setValue(224)
            self.spinBox_height.setValue(224)
        else:
            self.spinBox_width.setValue(1024)
            self.spinBox_height.setValue(1024)

    def update_quality_slider(self, value):
        self.horizontalSlider_quality.setValue(value)
        
    def update_quality_label(self, value):
       
        self.spinBox_num_quality.setValue(value)
        
    def select_box_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        #print(folder_path)
        self.lineEdit_box_location.setText(folder_path)
        
    def select_segment_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        #print(folder_path)
        self.lineEdit_segment_location.setText(folder_path)
        
    def reset_res(self):
        
        self.horizontalSlider_quality.setValue(90)
        self.comboBox_profile.setCurrentIndex(0)
        
        
        
    def new_window(self):
        global window1
        
        window1 = window()
        window1.show()

    def open_folder(self):
        # Relative folder path (adjust if needed)
        folder_path = os.path.abspath("./")
        QDesktopServices.openUrl(QUrl.fromLocalFile(folder_path))
    
   
    def open_box_folder(self):
        #os.makedirs("output_box/images", exist_ok=True)
        #os.makedirs("output_box/labels", exist_ok=True)
        
        folder_path = os.path.abspath(self.lineEdit_box_location.text()+"/Output_box")
        QDesktopServices.openUrl(QUrl.fromLocalFile(folder_path))
        
    def open_segment_folder(self):
        #toolButton_toolButton_open_segment_folder
        folder_path = os.path.abspath(self.lineEdit_segment_location.text()+"/Output_segment")
        QDesktopServices.openUrl(QUrl.fromLocalFile(folder_path))
        
    def merge_polygons(self,polygons):
        if len(polygons) < 2:
            return polygons
        all_points = np.vstack(polygons)
        hull = cv2.convexHull(all_points)
        return [hull.tolist()]

    def extract_and_merge_polygons(self,mask: Image.Image, class_id: int, image_size=(1000, 1000)):
        np_mask = np.array(mask)
        gray = np_mask[:, :, 3]  # Alpha channel
        _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        polygons = []
        for contour in contours:
            #epsilon defalt value is 0.01
            value = self.spinBox_resolution_epsilon.value()*0.001
            epsilon = value * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            if len(approx) >= 3:
                polygons.append(approx)
        merged = self.merge_polygons(polygons)
        
        label_lines = []
        for polygon in merged:
            norm_polygon = []
            for point in polygon:
                x, y = point[0]
                nx = round(x / image_size[0], 6)
                ny = round(y / image_size[1], 6)
                norm_polygon.extend([nx, ny])
            label_lines.append(f"{class_id} " + " ".join(map(str, norm_polygon)))

        return label_lines


    def generate_and_save_segmentations(self):
        width = self.spinBox_width.value()
        height = self.spinBox_height.value()

        try:
            count = int(self.spinBox_num_images_input.text())
            start_index = int(self.spinBox_starting_image_input.value())
        except ValueError:
            return

        if not self.cutout_images or not self.background_images:
            return

        folder = self.lineEdit_segment_location.text()
        if not folder:
            return

        image_dir = os.path.join(folder, "Output_segment", "images")
        label_dir = os.path.join(folder, "Output_segment", "labels")
        os.makedirs(image_dir, exist_ok=True)
        os.makedirs(label_dir, exist_ok=True)

        def generate(index):
            image_index = start_index + index
            background_path, bg_pil = random.choice(self.background_images)
            background = bg_pil.copy().resize((width, height))

            result = background.copy()
            label_lines = []

            for cutout_image, class_id in self.cutout_images:
                cutout_copy = cutout_image.copy()

                size = random.randint(
                    self.spinBox_min_size_input.value(),
                    self.spinBox_max_size_input.value()
                )
                resized = cutout_copy.resize((size, size), Image.Resampling.LANCZOS)
                angle = random.randint(0, 359)
                rotated = resized.rotate(angle, expand=True)

                w, h = rotated.size
                x = random.randint(0, width - w)
                y = random.randint(0, height - h)

                # Paste onto result
                result.paste(rotated, (x, y), rotated)

                # Prepare mask for polygon extraction
                mask = Image.new("RGBA", (width, height), (0, 0, 0, 0))
                mask.paste(rotated, (x, y), rotated)

                polygons = self.extract_and_merge_polygons(mask, class_id, image_size=(width, height))
                label_lines.extend(polygons)

            # Save image
            output_image = result.convert("RGB")
            image_name = f"Image{image_index}.jpg"
            label_name = f"Image{image_index}.txt"

            output_image.save(os.path.join(image_dir, image_name), format="JPEG", quality=self.horizontalSlider_quality.value())
            with open(os.path.join(label_dir, label_name), "w") as f:
                f.write("\n".join(label_lines))

        # Generate images in parallel
        with ThreadPoolExecutor() as executor:
            executor.map(generate, range(count))

        # Optional dataset division
        if self.checkBox.isChecked():
            self.image_folder = image_dir
            self.label_folder = label_dir
            self.divide_dataset(checks=True)

        self.notify_images_saved_seg(count)


    #------------------changes made------------------\
    def select_cutouts(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Cutout Images", "", "Images (*.png *.jpg *.jpeg)")
        for file in files:
            image = Image.open(file).convert("RGBA")
            class_id = len(self.cutout_images)
            self.cutout_images.append((image, class_id))  # store as (PIL.Image, class_id)
        self.generate_image_no_save()  # show random preview


    def select_background(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Background Images", "", "Images (*.jpg *.png *.jpeg)"
        )
        if files:
            self.background_images = []
            self.listWidget.clear()

            for file_path in files:
                pil_img = Image.open(file_path).convert("RGBA").resize((1605, 830))
                # Store tuple (file_path, pil_img)
                self.background_images.append((file_path, pil_img))

                # Make thumbnail for QListWidget
                thumb = pil_img.copy().resize((100, 60))
                buffer = io.BytesIO()
                thumb.save(buffer, format="PNG")
                qimg = QImage.fromData(buffer.getvalue(), "PNG")
                pixmap = QPixmap.fromImage(qimg)

                from PySide6.QtWidgets import QListWidgetItem
                item = QListWidgetItem(file_path.split("/")[-1])
                item.setIcon(pixmap)
                self.listWidget.addItem(item)

            self.current_index = 0
            self.show_image(self.background_images[self.current_index][1])  # Pass the PIL image



    def generate_random_image(self, size=(1605, 830)):
        if not self.cutout_images or not self.background_images:
            return None

        # Use currently selected background (not random)
        background_path = self.background_images[self.current_index][0]
        background = self.background_images[self.current_index][1].copy().resize(size)


        
        print("Background index:", self.current_index)
        print("Background path:", self.background_images[self.current_index][0])
        self.lineEdit_background_src.setText(background_path)


        min_size = self.spinBox_min_size_input.value()
        max_size = self.spinBox_max_size_input.value()
        if min_size > max_size:
            min_size, max_size = max_size, min_size

        self.bounding_boxes = []

        for cutout, class_id in self.cutout_images:
            cutout = cutout.copy()
            w = random.randint(min_size, max_size)
            cutout = cutout.resize((w, w), Image.Resampling.LANCZOS)

            angle = random.randint(0, 359)
            cutout_rotated = cutout.rotate(angle, expand=True)

            w, h = cutout_rotated.size
            x = random.randint(0, size[0] - w)
            y = random.randint(0, size[1] - h)

            background.paste(cutout_rotated, (x, y), cutout_rotated)

            bbox = (x + w / 2) / size[0], (y + h / 2) / size[1], w / size[0], h / size[1]
            self.bounding_boxes.append((class_id, *bbox))

        return background






    def generate_image_no_save(self):
        image = self.generate_random_image()
        if image is not None:
            qim = ImageQt.ImageQt(image)  # PIL.Image -> QImage
            pixmap = QPixmap.fromImage(qim)
            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    
    
    

  

    def generate_and_save_images(self):
        try:
            count = int(self.spinBox_num_images_input.text())
            start_index = int(self.spinBox_starting_image_input.value())
        except ValueError:
            return

        min_size = self.spinBox_min_size_input.value()
        max_size = self.spinBox_max_size_input.value()

        if min_size > max_size or not self.cutout_images or not self.background_images:
            return

        folder_path = self.lineEdit_box_location.text()
        if not folder_path:
            return

        # Create output directories
        image_dir = os.path.join(folder_path, "Output_box", "images")
        label_dir = os.path.join(folder_path, "Output_box", "labels")
        os.makedirs(image_dir, exist_ok=True)
        os.makedirs(label_dir, exist_ok=True)

        width = self.spinBox_width.value()
        height = self.spinBox_height.value()
        quality = self.horizontalSlider_quality.value()

        def generate_and_save(i):
            image_index = start_index + i

            # ✅ Correct way to get a PIL background image
            bg_path, bg_pil = random.choice(self.background_images)
            background = bg_pil.copy().resize((width, height))
            result = background.copy()
            bboxes = []

            for cutout_image, class_id in self.cutout_images:
                cutout_copy = cutout_image.copy()
                size = random.randint(min_size, max_size)
                cutout_resized = cutout_copy.resize((size, size), Image.Resampling.LANCZOS)

                angle = random.randint(0, 359)
                cutout_rotated = cutout_resized.rotate(angle, expand=True)

                w, h = cutout_rotated.size
                if w >= width or h >= height:
                    continue  # Skip if cutout is too large

                x = random.randint(0, width - w)
                y = random.randint(0, height - h)

                result.paste(cutout_rotated, (x, y), cutout_rotated)

                cx = (x + w / 2) / width
                cy = (y + h / 2) / height
                nw = w / width
                nh = h / height
                bboxes.append(f"{class_id} {cx:.6f} {cy:.6f} {nw:.6f} {nh:.6f}")

            image_name = f"Image{image_index}.jpg"
            label_name = f"Image{image_index}.txt"

            # Save image
            result.convert("RGB").save(os.path.join(image_dir, image_name), format="JPEG", quality=quality)

            # Save label
            with open(os.path.join(label_dir, label_name), "w") as f:
                f.write("\n".join(bboxes))

        with ThreadPoolExecutor() as executor:
            executor.map(generate_and_save, range(count))

        if self.checkBox.isChecked():
            self.image_folder = image_dir
            self.label_folder = label_dir
            self.divide_dataset(checks=True)

        self.notify_images_saved_box(count)


    def notify_images_saved_box(self, count):
        # Notify user after saving all images
        import time
                
        msg = QMessageBox(self)
        msg.setText(f"{count} images have been saved successfully!")
        msg.addButton("Open Folder", QMessageBox.AcceptRole)
        open_btn = msg.addButton("Done", QMessageBox.ActionRole)
        msg.exec(), None if msg.clickedButton() == open_btn else self.open_box_folder()


    
    def notify_images_saved_seg(self, count):
        # Notify user after saving all images
        import time
                
        msg = QMessageBox(self)
        msg.setText(f"{count} images have been saved successfully!")
        msg.addButton("Open Folder", QMessageBox.AcceptRole)
        open_btn = msg.addButton("Done", QMessageBox.ActionRole)
        msg.exec(), None if msg.clickedButton() == open_btn else self.open_segment_folder()
    
        
    
    
    '''def show_image(self, image):
        qimage = ImageQt.ImageQt(image.convert("RGBA"))
        pixmap = QPixmap.fromImage(QImage(qimage))
        self.label.setPixmap(pixmap)'''
    def show_image(self, pil_img):
        # Expecting a PIL Image already loaded and resized
        buffer = io.BytesIO()
        pil_img.save(buffer, format="PNG")
        qimg = QImage.fromData(buffer.getvalue(), "PNG")
        pixmap = QPixmap.fromImage(qimg)
        self.label.setPixmap(pixmap)  # Display in QLabel
    # Display in QLabel (adjust as needed)



    

'''
class FormTab(QWidget):
    """The tab content (form UI)"""
    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Phone:", QLineEdit())
        layout.addRow("Email:", QLineEdit())
        self.setLayout(layout)


'''



# ---------- Zoomable View ----------
class ZoomableGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.ScrollHandDrag)

    def wheelEvent(self, event):
        zoom_in = 1.25
        zoom_out = 0.8
        factor = zoom_in if event.angleDelta().y() > 0 else zoom_out
        self.scale(factor, factor)



# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py


from window1 import Ui_MainWindow
class window_main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_MainWindow()
        self.form.setupUi(self)
        
        self.form.actionExit.triggered.connect(QApplication.exit)
        
        self.tab_count = 2
        self.form.actionNew_Project.triggered.connect(self.add_new_tab)
        #-------------------Box Viewer------------------\
        
        
        self.cv_img = None
        self.label_path = None
        self.image = None
        self.form.pushButton_btn_select_image.clicked.connect(self.load_image)
        self.form.pushButton_btn_select_label.clicked.connect(self.load_labels)
        
        self.view = ZoomableGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        
        self.container_layout = QHBoxLayout(self.form.widget_box)
       
        self.container_layout.addWidget(self.view)
        #-------------------End------------------/

        #-------------------Segment Viewer------------------\
        self.image = None
        self.image_path = None
        self.form.pushButton_btn_image2.clicked.connect(self.load_image_2)
        self.form.pushButton_btn_txt2.clicked.connect(self.load_segments_2)

        # Set the size of the view
        self.scene_2 = QGraphicsScene()
        self.view_2 = ZoomableGraphicsView()
        self.view_2.setScene(self.scene_2)
        #self.view_2.setGeometry(0, 0, 800, 600)  # Set the size of the view
        
        self.container_layout_2 = QHBoxLayout(self.form.widget_segment)
       
        self.container_layout_2.addWidget(self.view_2)
        self.form.tabWidget_3.tabCloseRequested.connect(self.close_tab)
        
        self.add_new_tab()
        
        self.form.pushButton_show_in_browser.clicked.connect(self.open_photopea_url)
        profile = QWebEngineProfile.defaultProfile()
        settings = self.form.webEngineView.settings()
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)  # Allow remote URLs in local content
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)    # Allow local file URLs
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        profile.downloadRequested.connect(self.handle_download)
        
        self.form.actionSplash.triggered.connect(self.show_splash)

        
    def show_splash(self):
        about_dialog = AboutLicenseWindow(self)
        about_dialog.exec()  # Use exec() for modal dialog
        
        
    def close_tab(self, index):
        tab_text = self.form.tabWidget_3.tabText(index)

        if tab_text == "Generator 1" or tab_text == "Cutouts Maker" or tab_text == "Box View" or tab_text == "Masked Segment View" :  # or any specific tab name
                #print("This tab cannot be closed.")
                return  # Skip closing
        self.form.tabWidget_3.removeTab(index)



    def load_labels(self):
        if self.cv_img is None:
            return

        txt_path, _ = QFileDialog.getOpenFileName(self, "Select YOLO TXT", "", "Text Files (*.txt)")
        if txt_path:
            h, w = self.cv_img.shape[:2]
            bboxes = self.load_bboxes(txt_path, w, h)

            img_copy = self.cv_img.copy()
            overlay = img_copy.copy()
            cv2.addWeighted(overlay, 0.2, img_copy, 0.5, 0, img_copy)

            colors = {}
            for class_id, x_min, y_min, x_max, y_max in bboxes:
                if class_id not in colors:
                    colors[class_id] = self.random_light_color()
                color = colors[class_id]
                cv2.rectangle(img_copy, (x_min, y_min), (x_max, y_max), color, 2)
                cv2.putText(img_copy, str(class_id), (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            self.display_image(img_copy)
 
    
    def handle_download(self, download):
        filename = download.downloadFileName()
        path, _ = QFileDialog.getSaveFileName(self, "Save File As", filename)
        if path:
            try:
                download.setDownloadDirectory(os.path.dirname(path))
                download.setDownloadFileName(os.path.basename(path))
            except AttributeError:
                pass  # fallback for older versions
            download.accept()
            
            
    def open_photopea_url(self):
        url = "https://www.photopea.com#%7B%22files%22%3A%5B%22https%3A%2F%2Fwww.photopea.com%2Fapi%2Fimg2%2Fpug.png%22%5D%2C%22environment%22%3A%7B%7D%7D"
        QDesktopServices.openUrl(QUrl(url))
        
        

    def add_new_tab(self):
        tab = Ui_Form(self)
        
        insert_index = max(self.form.tabWidget_3.count() - 3, 0)
        self.form.tabWidget_3.insertTab(insert_index, tab, f"Generator {insert_index + 1}")
        
        self.form.tabWidget_3.setCurrentIndex(insert_index)
        
        #self.form.tabWidget_3.addTab(tab, f"Generator  {self.tab_count}")
        #self.form.tabWidget_3.setCurrentIndex(self.tab_count - 1)
        #self.tab_count += 1
        
        
        
        
        
        
    #------------------Box Viewer------------------\
    def load_bboxes(self,txt_file, img_width, img_height):
        bboxes = []
        with open(txt_file, 'r') as f:
            for line in f:
                parts = line.strip().split()
                class_id = int(parts[0])
                x_center, y_center, width, height = map(float, parts[1:])
                x_min = int((x_center - width / 2) * img_width)
                y_min = int((y_center - height / 2) * img_height)
                x_max = int((x_center + width / 2) * img_width)
                y_max = int((y_center + height / 2) * img_height)
                bboxes.append((class_id, x_min, y_min, x_max, y_max))
        return bboxes
            

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if path:
            self.image_path = path
            self.cv_img = cv2.imread(path)
            self.display_image(self.cv_img)
            
  
    def random_light_color(self):
        base = [random.randint(120, 200) for _ in range(3)]
        base[random.randint(0, 2)] = 255
        return tuple(base)

 

    def display_image(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qimg = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)

        self.scene.clear()
        item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.view.setSceneRect(pixmap.rect())
        
        
        
    #------------------Segment Viewer------------------\
    def load_image_2(self):
        path_2, _2 = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if path_2:
            self.image_path_2 = path_2
            self.image_2 = cv2.imread(path_2)
            self.show_image_2(self.image_2)
            
            
    def random_light_color_2(self):
        base_2 = [random.randint(150, 255) for _ in range(3)]
        base_2[random.randint(0, 2)] = 255
        return tuple(base_2)


    
    def overlay_masks_2(self,image_2, masks_2):
        darkened_2 = (image_2 * 0.7).astype(np.uint8)
        overlay_2 = darkened_2.copy()
        colors_2 = {}

        for class_id_2, polygon_2 in masks_2:
            if class_id_2 not in colors_2:
                colors_2[class_id_2] = self.random_light_color_2()
            color_2 = colors_2[class_id_2]

            cv2.fillPoly(overlay_2, [polygon_2], color_2)
            cv2.polylines(darkened_2, [polygon_2], isClosed=True, color=color_2, thickness=2)

            x_2, y_2 = polygon_2[0]
            cv2.putText(darkened_2, str(class_id_2), (x_2, y_2 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_2, 2)

        final_2 = cv2.addWeighted(overlay_2, 0.4, darkened_2, 0.6, 0)
        return final_2

    
    def load_segmentations_2(self,txt_file_2, img_width_2, img_height_2):
        masks_2 = []
        with open(txt_file_2, 'r') as f_2:
            for line_2 in f_2:
                parts_2 = line_2.strip().split()
                class_id_2 = int(parts_2[0])
                coords_2 = list(map(float, parts_2[1:]))
                points_2 = np.array([
                    [int(coords_2[i] * img_width_2), int(coords_2[i + 1] * img_height_2)]
                    for i in range(0, len(coords_2), 2)
                ], np.int32)
                masks_2.append((class_id_2, points_2))
        return masks_2



    def load_segments_2(self):
        if self.image_2 is None:
            return
        path_2, _2 = QFileDialog.getOpenFileName(self, "Select YOLO Segment TXT", "", "Text Files (*.txt)")
        if path_2:
            h_2, w_2 = self.image_2.shape[:2]
            masks_2 = self.load_segmentations_2(path_2, w_2, h_2)
            masked_2 = self.overlay_masks_2(self.image_2.copy(), masks_2)
            self.show_image_2(masked_2)
            
             
    def cv2_to_pixmap_2(self,img_2):
        h_2, w_2, ch_2 = img_2.shape
        bytes_per_line_2 = ch_2 * w_2
        qimg_2 = QImage(img_2.data, w_2, h_2, bytes_per_line_2, QImage.Format_BGR888)
        return QPixmap.fromImage(qimg_2)


            
 
    def show_image_2(self, img_2):
        self.scene_2.clear()
        pixmap_2 = self.cv2_to_pixmap_2(img_2)
        self.pixmap_item_2 = QGraphicsPixmapItem(pixmap_2)
        self.scene_2.addItem(self.pixmap_item_2)
        self.view_2.fitInView(self.pixmap_item_2, Qt.KeepAspectRatio)

   
    #--------------------Mannual Data Splitter--------------------\

from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton, QTextEdit
from PySide6.QtCore import Qt

class AboutLicenseWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About & License")
        self.setFixedSize(480, 360)
        self.setWindowModality(Qt.ApplicationModal)

        # Developer info label
        developer_label = QLabel(
            "Developer & Designer: Abhishek Verma\n"
            "B.Tech CS-AIML 6th Semester\n"
            "Feedback: abhi639679@gmail.com"
        )
        developer_label.setAlignment(Qt.AlignCenter)
        developer_label.setObjectName("developerLabel")

        # License text (non-editable)
        license_text = QTextEdit()
        license_text.setReadOnly(True)
        license_text.setText(
            "License:\n\n"
            "No one may use or sell this software or any part of it without "
            "explicit permission from the developer."
        )
        license_text.setObjectName("licenseText")

        # Close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        close_btn.setObjectName("closeButton")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(developer_label)
        layout.addWidget(license_text)
        layout.addWidget(close_btn, alignment=Qt.AlignCenter)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        self.setLayout(layout)

        # Apply stylesheet
        self.setStyleSheet("""
            QDialog {
                background-color: #56458f;
                border-radius: 12px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                font-size: 14px;
                color: #333;
            }
            QLabel#developerLabel {
                background-color: #433771;
                border-radius: 12px;
                
                font-weight: 600;
                font-size: 16px;
                color: #62dfb9;
                padding-bottom: 10px;
            }
            QTextEdit#licenseText {
                background-color: #433771;
                border: 1px solid #433771;
                border-radius: 8px;
                padding: 12px;
                font-weight: 600;
                font-size: 16px;
                color: #62dfb9;
                selection-background-color: #a3c1da;
            }
            QPushButton#closeButton {
                background-color: #2c7be5;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 24px;
                font-weight: 600;
                min-width: 100px;
                transition: background-color 0.3s ease;
            }
            QPushButton#closeButton:hover {
                background-color: #1a5fc1;
            }
            QPushButton#closeButton:pressed {
                background-color: #144a8c;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = window_main()
    window.showMaximized()

    window.show()
    sys.exit(app.exec())
