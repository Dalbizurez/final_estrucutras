from arbol import Tree
from window import Window
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    tree = Tree()
    app = QApplication([])
    main = Window(tree)
    main.show()
    app.exec()
    