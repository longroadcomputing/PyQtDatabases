import datetime

from PyQt4.QtSql import *

class SQLConnection:
    def __init__(self,path):
        self.path = path
        self.db = None

    def open_database(self):
        if self.db:
            self.close_database()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)
        ok = self.db.open()
        return ok

    def close_database(self):
        """closes the datbase that is currently open"""
        #del self.model
        #del self.query_result
        self.db.close()
        #del self.db
        QSqlDatabase.removeDatabase("conn")

    def closeEvent(self, event):
        """closes the database if a close event occurs -
        such as close window/quit application"""
        self.close_database()

    #customer queries
    def add_new_customer(self,details):
        query = QSqlQuery()
        query.prepare("""INSERT INTO customer (FirstName,LastName,Street,Town,PostCode,TelephoneNumber) VALUES
                        (?,?,?,?,?,?)""")
        query.addBindValue(details['first_name'])
        query.addBindValue(details['last_name'])
        query.addBindValue(details['street'])
        query.addBindValue(details['town'])
        query.addBindValue(details['post_code'])
        query.addBindValue(details['telephone'])
        query.exec_()

    def find_existing_customers_by_number(self,values):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.prepare("""SELECT * FROM customer WHERE CustomerID = ?""")
        query.addBindValue(values[0])
        query.exec_()
        model.setQuery(query)
        return model

    def find_existing_customers_by_name(self,values):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.prepare("""SELECT * FROM customer WHERE FirstName = ? and LastName = ?""")
        query.addBindValue(values[0])
        query.addBindValue(values[1])
        query.exec_()
        model.setQuery(query)
        return model

    def find_existing_customers_by_postcode(self,values):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.prepare("""SELECT * FROM customer WHERE PostCode = ?""")
        query.addBindValue(values[1])
        query.exec_()
        model.setQuery(query)
        return model

    def current_products(self):
        model = QSqlRelationalTableModel()
        print(self.db.tables())
        model.setTable(self.db.tables()[2])
        model.setRelation(3,QSqlRelation("ProductType","ProductTypeID","Description"))
        model.select()
        return model

    def create_new_order_for_customer(self,customer_id):
        query = QSqlQuery()
        query.prepare("""INSERT INTO CustomerOrder(Date,Time,CustomerID) values (?,?,?)""")
        today = datetime.datetime.today()
        date = today.strftime("%Y-%m-%d")
        time = today.strftime("%H:%M:%S")
        query.addBindValue(date)
        query.addBindValue(time)
        query.addBindValue(customer_id)
        query.exec_()
        return date, time

    def current_order_number(self,order_details):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM CustomerOrder WHERE CustomerID = ? AND Date = ? AND Time = ?""")
        query.addBindValue(order_details['customer'])
        query.addBindValue(order_details['date'])
        query.addBindValue(order_details['time'])
        query.exec_()
        query.first()
        order = query.record()
        order_id = order.value("OrderID")
        return order_id

    def add_product_to_order_with_details(self,order_details,product_id):
        order_id = self.current_order_number(order_details)
        query = QSqlQuery()
        query.prepare("""INSERT INTO OrderItem(OrderID,ProductID,Quantity) values(?,?,1)""")
        query.addBindValue(order_id)
        query.addBindValue(product_id)
        query.exec_()

    def current_order_items(self,order_details):
        order_id = self.current_order_number(order_details)
        model = QSqlRelationalTableModel()
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.setTable("OrderItem")
        model.setFilter("OrderID = {0}".format(order_id))
        model.setRelation(2,QSqlRelation("Product","ProductID","Name"))
        model.select()
        return model

    def current_order_total(self,order_details):
        order_id = self.current_order_number(order_details)
        query = QSqlQuery()
        query.prepare("""SELECT SUM(Product.Price * OrderItem.Quantity) AS Total
                         FROM Product, OrderItem
                         WHERE OrderItem.OrderID = ?
                         AND OrderItem.ProductID = Product.ProductID""")
        query.addBindValue(order_id)
        query.exec_()
        query.first()
        total = query.value(0)
        return total

