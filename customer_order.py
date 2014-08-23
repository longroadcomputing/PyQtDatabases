try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *

from find_customer import *
from create_order import *

class CustomerOrderWidget(QWidget):
    """creates a form allowing you to create an order for a particular customer"""
    def __init__(self,connection):
        super().__init__()
        self.connection = connection

        self.customer = FindCustomerWidget(self.connection)
        self.order = OrderWidget(self.connection)
        self.confirm_order = QPushButton("Confirm Order")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.customer)
        self.layout.addWidget(self.order)
        self.layout.addWidget(self.confirm_order)

        self.setLayout(self.layout)

        #connections
        self.customer.createdNewOrder.connect(self.new_order)

    def new_order(self):
        order_details = self.customer.most_recent_created_order_details()
        self.order.order_details = order_details
        self.order.enable_selection()

