from PyQt4.QtGui import *
from PyQt4.QtCore import *

class OrderWidget(QWidget):
    """provides a widget that enables you to create an order full of products"""
    def __init__(self,connection):
        super().__init__()
        self.connection = connection
        self.product_model = self.connection.current_products()
        self.order_details = None


        self.product_table = QTableView()
        self.product_table.setModel(self.product_model)
        self.product_table.setSelectionBehavior(1)

        self.order_item_table = QTableView()

        self.add_product_button = QPushButton("Add Product")
        self.remove_product_button = QPushButton("Remove Product")

        self.order_button_layout = QVBoxLayout()
        self.order_button_layout.addWidget(self.add_product_button)
        self.order_button_layout.addWidget(self.remove_product_button)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.order_item_table)
        self.layout.addLayout(self.order_button_layout)
        self.layout.addWidget(self.product_table)

        self.total_layout = QVBoxLayout()

        self.total_label = QLabel()

        self.total_layout.addLayout(self.layout)
        self.total_layout.addWidget(self.total_label)

        self.setLayout(self.total_layout)

        self.disable_selection()

        #connections
        self.add_product_button.clicked.connect(self.add_product)
        self.remove_product_button.clicked.connect(self.remove_product)

    def add_product(self):
        selected_indexes = self.product_table.selectedIndexes()
        product_index = self.product_table.model().data(selected_indexes[0]) #get product id
        self.connection.add_product_to_order_with_details(self.order_details,product_index)
        self.order_item_table.model().select()
        self.calculate_total()

    def remove_product(self):
        pass

    def disable_selection(self):
        self.product_table.setDisabled(True)
        self.add_product_button.setDisabled(True)
        self.remove_product_button.setDisabled(True)

    def enable_selection(self):
        self.product_table.setEnabled(True)
        self.add_product_button.setEnabled(True)
        self.remove_product_button.setEnabled(True)

        self.order_model = self.connection.current_order_items(self.order_details)
        self.order_item_table.setModel(self.order_model)
        self.order_item_table.hideColumn(0)
        self.order_item_table.hideColumn(1)
        self.order_model.dataChanged.connect(self.calculate_total)

    def calculate_total(self):
        total = self.connection.current_order_total(self.order_details)
        self.total_label.setText("Total Cost: £{0:.2f}".format(total))

