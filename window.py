from UI.main_window import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow
from arbol import Tree, binary_search, inorder
from graph import tree_g
from PyQt6.QtGui import QPixmap, QIcon


class Student:
    def __init__(self, id, nombre, telefono) -> None:
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self) -> str:
        return f"{self.id} - {self.nombre} - {self.telefono}"
    
    def __repr__(self) -> str:
        return f"{self.id}"
    
    def __lt__(self, other):
        return self.id < other.id
    
    def __gt__(self, other):
        return self.id > other.id
    
    def __eq__(self, other):
        return self.id == other.id
    
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, tree:Tree):
        super(Window, self).__init__(None)
        self.setupUi(self)
        self.tree = tree

        self.btn_buscar.setEnabled(True)

        self.btn_guardar.clicked.connect(self.guardar_estudiante)
        self.btn_buscar.clicked.connect(self.buscar_estudiante)

        self.btn_guardar.clicked.connect(self.update_graph)
        self.btn_eliminar.clicked.connect(self.update_graph)
    
    def guardar_estudiante(self):
        id = int(self.spn_id.value())
        nombre = self.txt_nombre.text()
        tel = self.txt_telefono.text()

        new = Student(id, nombre, tel)
        self.tree.insert(new, new.id)

    def update_graph(self):
        tree_g(self.tree.root)
        pixmap = QPixmap("img/btree.png")
        self.btn_arbol.setIcon(QIcon(pixmap))
        self.btn_arbol.setIconSize(pixmap.rect().size())

    def buscar_estudiante(self):
        id = self.spn_id.value()
        if binary_search(Student(id, None, None), self.tree.root, id):
            self.txt_nombre.setText("Estudiante en el arbol")
        else:
            self.txt_nombre.setText("Estudiante no en el arbol")