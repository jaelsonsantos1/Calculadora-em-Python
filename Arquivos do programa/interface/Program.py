# -*- coding: utf-8 -*- --noconsole

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from untitled import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        def calc(arg):
            text = self.tela.text()

            if arg == "1":
                self.tela.setText(str(text) + str(arg))
            elif arg == "2":
                self.tela.setText(str(text) + str(arg))
            elif arg == "3":
                self.tela.setText(str(text) + str(arg))
            elif arg == "4":
                self.tela.setText(str(text) + str(arg))
            elif arg == "5":
                self.tela.setText(str(text) + str(arg))
            elif arg == "6":
                self.tela.setText(str(text) + str(arg))
            elif arg == "7":
                self.tela.setText(str(text) + str(arg))
            elif arg == "8":
                self.tela.setText(str(text) + str(arg))
            elif arg == "9":
                self.tela.setText(str(text) + str(arg))
            elif arg == "0":
                self.tela.setText(str(text) + str(arg))
            elif arg == "-":
                self.tela.setText(str(text) + str(arg))
            elif arg == "+":
                self.tela.setText(str(text) + str(arg))
            elif arg == "*":
                self.tela.setText(str(text) + str(arg))
            elif arg == ".":
                self.tela.setText(str(text) + str(arg))
            elif arg == "/":
                self.tela.setText(str(text) + str(arg))
            elif arg == "Clear":
                self.tela.setText("")
            elif arg == "Del":
                self.tela.setText(text[:len(text) - 1])
            elif arg == "=":

                try:
                    ans = eval(text)
                    self.tela.setText(str(ans))
                except:
                    self.tela.setText("Erro!")

            if arg == "https://www.instagram.com/_jaelson1/?hl=pt-br":
                link = "https://www.instagram.com/_jaelson1/?hl=pt-br"
                QtGui.QDesktopServices.openUrl(QtCore.QUrl(link))

        self.botao1.clicked.connect(lambda: calc(self.botao1.text()))
        self.botao2.clicked.connect(lambda: calc(self.botao2.text()))
        self.botao3.clicked.connect(lambda: calc(self.botao3.text()))
        self.botao4.clicked.connect(lambda: calc(self.botao4.text()))
        self.botao5.clicked.connect(lambda: calc(self.botao5.text()))
        self.botao6.clicked.connect(lambda: calc(self.botao6.text()))
        self.botao7.clicked.connect(lambda: calc(self.botao7.text()))
        self.botao8.clicked.connect(lambda: calc(self.botao8.text()))
        self.botao9.clicked.connect(lambda: calc(self.botao9.text()))
        self.botao0.clicked.connect(lambda: calc(self.botao0.text()))
        self.ponto.clicked.connect(lambda: calc(self.ponto.text()))
        self.mais.clicked.connect(lambda: calc(self.mais.text()))
        self.menos.clicked.connect(lambda: calc(self.menos.text()))
        self.vezes.clicked.connect(lambda: calc("*"))
        self.dividir.clicked.connect(lambda: calc(self.dividir.text()))
        self.apagar.clicked.connect(lambda: calc(self.apagar.text()))
        self.igual.clicked.connect(lambda: calc(self.igual.text()))
        self.apagar_tudo.clicked.connect(lambda: calc(self.apagar_tudo.text()))
        self.botao_link.clicked.connect(lambda: calc(
            "https://www.instagram.com/_jaelson1/?hl=pt-br"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())