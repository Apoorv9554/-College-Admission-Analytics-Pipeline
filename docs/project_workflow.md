# Project Workflow

## Overview

The College Admission Analytics Pipeline follows a modern Data Engineering workflow using the Databricks Lakehouse Platform and Medallion Architecture.

The objective is to transform raw educational institution data into reliable analytical datasets that support business intelligence and decision making.

---

# Workflow

```
               Raw CSV Dataset
                      │
                      ▼
              Unity Catalog
                      │
                      ▼
             Source Data Table
                      │
                      ▼
          Bronze Layer (Raw Data)
                      │
                      ▼
     Silver Layer (Clean & Standardized)
                      │
                      ▼
      Gold Layer (Business Aggregations)
                      │
                      ▼
      Databricks SQL Dashboard
                      │
                      ▼
        Business Decision Making
```

---

# Step 1 — Data Ingestion

The raw college admission dataset is first loaded into the Unity Catalog under the Source Data schema.

Schema

```
college.source_data.college
```

The dataset contains institutional information including:

- Admissions
- Tuition
- Faculty
- Student Enrollment
- Graduation Rates
- Financial Expenditure

---

# Step 2 — Bronze Layer

Notebook

```
1_bronze
```

Purpose

- Read source table
- Preserve original data
- Minimal transformations
- Store raw Delta table

Output Table

```
college.bronze.bronze_college
```

---

# Step 3 — Silver Layer

Notebook

```
2_silver
```

Purpose

- Handle missing values
- Standardize data
- Rename columns
- Remove inconsistencies
- Improve data quality

Output Table

```
college.silver.silver_college
```

---

# Step 4 — Gold Layer

Notebook

```
3_gold
```

Purpose

Generate business-ready analytical tables.

Gold tables created:

- gold_overview_college
- gold_private
- gold_admission
- gold_tuition
- gold_faculty
- gold_ratio
- gold_expend

These tables power the dashboard directly.

---

# Step 5 — Dashboard

The Gold Layer is connected to Databricks Dashboards.

Dashboard contains:

- KPI Cards
- Admission Analysis
- Tuition Analysis
- Graduation Insights
- Faculty Analysis
- Institutional Comparison

---

# Pipeline Summary

```
CSV Dataset
      │
      ▼
Source Table
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

# Benefits

- Layered architecture
- Better maintainability
- High data quality
- Reusable business tables
- Faster dashboard performance
- Enterprise-ready design
