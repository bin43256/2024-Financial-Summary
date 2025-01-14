CREATE TABLE bank(
    bank_id SERIAL PRIMARY KEY,
    bank VARCHAR(50) NOT NULL,
    banking_type VARCHAR(20) NOT NULL,
    credit_limit VARCHAR(20) NOT NULL,
    date_start VARCHAR(20) NOT NULL
);
CREATE TABLE dates(
    date_id SERIAL PRIMARY KEY,
    full_date date NOT NULL,
    month_name VARCHAR(10),
    day_name VARCHAR(10),
    is_weekday VARCHAR(20),
    is_holiday VARCHAR(20)
);
CREATE TABLE payment_method(
    payment_method_id SERIAL PRIMARY KEY,
    payment_method VARCHAR(20)
);
CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    date_id INTEGER REFERENCES dates(date_id),
    bank_id INTEGER REFERENCES bank(bank_id),
    payment_method_id INTEGER REFERENCES payment_method(payment_method_id),
    description VARCHAR(50),
    category VARCHAR(50),
    amount DECIMAL(6,2) NOT NULL,
    payment_modality VARCHAR(20)
);



