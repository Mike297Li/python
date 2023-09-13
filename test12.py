def rank(scores):
    sorted_scores = sorted(set(scores), reverse=True)
    rank_dict = {score: i+1 for i, score in enumerate(sorted_scores)}
    ranks = [rank_dict[score] for score in scores]
    return ranks

scores = [98, 97, 67, 67, 89, 85]
result = rank(scores)

output = []
for i in range(len(scores)):
    output.append([scores[i], result[i]])

print("Output:")
print("+-------+------+")
for row in output:
    print("|", row[0], "|", row[1], "|")
print("+-------+------+")
