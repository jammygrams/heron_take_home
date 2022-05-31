from dataclasses import dataclass
# from datetime import datetime
import datetime
from collections import defaultdict
import json
from typing import List, Dict

COST_THRESHOLD = 2.0
TIME_THRESHOLD = 5


@dataclass
class Transaction:
    id: id
    description: str
    amount: float
    date: datetime.datetime

def load_transactions(filename: str) -> List[Transaction]:
    transactions = []
    with open(filename) as f:
        raw = json.load(f)
        
    for i, t in enumerate(raw['transactions']):
        transactions.append(Transaction(
            i,
            t['description'],
            float(t['amount']),
            datetime.datetime.strptime(t['date'], '%Y-%m-%d')
        ))
    return transactions


def create_transaction_groups(transactions: List[Transaction]) -> Dict[str, List[Transaction]]:
    groups = defaultdict(list)
    for t in transactions:
        groups[t.description].append(t)
    
    return groups

def sort_group(group: List[Transaction]) -> List[Transaction]:
    return sorted(group, key=lambda x: x.date)


def is_group_recurring(group: List[Transaction]) -> bool:
    if len(group) < 3:
        return False
    time_diffs = []
    for i in range(1, len(group)):
        cost_diff = group[i].amount - group[i-1].amount
        if cost_diff > COST_THRESHOLD:
            return False
        time_diffs.append((group[i].date - group[i-1].date).days)
    for i in range(1, len(time_diffs)):
        time_diff_diff = abs(time_diffs[i] - time_diffs[i-1])
        if time_diff_diff > TIME_THRESHOLD:
            return False
    return True

def identify_recurring_transactions(transactions: List[Transaction]) -> List[int]:
    out = []
    groups = create_transaction_groups(transactions)
    for _, group in groups.items():
        sorted_group = sort_group(group)
        if is_group_recurring(sorted_group):
            out.extend([t.id for t in sorted_group])
    return out

if __name__=='__main__':
    transactions = load_transactions('example.json')
    print(identify_recurring_transactions(transactions))
