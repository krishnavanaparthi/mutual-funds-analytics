-- 1 Top 5 Funds by AUM

SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM performance
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;


-- 2 Average NAV Per Fund

SELECT
amfi_code,
AVG(nav) AS avg_nav
FROM nav_history
GROUP BY amfi_code;


-- 3 Transactions By State

SELECT
state,
COUNT(*) AS total_transactions
FROM transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 4 Funds With Expense Ratio < 1%

SELECT
scheme_name,
expense_ratio_pct
FROM performance
WHERE expense_ratio_pct < 1;


-- 5 Average Return By Category

SELECT
category,
AVG(return_3yr_pct) AS avg_return
FROM performance
GROUP BY category
ORDER BY avg_return DESC;

-- 6 Top 5 Categories by Net Inflows

SELECT
category,
SUM(net_inflow_crore) AS total_inflow
FROM category_inflows
GROUP BY category
ORDER BY total_inflow DESC
LIMIT 5;


-- 7 Monthly SIP Growth

SELECT
month,
sip_inflow_crore,
yoy_growth_pct
FROM sip_inflows
ORDER BY month;


-- 8 Top States by Transaction Amount

SELECT
state,
SUM(amount_inr) AS total_amount
FROM transactions
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;


-- 9 Highest Return Funds

SELECT
scheme_name,
return_5yr_pct
FROM performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- 10 Most Popular Transaction Types

SELECT
transaction_type,
COUNT(*) AS total_transactions
FROM transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;