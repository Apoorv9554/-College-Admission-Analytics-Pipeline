# Databricks notebook source
# MAGIC %md
# MAGIC ## STEP 1: LOAD SILVER TABLE

# COMMAND ----------

df = spark.table("college.silver.silver_college")


# COMMAND ----------

# MAGIC %md
# MAGIC ## TABLE 1: OVERVIEW (KPI)

# COMMAND ----------

from pyspark.sql.functions import *

gold_overview = df.agg(
    count("*").alias("total_colleges"),
    avg("admission_rate").alias("avg_admission_rate"),
    avg("outstate").alias("avg_tuition"),
    avg("grad_rate").alias("avg_grad_rate")
)

gold_overview.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("college.gold.gold_overview_college")


# COMMAND ----------

# MAGIC %md
# MAGIC ## TABLE 2: PRIVATE vs PUBLIC

# COMMAND ----------

gold_private = df.groupBy("private_flag") \
    .agg(count("*").alias("college_count"))

gold_private.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("college.gold.gold_private")

# COMMAND ----------

# MAGIC %md
# MAGIC ## TABLE 3: ADMISSION ANALYSIS

# COMMAND ----------

gold_admission = df.groupBy("admission_selectivity") \
    .agg(
        count("*").alias("college_count"),
        avg("admission_rate").alias("avg_admission_rate")
    )

gold_admission.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("college.gold.gold_admission")

# COMMAND ----------

# MAGIC %md
# MAGIC ## TABLE 4: TUITION ANALYSIS

# COMMAND ----------

gold_tuition = df.groupBy("tuition_group") \
    .agg(
        count("*").alias("college_count"),
        avg("grad_rate").alias("avg_grad_rate")
    )

gold_tuition.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("college.gold.gold_tuition")

# COMMAND ----------

# MAGIC %md
# MAGIC ## TABLE 5: FACULTY QUALITY

# COMMAND ----------

gold_faculty = df.groupBy("phd_group") \
    .agg(
        count("*").alias("college_count"),
        avg("grad_rate").alias("avg_grad_rate")
    )

gold_faculty.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("college.gold.gold_faculty")

# COMMAND ----------

# MAGIC %md
# MAGIC ## TABLE 6: STUDENT-FACULTY RATIO
# MAGIC ## 

# COMMAND ----------

gold_ratio = df.groupBy("sf_ratio_group") \
    .agg(
        count("*").alias("college_count"),
        avg("grad_rate").alias("avg_grad_rate")
    )

gold_ratio.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("college.gold.gold_ratio")

# COMMAND ----------

# MAGIC %md
# MAGIC ## TABLE 7: EXPENDITURE ANALYSIS

# COMMAND ----------

gold_expend = df.groupBy("expend_group") \
    .agg(
        count("*").alias("college_count"),
        avg("grad_rate").alias("avg_grad_rate")
    )

gold_expend.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("college.gold.gold_expend")

# COMMAND ----------

