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
from pochete_parser import parser, SemanticTools
tokens = {"ID":"identificador", "RESERVADO":"palavra reservada", "INTEIRO":"constante inteira", 
          "BINARIO":"constante binária", "OCTAL":"constante octal", "HEXADECIMAL":"constante hexadecimal",
           "REAL":"constante real", "LITERAL":"constante literal", "SIMBOLO":u"símbolo especial" }
           
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # teste
        self.filename = ""

        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 529)
        MainWindow.setMinimumSize(QtCore.QSize(870, 0))
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

        self.editor.setUtf8(True)
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
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
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
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Pochete Compiler", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionNovo.setText(QtGui.QApplication.translate("MainWindow", "Novo[Ctrl+N]", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionNovo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", 
            None, QtGui.QApplication.UnicodeUTF8))
        
        
        self.actionAbri.setText(QtGui.QApplication.translate("MainWindow", "Abrir[Ctrl+A]", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbri.setToolTip(QtGui.QApplication.translate("MainWindow", "Abrir", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbri.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalvar.setText(QtGui.QApplication.translate("MainWindow", "Salvar[Ctrl+S]", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalvar.setToolTip(QtGui.QApplication.translate("MainWindow", "Salvar", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalvar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopiar.setText(QtGui.QApplication.translate("MainWindow", "Copiar[Ctrl+C]", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopiar.setToolTip(QtGui.QApplication.translate("MainWindow", "Copiar", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopiar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+C", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionColar.setText(QtGui.QApplication.translate("MainWindow", "Colar[Ctrl+V]", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionColar.setToolTip(QtGui.QApplication.translate("MainWindow", "Colar", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionColar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecortar.setText(QtGui.QApplication.translate("MainWindow", "Recortar[Ctrl+X]", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecortar.setToolTip(QtGui.QApplication.translate("MainWindow", "Recortar", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecortar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+X", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompilar.setText(QtGui.QApplication.translate("MainWindow", "Compilar[F8]", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompilar.setToolTip(QtGui.QApplication.translate("MainWindow", "Compilar", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompilar.setShortcut(QtGui.QApplication.translate("MainWindow", "F8", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionGerar_Codigo.setText(QtGui.QApplication.translate("MainWindow", "Gerar Código[F9]", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionGerar_Codigo.setToolTip(QtGui.QApplication.translate("MainWindow", "Gerar Código", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionGerar_Codigo.setShortcut(QtGui.QApplication.translate("MainWindow", "F9", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionEquipe.setText(QtGui.QApplication.translate("MainWindow", "Equipe[F1]", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionEquipe.setToolTip(QtGui.QApplication.translate("MainWindow", "Equipe", 
            None, QtGui.QApplication.UnicodeUTF8))
        self.actionEquipe.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", 
            None, QtGui.QApplication.UnicodeUTF8))
        
        self.actionNovo.pyqtConfigure(triggered=self._novo)
        self.actionColar.pyqtConfigure(triggered=self._paste)
        self.actionCopiar.pyqtConfigure(triggered=self._copy)
        self.actionRecortar.pyqtConfigure(triggered=self._cut)
        self.actionAbri.pyqtConfigure(triggered=self._open)
        self.actionEquipe.pyqtConfigure(triggered=self._about)
        self.actionSalvar.pyqtConfigure(triggered=self._save)
        self.actionCompilar.pyqtConfigure(triggered=self._compile)
        self.actionGerar_Codigo.pyqtConfigure(triggered=self._generate)

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
        print(self.editor.text())
        try:
          parser.parse(str(self.editor.text()), lexer())
          self.plainTextEdit.appendPlainText("Programa compilado com sucesso")
          SemanticTools.reset()
        except Exception, e:
          self.plainTextEdit.setPlainText(unicode(e.message))
    
    def _generate(self):
      self.plainTextEdit.clear()
      try:
        fileInfo = QtCore.QFileInfo(self.filename)
        nameLayer = str(fileInfo.baseName())
        SemanticTools.program_name = nameLayer
        parser.parse(str(self.editor.text()), lexer())
        self.plainTextEdit.appendPlainText(u"Código objeto gerado com sucesso")
        fname = open(self.filename + ".il", 'w')
        fname.write("\n".join(SemanticTools.code))
        fname.close()
        SemanticTools.reset()
      except Exception, e:
        self.plainTextEdit.setPlainText(unicode(e.message))

    def _about(self):
        QtGui.QMessageBox.about(self.MainWindow, "Sobre:", "Equipe:\nPaulo Eduardo Danker\nThiago Pradi")

    def _updateStatusbar(self):
        self.status_filename.setText(self.filename)
        self.status_file.setText(u"Não modificado")
