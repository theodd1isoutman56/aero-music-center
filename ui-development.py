import sys 
import os 
from PySide6.QtWidgets import (
    QApplication, QMainWindow,QWidget,QVBoxLayout,QLabel,QPushButton,QLineEdit,QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
class AEROMUSICCENTRE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFilePath('AERO MUSIC CENTER')
        screen = QApplication.primaryScreen().availableGeometry()
        width = int(screen.width()*0.9)
        height = int(screen.height()*0.9)
        self.resize(width,height)
        central_widget = QWidget()
        central_widget.setObjectName('MainWindow')
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        layout.setContentsMargins(40,30,40,40)

        title = QLabel("AERO MUSIC CENTER")
        title.setFont(QFont("Segoe UI", 30, QFont.Bold))
        title.setStyleSheet("color: white;")
        title.setAlignment(Qt.AlignCenter)
        title_below = QLabel("VERSION : NOSTALGIA :]")
        title_below.setFont(QFont("Segoe UI", 16)) 
        title_below.setStyleSheet("color: rgb(99, 196, 142); background: transparent;")    
        title_below.setAlignment(Qt.AlignCenter)

        main_box = QFrame()
        main_box.setFixedSize(600,400)
        main_box.setStyleSheet('''
            QFrame {
            border: 2px solid white;
            border-radius: 10px;
            background-color: rgba(255,255,255,0.15)
            }
''')
        box_layout = QVBoxLayout(main_box) 
        box_layout.setAlignment(Qt.AlignCenter)
        box_layout.setContentsMargins(20,20,20,20)

        heading = QLabel("Welcome to AERO MUSIC CENTER")    
        heading.setFont(QFont('Segoe UI', 18 , QFont.Bold))
        heading.setStyleSheet("color: white; border:none ;background : transparent;")
        box_layout.addWidget(heading)
        
        layout.addWidget(title)
        layout.addWidget(title_below)
        layout.addSpacing(20)
        layout.addWidget(main_box)

        self.setStyleSheet("""
            QWidget#MainWindow {
                background-color: rgb(74, 201, 227);
                border-image: url(fruitiger1.webp) 0 0 0 0 stretch stretch;
            }
        """)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AEROMUSICCENTRE()
    window.show()
    sys.exit(app.exec())