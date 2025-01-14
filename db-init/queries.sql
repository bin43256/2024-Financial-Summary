WITH spend_hierarchy AS (
    SELECT t.description, t.amount, c.category_name,
     CASE
     WHEN t.amount >= 100 THEN 'High'
     WHEN t.amount BETWEEN 20 AND 50 THEN 'Moderate'
     ELSE 'Low'
     END AS "Spend level"
    FROM transactions t
    JOIN categories c ON t.category_id = c.category_id
    WHERE t.banking_type = 'credit card'
)
-- I want to know the average amount I spend for each grocery store and how many times I went there
SELECT description, round(avg(amount),2) as avg_amount, count(description)
FROM transactions 
WHERE category = 'Grocery'
GROUP BY description
ORDER BY avg_amount DESC;
-- What are the max amount I've spend on a single grocery store trip?
SELECT description,round(max(amount),2) as max_amount
FROM transactions 
WHERE category = 'Grocery'
GROUP BY description
ORDER BY max_amount DESC;

SELECT description,round(sum(amount),2) as sum_amount
FROM transactions 
WHERE category = 'Grocery'
GROUP BY description
ORDER BY sum_amount DESC;

SELECT category,round(sum(amount),2) as sum_amount
FROM transactions 
GROUP BY category
ORDER BY sum_amount DESC;


