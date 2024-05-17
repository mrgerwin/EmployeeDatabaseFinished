import sqlite3

class Database:
    def __init__(self, fn):
        self.db = sqlite3.connect(fn)
        self.conn = self.db.cursor()
        self.id = 1
        
        
    def createTable(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE(ID INTEGER PRIMARY KEY AUTOINCREMENT, PICFILE TEXT NOT NULL, FIRSTNAME TEXT NOT NULL, LASTNAME TEXT NOT NULL, EMPLOYEENUM INT NOT NULL, SALARY REAL NOT NULL, JOB TEXT NOT NULL, YEARS INT NOT NULL);''')
        
    def addEmployee(self, pf, fn, ln, en, sal, job, yrs):
        sql = 'INSERT INTO EMPLOYEE(PICFILE, FIRSTNAME, LASTNAME, EMPLOYEENUM, SALARY, JOB, YEARS) VALUES (?,?,?,?,?,?,?);'
        print(sql)
        print((pf, fn, ln, en, sal, job, yrs))
        self.conn.execute(sql, (pf, fn, ln, en, sal, job, yrs))
        self.db.commit()
    
    def removeEmployee(self, en):
        sql = 'DELETE FROM EMPLOYEE WHERE EMPLOYEENUM = "' + str(en) + '";'
        self.conn.execute(sql)
        self.db.commit()
    
    def loadDB(self):
        sql = 'SELECT * FROM EMPLOYEE;'
        self.conn.execute(sql)
        data = self.conn.fetchall()
        return data
    
    def close(self):
        self.conn.close()
        
filename = "./employee.db"

db = Database(filename)

db.createTable()
#db.addEmployee('test2', 'test2L', 1002, 100000, 'testJob2', 21)