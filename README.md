# Trade Processing & Reconciliation Pipeline

A production-style **post-trade processing system** implemented in Python.
The pipeline ingests trade data from CSV files, validates and normalizes records, stores them in a MySQL database with indexed schemas, reconciles them against settlement data, tracks mismatches, and computes daily Profit & Loss (P&L).

This project simulates the **core workflow of backend trade processing systems used in financial trading infrastructure**.

---

## Features

* **Trade Ingestion**

  * Reads trade data from CSV files.
  * Supports structured trade records with symbol, quantity, price, side, and trade date.

* **Data Validation**

  * Ensures required fields are present.
  * Rejects invalid trades (e.g., negative quantity or incorrect side values).

* **Data Normalization**

  * Converts data types (e.g., quantity → integer, price → float).
  * Standardizes symbol and trade side formatting.

* **MySQL Persistence**

  * Stores validated trades in a relational database.
  * Uses indexed schema for optimized lookups.

* **Trade Reconciliation**

  * Compares internal trade records with settlement records.
  * Detects mismatches such as price or quantity differences.

* **Exception Tracking**

  * Persists reconciliation mismatches in a dedicated `exceptions` table.

* **Daily P&L Computation**

  * Calculates profit and loss based on executed trades.

* **Batch Execution**

  * Provides automation through shell and Windows batch scripts.

---

## Project Architecture

```
CSV Trades
   │
   ▼
Validation
   │
   ▼
Normalization
   │
   ▼
MySQL Storage (trades table)
   │
   ▼
Settlement Comparison
   │
   ▼
Exceptions Table
   │
   ▼
Daily P&L Computation
```

---

## Project Structure

```
trade_pipeline
│
├── app
│   ├── ingestion
│   │   ├── csv_reader.py
│   │   └── settlement_reader.py
│   │
│   ├── validation
│   │   └── trade_validator.py
│   │
│   ├── normalization
│   │   └── trade_normalizer.py
│   │
│   ├── persistence
│   │   └── mysql_repo.py
│   │
│   ├── reconciliation
│   │   └── recon_engine.py
│   │
│   └── pnl
│       └── pnl_engine.py
│
├── data
│   ├── trades.csv
│   └── settlements.csv
│
├── scripts
│   ├── run_pipeline.sh
│   └── run_pipeline.bat
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Database Schema

### Trades Table

```sql
CREATE TABLE trades (
    trade_id VARCHAR(50) PRIMARY KEY,
    symbol VARCHAR(20) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(15,2) NOT NULL,
    side ENUM('BUY','SELL') NOT NULL,
    trade_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Indexes:

```sql
CREATE INDEX idx_symbol ON trades(symbol);
CREATE INDEX idx_trade_date ON trades(trade_date);
```

---

### Exceptions Table

```sql
CREATE TABLE exceptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trade_id VARCHAR(50),
    reason VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Example Input

### Trades

```
trade_id,symbol,quantity,price,side,trade_date
T1,AAPL,100,150,BUY,2026-02-10
T2,GOOG,50,200,SELL,2026-02-10
```

### Settlements

```
trade_id,quantity,price
T1,100,150
T2,45,201
```

---

## Example Output

```
Processing trades...
Trade T1 processed
Trade T2 processed

Daily P&L: -5000
```

---

## Running the Pipeline

Activate virtual environment:

```
venv\Scripts\activate
```

Run pipeline:

```
python main.py
```

Or use batch execution:

```
scripts\run_pipeline.bat
```

---

## Tech Stack

* Python
* MySQL
* SQL
* Shell Scripting
* Windows Batch Scripts

---

## Learning Outcomes

This project demonstrates:

* Data pipeline design
* Backend system architecture
* SQL schema design and indexing
* Financial data reconciliation
* Batch processing workflows

---

## Author

Computer Science undergraduate focused on **backend and systems engineering**, building infrastructure-style software components involving data processing, database design, and batch workflows.
