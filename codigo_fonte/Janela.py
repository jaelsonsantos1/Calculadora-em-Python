from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import imagens

class Janela_calculadora(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(277, 428)
        MainWindow.setMinimumSize(QSize(277, 428))
        MainWindow.setMaximumSize(QSize(277, 428))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/newPrefix/calculator_icon-icons.com_53152.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(61, 61, 61);\n"
"border-color: rgb(255, 255, 255);")
        self.quit = QAction(MainWindow)
        self.quit.setObjectName(u"quit")
        self.actionhelp_2 = QAction(MainWindow)
        self.actionhelp_2.setObjectName(u"actionhelp_2")
        self.ajuda = QAction(MainWindow)
        self.ajuda.setObjectName(u"ajuda")
        self.develop = QAction(MainWindow)
        self.develop.setObjectName(u"develop")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.read_me = QFrame(self.centralwidget)
        self.read_me.setObjectName(u"read_me")
        self.read_me.setGeometry(QRect(0, 0, 281, 411))
        self.read_me.setFrameShape(QFrame.StyledPanel)
        self.read_me.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.read_me)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(13, 20, 251, 41))
        self.label_3 = QLabel(self.read_me)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 80, 121, 111))
        self.label_3.setStyleSheet(u"image: url(:/newPrefix/download.png);\n"
"border-radius: 20px;")
        self.label_4 = QLabel(self.read_me)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 210, 261, 81))
        self.label_5 = QLabel(self.read_me)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(13, 301, 81, 31))
        self.voltar_2 = QPushButton(self.read_me)
        self.voltar_2.setObjectName(u"voltar_2")
        self.voltar_2.setGeometry(QRect(95, 377, 75, 23))
        self.botao_link = QPushButton(self.read_me)
        self.botao_link.setObjectName(u"botao_link")
        self.botao_link.setGeometry(QRect(96, 335, 171, 21))
        self.botao_link.setStyleSheet(u"image: url(:/newPrefix/insta.jpg);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label_6 = QLabel(self.read_me)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(15, 334, 71, 20))
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.tela_principal = QFrame(self.centralwidget)
        self.tela_principal.setObjectName(u"tela_principal")
        self.tela_principal.setGeometry(QRect(0, 0, 301, 411))
        self.tela_principal.setFrameShape(QFrame.StyledPanel)
        self.tela_principal.setFrameShadow(QFrame.Raised)
        self.botao1 = QPushButton(self.tela_principal)
        self.botao1.setObjectName(u"botao1")
        self.botao1.setGeometry(QRect(9, 281, 61, 61))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao1.setFont(font)
        self.botao1.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.botao4 = QPushButton(self.tela_principal)
        self.botao4.setObjectName(u"botao4")
        self.botao4.setGeometry(QRect(10, 219, 61, 61))
        self.botao4.setFont(font)
        self.botao4.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.dividir = QPushButton(self.tela_principal)
        self.dividir.setObjectName(u"dividir")
        self.dividir.setGeometry(QRect(200, 282, 71, 61))
        self.dividir.setFont(font)
        self.dividir.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.botao0 = QPushButton(self.tela_principal)
        self.botao0.setObjectName(u"botao0")
        self.botao0.setGeometry(QRect(11, 344, 121, 61))
        self.botao0.setFont(font)
        self.botao0.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.botao2 = QPushButton(self.tela_principal)
        self.botao2.setObjectName(u"botao2")
        self.botao2.setGeometry(QRect(72, 280, 61, 61))
        self.botao2.setFont(font)
        self.botao2.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.mais = QPushButton(self.tela_principal)
        self.mais.setObjectName(u"mais")
        self.mais.setGeometry(QRect(201, 93, 71, 60))
        self.mais.setFont(font)
        self.mais.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.menos = QPushButton(self.tela_principal)
        self.menos.setObjectName(u"menos")
        self.menos.setGeometry(QRect(201, 156, 71, 61))
        self.menos.setFont(font)
        self.menos.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.botao3 = QPushButton(self.tela_principal)
        self.botao3.setObjectName(u"botao3")
        self.botao3.setGeometry(QRect(137, 281, 60, 61))
        self.botao3.setFont(font)
        self.botao3.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.botao9 = QPushButton(self.tela_principal)
        self.botao9.setObjectName(u"botao9")
        self.botao9.setGeometry(QRect(136, 155, 61, 60))
        self.botao9.setFont(font)
        self.botao9.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.botao8 = QPushButton(self.tela_principal)
        self.botao8.setObjectName(u"botao8")
        self.botao8.setGeometry(QRect(71, 155, 61, 60))
        self.botao8.setFont(font)
        self.botao8.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.ponto = QPushButton(self.tela_principal)
        self.ponto.setObjectName(u"ponto")
        self.ponto.setGeometry(QRect(136, 344, 60, 61))
        self.ponto.setFont(font)
        self.ponto.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.apagar = QPushButton(self.tela_principal)
        self.apagar.setObjectName(u"apagar")
        self.apagar.setGeometry(QRect(136, 92, 61, 60))
        self.apagar.setFont(font)
        self.apagar.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.botao7 = QPushButton(self.tela_principal)
        self.botao7.setObjectName(u"botao7")
        self.botao7.setGeometry(QRect(9, 155, 60, 61))
        self.botao7.setFont(font)
        self.botao7.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.igual = QPushButton(self.tela_principal)
        self.igual.setObjectName(u"igual")
        self.igual.setGeometry(QRect(200, 346, 71, 61))
        self.igual.setFont(font)
        self.igual.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.botao5 = QPushButton(self.tela_principal)
        self.botao5.setObjectName(u"botao5")
        self.botao5.setGeometry(QRect(73, 218, 61, 60))
        self.botao5.setFont(font)
        self.botao5.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.botao6 = QPushButton(self.tela_principal)
        self.botao6.setObjectName(u"botao6")
        self.botao6.setGeometry(QRect(136, 218, 61, 61))
        self.botao6.setFont(font)
        self.botao6.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.apagar_tudo = QPushButton(self.tela_principal)
        self.apagar_tudo.setObjectName(u"apagar_tudo")
        self.apagar_tudo.setGeometry(QRect(10, 92, 121, 60))
        self.apagar_tudo.setFont(font)
        self.apagar_tudo.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.vezes = QPushButton(self.tela_principal)
        self.vezes.setObjectName(u"vezes")
        self.vezes.setGeometry(QRect(200, 219, 71, 61))
        self.vezes.setFont(font)
        self.vezes.setStyleSheet(u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(85, 170, 255);\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"")
        self.gridLayoutWidget = QWidget(self.tela_principal)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 0, 261, 91))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tela = QLineEdit(self.gridLayoutWidget)
        self.tela.setObjectName(u"tela")
        self.tela.setStyleSheet(u"QLineEdit{\n"
"	font: 75 30pt \"MS Shell Dlg 2\";\n"
"	color: rgb(139, 139, 209);\n"
"	border: 3px solid rgb(35, 35, 35);\n"
"	border-radius: 20px;\n"
"	padding-right: 15px;\n"
"}")
        self.tela.setMaxLength(10)
        self.tela.setDragEnabled(False)
        self.tela.setReadOnly(True)
        self.tela.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.tela, 0, 0, 1, 1)

        self.apagar_tudo.raise_()
        self.dividir.raise_()
        self.vezes.raise_()
        self.botao7.raise_()
        self.botao8.raise_()
        self.botao9.raise_()
        self.menos.raise_()
        self.botao4.raise_()
        self.botao5.raise_()
        self.botao6.raise_()
        self.mais.raise_()
        self.botao1.raise_()
        self.botao2.raise_()
        self.botao3.raise_()
        self.botao0.raise_()
        self.ponto.raise_()
        self.apagar.raise_()
        self.igual.raise_()
        self.gridLayoutWidget.raise_()
        self.tela_ajuda = QFrame(self.centralwidget)
        self.tela_ajuda.setObjectName(u"tela_ajuda")
        self.tela_ajuda.setGeometry(QRect(0, 0, 281, 411))
        self.tela_ajuda.setFrameShape(QFrame.StyledPanel)
        self.tela_ajuda.setFrameShadow(QFrame.Raised)
        self.voltar = QPushButton(self.tela_ajuda)
        self.voltar.setObjectName(u"voltar")
        self.voltar.setGeometry(QRect(98, 368, 75, 23))
        self.textBrowser = QTextBrowser(self.tela_ajuda)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(8, 63, 261, 291))
        self.label = QLabel(self.tela_ajuda)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 14, 261, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.tela_ajuda.raise_()
        self.read_me.raise_()
        self.tela_principal.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 277, 18))
        self.menumenu = QMenu(self.menubar)
        self.menumenu.setObjectName(u"menumenu")
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menumenu.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menumenu.addAction(self.quit)
        self.menuhelp.addAction(self.ajuda)
        self.menuhelp.addAction(self.develop)

        self.retranslateUi(MainWindow)
        self.quit.triggered.connect(MainWindow.close)
        self.develop.triggered.connect(self.read_me.raise_)
        self.ajuda.triggered.connect(self.tela_ajuda.raise_)
        self.voltar.clicked.connect(self.tela_principal.raise_)
        self.voltar_2.clicked.connect(self.tela_principal.raise_)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple Calculator", None))
        MainWindow.setWindowFilePath("")
        self.quit.setText(QCoreApplication.translate("MainWindow", u"quit", None))
        self.actionhelp_2.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.ajuda.setText(QCoreApplication.translate("MainWindow", u"calculator funtion", None))
        self.develop.setText(QCoreApplication.translate("MainWindow", u"READ ME", None))
#if QT_CONFIG(tooltip)
        self.read_me.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Century Schoolbook','serif'; font-size:18pt; font-weight:600; font-style:italic;\">Simple Caculator</span></p></body></html>", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Desenvovida por Jaelson Santos</span></p><p><span style=\" font-size:10pt;\">Programada em linguagem Python</span></p><p><span style=\" font-size:10pt;\">Ultiliza\u00e7\u00e3o da biblioteca PySide2</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">contatos</span></p><p><br/></p></body></html>", None))
        self.voltar_2.setText(QCoreApplication.translate("MainWindow", u"back", None))
        self.botao_link.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Instagran", None))
        self.tela_principal.setStyleSheet(QCoreApplication.translate("MainWindow", u"QPushButton{	\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border-radius:30px;\n"
"	\n"
"	color: rgb(139, 139, 209);\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(170, 170, 255);\n"
"background-color: rgb(45,45, 45);\n"
"\n"
"}\n"
"", None))
        self.botao1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.botao1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.botao4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.botao4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.dividir.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.dividir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+/", None))
#endif // QT_CONFIG(shortcut)
        self.botao0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.botao0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.botao2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.botao2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.mais.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.mais.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.menos.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.menos.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.botao3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.botao3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.botao9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.botao9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.botao8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.botao8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.ponto.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.ponto.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.apagar.setText(QCoreApplication.translate("MainWindow", u"Del", None))
#if QT_CONFIG(shortcut)
        self.apagar.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.botao7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">7</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.botao7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.botao7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.igual.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.botao5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.botao5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.botao6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.botao6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.apagar_tudo.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(shortcut)
        self.apagar_tudo.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.vezes.setText(QCoreApplication.translate("MainWindow", u"x", None))
#if QT_CONFIG(shortcut)
        self.vezes.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.tela.setText("")
        self.voltar.setText(QCoreApplication.translate("MainWindow", u"back", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Realiza c\u00e1lculos matem\u00e1ticos b\u00e1sicos;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Realiza as seguintes opera\u00e7\u00f5es:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* Adi\u00e7\u00e3o</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; m"
                        "argin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* subtra\u00e7\u00e3o</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* multiplica\u00e7\u00e3o</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* divis\u00e3o</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Calculadora pr\u00e1tica e f\u00e1cil de usar;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- C\u00e1lculos de n\u00fameros de ponto flutuante ou n\u00fameros decimais;</span></p>\n"
"<p style=\" margin-top:12px; ma"
                        "rgin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- N\u00fameros tamb\u00e9m podem ser digitados atrav\u00e9s do teclado;</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Century Schoolbook','serif'; font-size:18pt; font-weight:600; font-style:italic;\">Simple Caculator</span></p></body></html>", None))
        self.menumenu.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
    # retranslateUi

