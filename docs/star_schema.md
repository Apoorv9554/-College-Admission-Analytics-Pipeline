# Logical Analytical Model

## Overview

The Gold Layer organizes analytical datasets that support business intelligence reporting.

Unlike a traditional transactional system, the project focuses on analytical aggregations generated from a cleaned college dataset.

---

# Source Table

```
college.source_data.college
```

↓

```
bronze_college
```

↓

```
silver_college
```

↓

Business Tables

---

# Gold Tables

| Table | Business Purpose |
|---------|-----------------|
| gold_overview_college | Executive KPIs |
| gold_private | Institution comparison |
| gold_admission | Admission trends |
| gold_tuition | Tuition analysis |
| gold_faculty | Faculty quality |
| gold_ratio | Student-Faculty ratio |
| gold_expend | Expenditure analysis |

---

# Logical Model

```
                 Silver College
                       │
      ┌────────────────┼─────────────────┐
      │                │                 │
      ▼                ▼                 ▼
Admission         Tuition          Faculty
      │                │                 │
      ▼                ▼                 ▼
Graduation     Expenditure      Student Ratio
      │                │                 │
      └────────────────┼─────────────────┘
                       ▼
              Executive Dashboard
```

---

# Dashboard Consumption

The Databricks Dashboard directly consumes the Gold tables.

Each visualization is connected to a dedicated Gold table, ensuring:

- Fast query performance
- Simplified SQL
- Reusable business metrics
- Easy maintenance

---

# Benefits

- Optimized reporting
- Minimal dashboard calculations
- Clean business layer
- Easy future enhancements
