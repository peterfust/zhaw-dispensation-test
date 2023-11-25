from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

# EXERCISE 1
# ==========
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dataRDD = sc.parallelize(data, 2)
print(dataRDD.count())
print(dataRDD.take(5))
print(dataRDD.collect())
print(dataRDD.min())
print(dataRDD.max())
print(dataRDD.mean())

dataRDD2 = dataRDD.map(lambda x: x * 3.14)
print(dataRDD2.filter(lambda x: x > 10).collect())

# EXERCISE 2
# ==========
textRDD = sc.textFile('./exercise_03_data_text.txt', 2)
print(textRDD.collect())
textRDD.cache()
print(textRDD.filter(lambda x: 'file2' in x).collect())

# Count the numbers of words
words_rdd = textRDD.flatMap(lambda line: line.split())  # Split the lines into words using flatMap
words_key_value_rdd = words_rdd.map(lambda word: (word, 1))  # Map each word to a key-value pair
word_counts_rdd = words_key_value_rdd.reduceByKey(lambda a, b: a + b)  # Reduce by key to count each word
word_counts = word_counts_rdd.collect()  # Collect the results
print(word_counts)

# Sort the words by key
output = word_counts_rdd.sortByKey()  # sortByKey can only be applied to key-value pairs (tuples)
print(output.collect())

# Save the output as file
output.saveAsTextFile('./exercise_03_output/textfile.txt')

# EXERCISE 3
# ==========
numericRDD = sc.textFile('./exercise_03_data_numeric.txt', 2)
numericRDD.cache()
print(numericRDD.collect())


def extract_column(index):
    return numericRDD.map(lambda line: int(line.split(",")[index].strip()))


# Create RDDs for each column
column1_rdd = extract_column(0)
column2_rdd = extract_column(1)
column3_rdd = extract_column(2)
column4_rdd = extract_column(3)
print(column1_rdd.collect())
print(column2_rdd.collect())
print(column3_rdd.collect())
print(column4_rdd.collect())
print(column3_rdd.mean())
print(column2_rdd.takeSample(False,2))
print(column3_rdd.filter(lambda x: x >= 300).collect())
print(column1_rdd.reduce(lambda x, y: x + y))

