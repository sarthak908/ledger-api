from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
import uuid

app = FastAPI(title="Ledger API")

# id -> balance in paise (smallest currency unit); replaced by a database later
accounts: dict[int, int] = {1: 50000, 2: 20000}
transfers: list[dict] = []


class TransferIn(BaseModel):
    from_account: int = Field(gt=0)
    to_account: int = Field(gt=0)
    amount: int = Field(gt=0, description="Amount in paise")


@app.get("/accounts/{account_id}/balance")
def get_balance(account_id: int):
    if account_id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"account_id": account_id, "balance": accounts[account_id]}


@app.post("/transfer", status_code=201)
def create_transfer(body: TransferIn):
    if body.from_account == body.to_account:
        raise HTTPException(status_code=400, detail="Cannot transfer to the same account")
    if body.from_account not in accounts or body.to_account not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    if accounts[body.from_account] < body.amount:
        raise HTTPException(status_code=409, detail="Insufficient funds")

    accounts[body.from_account] -= body.amount
    accounts[body.to_account] += body.amount

    record = {
        "id": str(uuid.uuid4()),
        "from_account": body.from_account,
        "to_account": body.to_account,
        "amount": body.amount,
        "created_at": datetime.now().isoformat(),
    }
    transfers.append(record)
    return record