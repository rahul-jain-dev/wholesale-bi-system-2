"""
tests/conftest.py
=================
Shared test fixtures and sample data for the Wholesale BI System test suite.
"""

from __future__ import annotations

import pandas as pd


def get_sample_sales_df() -> pd.DataFrame:
    """Generate a valid canonical sales DataFrame for testing."""
    return pd.DataFrame({
        "invoice_no": ["INV-001", "INV-002", "INV-003", "INV-004"],
        "date": pd.to_datetime(["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15"]),
        "customer_name": ["Sharma Kirana", "Verma Traders", "Gupta Store", "Sharma Kirana"],
        "customer_area": ["Tonk", "Uniara", "Deoli", "Tonk"],
        "product_name": ["Parle-G 100g", "Tata Salt 1kg", "Fortune Oil 1L", "Parle-G 100g"],
        "category": ["Biscuits", "Groceries", "Edible Oil", "Biscuits"],
        "company": ["Parle", "Tata", "Adani", "Parle"],
        "size_variant": ["100g", "1kg", "1L", "100g"],
        "quantity": [50.0, 20.0, 10.0, 30.0],
        "purchase_price": [8.0, 20.0, 120.0, 8.0],
        "sale_price": [10.0, 25.0, 140.0, 10.0],
        "discount_pct": [0.0, 0.0, 5.0, 0.0],
        "salesperson": ["Rahul", "Amit", "Rahul", "Amit"],
        "payment_status": ["PAID", "UNPAID", "PAID", "UNPAID"],
        "payment_due_date": pd.to_datetime(["2024-01-20", "2024-01-25", "2024-01-22", "2024-01-30"]),
    })


def get_sample_inventory_df() -> pd.DataFrame:
    """Generate a valid canonical inventory DataFrame for testing."""
    return pd.DataFrame({
        "product_name": ["Parle-G 100g", "Tata Salt 1kg", "Dead Soap 100g"],
        "category": ["Biscuits", "Groceries", "Personal Care"],
        "company": ["Parle", "Tata", "TestBrand"],
        "size_variant": ["100g", "1kg", "100g"],
        "current_stock": [120, 45, 200],
        "last_purchase_date": pd.to_datetime(["2024-01-01", "2024-01-05", "2023-08-01"]),
        "last_sale_date": pd.to_datetime(["2024-01-15", "2024-01-10", "2023-09-01"]),
        "purchase_price": [8.0, 20.0, 35.0],
        "mrp": [10.0, 25.0, 45.0],
        "reorder_level": [30, 20, 50],
    })


# Pytest fixture wrappers if pytest is active
try:
    import pytest

    @pytest.fixture
    def sample_sales() -> pd.DataFrame:
        return get_sample_sales_df()

    @pytest.fixture
    def sample_inventory() -> pd.DataFrame:
        return get_sample_inventory_df()

except ImportError:
    pass
