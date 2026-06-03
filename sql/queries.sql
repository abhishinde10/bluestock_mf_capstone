-- Top 5 Funds by AUM
SELECT scheme_name,aum_crore
FROM 07_scheme_performance_clean
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM 02_nav_history_clean;

-- Transactions by State
SELECT state,COUNT(*)
FROM 08_investor_transactions_clean
GROUP BY state;

-- Expense Ratio <1
SELECT scheme_name
FROM 07_scheme_performance_clean
WHERE expense_ratio_pct <1;

-- Top Fund Houses
SELECT fund_house,COUNT(*)
FROM 01_fund_master
GROUP BY fund_house;

-- Additional Queries
SELECT category,COUNT(*) FROM 01_fund_master GROUP BY category;

SELECT risk_category,COUNT(*) FROM 01_fund_master GROUP BY risk_category;

SELECT transaction_type,COUNT(*) FROM 08_investor_transactions_clean GROUP BY transaction_type;

SELECT AVG(return_1yr_pct) FROM 07_scheme_performance_clean;

SELECT MAX(nav) FROM 02_nav_history_clean;