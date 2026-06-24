-- =====================================================
-- DIMENSION TABLES
-- =====================================================

CREATE TABLE IF NOT EXISTS dim_fund (

    fund_key INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER UNIQUE,

    scheme_name TEXT,

    fund_house TEXT,

    category TEXT,

    risk_grade TEXT
);

CREATE TABLE IF NOT EXISTS dim_date (

    date_key INTEGER PRIMARY KEY AUTOINCREMENT,

    full_date DATE,

    year INTEGER,

    quarter INTEGER,

    month INTEGER,

    day INTEGER
);

-- =====================================================
-- FACT NAV
-- =====================================================

CREATE TABLE IF NOT EXISTS fact_nav (

    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_key INTEGER,

    date_key INTEGER,

    nav REAL,

    FOREIGN KEY (fund_key)
        REFERENCES dim_fund(fund_key),

    FOREIGN KEY (date_key)
        REFERENCES dim_date(date_key)
);

-- =====================================================
-- FACT TRANSACTIONS
-- =====================================================

CREATE TABLE IF NOT EXISTS fact_transactions (

    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_key INTEGER,

    date_key INTEGER,

    investor_id TEXT,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    kyc_status TEXT,

    FOREIGN KEY (fund_key)
        REFERENCES dim_fund(fund_key),

    FOREIGN KEY (date_key)
        REFERENCES dim_date(date_key)
);

-- =====================================================
-- FACT PERFORMANCE
-- =====================================================

CREATE TABLE IF NOT EXISTS fact_performance (

    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_key INTEGER,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    alpha REAL,

    beta REAL,

    sharpe_ratio REAL,

    expense_ratio_pct REAL,

    aum_crore REAL,

    FOREIGN KEY (fund_key)
        REFERENCES dim_fund(fund_key)
);

-- =====================================================
-- FACT AUM
-- =====================================================

CREATE TABLE IF NOT EXISTS fact_aum (

    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date_key INTEGER,

    fund_house TEXT,

    aum_crore REAL,

    num_schemes INTEGER,

    FOREIGN KEY (date_key)
        REFERENCES dim_date(date_key)
);