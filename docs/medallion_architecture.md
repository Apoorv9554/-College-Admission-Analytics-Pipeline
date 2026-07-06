# Medallion Architecture

## Overview

The College Admission Analytics project follows the Medallion Architecture, a modern data engineering design pattern widely adopted in enterprise lakehouse platforms.

The architecture separates data into three logical layers:

- Bronze
- Silver
- Gold

Each layer progressively improves data quality and prepares it for analytics.

---

# Architecture Diagram

> Place the image below in the architecture folder.

<p align="center">
<img src="../architecture/medallion_architecture.png" width="100%">
</p>

---

# Bronze Layer

## Purpose

The Bronze Layer stores raw ingested data exactly as received from the source system.

Notebook

```
1_bronze
```

Output Table

```
college.bronze.bronze_college
```

Characteristics

- Raw records
- No business logic
- Historical preservation
- Initial Delta format

---

# Silver Layer

## Purpose

The Silver Layer improves data quality by cleaning and standardizing the dataset.

Notebook

```
2_silver
```

Output Table

```
college.silver.silver_college
```

Processing includes:

- Null handling
- Standardized column names
- Data validation
- Consistent formatting

---

# Gold Layer

## Purpose

The Gold Layer contains curated business datasets optimized for reporting and dashboarding.

Notebook

```
3_gold
```

Generated Tables

| Table | Purpose |
|--------|----------|
| gold_overview_college | KPI metrics |
| gold_private | Private/Public comparison |
| gold_admission | Admission analytics |
| gold_tuition | Tuition insights |
| gold_faculty | Faculty quality |
| gold_ratio | Student-Faculty ratio |
| gold_expend | Expenditure analysis |

---

# Data Flow

```
CSV Dataset
      │
      ▼
Source Data
      │
      ▼
 Bronze
      │
      ▼
 Silver
      │
      ▼
 Gold
      │
      ▼
 Dashboard
```

---

# Advantages

- Better data quality
- Easier debugging
- Faster analytics
- Reusable datasets
- Scalable ETL pipelines
- Enterprise best practice
