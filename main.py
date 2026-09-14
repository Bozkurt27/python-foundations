skills = ["Python", "SQL", "Git", "R"]

for index, skill in enumerate(skills):
    print(index, skill)


names = ["Ali", "Ayşe", "Mehmet"]
scores = [75, 90, 82]

for name, score in zip(names, scores):
    print(name, score)

models = ["Logistic Regression", "Random Forest", "XGBoost"]
scores = [0.82, 0.89, 0.91]

for model, score in zip(models, scores):
    print(f"{model}: {score:.2%}")


model_scores = dict(zip(models, scores))

print(model_scores)

numbers = [1, 2, 3, 4, 5]
squares = [number **2 for number in numbers]
even_number = [number for number in numbers if number % 2 == 0]
print(even_number)
print(squares)


skills = ["Python", "SQL", "Git"]
skill_lengths = {skill: len(skill) for skill in skills}
print(skill_lengths)


scores = [40, 75, 90]
results = ["Passed" if score > 50 else "Failed" for score in scores]
print(results)






