# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(469, 648)
        Widget.setStyleSheet(u"background:black;\n"
"font: 10pt \"JetBrainsMono Nerd Font\";\n"
"selection-background-color: black;")
        self.verticalLayout_37 = QVBoxLayout(Widget)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.inLabel = QLabel(Widget)
        self.inLabel.setObjectName(u"inLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inLabel.sizePolicy().hasHeightForWidth())
        self.inLabel.setSizePolicy(sizePolicy)
        self.inLabel.setMinimumSize(QSize(0, 60))
        self.inLabel.setStyleSheet(u"font: 12pt \"JetBrainsMono Nerd Font\";")
        self.inLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_35.addWidget(self.inLabel)

        self.outLabel = QLabel(Widget)
        self.outLabel.setObjectName(u"outLabel")
        sizePolicy.setHeightForWidth(self.outLabel.sizePolicy().hasHeightForWidth())
        self.outLabel.setSizePolicy(sizePolicy)
        self.outLabel.setMinimumSize(QSize(0, 40))
        self.outLabel.setStyleSheet(u"font: 16pt \"JetBrainsMono Nerd Font\";")
        self.outLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_35.addWidget(self.outLabel)


        self.verticalLayout_37.addLayout(self.verticalLayout_35)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.pushButton_35 = QPushButton(Widget)
        self.pushButton_35.setObjectName(u"pushButton_35")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy1)
        self.pushButton_35.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_35.setStyleSheet(u"color:#fff")

        self.verticalLayout_28.addWidget(self.pushButton_35)


        self.horizontalLayout_40.addLayout(self.verticalLayout_28)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.pushButton_26 = QPushButton(Widget)
        self.pushButton_26.setObjectName(u"pushButton_26")
        sizePolicy1.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy1)
        self.pushButton_26.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_31.addWidget(self.pushButton_26)


        self.horizontalLayout_40.addLayout(self.verticalLayout_31)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.pushButton_27 = QPushButton(Widget)
        self.pushButton_27.setObjectName(u"pushButton_27")
        sizePolicy1.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy1)
        self.pushButton_27.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_34.addWidget(self.pushButton_27)


        self.verticalLayout_32.addLayout(self.verticalLayout_34)


        self.horizontalLayout_40.addLayout(self.verticalLayout_32)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.pushButton_37 = QPushButton(Widget)
        self.pushButton_37.setObjectName(u"pushButton_37")
        sizePolicy1.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy1)
        self.pushButton_37.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_37.setStyleSheet(u"color:#fff")

        self.verticalLayout_33.addWidget(self.pushButton_37)


        self.horizontalLayout_40.addLayout(self.verticalLayout_33)


        self.verticalLayout_37.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.pushButton_31 = QPushButton(Widget)
        self.pushButton_31.setObjectName(u"pushButton_31")
        sizePolicy1.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy1)
        self.pushButton_31.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_31.setStyleSheet(u"color:#5bf2fa")

        self.verticalLayout_27.addWidget(self.pushButton_31)

        self.pushButton_34 = QPushButton(Widget)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy1.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy1)
        self.pushButton_34.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_34.setStyleSheet(u"color:#f75d54")

        self.verticalLayout_27.addWidget(self.pushButton_34)


        self.horizontalLayout_37.addLayout(self.verticalLayout_27)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_43 = QLabel(Widget)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"color:#f75d54")

        self.horizontalLayout_27.addWidget(self.label_43)


        self.verticalLayout_22.addLayout(self.horizontalLayout_27)

        self.pushButton_22 = QPushButton(Widget)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy1.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy1)
        self.pushButton_22.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_22.setStyleSheet(u"color:#fff")

        self.verticalLayout_22.addWidget(self.pushButton_22)


        self.horizontalLayout_37.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_45 = QLabel(Widget)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"color:#f75d54")

        self.horizontalLayout_28.addWidget(self.label_45)


        self.verticalLayout_23.addLayout(self.horizontalLayout_28)

        self.pushButton_23 = QPushButton(Widget)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy1.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy1)
        self.pushButton_23.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_23.setStyleSheet(u"color:#fff")

        self.verticalLayout_23.addWidget(self.pushButton_23)


        self.horizontalLayout_37.addLayout(self.verticalLayout_23)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_47 = QLabel(Widget)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"color:#f75d54")

        self.horizontalLayout_29.addWidget(self.label_47)


        self.verticalLayout_24.addLayout(self.horizontalLayout_29)

        self.pushButton_24 = QPushButton(Widget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy1.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy1)
        self.pushButton_24.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_24.setStyleSheet(u"color:#fff")

        self.verticalLayout_24.addWidget(self.pushButton_24)


        self.horizontalLayout_37.addLayout(self.verticalLayout_24)


        self.verticalLayout_37.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_31 = QLabel(Widget)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_20.addWidget(self.label_31)


        self.verticalLayout_16.addLayout(self.horizontalLayout_20)

        self.pushButton_16 = QPushButton(Widget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy1.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy1)
        self.pushButton_16.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_16.setStyleSheet(u"color:#fff")

        self.verticalLayout_16.addWidget(self.pushButton_16)


        self.horizontalLayout_19.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_33 = QLabel(Widget)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_21.addWidget(self.label_33)


        self.verticalLayout_17.addLayout(self.horizontalLayout_21)

        self.pushButton_17 = QPushButton(Widget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy1.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy1)
        self.pushButton_17.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_17.setStyleSheet(u"color:#fff")

        self.verticalLayout_17.addWidget(self.pushButton_17)


        self.horizontalLayout_19.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_35 = QLabel(Widget)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_22.addWidget(self.label_35)


        self.verticalLayout_18.addLayout(self.horizontalLayout_22)

        self.pushButton_18 = QPushButton(Widget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy1.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy1)
        self.pushButton_18.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_18.setStyleSheet(u"color:#fff")

        self.verticalLayout_18.addWidget(self.pushButton_18)


        self.horizontalLayout_19.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_37 = QLabel(Widget)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_23.addWidget(self.label_37)


        self.verticalLayout_19.addLayout(self.horizontalLayout_23)

        self.pushButton_19 = QPushButton(Widget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        sizePolicy1.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy1)
        self.pushButton_19.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_19.setStyleSheet(u"color:#fff")

        self.verticalLayout_19.addWidget(self.pushButton_19)


        self.horizontalLayout_19.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_39 = QLabel(Widget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"color:#f75d54")

        self.horizontalLayout_24.addWidget(self.label_39)


        self.verticalLayout_20.addLayout(self.horizontalLayout_24)

        self.pushButton_20 = QPushButton(Widget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy1.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy1)
        self.pushButton_20.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_20.setStyleSheet(u"color:#fff")

        self.verticalLayout_20.addWidget(self.pushButton_20)


        self.horizontalLayout_19.addLayout(self.verticalLayout_20)


        self.verticalLayout_37.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_21 = QLabel(Widget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_14.addWidget(self.label_21)


        self.verticalLayout_11.addLayout(self.horizontalLayout_14)

        self.pushButton_11 = QPushButton(Widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy1.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy1)
        self.pushButton_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"color:#fff")

        self.verticalLayout_11.addWidget(self.pushButton_11)


        self.horizontalLayout_13.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_23 = QLabel(Widget)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_15.addWidget(self.label_23)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

        self.pushButton_12 = QPushButton(Widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy1.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy1)
        self.pushButton_12.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"color:#fff")

        self.verticalLayout_12.addWidget(self.pushButton_12)


        self.horizontalLayout_13.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_25 = QLabel(Widget)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_16.addWidget(self.label_25)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.pushButton_13 = QPushButton(Widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy1.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy1)
        self.pushButton_13.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"color:#fff")

        self.verticalLayout_13.addWidget(self.pushButton_13)


        self.horizontalLayout_13.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_27 = QLabel(Widget)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_17.addWidget(self.label_27)


        self.verticalLayout_14.addLayout(self.horizontalLayout_17)

        self.pushButton_14 = QPushButton(Widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy1.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy1)
        self.pushButton_14.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"color:#fff")

        self.verticalLayout_14.addWidget(self.pushButton_14)


        self.horizontalLayout_13.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_29 = QLabel(Widget)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_18.addWidget(self.label_29)


        self.verticalLayout_15.addLayout(self.horizontalLayout_18)

        self.pushButton_15 = QPushButton(Widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy1.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy1)
        self.pushButton_15.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_15.setStyleSheet(u"color:#fff")

        self.verticalLayout_15.addWidget(self.pushButton_15)


        self.horizontalLayout_13.addLayout(self.verticalLayout_15)


        self.verticalLayout_37.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(Widget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_8.addWidget(self.label_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.pushButton_6 = QPushButton(Widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"color:#fff")

        self.verticalLayout_6.addWidget(self.pushButton_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(Widget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_9.addWidget(self.label_13)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.pushButton_7 = QPushButton(Widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"color:#fff")

        self.verticalLayout_7.addWidget(self.pushButton_7)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_15 = QLabel(Widget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_10.addWidget(self.label_15)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.pushButton_8 = QPushButton(Widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)
        self.pushButton_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"color:#fff")

        self.verticalLayout_8.addWidget(self.pushButton_8)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_17 = QLabel(Widget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_11.addWidget(self.label_17)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.pushButton_9 = QPushButton(Widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)
        self.pushButton_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"color:#fff")

        self.verticalLayout_9.addWidget(self.pushButton_9)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(Widget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_12.addWidget(self.label_19)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.pushButton_10 = QPushButton(Widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy1.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy1)
        self.pushButton_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"color:#fff")

        self.verticalLayout_10.addWidget(self.pushButton_10)


        self.horizontalLayout_7.addLayout(self.verticalLayout_10)


        self.verticalLayout_37.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:#f75d54")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:#5bf2fa")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"color:#fff")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:#f75d54")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color:#5bf2fa")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"color:#fff")

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color:#f75d54")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color:#5bf2fa")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"color:#fff")

        self.verticalLayout_3.addWidget(self.pushButton_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color:#f75d54")

        self.horizontalLayout_5.addWidget(self.label_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"color:#fff")

        self.verticalLayout_4.addWidget(self.pushButton_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(Widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color:#f75d54")

        self.horizontalLayout_6.addWidget(self.label_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.pushButton_5 = QPushButton(Widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"color:#fff")

        self.verticalLayout_5.addWidget(self.pushButton_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_37.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Calculadora", None))
        self.inLabel.setText(QCoreApplication.translate("Widget", u"0", None))
        self.outLabel.setText(QCoreApplication.translate("Widget", u"0", None))
        self.pushButton_35.setText(QCoreApplication.translate("Widget", u"RAD", None))
        self.pushButton_26.setText(QCoreApplication.translate("Widget", u"<", None))
        self.pushButton_27.setText(QCoreApplication.translate("Widget", u">", None))
        self.pushButton_37.setText(QCoreApplication.translate("Widget", u"NORM", None))
        self.pushButton_31.setText(QCoreApplication.translate("Widget", u"ALPHA", None))
        self.pushButton_34.setText(QCoreApplication.translate("Widget", u"SHIFT", None))
        self.label_43.setText(QCoreApplication.translate("Widget", u"ASIN", None))
        self.pushButton_22.setText(QCoreApplication.translate("Widget", u"SIN", None))
        self.label_45.setText(QCoreApplication.translate("Widget", u"ACOS", None))
        self.pushButton_23.setText(QCoreApplication.translate("Widget", u"COS", None))
        self.label_47.setText(QCoreApplication.translate("Widget", u"ATAN", None))
        self.pushButton_24.setText(QCoreApplication.translate("Widget", u"TAN", None))
        self.label_31.setText("")
        self.pushButton_16.setText(QCoreApplication.translate("Widget", u"7", None))
        self.label_33.setText("")
        self.pushButton_17.setText(QCoreApplication.translate("Widget", u"8", None))
        self.label_35.setText("")
        self.pushButton_18.setText(QCoreApplication.translate("Widget", u"9", None))
        self.label_37.setText("")
        self.pushButton_19.setText(QCoreApplication.translate("Widget", u"DEL", None))
        self.label_39.setText("")
        self.pushButton_20.setText(QCoreApplication.translate("Widget", u"CLR", None))
        self.label_21.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("Widget", u"4", None))
        self.label_23.setText("")
        self.pushButton_12.setText(QCoreApplication.translate("Widget", u"5", None))
        self.label_25.setText("")
        self.pushButton_13.setText(QCoreApplication.translate("Widget", u"6", None))
        self.label_27.setText("")
        self.pushButton_14.setText(QCoreApplication.translate("Widget", u"x", None))
        self.label_29.setText("")
        self.pushButton_15.setText(QCoreApplication.translate("Widget", u"/", None))
        self.label_11.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"1", None))
        self.label_13.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("Widget", u"2", None))
        self.label_15.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("Widget", u"3", None))
        self.label_17.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("Widget", u"+", None))
        self.label_19.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("Widget", u"-", None))
        self.label.setText(QCoreApplication.translate("Widget", u"COPY", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"PASTE", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Rand", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"RandInt", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u".", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u03c0", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"e", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Exp", None))
        self.label_7.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"Ans", None))
        self.label_9.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"=", None))
    # retranslateUi

