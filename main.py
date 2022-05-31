from dataclasses import dataclass
from datetime import datetime

import json
from typing import List

@dataclass
class Transaction:
    id: int
    description: str
    amount: float
    date: datetime

def load_transactions(filename: str) -> List[Transaction]:
    transactions = []
    with open(filename) as f:
        raw = json.load(f)
        
    for i, t in enumerate(raw['transactions']):
        transactions.append(Transaction(
            i,
            t['description'],
            float(t['amount']),
            datetime.strptime(t['date'], '%Y-%m-%d')
        ))
    return transactions

# def identify_recurring_transactions(transactions: List[Transaction]) -> List[Transaction.id]


if __name__=='__main__':
    transactions = load_transactions('example.json')
    print(transactions)
