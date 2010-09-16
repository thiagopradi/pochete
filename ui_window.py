# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\teste.ui'
#
# Created: Mon Aug 30 15:24:06 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import Qsci
import icons_rc
from lexer import lexer
tokens = {"ID":"identificador", "RESERVADO":"palavra reservada", "INTEIRO":"constante inteira", 
          "BINARIO":"constante binária", "OCTAL":"constante octal", "HEXADECIMAL":"constante hexadecimal",
           "REAL":"constante real", "LITERAL":"constante literal", "SIMBOLO":u"símbolo especial" }
           
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # teste
        self.filename = ""

        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 529)
        #MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
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
        font.setPointSize(14)
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
        # teste
        self.status_file = QtGui.QLabel(u"Não modificado")
        self.status_file.setFrameShape(QtGui.QFrame.StyledPanel)
        self.statusbar.addWidget(self.status_file, 0)
        self.status_filename = QtGui.QLabel("-")
        self.status_filename.setFrameShape(QtGui.QFrame.StyledPanel)
        self.statusbar.addWidget(self.status_filename, 1)

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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imagens/filenew-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNovo.setIcon(icon)
        self.actionNovo.setObjectName("actionNovo")
        self.actionAbri = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imagens/fileopen-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbri.setIcon(icon1)
        self.actionAbri.setObjectName("actionAbri")
        self.actionSalvar = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imagens/filesave-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalvar.setIcon(icon2)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionCopiar = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imagens/editcopy-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopiar.setIcon(icon3)
        self.actionCopiar.setObjectName("actionCopiar")
        self.actionColar = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imagens/editpaste-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColar.setIcon(icon4)
        self.actionColar.setObjectName("actionColar")
        self.actionRecortar = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imagens/editcut-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRecortar.setIcon(icon5)
        self.actionRecortar.setObjectName("actionRecortar")
        self.actionCompilar = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/imagens/artsbuilderexecute-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompilar.setIcon(icon6)
        self.actionCompilar.setObjectName("actionCompilar")
        self.actionGerar_Codigo = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/imagens/compfile-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGerar_Codigo.setIcon(icon7)
        self.actionGerar_Codigo.setObjectName("actionGerar_Codigo")
        self.actionEquipe = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/imagens/groupevent-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEquipe.setIcon(icon8)
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
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Pochete Compiler", None, QtGui.QApplication.UnicodeUTF8))
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
        MainWindow.connect(self.actionSalvar, QtCore.SIGNAL("activated()"), self._save)
        MainWindow.connect(self.actionCompilar, QtCore.SIGNAL("activated()"), self._compile)
        MainWindow.connect(self.actionGerar_Codigo, QtCore.SIGNAL("activated()"), self._generate)

        MainWindow.connect(self.editor, QtCore.SIGNAL("textChanged()"), self._onChange)

    
    def _onChange(self):
        self.status_file.setText(u"Modificado")

    def _novo(self):
        self.editor.setText("")
        self.plainTextEdit.clear()
        self.filename = ""
        self.status_file.setText(u"Não modificado")
        self.status_filename.setText("-")
        
    def _paste(self):
        self.editor.paste()
    
    def _copy(self):
        self.editor.copy()

    def _cut(self):
        self.editor.cut()
    
    def _open(self):
        filename = unicode(QtGui.QFileDialog.getOpenFileName(self.MainWindow, 'Abrir Arquivo', ''))
        if filename:
            fname = open(filename)
            data = fname.read()
            self.editor.setText(data)
            self.plainTextEdit.clear()
            self.filename = filename
            self._updateStatusbar()
    
    def _save(self):
        if not self.filename:
            filename = unicode(QtGui.QFileDialog.getSaveFileName(self.MainWindow, 'Salvar Arquivo', ''))
            if filename:
                fname = open(filename, 'w')
                fname.write(self.editor.text())
                fname.close()
                self.filename = filename
                self._updateStatusbar()
        else:
            fname = open(self.filename, 'w')
            fname.write(self.editor.text())
            fname.close()
            self._updateStatusbar()
    
    def _compile(self):
        self.plainTextEdit.clear()
        var_lex = lexer()
        var_lex.input(str(self.editor.text()))
        try:
          self.plainTextEdit.appendPlainText("linha\tclasse\t\ttoken")
          for token in var_lex:
            self.plainTextEdit.appendPlainText("%s\t%s\t%s" % (token.lineno, tokens[token.type], token.value))
          self.plainTextEdit.appendPlainText("Programa compilado com sucesso")
        except Exception, e:
          self.plainTextEdit.setPlainText(unicode(e))
    
    def _generate(self):
        QtGui.QMessageBox.warning(self.MainWindow, "Aviso!", u"Não implementado ainda!")

    def _about(self):
        QtGui.QMessageBox.about(self.MainWindow, "Sobre:", "Equipe:\nPaulo Eduardo Danker\nThiago Pradi")

    def _updateStatusbar(self):
        self.status_filename.setText(self.filename)
        self.status_file.setText(u"Não modificado")
