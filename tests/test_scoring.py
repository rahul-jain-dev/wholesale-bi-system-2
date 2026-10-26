"""
tests/test_scoring.py
=====================
Unit tests for the scoring module (engine/scoring.py).
Tests core urgency formulas, boundary handling, and normalization logic.
"""

import unittest
from engine.scoring import (
    URGENCY_WEIGHTS,
    compute_amount_factor,
    compute_days_factor,
    normalize_factor,
    urgency_score,
)


class TestScoring(unittest.TestCase):
    """Test suite for deterministic scoring algorithms."""

    def test_urgency_weights_sum_to_one(self):
        """Ensure all component weights sum to 1.0."""
        total_weight = sum(URGENCY_WEIGHTS.values())
        self.assertAlmostEqual(total_weight, 1.0, places=5)

    def test_urgency_score_boundaries(self):
        """Urgency score should clip between 0.0 and 1.0."""
        self.assertEqual(urgency_score(0.0, 0.0, 0.0), 0.0)
        self.assertEqual(urgency_score(1.0, 1.0, 1.0), 1.0)
        # Check boundary overflow clipping
        self.assertEqual(urgency_score(2.0, 3.0, 1.5), 1.0)
        self.assertEqual(urgency_score(-1.0, -0.5, 0.0), 0.0)

    def test_urgency_score_midpoint(self):
        """Check expected intermediate calculation with known weights."""
        score = urgency_score(0.5, 0.5, 0.5)
        self.assertAlmostEqual(score, 0.5, places=4)

    def test_normalize_factor(self):
        """Test standard min-max normalization."""
        self.assertEqual(normalize_factor(50.0, 0.0, 100.0), 0.5)
        self.assertEqual(normalize_factor(0.0, 0.0, 100.0), 0.0)
        self.assertEqual(normalize_factor(100.0, 0.0, 100.0), 1.0)

    def test_compute_days_factor(self):
        """Days factor should scale monotonically with overdue days."""
        factor_30 = compute_days_factor(30)
        factor_60 = compute_days_factor(60)
        factor_90 = compute_days_factor(90)
        self.assertTrue(0.0 <= factor_30 < factor_60 < factor_90 <= 1.0)

    def test_compute_amount_factor(self):
        """Amount factor should be log-normalized between 0.0 and 1.0."""
        factor_small = compute_amount_factor(1000.0, 100000.0)
        factor_large = compute_amount_factor(50000.0, 100000.0)
        self.assertTrue(0.0 <= factor_small < factor_large <= 1.0)
        # Edge case: amount is 0 or negative
        self.assertEqual(compute_amount_factor(0.0, 100000.0), 0.0)


if __name__ == "__main__":
    unittest.main()
