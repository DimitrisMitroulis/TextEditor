from PyQt5.QtWidgets import*
from PyQt5.QtGui import QFont
from PyQt5 import uic


class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('TextEditor.ui',self)
        self.show()


        self.action8pt.triggered.connect(lambda: self.changeFontSize(8))
        self.action12pt.triggered.connect(lambda: self.changeFontSize(12))
        self.action16pt.triggered.connect(lambda: self.changeFontSize(16))
        self.action18pt.triggered.connect(lambda: self.changeFontSize(18))
        self.action24pt.triggered.connect(lambda: self.changeFontSize(24))

        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionClose.triggered.connect(self.close)


    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self,"OpenFile","","Text Files (*.txt);;Python Files(*.py)",options=options)
        if filename != "":
            with open(filename,"r") as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self,"Save File","","Text Files (*.txt);;Python Files(*.py)",options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

    def closeEvent(self,event):
        dialog = QMessageBox()
        dialog.setText("Do you want to save your text?")
        dialog.addButton(QPushButton("Yes"),QMessageBox.YesRole)
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole)
        dialog.addButton(QPushButton("Cancel"), QMessageBox.CancelRole)

        answer = dialog.exec_()

        if answer == 0:
            self.save_file()
            event.accept()
        elif answer == 2:
            event.ignore()


    def changeFontSize(self,size):
        self.plainTextEdit.setFont(QFont("Arial",size))


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()



if __name__ == '__main__':
    main()

