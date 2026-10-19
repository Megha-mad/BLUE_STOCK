# Mutual Fund Analytics - Data Dictionary

## dim_fund

| Column | Description |
|---|---|
| fund_key | Unique internal fund identifier |
| scheme_code | AMFI scheme code |
| fund_name | Name of mutual fund |
| fund_house | Mutual fund company |
| category | Fund category |
| sub_category | Fund sub-category |
| risk_grade | Risk classification |

## fact_nav

| Column | Description |
|---|---|
| nav_key | Unique NAV record |
| fund_key | Reference to fund |
| date_key | Reference to date |
| nav | Net Asset Value |

## fact_transactions

| Column | Description |
|---|---|
| transaction_key | Unique transaction record |
| transaction_id | Transaction identifier |
| fund_key | Reference to fund |
| investor_id | Investor identifier |
| date_key | Transaction date |
| transaction_type | SIP, Lumpsum or Redemption |
| amount | Transaction amount |
| kyc_status | KYC verification status |
| state | Investor state |

## fact_performance

| Column | Description |
|---|---|
| performance_key | Unique performance record |
| fund_key | Reference to fund |
| year | Performance year |
| return_1y | One-year return |
| return_3y | Three-year return |
| return_5y | Five-year return |
| expense_ratio | Fund expense ratio |

## fact_aum

| Column | Description |
|---|---|
| aum_key | Unique AUM record |
| fund_key | Reference to fund |
| date_key | Date reference |
| aum | Assets Under Management |