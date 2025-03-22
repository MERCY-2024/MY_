from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGridLayout


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 300, 400)

        # Main widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Layouts
        self.layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        # Entry field
        self.entry = QLineEdit()
        self.entry.setReadOnly(True)
        self.entry.setFixedHeight(50)
        self.layout.addWidget(self.entry)

        # Buttons
        self.buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        # Add buttons to the grid layout
        for (text, row, col) in self.buttons:
            button = QPushButton(text)
            button.setFixedSize(60, 60)
            self.grid_layout.addWidget(button, row, col)
            button.clicked.connect(lambda checked, t=text: self.on_button_click(t))

        self.layout.addLayout(self.grid_layout)
        self.central_widget.setLayout(self.layout)

    def on_button_click(self, text):
        if text == "C":
            self.entry.clear()
        elif text == "=":
            try:
                result = eval(self.entry.text())
                self.entry.setText(str(result))
            except Exception:
                self.entry.setText("Error")
        else:
            self.entry.setText(self.entry.text() + text)


if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()