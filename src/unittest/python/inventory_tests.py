import unittest
from inventory import VaccineManager
from validator import check_temp

class TestBioGuard(unittest.TestCase):
    def setUp(self):
        self.vm = VaccineManager()

    def test_stock_incremental(self):
        self.vm.add_doses("Moderna", 100)
        self.vm.add_doses("Moderna", 50)
        self.assertEqual(self.vm.stock["Moderna"], 150)

    def test_exception_negative_qty(self):
        with self.assertRaises(ValueError):
            self.vm.add_doses("Error_Vial", -1)

    def test_range_temperature(self):
        # Nuevo rango legal: 2 a 8 grados
        self.assertTrue(check_temp(4))   
        self.assertFalse(check_temp(0))