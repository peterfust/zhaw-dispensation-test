import math

d0 = "Auge um Auge, Zahn um Zahn"
d1 = "aus den Augen, aus dem Sinn"
d2 = "das Auge isst mit"
d3 = "Schönheit liegt im Auge des Betrachters"
d4 = "Schönheit vor Alter"

dimensions = {"Auge": 0, "Zahn": 1, "Sinn": 2, "isst": 3, "Schönheit": 4, "liegt": 5, "Betrachters": 6, "Alter": 7}
print("Number of dimensions: " + str(len(dimensions)))

vectors = [[2, 2, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 1]]

# VECTOR MODEL SPACE MATCHING WITH COSINUS SIMILARITY

# Iterate through all vectors
for i, vector in enumerate(vectors):

    # Calculate cosinus similarity for each vector with all other vectors
    for j, other_vector in enumerate(vectors):
        if j > i:
            scalar_product = 0.0
            norm_vec_1 = 0.0
            norm_vec_2 = 0.0
            for k, value in enumerate(vector):
                scalar_product += value * other_vector[k]
                norm_vec_1 += value ** 2
                norm_vec_2 += other_vector[k] ** 2

            norm_vec_1 = math.sqrt(norm_vec_1)
            norm_vec_2 = math.sqrt(norm_vec_2)

            cosinus_similarity = scalar_product / (norm_vec_1 * norm_vec_2)
            print("Cosinus similarity between Doc" + str(i) + " and Doc" + str(j) + ": " + str(cosinus_similarity))

print("==============================================================================")

# VECTOR MODEL SPACE MATCHING WITH TF-IDF

# Wieviel mal kommt ein Wort im Dokument/Buch vor, Bsp. affection in 115x in Doc1, 88x in Doc2, 0x in Doc3
tf = [[115, 10, 50, 0], [88, 11, 0, 5], [0, 0, 6, 38]]
log_weighted_tf = [[] for _ in tf] # create a new list with same layout as an existing one
idf = [[] for _ in tf] # create a new list with same layout as an existing one
tfidf = [[] for _ in tf] # create a new list with same layout as an existing one
cosinus_normalized = [[] for _ in tf] # create a new list with same layout as an existing one

# iterate through vectors
for i, vector in enumerate(tf):

    # iterate through the elements of a vector to determine TF = 1 + log(word counts in doc)
    for j, value in enumerate(vector):
        if value != 0:
            log_weighted_tf[i].append(1 + math.log10(value))

            # find out in which documents the value exists
            temp = 0
            for k, vec in enumerate(tf):
                if vec[j] != 0:
                    temp += 1

            if temp > 0:
                idf[i].append(math.log10(len(tf) / temp))  # IDF = log(number of docs / number of docs where token exists)
            else:
                idf[i].append(0.00)

            tfidf[i].append(log_weighted_tf[i][j] * idf[i][j])  # TD-IDF = TF * IDF
        else:
            log_weighted_tf[i].append(0.0)
            idf[i].append(0.00)
            tfidf[i].append(0.00)

# calculate cosinus normalization of each word: tf-idf / vector-length (where vector lenght = sqrt(i^2 + j^2...)
for i, vector in enumerate(tfidf):
    temp = 0.0
    for j, value in enumerate(vector):
        temp += value ** 2

    vector_length = math.sqrt(temp)
    for j, value in enumerate(vector):
        cosinus_normalized[i].append(value / vector_length)

# .....

print(log_weighted_tf)
print(idf)
print(tfidf)
print(cosinus_normalized)