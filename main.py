# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.file = open('translate.txt')
        self.big_text = self.file.read()
        self.parts = self.big_text.split('\n')
        self.words = []
        i = 0
        while i < len(self.parts):
            my_dict = {'english': self.parts[i], 'persian': self.parts[i + 1]}
            self.words.append(my_dict)
            i += 2
        self.ui.btn_3.clicked.connect(self.translate)

    def translate(self):
        if self.ui.btn_1.isChecked():
            user_string = self.ui.line_1.text()
            user_words = user_string.split()
            self.sen = ' '
            print(self.sen)
            for j in range(len(user_words)):
                for i in range(len(self.words)):

                    if self.words[i]['english'] == user_words[j]:

                        self.sen = self.sen + self.words[i]['persian'] + ' '
                        self.ui.line_2.setText(self.sen)
                        break

                else:  # word not found
                    self.sen += user_words[j] + ' '
                    self.ui.line_2.setText(self.sen)

        elif self.ui.btn_2.isChecked():
            user_string = self.ui.line_1.text()
            user_words = user_string.split()
            self.sen = ' '
            print(self.sen)
            for j in range(len(user_words)):
                for i in range(len(self.words)):

                    if self.words[i]['persian'] == user_words[j]:

                        self.sen = self.sen + self.words[i]['english'] + ' '
                        self.ui.line_2.setText(self.sen)
                        break

                else:  # word not found
                    self.sen += user_words[j] + ' '
                    self.ui.line_2.setText(self.sen)
            print(self.sen)

if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    sys.exit(app.exec_())

