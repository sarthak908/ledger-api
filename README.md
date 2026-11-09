# Ledger API

A double-entry ledger backend built with Python and FastAPI.

## Goal
Every transfer is recorded as paired debit and credit entries, so balances
can always be reconciled from the history.

## Status
- [x] In-memory accounts and transfer endpoint with validation
- [x] Tests for transfer, overdraft, and invalid amount
- [ ] Database schema and persistence
- [ ] Idempotency keys
- [ ] Concurrency safety (row locking)
- [ ] Sliding-window transfer-frequency check

## Run
pip install -r requirements.txt
uvicorn main:app --reload
pytest