"""
engine/__init__.py
==================
Engine package for the Wholesale BI System.

Exposes the primary public API from all seven engine modules so that
Streamlit pages and FastAPI routes can import with a single line:

    from engine import standardize_sales, detect_dead_stock, forecast_demand

Modules:
    data_cleaner     — Canonical schema standardizer
    analytics        — Business analytics (dead stock, payments, margins)
    scoring          — Urgency and risk scoring formulas
    forecasting      — Facebook Prophet demand forecasting
    segmentation     — RFM + K-Means customer segmentation
    anomaly_detector — Isolation Forest anomaly detection
    recommender      — Recommendation engine orchestrator

Author: Wholesale BI System
Python: 3.12
"""

# Data cleaning & validation
# Business analytics
from engine.analytics import (
    area_sales_ranking,
    calculate_margins,
    category_month_heatmap,
    detect_dead_stock,
    get_outstanding_payments,
    monthly_revenue_trend,
)

# Anomaly detection
from engine.anomaly_detector import (
    detect_anomalies,
    flag_discount_anomalies,
    flag_salesperson_anomalies,
    get_anomaly_summary,
)
from engine.data_cleaner import (
    clean_dataframe,
    load_and_standardize,
    standardize_customers,
    standardize_inventory,
    standardize_purchases,
    standardize_sales,
    validate_csv_upload,
)

# Demand forecasting
from engine.forecasting import (
    INDIAN_FESTIVALS,
    detect_declining_products,
    detect_demand_spikes,
    forecast_demand,
    get_days_coverage,
)

# Recommendation engine
from engine.recommender import (
    Recommendation,
    ceo_morning_briefing,
    filter_by_category,
    generate_recommendations,
    recommendations_to_dataframe,
)

# Scoring formulas
from engine.scoring import (
    compute_amount_factor,
    compute_days_factor,
    compute_trend_factor,
    dead_stock_score,
    normalize_factor,
    risk_score_payment,
    score_payment_dataframe,
    urgency_score,
)

# Customer segmentation
from engine.segmentation import (
    cohort_retention,
    compute_rfm,
    get_segment_recommendations,
    segment_customers,
)

__all__ = [
    # data_cleaner
    "standardize_sales",
    "standardize_inventory",
    "standardize_customers",
    "standardize_purchases",
    "clean_dataframe",
    "validate_csv_upload",
    "load_and_standardize",
    # analytics
    "detect_dead_stock",
    "get_outstanding_payments",
    "calculate_margins",
    "area_sales_ranking",
    "monthly_revenue_trend",
    "category_month_heatmap",
    # scoring
    "urgency_score",
    "normalize_factor",
    "risk_score_payment",
    "dead_stock_score",
    "compute_days_factor",
    "compute_amount_factor",
    "compute_trend_factor",
    "score_payment_dataframe",
    # forecasting
    "forecast_demand",
    "detect_demand_spikes",
    "detect_declining_products",
    "get_days_coverage",
    "INDIAN_FESTIVALS",
    # segmentation
    "compute_rfm",
    "segment_customers",
    "get_segment_recommendations",
    "cohort_retention",
    # anomaly_detector
    "detect_anomalies",
    "flag_discount_anomalies",
    "flag_salesperson_anomalies",
    "get_anomaly_summary",
    # recommender
    "Recommendation",
    "generate_recommendations",
    "ceo_morning_briefing",
    "filter_by_category",
    "recommendations_to_dataframe",
]
