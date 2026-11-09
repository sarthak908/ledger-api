from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_transfer_moves_money():
    r = client.post("/transfer", json={"from_account": 1, "to_account": 2, "amount": 100})
    assert r.status_code == 201


def test_overdraft_is_rejected():
    r = client.post("/transfer", json={"from_account": 2, "to_account": 1, "amount": 10**9})
    assert r.status_code == 409


def test_negative_amount_is_rejected():
    r = client.post("/transfer", json={"from_account": 1, "to_account": 2, "amount": -5})
    assert r.status_code == 422