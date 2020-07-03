import unittest
import pandas as pd

import exercise

# %% Parameter declaration
supplier_lists = []
supplier_lists.append(pd.read_csv("preprocessed_files/suppliernames.csv"))
supplier_lists.append(pd.read_csv("preprocessed_files/fake_suppliers.csv"))
invoice = pd.read_json("preprocessed_files/invoice.jsonl", lines=True)

# %% Tests
class TestSupplierFromInvoice(unittest.TestCase):
    
    def test_get_supplier_from_invoice(self):
        expected_value = "Demo Company"
        for suppliers in supplier_lists:
            value = exercise.get_supplier_from_invoice(invoice, suppliers)
            with self.subTest():
                self.assertEqual(expected_value, value)
        
if __name__ == '__main__':
    unittest.main()