from PySide6.QtWidgets import QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import numpy as np

class TableWindow(QWidget):
    def __init__(self, data, headers=None):
        super().__init__()
        self.setWindowTitle("Data Table")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

        self.populate_table(data, headers)

    def populate_table(self, data, headers=None):
        rows = len(data)
        cols = len(data[0]) if rows > 0 else 0
        self.table_widget.setRowCount(rows)
        self.table_widget.setColumnCount(cols)

        if headers:
            self.table_widget.setHorizontalHeaderLabels(headers)

        for row in range(rows):
            for col in range(cols):
                self.table_widget.setItem(row, col, QTableWidgetItem(str(data[row][col])))

def load_cutting_list(parent):
    FileName = QFileDialog.getOpenFileName(
        caption="Select the file to open",
        options=QFileDialog.Option.DontUseNativeDialog,
        filter="All Files (*)"
    )[0]
    if FileName:
        # Open file
        with open(FileName, "r") as file:
            data = file.read()
            # Split at commas and lines
            data = data.split("\n")
            data = [line.split(",") for line in data]
            # Remove empty lines
            data = [line for line in data if line != [""]]

        # Store the data in the parent instance
        parent.loaded_cutting_list = data

def load_storage(parent):
    FileName = QFileDialog.getOpenFileName(
        caption="Select the file to open",
        options=QFileDialog.Option.DontUseNativeDialog,
        filter="All Files (*)"
    )[0]
    if FileName:
        # Open file
        with open(FileName, "r") as file:
            data = file.read()
            # Split at commas and lines
            data = data.split("\n")
            data = [line.split(",") for line in data]
            # Remove empty lines
            data = [line for line in data if line != [""]]

        # Store the data in the parent instance
        parent.loaded_storage = data