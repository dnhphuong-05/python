from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QDate
from expense_tracker_ui import Ui_MainWindow  # Import class from the generated UI file
import sys


class ExpenseTracker(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Call the setupUi method from Ui_MainWindow class

        self.so_du = 0.0  # Starting balance
        self.danh_sach_giao_dich = []  # List to store transactions

        # Connect the buttons to their respective methods
        self.pushButton_add_expense.clicked.connect(self.add_expense)
        self.pushButton_add_income.clicked.connect(self.add_income)

        self.show()  # Show the main window

    def add_expense(self):
        try:
            amount = float(self.lineEdit_expense_amount.text())  # Get the amount
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            note = self.lineEdit_expense_note.text()  # Get the note
            date = self.dateEdit_expense_date.date().toString("dd/MM/yyyy")  # Get the date

            # Update balance and add the transaction
            self.so_du -= amount
            self.danh_sach_giao_dich.append({"Loại": "Chi", "Tên": note, "Số tiền": amount, "Ngày": date})

            # Reset fields
            self.lineEdit_expense_note.clear()
            self.lineEdit_expense_amount.setText("0")
            self.dateEdit_expense_date.setDate(QDate.currentDate())  # Set the date to today
            print(f"Added expense: {note} - {amount} VND")
        except ValueError:
            print("Số tiền không hợp lệ, vui lòng nhập một số hợp lệ.")  # Invalid input

    def add_income(self):
        try:
            amount = float(self.lineEdit_income_amount.text())  # Get the amount
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            note = self.lineEdit_income_note.text()  # Get the note
            date = self.dateEdit_income_date.date().toString("dd/MM/yyyy")  # Get the date

            # Update balance and add the transaction
            self.so_du += amount
            self.danh_sach_giao_dich.append({"Loại": "Thu", "Tên": note, "Số tiền": amount, "Ngày": date})

            # Reset fields
            self.lineEdit_income_note.clear()
            self.lineEdit_income_amount.setText("0")
            self.dateEdit_income_date.setDate(QDate.currentDate())  # Set the date to today
            print(f"Added income: {note} - {amount} VND")
        except ValueError:
            print("Số tiền không hợp lệ, vui lòng nhập một số hợp lệ.")  # Invalid input


# Start the application
app = QApplication(sys.argv)
window = ExpenseTracker()
sys.exit(app.exec())

