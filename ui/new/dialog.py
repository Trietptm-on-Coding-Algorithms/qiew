# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Tue Apr 15 01:26:22 2014
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(803, 594)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 791, 581))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.treeWidget = QtGui.QTreeWidget(self.tab)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 781, 551))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(781, 551))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        brush = QtGui.QBrush(QtGui.QColor(176, 97, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item_0.setBackground(0, brush)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_1.setBackground(1, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 106, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item_1.setForeground(1, brush)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        brush = QtGui.QBrush(QtGui.QColor(182, 70, 70))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_1.setBackground(1, brush)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tableWidget = QtGui.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 351, 211))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 230, 611, 241))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(0, 192))
        self.tableWidget_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(7)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 0, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "Header", None))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "Type", None))
        self.treeWidget.headerItem().setText(2, _translate("Dialog", "Value", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Dialog", "IMAGE_NT_HEADER", None))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Dialog", "Magic", None))
        self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("Dialog", "word", None))
        self.treeWidget.topLevelItem(0).child(0).setText(2, _translate("Dialog", "PE", None))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("Dialog", "VirtuallAddress", None))
        self.treeWidget.topLevelItem(0).child(1).setText(1, _translate("Dialog", "dword", None))
        self.treeWidget.topLevelItem(0).child(1).setText(2, _translate("Dialog", "400000h", None))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Dialog", "New Item", None))
        self.treeWidget.topLevelItem(2).setText(0, _translate("Dialog", "DOS_HEADER", None))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("Dialog", "Signature", None))
        self.treeWidget.topLevelItem(2).child(0).setText(1, _translate("Dialog", "word", None))
        self.treeWidget.topLevelItem(2).child(0).setText(2, _translate("Dialog", "MZ", None))
        self.treeWidget.topLevelItem(3).setText(0, _translate("Dialog", "SECTION_HEADER", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Header", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Size", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Overlay", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Type", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Machine", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "PDB File", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Value", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "CompanyName", None))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "FileDescription", None))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "FileVersion", None))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "CopyRight", None))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "OriginalFileName", None))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "ProductName", None))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "ProductVersion", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Value", None))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "VersionInfo", None))

