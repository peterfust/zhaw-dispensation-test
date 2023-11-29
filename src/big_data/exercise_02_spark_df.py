from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

cities_data = [
    ("Zurich", 400000, "Limmat"),
    ("Vienna", 1900000, "Danube"),
    ("Paris", 2200000, "Seine"),
    ("Rome", 2900000, "Tiber"),
    ("London", 8700000, "Thames")
]
df0 = spark.createDataFrame(cities_data, ['city', 'population', 'river'])
print(df0.show())


df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("./exercise_02_data.txt")

# Using the Dataframe API
print('DATAFRAME API')
df.filter(df['river'] == 'Danube').select('city').show()
df.select('city', 'population').orderBy('population').show()
print(df.count())

# Using SQL with a temp table
df.createOrReplaceTempView('tempTable')
sqlDF = spark.sql("SELECT city, population FROM tempTable WHERE river = 'Danube'")
sqlDF.show()

# Count rows
num = df.count()
print(num)

# Show first 2 entries
entries = df.take(2)
print(entries)
