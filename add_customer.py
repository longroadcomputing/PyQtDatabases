from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AddCustomerWidget(QWidget):
    #customer signal to fire when details added
    customerAddedSignal = pyqtSignal()

    def __init__(self):
        super().__init__()

        #create widgets
        self.title_label = QLabel("Add New Customer")

        self.first_name_label = QLabel("First Name")
        self.last_name_label = QLabel("Last Name")
        self.house_no_label = QLabel("House Number")
        self.street_label = QLabel("Street")
        self.town_label = QLabel("Town")
        self.post_code_label = QLabel("Post Code")
        self.telephone_label = QLabel("Telephone")
        self.email_label = QLabel("E-Mail")

        self.first_name_edit = QLineEdit()
        self.last_name_edit = QLineEdit()
        self.house_no_edit = QLineEdit()
        self.street_edit = QLineEdit()
        self.town_edit = QLineEdit()
        self.post_code_edit = QLineEdit()
        self.telephone_edit = QLineEdit()
        self.email_edit = QLineEdit()

        self.clear_button = QPushButton("Clear")
        self.save_button = QPushButton("Save")

        #layouts
        self.layout = QVBoxLayout()
        self.details_layout = QGridLayout()

        self.details_layout.addWidget(self.first_name_label,0,0)
        self.details_layout.addWidget(self.first_name_edit,0,1)
        self.details_layout.addWidget(self.last_name_label,0,2)
        self.details_layout.addWidget(self.last_name_edit,0,3)

        self.details_layout.addWidget(self.house_no_label,1,0)
        self.details_layout.addWidget(self.house_no_edit,1,1)
        self.details_layout.addWidget(self.street_label,1,2)
        self.details_layout.addWidget(self.street_edit,1,3)
        self.details_layout.addWidget(self.town_label,2,0)
        self.details_layout.addWidget(self.town_edit,2,1)
        self.details_layout.addWidget(self.post_code_label,2,2)
        self.details_layout.addWidget(self.post_code_edit,2,3)
        self.details_layout.addWidget(self.telephone_label,3,0)
        self.details_layout.addWidget(self.telephone_edit,3,1)
        self.details_layout.addWidget(self.email_label,3,2)
        self.details_layout.addWidget(self.email_edit,3,3)
        self.details_layout.addWidget(self.save_button,4,1)
        self.details_layout.addWidget(self.clear_button,4,0)

        self.layout.addWidget(self.title_label)
        self.layout.addLayout(self.details_layout)
        self.setLayout(self.layout)

        #connections
        self.clear_button.clicked.connect(self.clear_details)
        self.save_button.clicked.connect(self.save_details)

    def save_details(self):
        self.customerAddedSignal.emit()

    def clear_details(self):
        self.first_name_edit.clear()
        self.last_name_edit.clear()
        self.house_no_edit.clear()
        self.street_edit.clear()
        self.town_edit.clear()
        self.post_code_edit.clear()
        self.telephone_edit.clear()
        self.email_edit.clear()

    def customer_details(self):
        details = {'first_name':self.first_name_edit.text(),
                    'last_name':self.last_name_edit.text(),
                    'house_number':self.house_no_edit.text(),
                    'street':self.street_edit.text(),
                    'town':self.town_edit.text(),
                    'post_code':self.post_code_edit.text(),
                    'telephone':self.telephone_edit.text(),
                    'email':self.email_edit.text()}
        return details