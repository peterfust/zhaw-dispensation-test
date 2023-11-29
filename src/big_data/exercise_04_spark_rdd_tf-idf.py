import os
import re
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

GOOGLE_PATH = './exercise_04_input/Google.csv'
GOOGLE_SMALL_PATH = './exercise_04_input/Google_small.csv'
AMAZON_PATH = './exercise_04_input/Amazon.csv'
AMAZON_SMALL_PATH = './exercise_04_input/Amazon_small.csv'
GOLD_STANDARD_PATH = './exercise_04_input/Amazon_Google_perfectMapping.csv'
STOPWORDS_PATH = './exercise_04_input/stopwords.txt'

DATAFILE_PATTERN = '^(.+),"(.+)",(.*),(.*),(.*)'
stopwords = set(sc.textFile(STOPWORDS_PATH).collect())


def remove_quotes(s):
    return ''.join(i for i in s if i != '"')


def parse_datafile_line(datafile_line):
    datafile_line = datafile_line.decode('utf-8')
    match = re.search(DATAFILE_PATTERN, datafile_line)
    if match is None:
        print('Invalid datafile line: %s' % datafile_line)
        return datafile_line, -1
    elif match.group(1) == '"id"':
        print('Header datafile line: %s' % datafile_line)
        return datafile_line, 0
    else:
        product = '%s %s %s' % (match.group(2), match.group(3), match.group(4))
        return (remove_quotes(match.group(1)), product), 1


def load_data(filename):
    raw = (sc
           .textFile(filename, 4, False)
           .map(parse_datafile_line)
           .cache())
    failed = (raw
              .filter(lambda s: s[1] == -1)
              .map(lambda s: s[0]))
    for line in failed.take(10):
        print('%s - Invalid datafile line: %s' % (filename, line))
    valid = (raw
             .filter(lambda s: s[1] == 1)
             .map(lambda s: s[0])
             .cache())
    print('%s - Read %d lines, successfully parsed %d lines, failed to parse %d lines' % (filename,
                                                                                          raw.count(),
                                                                                          valid.count(),
                                                                                          failed.count()))
    assert failed.count() == 0
    assert raw.count() == (valid.count() + 1)
    return valid


# ----------------------------------------------------------
# LOAD RDDs
# ----------------------------------------------------------
google_small = load_data(GOOGLE_SMALL_PATH)
print(google_small.take(1))
amazon_small = load_data(AMAZON_SMALL_PATH)

# ----------------------------------------------------------
# TOKENIZE
# ----------------------------------------------------------
def tokenize(string):
    split_regex = r'\W+'  # Matches one or more (+) non-word chars

    # Split the string into array of tokens (aka words)
    tokenized_string = [item for item in re.split(split_regex, string.lower()) if
                        item]  # using a comprehension to remove empty items of list

    # Remove stopwords
    return [item for item in tokenized_string if item not in stopwords]


google_small_tokenized = google_small.map(lambda item: (item[0], tokenize(item[1])))  # Tokenize 2nd item in tupel
amazon_small_tokenized = amazon_small.map(lambda item: (item[0], tokenize(item[1])))  # Tokenize 2nd item in tupel
print(google_small_tokenized.take(1))

# Count all tokens of all items
recordCount = google_small_tokenized.map(lambda s: len(s[1]))
recordSum = recordCount.reduce(lambda a, b: a + b)
print('Number of total google tokens: ' + str(recordSum))

# Show item with most tokens
biggestItem = amazon_small_tokenized.max(key=lambda x: len(x[1]))
print('Amazon item with most tokens (' + str(len(biggestItem[1])) + '): ' + str(biggestItem))

# ----------------------------------------------------------
# STEMMING: n/a here
# ----------------------------------------------------------


# ----------------------------------------------------------
# (VECTOR SPACE MODEL) MATCHING
# ----------------------------------------------------------
