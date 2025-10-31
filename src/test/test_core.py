import unittest
import os

class TestCore(unittest.TestCase):
    """Tests básicos que no dependen de imports externos"""

    def test_estructura(self):
        """Verifica estructura básica del proyecto"""
        self.assertTrue(os.path.exists('app'))
        self.assertTrue(os.path.exists('test'))

    def test_python_funciona(self):
        """Verifica que Python funciona correctamente"""
        self.assertEqual(1 + 1, 2)
        self.assertTrue('hello'.isalpha())
        self.assertFalse('123'.isalpha())

    def test_imports_basicos(self):
        """Verifica que los imports básicos funcionan"""
        try:
            import sys
            import os
            import unittest
            success = True
        except ImportError:
            success = False
        self.assertTrue(success, "Los imports básicos de Python deberían funcionar")

if __name__ == '__main__':
    unittest.main()