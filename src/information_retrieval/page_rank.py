d = 0.5
iterations = 20
sites = {'A': {'out': {'B', 'C'}, 'inc': {'C'}}, 'B': {'out': {'C'}, 'inc': {'A'}},
         'C': {'out': {'A'}, 'inc': {'A', 'B'}}}
pr_values = {'A': 1.0, 'B': 1.0, 'C': 1.0}

def calculatePR(site):
    inner_sum = 0.0
    for inc_site in sites[site]['inc']:
        inner_sum += pr_values[inc_site] / len(sites[inc_site]['out'])
    return (1 - d) + (d * inner_sum)

for _ in range(iterations):
    new_pr_values = {}
    for site in sites:
        new_pr_values[site] = calculatePR(site)
    pr_values = new_pr_values

print(new_pr_values)