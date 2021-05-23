import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QListWidgetItem, QPushButton, QWidget

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.height1 = QLabel('키')
        self.weight1 = QLabel('몸무게')

        grid.addWidget(self.height1, 0,0)
        grid.addWidget(self.weight1, 1,0)

        self.height2 = QLineEdit()
        self.weight2 = QLineEdit()
        self.result = QLineEdit()
        

        grid.addWidget(self.height2,0,1)
        grid.addWidget(self.weight2,1,1)
        grid.addWidget(self.result, 4,1)

        self.mybutton = QPushButton('BMI 계산', self)
        self.mybutton.clicked.connect(self.bmi)

        grid.addWidget(self.mybutton, 3,1)

        self.setWindowTitle("제목부분")
        self.setGeometry(300,300,400,100)
        self.show()

    def bmi(self):
        self.bmi_result = int(self.weight2.text()) / (int(self.height2.text()) * int(self.height2.text()) / 10000)
        self.weight2.setText("")
        self.height2.setText("")

        if(self.bmi_result < 18.5):
            self.result.setText("저체중")

        elif(self.bmi_result < 23):
            self.result.setText("정상"),

        elif(self.bmi_result < 25):
            self.result.setText("과체중")
        
        elif(self.bmi_result < 30):
            self.result.setText("비만")

        else:
            self.result.setText("고도 비만")



        
    

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())