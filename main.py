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

        loadcuttinglist = QPushButton("Load cutting list", self)  # Create a button with the label "Load cutting list"
        loadcuttinglist.clicked.connect(self.load_cutting_list)  # Connect the button's click event to the load_cutting_list function
        layout.addWidget(loadcuttinglist)  # Add the button to the layout

        loadstorage = QPushButton("Load storage", self)  # Create a button with the label "Load storage"
        loadstorage.clicked.connect(self.load_storage)  # Connect the button's click event to the load_storage function
        layout.addWidget(loadstorage)

        optimize_button = QPushButton("Optimize", self)
        optimize_button.clicked.connect(self.optimize)
        layout.addWidget(optimize_button)

        displaycuttinglist = QPushButton("Display Cutting List", self)
        displaycuttinglist.clicked.connect(self.display_cutting_list)  # Connect the button's click event to the display_cutting_list function
        layout.addWidget(displaycuttinglist)

        displaystorage = QPushButton("Display Storage", self)
        displaystorage.clicked.connect(self.display_storage)
        layout.addWidget(displaystorage)

        # Show layout
        self.setLayout(layout)  # Set the layout for the main window
        self.show()  # Show the main window

    def load_cutting_list(self):
        csvloader.load_cutting_list(self)

    def load_storage(self):
        csvloader.load_storage(self)

    def optimize(self):
        if hasattr(self, "loaded_cutting_list") and hasattr(self, "loaded_storage"):
            result = optimize.main(self.loaded_cutting_list, self.loaded_storage)
            if result is not None:
                self.optimized_cutting_list, self.optimized_storage = result
            else:
                self.optimized_cutting_list = None
                self.optimized_storage = None
                self.optimization_failed()
        else:
            self.not_loaded()

    def display_cutting_list(self):
        if hasattr(self, "loaded_cutting_list"):
            self.table_window = TableWindow(self.loaded_cutting_list)
            self.table_window.show()
        else:
            self.not_loaded()

    def display_storage(self):
        if hasattr(self, "loaded_storage"):
            self.table_window = TableWindow(self.loaded_storage)
            self.table_window.show()
        else:
            self.not_loaded()

    def display_optimized_cutting_list(self):
        if hasattr(self, "optimized_cutting_list") and self.optimized_cutting_list is not None:
            self.table_window = TableWindow(self.optimized_cutting_list)
            self.table_window.show()
        else:
            self.not_loaded()

    def display_optimized_storage(self):
        if hasattr(self, "optimized_storage") and self.optimized_storage is not None:
            self.table_window = TableWindow(self.optimized_storage)
            self.table_window.show()
        else:
            self.not_loaded()

    def not_loaded(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("Data not loaded")
        msg.setWindowTitle("Warning")
        msg.exec()

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