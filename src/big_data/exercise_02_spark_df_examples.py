from pyspark.sql import *
spark = SparkSession.builder.getOrCreate()
from pyspark.sql.functions import explode, col, asc, countDistinct

# Create the Departments
department1 = Row(id='123456', name='Computer Science')
department2 = Row(id='789012', name='Mechanical Engineering')
department3 = Row(id='345678', name='Theater and Drama')
department4 = Row(id='901234', name='Indoor Recreation')

# Create the Employees
Employee = Row("firstName", "lastName", "email", "salary")
employee1 = Employee('michael', 'armbrust', 'no-reply@berkeley.edu', 100000)
employee2 = Employee('xiangrui', 'meng', 'no-reply@stanford.edu', 120000)
employee3 = Employee('matei', None, 'no-reply@waterloo.edu', 140000)
employee4 = Employee(None, 'wendell', 'no-reply@berkeley.edu', 160000)

# Create the DepartmentWithEmployees instances from Departments and Employees
departmentWithEmployees1 = Row(department=department1, employees=[employee1, employee2])
departmentWithEmployees2 = Row(department=department2, employees=[employee3, employee4])
departmentWithEmployees3 = Row(department=department3, employees=[employee1, employee4])
departmentWithEmployees4 = Row(department=department4, employees=[employee2, employee3])

print (department1)
print (employee2)
print (departmentWithEmployees1.employees[0].email)
print(departmentWithEmployees1)

# Create DataFrame from list of rows
departmentsWithEmployeesSeq1 = [departmentWithEmployees1, departmentWithEmployees2]
df1 = spark.createDataFrame(departmentsWithEmployeesSeq1)
df1.show()

# Create a second DataFrame from a list of rows
departmentsWithEmployeesSeq2 = [departmentWithEmployees3, departmentWithEmployees4]
df2 = spark.createDataFrame(departmentsWithEmployeesSeq2)
df2.show()

# Union of 2 DataFrames
unionDF = df1.unionAll(df2)
unionDF.show()

# Explode the employees column
df = unionDF.select(explode("employees").alias("e"))
explodeDF = df.selectExpr("e.firstName", "e.lastName", "e.email", "e.salary")
explodeDF.show()

# Use filter() to return only the rows that match the given predicate
filterDF = explodeDF.filter(explodeDF.firstName == "xiangrui").sort(explodeDF.lastName)
filterDF.show()
filterDF = explodeDF.filter((col("firstName") == "xiangrui") | (col("firstName") == "michael")).sort(asc("lastName"))
filterDF.show()
whereDF = explodeDF.where((col("firstName") == "xiangrui") | (col("firstName") == "michael")).sort(asc("lastName"))
whereDF.show()
filterNonNullDF = explodeDF.filter(col("firstName").isNull() | col("lastName").isNull()).sort("email")
filterNonNullDF.show()

# Replace null values with -- using DataFrame Na functions
nonNullDF = explodeDF.fillna("--")
nonNullDF.show()

# Example aggregations using agg() and countDistinct()
countDistinctDF = explodeDF.select("firstName", "lastName") \
    .groupBy("firstName", "lastName") \
    .agg(countDistinct("firstName"))
countDistinctDF.show()

# Compare the DataFrame and SQL Query Physical Plans (Hint: They should be the same.)
countDistinctDF.explain()

explodeDF.createOrReplaceTempView("databricks_df_example")
# Perform the same query as the DataFrame above and return ``explain``
countDistinctDF_sql = spark.sql("SELECT firstName, lastName, count(distinct firstName) as distinct_first_names FROM databricks_df_example GROUP BY firstName, lastName")
countDistinctDF_sql.explain()


# Sum up all salaries
salarySumDF = explodeDF.agg({"salary": "sum"})
salarySumDF.show()
# Show type
print(type(explodeDF.salary))

# Print the summary statistics for the salaries.
explodeDF.describe("salary").show()