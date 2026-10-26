"""
tests/test_data_cleaner.py
==========================
Unit tests for data cleaning and schema standardizer (engine/data_cleaner.py).
"""

import unittest
import pandas as pd
from engine.data_cleaner import (
    clean_dataframe,
    standardize_sales,
    SALES_ALIASES,
)


class TestDataCleaner(unittest.TestCase):
    """Test suite for data cleaning and canonical mapping."""

    def test_clean_dataframe_strips_column_whitespace(self):
        """clean_dataframe should strip leading and trailing whitespace from column names."""
        df = pd.DataFrame({"  col_a  ": [1, 2], " col_b": [3, 4]})
        cleaned = clean_dataframe(df)
        self.assertIn("col_a", cleaned.columns)
        self.assertIn("col_b", cleaned.columns)

    def test_sales_aliases_contains_standard_keys(self):
        """Verify that core ERP aliases exist in the lookup map."""
        self.assertIn("bill no.", SALES_ALIASES)  # Kuber ERP variant
        self.assertIn("voucher_no", SALES_ALIASES)  # Tally variant
        self.assertIn("party name", SALES_ALIASES)

    def test_standardize_sales_canonical_columns(self):
        """standardize_sales must produce canonical output schema."""
        raw_df = pd.DataFrame({
            "bill no.": ["B101", "B102"],
            "bill date": ["2024-01-01", "2024-01-02"],
            "party name": ["Kirana Store A", "Kirana Store B"],
            "place": ["Tonk", "Uniara"],
            "item_name": ["Soap 100g", "Oil 1L"],
            "item_category": ["Personal Care", "Edible Oil"],
            "company": ["BrandA", "BrandB"],
            "variant": ["100g", "1L"],
            "qty": [10, 5],
            "cost_price": [20.0, 120.0],
            "rate": [25.0, 150.0],
            "discount": [0.0, 2.0],
            "salesman": ["Rahul", "Amit"],
            "status": ["PAID", "UNPAID"],
            "due_date": ["2024-01-10", "2024-01-15"],
        })
        std_df = standardize_sales(raw_df)
        self.assertIn("invoice_no", std_df.columns)
        self.assertIn("customer_name", std_df.columns)
        self.assertIn("customer_area", std_df.columns)
        self.assertIn("product_name", std_df.columns)
        self.assertIn("quantity", std_df.columns)
        self.assertIn("sale_price", std_df.columns)
        self.assertIn("purchase_price", std_df.columns)


if __name__ == "__main__":
    unittest.main()
