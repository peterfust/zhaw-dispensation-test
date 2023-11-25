import math

d0 = "Auge um Auge, Zahn um Zahn"
d1 = "aus den Augen, aus dem Sinn"
d2 = "das Auge isst mit"
d3 = "Schönheit liegt im Auge des Betrachters"
d4 = "Schönheit vor Alter"

dimensions = {"Auge": 0, "Zahn": 1, "Sinn": 2, "isst": 3, "Schönheit": 4, "liegt": 5, "Betrachters": 6, "Alter": 7}
print("Number of dimensions: " + str(len(dimensions)))

vectors = [[2, 2, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 1]]

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

tf = [[115, 10, 50, 0], [88, 11, 0, 5], [0, 0, 6, 38]]
log_weighted_tf = [[] for _ in tf] # create a new list with same layout as an existing one

for i, vector in enumerate(tf):
    for j, value in enumerate(vector):
        if value != 0:
            log_weighted_tf[i].append(1 + math.log10(value))
        else:
            log_weighted_tf[i].append(0.0)

print(log_weighted_tf)