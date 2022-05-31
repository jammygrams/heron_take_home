# Heron Take Home

### Approach:

Due to the time constraint, I implemented an absolute barebones approach:

1) Create groups of transactions based on exact match of transaction description.
    * TODO: fuzzy match based on edit distance, or other character overlap metric. 
2) Sort each group of transaction by date (can't assume they are sorted from example data)
3) Accept each group as recurring transactions if a) there are 3 or more transactions, b) the difference in cost is less than a threshold, c) the difference in timedeltas is less than a threshold
    * TODO: so much possible here.  For a start, check if cost and timedelta differences are within a % of their absolute values, rather than an absolute difference.

### Discussion:
* Measure accuracy: 
    * For a start, run the transaction grouping and manually review the results. 
    * Come up with a list of known repeated transactions (e.g. Netflix, payroll, cloud bills), manually search for them by regex on description, and check algo performance against them.
* Measure customer impact:
    * Need to have a clearer idea of the business value of grouping recurring transactions.  Presumably it makes enriched/ normalised data more digestible to customers.
    * But if customers are more interested in summary numbers (e.g. total spend on salary vs. rent) than reviewing individual transactions, it may not be that important? For instance, grouping all transactions with a description like "business lunch" is valuable enough, regardless of whether they happen at regular intervals.
* Deploy: we probably wouldn't have all transactions for a customer available at a time (e.g. may only receive updates of the last month), or they may be too large for memory. We may need to adapt the approach to consume a stream of transactions per customer, which is compared to a database / map of potential repeated transactions.

