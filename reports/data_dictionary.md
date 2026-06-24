# Data Dictionary

## 01_fund_master

| Column | Data Type | Description |
|----------|----------|-------------|
| scheme_code | Integer | Unique AMFI Scheme Code |
| scheme_name | Text | Name of Mutual Fund Scheme |

---

## 02_nav_history

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | Integer | Fund Identifier |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |