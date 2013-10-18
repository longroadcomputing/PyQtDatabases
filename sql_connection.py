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