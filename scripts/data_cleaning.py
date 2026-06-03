import pandas as pd
import os

raw = "../data/raw"
processed = "../data/processed"

os.makedirs(processed, exist_ok=True)

# 1 NAV HISTORY
nav = pd.read_csv(f"{raw}/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code","date"])

nav = nav.drop_duplicates()

nav["nav"] = nav["nav"].ffill()

nav = nav[nav["nav"] > 0]

nav.to_csv(f"{processed}/02_nav_history_clean.csv",index=False)

# 2 INVESTOR TRANSACTIONS
txn = pd.read_csv(f"{raw}/08_investor_transactions.csv")

txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])

txn["transaction_type"] = txn["transaction_type"].str.strip()

txn = txn[txn["amount_inr"] > 0]

txn.to_csv(f"{processed}/08_investor_transactions_clean.csv",index=False)

# 3 SCHEME PERFORMANCE
perf = pd.read_csv(f"{raw}/07_scheme_performance.csv")

perf = perf[
    (perf["expense_ratio_pct"]>=0.1)
    &
    (perf["expense_ratio_pct"]<=2.5)
]

perf.to_csv(f"{processed}/07_scheme_performance_clean.csv",index=False)

print("Cleaning Completed")