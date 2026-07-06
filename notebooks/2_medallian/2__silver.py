# Databricks notebook source
# MAGIC %md
# MAGIC ## STEP 1: LOAD BRONZE TABLE

# COMMAND ----------

df = spark.table("college.bronze.bronze_college")

# COMMAND ----------

# MAGIC %md
# MAGIC ## STEP 2: BASIC CLEANING

# COMMAND ----------

# 2.1 HANDLE PRIVATE COLUMN
from pyspark.sql.functions import when, col

df = df.withColumn(
    "private_flag",
    when(col("private") == "Yes", "Private").otherwise("Public")
)

# COMMAND ----------

# 2.2 CHECK GRAD RATE
df = df.withColumn(
    "grad_rate",
    when(col("grad_rate") > 100, 100).otherwise(col("grad_rate"))
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## STEP 3: FEATURE ENGINEERING

# COMMAND ----------

# 3.1 ADMISSION RATE
df = df.withColumn(
    "admission_rate",
    col("accept") / col("apps")
)

# COMMAND ----------

# 3.2 ENROLLMENT RATE
df = df.withColumn(
    "enrollment_rate",
    col("enroll") / col("accept")
)

# COMMAND ----------

# 3.3 TUITION GROUP
df = df.withColumn(
    "tuition_group",
    when(col("outstate") < 8000, "Low")
    .when(col("outstate") < 15000, "Medium")
    .otherwise("High")
)

# COMMAND ----------

# 3.4 FACULTY QUALITY GROUP (PhD %)
df = df.withColumn(
    "phd_group",
    when(col("phd") < 60, "Low")
    .when(col("phd") < 80, "Medium")
    .otherwise("High")
)

# COMMAND ----------

# 3.5 STUDENT-FACULTY RATIO GROUP
df = df.withColumn(
    "sf_ratio_group",
    when(col("s_f_ratio") < 10, "Low")
    .when(col("s_f_ratio") < 20, "Medium")
    .otherwise("High")
)

# COMMAND ----------

# 3.6 EXPENDITURE GROUP
df = df.withColumn(
    "expend_group",
    when(col("expend") < 8000, "Low")
    .when(col("expend") < 15000, "Medium")
    .otherwise("High")
)

# COMMAND ----------

# 3.7 ADMISSION SELECTIVITY
df = df.withColumn(
    "admission_selectivity",
    when(col("admission_rate") < 0.3, "Highly Selective")
    .when(col("admission_rate") < 0.6, "Moderate")
    .otherwise("Easy")
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## STEP 4: FINAL COLUMN SELECTION

# COMMAND ----------

df_silver = df.select(
    "private_flag",
    "apps", "accept", "enroll",
    "admission_rate",
    "enrollment_rate",
    "outstate", "tuition_group",
    "room_board",
    "phd", "phd_group",
    "s_f_ratio", "sf_ratio_group",
    "expend", "expend_group",
    "grad_rate",
    "admission_selectivity"
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## STEP 5: SAVE SILVER TABLE

# COMMAND ----------


df_silver.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("college.silver.silver_college")


# COMMAND ----------

df.columns

# COMMAND ----------

