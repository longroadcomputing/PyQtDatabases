from PyQt4.QtGui import *
from PyQt4.QtCore import *

class FindCustomerWidget(QWidget):
    """finds and displays all customers with given values"""

     #customer signal to fire when details added
    findCustomerSignal = pyqtSignal()

    def __init__(self,connection):
        super().__init__()

        self.connection = connection

        self.stacked_layout = QStackedLayout()
        self.find_customer_layout()

        self.setLayout(self.stacked_layout)


        #connections
        self.radio_button_group.buttonClicked.connect(self.change_search)
        self.find_customer_button.clicked.connect(self.find_customer)

    def find_customer_layout(self):
        #create widgets
        self.customer_number_label = QLabel("Customer Number")
        self.customer_first_name_label = QLabel("First Name")
        self.customer_last_name_label = QLabel("Last Name")
        self.customer_house_number_label = QLabel("House No")
        self.customer_postcode_label = QLabel("Postcode")

        self.customer_number_edit = QLineEdit()
        self.customer_first_name_edit = QLineEdit()
        self.customer_first_name_edit.setEnabled(False)
        self.customer_last_name_edit = QLineEdit()
        self.customer_last_name_edit.setEnabled(False)
        self.customer_house_number_edit = QLineEdit()
        self.customer_house_number_edit.setEnabled(False)
        self.customer_postcode_edit = QLineEdit()
        self.customer_postcode_edit.setEnabled(False)

        self.find_customer_button = QPushButton("Find Customer")

        self.radio_button_box = QGroupBox()
        self.radio_button_group = QButtonGroup()

        self.number_radio = QRadioButton()
        self.postcode_radio = QRadioButton()
        self.name_radio = QRadioButton()

        self.number_radio.setChecked(True)

        self.radio_button_group.addButton(self.number_radio)
        self.radio_button_group.setId(self.number_radio,0)
        self.radio_button_group.addButton(self.name_radio)
        self.radio_button_group.setId(self.name_radio,1)
        self.radio_button_group.addButton(self.postcode_radio)
        self.radio_button_group.setId(self.postcode_radio,2)


        self.customer_number_layout = QGridLayout()
        self.customer_number_layout.addWidget(self.customer_number_label,0,0)
        self.customer_number_layout.addWidget(self.customer_number_edit,0,1)

        self.customer_name_layout = QGridLayout()
        self.customer_name_layout.addWidget(self.customer_first_name_label,0,0)
        self.customer_name_layout.addWidget(self.customer_first_name_edit,0,1)
        self.customer_name_layout.addWidget(self.customer_last_name_label,1,0)
        self.customer_name_layout.addWidget(self.customer_last_name_edit,1,1)

        self.customer_postcode_layout = QGridLayout()
        self.customer_postcode_layout.addWidget(self.customer_house_number_label,0,0)
        self.customer_postcode_layout.addWidget(self.customer_house_number_edit,0,1)
        self.customer_postcode_layout.addWidget(self.customer_postcode_label,1,0)
        self.customer_postcode_layout.addWidget(self.customer_postcode_edit,1,1)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.number_radio,0,0)
        self.grid_layout.addWidget(self.name_radio,1,0)
        self.grid_layout.addWidget(self.postcode_radio,2,0)
        self.grid_layout.addLayout(self.customer_number_layout,0,1)
        self.grid_layout.addLayout(self.customer_name_layout,1,1)
        self.grid_layout.addLayout(self.customer_postcode_layout,2,1)
        self.grid_layout.addWidget(self.find_customer_button,3,1)

        self.radio_button_box.setLayout(self.grid_layout)

        self.final_layout = QVBoxLayout()
        self.final_layout.addWidget(self.radio_button_box)

        self.find_customer_widget = QWidget()
        self.find_customer_widget.setLayout(self.final_layout)
        self.stacked_layout.addWidget(self.find_customer_widget)

    def select_customer_layout(self):
        self.customer_table = QTableView()
        self.customer_table.setSelectionBehavior(1)
        self.customer_table.setModel(self.model)

        self.customer_table_layout = QVBoxLayout()
        self.customer_table_layout.addWidget(self.customer_table)

        self.select_customer_widget = QWidget()
        self.select_customer_widget.setLayout(self.customer_table_layout)
        self.stacked_layout.addWidget(self.select_customer_widget)




    def change_search(self):
        if self.radio_button_group.checkedId() == 0:
            self.customer_number_edit.setEnabled(True)
            self.customer_first_name_edit.setEnabled(False)
            self.customer_last_name_edit.setEnabled(False)
            self.customer_house_number_edit.setEnabled(False)
            self.customer_postcode_edit.setEnabled(False)
        elif self.radio_button_group.checkedId() == 1:
            self.customer_number_edit.setEnabled(False)
            self.customer_first_name_edit.setEnabled(True)
            self.customer_last_name_edit.setEnabled(True)
            self.customer_house_number_edit.setEnabled(False)
            self.customer_postcode_edit.setEnabled(False)
        elif self.radio_button_group.checkedId() == 2:
            self.customer_number_edit.setEnabled(False)
            self.customer_first_name_edit.setEnabled(False)
            self.customer_last_name_edit.setEnabled(False)
            self.customer_house_number_edit.setEnabled(True)
            self.customer_postcode_edit.setEnabled(True)

    def find_customer(self):
        if self.radio_button_group.checkedId() == 0:
            self.search_values = (self.customer_number_edit.text(),)
            self.model = self.connection.find_existing_customers_by_number(self.search_values)
        elif self.radio_button_group.checkedId() == 1:
            self.search_values = (self.customer_first_name_edit.text(),self.customer_last_name_edit.text())
            self.model = self.connection.find_existing_customers_by_name(self.search_values)
        elif self.radio_button_group.checkedId() == 2:
            self.search_values = (self.customer_house_number_edit.text(),self.customer_postcode_edit.text())
            self.model = self.connection.find_existing_customers_by_postcode(self.search_values)
        self.select_customer_layout()
        self.stacked_layout.setCurrentIndex(1)


