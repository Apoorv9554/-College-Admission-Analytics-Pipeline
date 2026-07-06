# Databricks notebook source
# MAGIC %md
# MAGIC ## STEP 1: LOAD CSV FILE

# COMMAND ----------

df = spark.table("college.source_data.college")

# COMMAND ----------

# MAGIC %md
# MAGIC ## STEP 2: VERIFY DATA

# COMMAND ----------

df.show(5)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## STEP 3: CLEAN COLUMN NAMES

# COMMAND ----------

df = df.select(
    [col(f"`{c}`").alias(c.lower().replace(".", "_").replace(" ", "_")) for c in df.columns]
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## STEP 4: LIGHT DATA TYPE CHECK

# COMMAND ----------


# ✅ type casting 
df = df.withColumn("apps", col("apps").cast("int")) \
       .withColumn("accept", col("accept").cast("int")) \
       .withColumn("enroll", col("enroll").cast("int")) \
       .withColumn("grad_rate", col("grad_rate").cast("int"))


# COMMAND ----------

# MAGIC %md
# MAGIC ## STEP 5: SAVE BRONZE TABLE

# COMMAND ----------


# ✅ Save Bronze
df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("college.bronze.bronze_college")


# COMMAND ----------

# MAGIC %md
# MAGIC ## STEP 6: VERIFY TABLE

# COMMAND ----------

spark.sql("SELECT * FROM college.bronze.bronze_college LIMIT 10").show()

# COMMAND ----------

df.printSchema()