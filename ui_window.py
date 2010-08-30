# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\teste.ui'
#
# Created: Mon Aug 30 15:24:06 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import Qsci

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # teste
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 529)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editor = Qsci.QsciScintilla(self.centralwidget)
        self.editor.setToolTip("")
        self.editor.setWhatsThis("")
        self.editor.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.editor.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.editor.setObjectName("editor")
        self.verticalLayout.addWidget(self.editor)
        
        # Alteracoes minhas!
        # baseado em: http://kib2.free.fr/tutos/PyQt4/QScintilla2.html
        ## define the font to use
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setFixedPitch(True)
        font.setPointSize(10)
        # the font metrics here will help
        # building the margin width later
        fm = QtGui.QFontMetrics(font)

        ## set the default font of the editor
        ## and take the same font for line numbers
        self.editor.setFont(font)
        self.editor.setMarginsFont(font)

        ## Line numbers
        # conventionnaly, margin 0 is for line numbers
        self.editor.setMarginWidth(0, fm.width( "00000" ) + 5)
        self.editor.setMarginLineNumbers(0, True)
        
        ## Editing line color
        self.editor.setCaretLineVisible(True)
        self.editor.setCaretLineBackgroundColor(QtGui.QColor("#e8e8ff"))
        # fim alteracoes
        
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setReadOnly(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setSizeIncrement(QtCore.QSize(0, 0))
        self.toolBar.setBaseSize(QtCore.QSize(0, 0))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.actionNovo = QtGui.QAction(MainWindow)
        self.actionNovo.setObjectName("actionNovo")
        self.actionAbri = QtGui.QAction(MainWindow)
        self.actionAbri.setObjectName("actionAbri")
        self.actionSalvar = QtGui.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionCopiar = QtGui.QAction(MainWindow)
        self.actionCopiar.setObjectName("actionCopiar")
        self.actionColar = QtGui.QAction(MainWindow)
        self.actionColar.setObjectName("actionColar")
        self.actionRecortar = QtGui.QAction(MainWindow)
        self.actionRecortar.setObjectName("actionRecortar")
        self.actionCompilar = QtGui.QAction(MainWindow)
        self.actionCompilar.setObjectName("actionCompilar")
        self.actionGerar_Codigo = QtGui.QAction(MainWindow)
        self.actionGerar_Codigo.setObjectName("actionGerar_Codigo")
        self.actionEquipe = QtGui.QAction(MainWindow)
        self.actionEquipe.setObjectName("actionEquipe")
        self.toolBar.addAction(self.actionNovo)
        self.toolBar.addAction(self.actionAbri)
        self.toolBar.addAction(self.actionSalvar)
        self.toolBar.addAction(self.actionCopiar)
        self.toolBar.addAction(self.actionColar)
        self.toolBar.addAction(self.actionRecortar)
        self.toolBar.addAction(self.actionCompilar)
        self.toolBar.addAction(self.actionGerar_Codigo)
        self.toolBar.addAction(self.actionEquipe)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Compilador", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNovo.setText(QtGui.QApplication.translate("MainWindow", "Novo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNovo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        
        
        self.actionAbri.setText(QtGui.QApplication.translate("MainWindow", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbri.setToolTip(QtGui.QApplication.translate("MainWindow", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbri.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalvar.setText(QtGui.QApplication.translate("MainWindow", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalvar.setToolTip(QtGui.QApplication.translate("MainWindow", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalvar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopiar.setText(QtGui.QApplication.translate("MainWindow", "Copiar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopiar.setToolTip(QtGui.QApplication.translate("MainWindow", "Copiar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopiar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionColar.setText(QtGui.QApplication.translate("MainWindow", "Colar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionColar.setToolTip(QtGui.QApplication.translate("MainWindow", "Colar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionColar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecortar.setText(QtGui.QApplication.translate("MainWindow", "Recortar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecortar.setToolTip(QtGui.QApplication.translate("MainWindow", "Recortar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecortar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompilar.setText(QtGui.QApplication.translate("MainWindow", "Compilar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompilar.setToolTip(QtGui.QApplication.translate("MainWindow", "Compilar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompilar.setShortcut(QtGui.QApplication.translate("MainWindow", "F8", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGerar_Codigo.setText(QtGui.QApplication.translate("MainWindow", "Gerar Código", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGerar_Codigo.setToolTip(QtGui.QApplication.translate("MainWindow", "Gerar Código", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGerar_Codigo.setShortcut(QtGui.QApplication.translate("MainWindow", "F9", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEquipe.setText(QtGui.QApplication.translate("MainWindow", "Equipe", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEquipe.setToolTip(QtGui.QApplication.translate("MainWindow", "Equipe", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEquipe.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        
        MainWindow.connect(self.actionNovo, QtCore.SIGNAL("activated()"), self._novo)
        MainWindow.connect(self.actionColar, QtCore.SIGNAL("activated()"), self._paste)
        MainWindow.connect(self.actionCopiar, QtCore.SIGNAL("activated()"), self._copy)
        MainWindow.connect(self.actionRecortar, QtCore.SIGNAL("activated()"), self._cut)
        MainWindow.connect(self.actionAbri, QtCore.SIGNAL("activated()"), self._open)
        MainWindow.connect(self.actionEquipe, QtCore.SIGNAL("activated()"), self._about)

    
    def _novo(self):
        self.editor.setText("")
        self.plainTextEdit.clear()
        
    
    def _paste(self):
        self.editor.paste()
    
    def _copy(self):
        self.editor.copy()

    def _cut(self):
        self.editor.cut()
    
    def _open(self):
        filename = QtGui.QFileDialog.getOpenFileName(self.MainWindow, 'Abrir Arquivo', '')
        if filename:
            fname = open(filename)
            data = fname.read()
            self.editor.setText(data)
            self.plainTextEdit.clear()

    def _about(self):
        QtGui.QMessageBox.about(self.MainWindow, "Sobre:", "Equipe: ")
