CREATE TABLE categories(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(20) NOT NULL
);
CREATE TABLE banks(
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(50) NOT NULL
);
CREATE TABLE transactions(
    transaction_id SERIAL PRIMARY KEY,
    date DATE, 
    description VARCHAR(50) NOT NULL,
    amount DECIMAL(6,2) NOT NULL,
    category_id INTEGER REFERENCES categories(category_id),
    bank_id INTEGER REFERENCES banks(bank_id),
    banking_type VARCHAR(50) NOT NULL
);



