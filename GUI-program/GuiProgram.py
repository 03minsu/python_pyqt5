import sys
import requests
import pymysql
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QPushButton, QWidget


conn = pymysql.connect(host='localhost', user='root', password='123456', db='study_db', charset='utf8')
curs = conn.cursor()

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        
        label = QLabel(self)
        label.setText("이름 : ")
        grid.addWidget(label,0,0)
        
        self.qle = QLineEdit(self)
        grid.addWidget(self.qle,0,1)
        
        label2 = QLabel(self)
        label2.setText("키 : ")
        grid.addWidget(label2,1,0)
        
        self.qle2 = QLineEdit(self)
        grid.addWidget(self.qle2,1,1)
        
        label3 = QLabel(self)
        label3.setText("몸무게 : ")
        grid.addWidget(label3,2,0)

        self.qle3 = QLineEdit(self)
        grid.addWidget(self.qle3,2,1)

        btn = QPushButton(self)
        btn.setText("데이터 삽입")
        grid.addWidget(btn,3,1)
        btn.clicked.connect(self.insert)

        btn1 = QPushButton(self)
        btn1.setText("삭제")  
        grid.addWidget(btn1,3,2)
        btn1.clicked.connect(self.delete) 

        self.setWindowTitle('사용자 정보 입력')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()
    
    def delete(self):
        self.qle.setText("")
        self.qle2.setText("")
        self.qle3.setText("")
    def insert(self):
        name = self.qle.text()
        height = int(self.qle2.text())
        weight = int(self.qle3.text())

        curs.execute("use study_db;")
        sql = "insert into user_info (name,height,weight) values (%s,%s,%s)"
        curs.execute(sql,(name,height,weight))
        
        conn.commit()   
        conn.close()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())