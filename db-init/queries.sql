-- drill down questions to answer with SQL queries
-- I’m curious about the average amount I spend at each grocery store and how often I go there.
SELECT description, 
       ROUND(AVG(amount), 2) AS avg_amount, 
       COUNT(description) AS visit_count
FROM transactions 
WHERE category = 'Grocery'
GROUP BY description
ORDER BY avg_amount DESC;

-- What’s the most I’ve ever spent in one trip to a grocery store?
SELECT description, 
       ROUND(MAX(amount), 2) AS max_amount
FROM transactions 
WHERE category = 'Grocery'
GROUP BY description
ORDER BY max_amount DESC;

-- I wanted to see and figure out the total I’ve spent at each grocery store.
SELECT description, 
       ROUND(SUM(amount), 2) AS total_amount
FROM transactions 
WHERE category = 'Grocery'
GROUP BY description
ORDER BY total_amount DESC;

-- Which days am I most likely to go grocery shopping, is there a pattern?
SELECT d.day_name, 
       COUNT(t.description) AS frequency
FROM transactions t
JOIN dates d ON t.date_id = d.date_id
WHERE t.category = 'Grocery'
GROUP BY d.day_name
ORDER BY frequency DESC;

-- What’s the percentage difference between my spending on dining out and groceries?
SELECT category, 
       ROUND(SUM(amount), 2) AS total_amount, 
       ROUND(SUM(amount) * 100.0 / 
       (SELECT SUM(amount) 
        FROM transactions 
        WHERE category IN ('Grocery', 'Dining')), 2) AS percentage
FROM transactions
WHERE category IN ('Dining', 'Grocery')
GROUP BY category;

-- Do I spend any on holidays?
SELECT d.is_holiday, 
       ROUND(SUM(t.amount), 2) AS total_holiday_spend
FROM transactions t
JOIN dates d ON t.date_id = d.date_id
WHERE d.is_holiday = 'Holiday'
GROUP BY d.is_holiday;

-- What’s my favorite dining place?
SELECT description, 
       COUNT(description) AS frequency
FROM transactions
WHERE category = 'Dining'
GROUP BY description
ORDER BY frequency DESC;

-- Which category got the the most “High Spend” counts, in other word, that I spent more than $100?
WITH spend_level AS (
    SELECT t.description,
           t.category, 
           t.amount,
           CASE
               WHEN t.amount >= 100 THEN 'High Spend'
               WHEN t.amount BETWEEN 20 AND 50 THEN 'Moderate Spend'
               ELSE 'Minimal Spend'
           END AS spend_level
    FROM transactions t
)
SELECT category, 
       COUNT(*) AS frequency
FROM spend_level
WHERE spend_level = 'High Spend'
GROUP BY category
ORDER BY frequency DESC;






