import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt

class AndroidUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simple Android UI")
        self.setGeometry(100, 100, 360, 640)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Tulis teks di sini")
        layout.addWidget(self.text_input)


        self.button = QPushButton("Submit", self)
        layout.addWidget(self.button, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AndroidUI()
    window.show()
    sys.exit(app.exec_())