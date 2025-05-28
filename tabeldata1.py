import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector as mc

class HalloPython(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('format.ui', self)
        self.setWindowTitle('PYTHON GUI TABLEWIDGET')
        self.pushButton.clicked.connect(self.hapus)
        self.pushButton_2.clicked.connect(self.sqlLoad)

    def hapus(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.label.setText("Data telah dihapus")

    def sqlLoad(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_latihan"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM Mahasiswa ORDER BY nama ASC")
            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            self.label.setText("Data Berhasil Ditampilkan")

        except mc.Error as err:
            print("Error:", err)
            self.label.setText("Data Gagal Ditampilkan")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = HalloPython()
    form.show()
    sys.exit(app.exec_())
