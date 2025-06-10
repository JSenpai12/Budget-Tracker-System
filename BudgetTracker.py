import sys 
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidget, QTableWidgetItem
)
from BudgetDesign2 import Ui_MainWindow
import mysql.connector
import pandas as pd
from datetime import date
import json 
import os

def load_budget_data():
    if not os.path.exists("totalBudget.json"):
        return {"total_budget": 0, "total_expenses": 0}
    with open("totalBudget.json", "r") as f:
        return json.load(f)
    
def save_budget_data(data):
    with open("totalBudget.json", "w") as f:
        json.dump(data, f, indent= 4)

class BudgetDb:
    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'budget_system_db'
        )
        self.cursorr = self.connection.cursor()

    def read_expenses(self):
        query = "SELECT * FROM expenses"
        df = pd.read_sql_query(query, self.connection)
        return df
    
    def insert_expense(self, title, amount, date):
        query = "INSERT INTO expenses (title, amount, date_exp) VALUES (%s, %s, %s)"
        self.cursorr.execute(query, (title, amount, date))
        self.connection.commit()
    
    def delete_all(self):
        query = "TRUNCATE TABLE expenses;"
        self.cursorr.execute(query)
        self.connection.commit()


class BudgetSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = BudgetDb()


        #   Table Widget
        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(299, 216, 332, 250)
        self.table_widget.setStyleSheet(
            "background-color: white;" \
            "color: black;"
        )

        self.pushButton.clicked.connect(self.add_budget)
        self.pushButton_2.clicked.connect(self.add_expenses)
        self.pushButton_3.clicked.connect(self.reset_all)

        self.load_table()
        self.budget_data = load_budget_data()
        self.total_budget = self.budget_data["total_budget"]
        self.total_expenses = self.budget_data["total_expenses"]
        self.update_labels()

    def add_budget(self):
        try:
            budget = int(self.lineEdit.text())
            self.total_budget += budget
            self.budget_data["total_budget"] = self.total_budget

            self.update_labels()
            self.lineEdit.clear()
        except ValueError:
            QMessageBox.warning(self, "System", "Please Enter a valid number.")
            return
    
    def update_labels(self):
        budget_left = self.total_budget - self.total_expenses
        self.label_7.setText(f"Total Budget: \n{self.total_budget}")
        self.label_8.setText(f"Total Expenses: \n{self.total_expenses}")
        self.label_9.setText(f"Budget Left: \n{budget_left}")
    
    def add_expenses(self):
        try:
            today = date.today()
            expense_title = self.lineEdit_2.text()
            expense_amount = int(self.lineEdit_3.text())
            self.total_expenses += expense_amount
            self.budget_data["total_expenses"] = self.total_expenses
            save_budget_data(self.budget_data)

            self.db.insert_expense(expense_title, expense_amount, str(today))

            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.update_labels()
            self.load_table()
        except ValueError:
            QMessageBox.warning(self, "System", "Please enter a valid input.")
            return            
                
    def load_table(self):
        df = self.db.read_expenses()
        self.table_widget.setRowCount(len(df))
        self.table_widget.setColumnCount(len(df.columns))
        self.table_widget.setHorizontalHeaderLabels(["ID", "Title", "Amount", "Date"])

        for row in range(len(df)):
            for col in range(len(df.columns)):
                value = str(df.iat[row, col])
                self.table_widget.setItem(row, col, QTableWidgetItem(value))
    
    def reset_all(self):
        confirm = QMessageBox.question(self, "System Confirmation", "Are you sure you want to reset the data?")
        if confirm == QMessageBox.Yes:
            self.db.delete_all()
            QMessageBox.information(self, "System", "Data is now cleared.")
            self.budget_data["total_budget"] = 0
            self.budget_data["total_expenses"] = 0
            save_budget_data(self.budget_data)
            self.total_budget = 0
            self.total_expenses = 0
            self.update_labels()
            self.load_table()
        return

    
if __name__ == '__main__':
    app = QApplication([])
    window = BudgetSystem()
    window.show()
    sys.exit(app.exec())