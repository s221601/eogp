# delete .venv folder if already exists
# shift+command+p -> create new environment
# pip install PySide6
# pip install numpy

import os
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
import functions.csvloader as csvloader
from functions.csvloader import TableWindow
import functions.optimizecuts as optimize

# Set path for helper function scripts
functions_path = os.getcwd() + "\\functions\\"

# Create the main window class inheriting from QWidget
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Call the parent class (QWidget) constructor

        self.setWindowTitle("Main Window")  # Set the window title
        self.setGeometry(100, 100, 800, 600)  # Set the window size and position

        layout = QVBoxLayout()  # Create a vertical box layout

        # Load cutting list button
        loadcuttinglist = QPushButton("Load cutting list", self) 
        loadcuttinglist.clicked.connect(self.load_cutting_list)  
        layout.addWidget(loadcuttinglist)  

        # Load storage button
        loadstorage = QPushButton("Load storage", self)
        loadstorage.clicked.connect(self.load_storage)
        layout.addWidget(loadstorage)

        # Optimize button
        optimize_button = QPushButton("Optimize", self)
        optimize_button.clicked.connect(self.optimize)
        layout.addWidget(optimize_button)

        # Display cutting list
        displaycuttinglist = QPushButton("Display Cutting List", self)
        displaycuttinglist.clicked.connect(self.display_cutting_list)
        layout.addWidget(displaycuttinglist)

        # Display storage
        displaystorage = QPushButton("Display Storage", self)
        displaystorage.clicked.connect(self.display_storage)
        layout.addWidget(displaystorage)

        # Show layout
        self.setLayout(layout)  # Set the layout for the main window
        self.show()  # Show the main window

    # Load the cutting list from a file
    def load_cutting_list(self):
        csvloader.load_cutting_list(self)

    # Load the storage from a file
    def load_storage(self):
        csvloader.load_storage(self)

    # Optimize the cutting list
    def optimize(self):
        if hasattr(self, "loaded_cutting_list") and hasattr(self, "loaded_storage"):
            result = optimize.main(self.loaded_cutting_list, self.loaded_storage)
            if result is not None:
                self.table = result
                self.display_result_table(self.table)
            else:
                self.optimization_failed()
        else:
            self.not_loaded()

    # Display the result table
    def display_result_table(self, table_data):
        headers = ["Storage Length", "Usage Count", "Cut Size", "Remaining Length", "Cumulative Waste"]
        self.table_window = TableWindow(table_data, headers)
        self.table_window.show()

    # Display cutting list input
    def display_cutting_list(self):
        if hasattr(self, "loaded_cutting_list"):
            self.table_window = TableWindow(self.loaded_cutting_list)
            self.table_window.show()
        else:
            self.not_loaded()

    # Display storage input
    def display_storage(self):
        if hasattr(self, "loaded_storage"):
            self.table_window = TableWindow(self.loaded_storage)
            self.table_window.show()
        else:
            self.not_loaded()

    # Error message for data not loaded
    def not_loaded(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("Data not loaded")
        msg.setWindowTitle("Warning")
        msg.exec()

    # Error message for optimization failure
    def optimization_failed(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("Optimization failed")
        msg.setWindowTitle("Warning")
        msg.exec()

# Create the application instance
app = QApplication([])
# Create the main window instance
window = MainWindow()
# Execute the application
app.exec()