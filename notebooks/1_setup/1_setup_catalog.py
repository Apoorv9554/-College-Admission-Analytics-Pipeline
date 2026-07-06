# Databricks notebook source
# MAGIC %sql
# MAGIC create catalog if not exists college

# COMMAND ----------

# MAGIC %sql
# MAGIC USE catalog college

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists college.bronze;
# MAGIC create schema if not exists college.silver;
# MAGIC create schema if not exists college.gold;
# MAGIC create schema if not exists college.source_data;

# COMMAND ----------

# MAGIC %sql
# MAGIC show databases from college;

# COMMAND ----------

