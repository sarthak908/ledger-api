CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE accounts (
    id INT PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id)
);

CREATE TABLE transactions (
    id VARCHAR(36) PRIMARY KEY,
    idempotency_key VARCHAR(64) UNIQUE,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE ledger_entries (
    id INT PRIMARY KEY,
    transaction_id VARCHAR(36) NOT NULL REFERENCES transactions(id),
    account_id INT NOT NULL REFERENCES accounts(id),
    amount BIGINT NOT NULL CHECK (amount <> 0)   -- positive = credit, negative = debit
);