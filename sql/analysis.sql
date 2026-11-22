
-- 1. Total number of customers
SELECT
    COUNT(*) AS total_customers
FROM credit_customers;


-- 2. Number of customers who defaulted
SELECT
    COUNT(*) AS defaulted_customers
FROM credit_customers
WHERE default_next_month = 1;


-- 3. Overall default rate
SELECT
    ROUND(AVG(default_next_month) * 100, 2) AS default_rate_percentage
FROM credit_customers;


-- 4. Default rate by credit limit band
SELECT
    credit_limit_band,
    COUNT(*) AS total_customers,
    ROUND(AVG(default_next_month) * 100, 2) AS default_rate
FROM credit_customers
GROUP BY credit_limit_band
ORDER BY default_rate DESC;


-- 5. Default rate by age group
SELECT
    age_group,
    COUNT(*) AS total_customers,
    ROUND(AVG(default_next_month) * 100, 2) AS default_rate
FROM credit_customers
GROUP BY age_group
ORDER BY default_rate DESC;
