# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.books_tab = QtWidgets.QWidget()
        self.books_tab.setObjectName("books_tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.books_tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.query_label = QtWidgets.QLabel(self.books_tab)
        self.query_label.setText("")
        self.query_label.setObjectName("query_label")
        self.verticalLayout_2.addWidget(self.query_label)
        self.books_table = QtWidgets.QTableWidget(self.books_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.books_table.sizePolicy().hasHeightForWidth())
        self.books_table.setSizePolicy(sizePolicy)
        self.books_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.books_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.books_table.setTabKeyNavigation(False)
        self.books_table.setProperty("showDropIndicator", False)
        self.books_table.setDragDropOverwriteMode(False)
        self.books_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.books_table.setTextElideMode(QtCore.Qt.ElideLeft)
        self.books_table.setCornerButtonEnabled(False)
        self.books_table.setRowCount(0)
        self.books_table.setColumnCount(0)
        self.books_table.setObjectName("books_table")
        self.books_table.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.books_table)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.book_search_widget = QtWidgets.QWidget(self.books_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_search_widget.sizePolicy().hasHeightForWidth())
        self.book_search_widget.setSizePolicy(sizePolicy)
        self.book_search_widget.setObjectName("book_search_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.book_search_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.book_search_label = QtWidgets.QLabel(self.book_search_widget)
        self.book_search_label.setObjectName("book_search_label")
        self.verticalLayout.addWidget(self.book_search_label)
        self.cipher_le = QtWidgets.QLineEdit(self.book_search_widget)
        self.cipher_le.setObjectName("cipher_le")
        self.verticalLayout.addWidget(self.cipher_le)
        self.title_le = QtWidgets.QLineEdit(self.book_search_widget)
        self.title_le.setObjectName("title_le")
        self.verticalLayout.addWidget(self.title_le)
        self.author_le = QtWidgets.QLineEdit(self.book_search_widget)
        self.author_le.setObjectName("author_le")
        self.verticalLayout.addWidget(self.author_le)
        self.room_combo_box = QtWidgets.QComboBox(self.book_search_widget)
        self.room_combo_box.setEditable(False)
        self.room_combo_box.setObjectName("room_combo_box")
        self.verticalLayout.addWidget(self.room_combo_box)
        self.book_search_btn = QtWidgets.QPushButton(self.book_search_widget)
        self.book_search_btn.setObjectName("book_search_btn")
        self.verticalLayout.addWidget(self.book_search_btn)
        self.readers_book_label = QtWidgets.QLabel(self.book_search_widget)
        self.readers_book_label.setObjectName("readers_book_label")
        self.verticalLayout.addWidget(self.readers_book_label)
        self.card_number_le = QtWidgets.QLineEdit(self.book_search_widget)
        self.card_number_le.setText("")
        self.card_number_le.setObjectName("card_number_le")
        self.verticalLayout.addWidget(self.card_number_le)
        self.readers_book_search_btn = QtWidgets.QPushButton(self.book_search_widget)
        self.readers_book_search_btn.setObjectName("readers_book_search_btn")
        self.verticalLayout.addWidget(self.readers_book_search_btn)
        self.horizontalLayout.addWidget(self.book_search_widget)
        self.tabWidget.addTab(self.books_tab, "")
        self.readers_tab = QtWidgets.QWidget()
        self.readers_tab.setObjectName("readers_tab")
        self.tabWidget.addTab(self.readers_tab, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Библиотека"))
        self.books_table.setSortingEnabled(False)
        self.book_search_label.setText(_translate("MainWindow", "Поиск книг"))
        self.cipher_le.setPlaceholderText(_translate("MainWindow", "Шифр"))
        self.title_le.setPlaceholderText(_translate("MainWindow", "Название"))
        self.author_le.setPlaceholderText(_translate("MainWindow", "Автор"))
        self.book_search_btn.setText(_translate("MainWindow", "Поиск"))
        self.readers_book_label.setText(_translate("MainWindow", "Поиск книг закрепленных за читателем"))
        self.card_number_le.setPlaceholderText(_translate("MainWindow", "Номер билета"))
        self.readers_book_search_btn.setText(_translate("MainWindow", "Поиск"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.books_tab), _translate("MainWindow", "Книги"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.readers_tab), _translate("MainWindow", "Читатели"))
