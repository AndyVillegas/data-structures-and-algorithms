import unittest
import os
import sys

# Obtén la ruta absoluta de la carpeta que contiene el archivo EXCERCISE.py
path = os.path.abspath(os.path.join('10-Recursive Binary Search Trees'))

# Agrega la ruta a la lista de rutas de importación de Python
sys.path.append(path)

# Importa la clase BinarySearchTree desde el archivo EXCERCISE
from BinarySearchTree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()

    def test_insert(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(8)
        self.assertTrue(self.tree.contains(5))
        self.assertTrue(self.tree.contains(3))
        self.assertTrue(self.tree.contains(7))
        self.assertTrue(self.tree.contains(2))
        self.assertTrue(self.tree.contains(4))
        self.assertTrue(self.tree.contains(6))
        self.assertTrue(self.tree.contains(8))
        self.assertFalse(self.tree.contains(1))
        self.assertFalse(self.tree.contains(9))
    
    def test_delete(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(8)
        self.tree.delete_node(5)
        self.assertFalse(self.tree.contains(5))
        self.assertTrue(self.tree.contains(3))
        self.assertTrue(self.tree.contains(7))
        self.assertTrue(self.tree.contains(2))
        self.assertTrue(self.tree.contains(4))
        self.assertTrue(self.tree.contains(6))
        self.assertTrue(self.tree.contains(8))

    def test_min_value(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(8)
        self.assertEqual(self.tree.min_value(self.tree.root), 2)

    def test_empty_tree(self):
        self.assertFalse(self.tree.contains(5))
        self.assertIsNone(self.tree.min_value(self.tree.root))

if __name__ == '__main__':
    unittest.main()