from PyQt5 import QtWidgets, uic

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi("format.ui", self) 

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Nama", "Jurusan"])

        data = [
            ["Ebah", "Tekhnik Informasi"],
            ["Nanda", "Tekhnik Informasi"]
        ]

        self.tableWidget.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, value in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(value))

        self.pushButton.clicked.connect(self.clear_table)
        self.pushButton_2.clicked.connect(self.load_data)

    def clear_table(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.label.setText("Data dikosongkan")

    def load_data(self):
        data = [
            ["Ebah", "Tekhnik Informasi"],
            ["Nanda", "Tekhnik Informasi"]
        ]
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Nama", "Jurusan"])
        for row_num, row_data in enumerate(data):
            for col_num, value in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(value))
        self.label.setText("Data berhasil")

app = QtWidgets.QApplication([])
window = MyApp()
window.show()
app.exec_()
