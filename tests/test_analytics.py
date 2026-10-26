"""
tests/test_analytics.py
=======================
Unit tests for business analytics (engine/analytics.py).
"""

import unittest
from engine.analytics import (
    area_sales_ranking,
    calculate_margins,
    detect_dead_stock,
)
from tests.conftest import get_sample_inventory_df, get_sample_sales_df


class TestAnalytics(unittest.TestCase):
    """Test suite for core analytics metrics."""

    def setUp(self):
        self.sales_df = get_sample_sales_df()
        self.inventory_df = get_sample_inventory_df()

    def test_calculate_margins_generates_margin_columns(self):
        """calculate_margins should compute aggregated margins and profits."""
        df_with_margins = calculate_margins(self.sales_df)
        self.assertIn("total_profit", df_with_margins.columns)
        self.assertIn("avg_real_margin_pct", df_with_margins.columns)
        self.assertIn("total_revenue", df_with_margins.columns)
        self.assertGreater(len(df_with_margins), 0)

    def test_area_sales_ranking_ordering(self):
        """area_sales_ranking should return areas ordered by total revenue."""
        area_rank = area_sales_ranking(self.sales_df)
        self.assertIn("customer_area", area_rank.columns)
        self.assertIn("total_revenue", area_rank.columns)
        # Verify descending order
        revenues = area_rank["total_revenue"].tolist()
        self.assertEqual(revenues, sorted(revenues, reverse=True))

    def test_detect_dead_stock_identifies_dead_items(self):
        """detect_dead_stock should identify items unsold past threshold."""
        dead_stock = detect_dead_stock(self.inventory_df)
        self.assertIn("days_unsold", dead_stock.columns)
        self.assertIn("stock_status", dead_stock.columns)
        self.assertIn("capital_blocked", dead_stock.columns)
        self.assertGreater(len(dead_stock), 0)


if __name__ == "__main__":
    unittest.main()
