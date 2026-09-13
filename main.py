daily_sales = [12500, 14100, 9800, 16200, 15300, 8700, 17500]

total_sales = sum(daily_sales)
average_sales = total_sales / len(daily_sales)
highest_sales = max(daily_sales)
lowest_sales = min(daily_sales)

print(f"Toplam satış: {total_sales}")
print(f"Ortalama satış: {average_sales}")
print(f"En yüksek satış: {highest_sales}")
print(f"En düşük satış: {lowest_sales}")

for sale in daily_sales:
    if sale > average_sales:
        print(f"{sale} ortalamanın üzerinde.")
    else:
        print(f"{sale} ortalamanın altında veya eşit.")


liste = [36.1, 38.3]  # mutable , indekslenir
tuple = (36.1, 38.3)  # immutable , indekslenir
candidate_a = {"Python", "SQL", "Git", "Power BI"}  # indekslenmez, mutable, tekrar eden elemanları göstermez.
student = {
    "name": "Şamil",
    "age": 25,
    "career": "Data Scientist",
    "weekly_hours": 10.5
} # mutable, indekslenir, key-value pair

# unpacking
model_result = ("Random Forest", 0.91)

model_name, accuracy = model_result

print(model_name)
print(accuracy)


candidate_a = {"Python", "SQL", "Git", "Power BI"}
candidate_b = {"Python", "SQL", "R", "Machine Learning"}
common_skills = candidate_a & candidate_b  # kesişim
all_skills = candidate_a | candidate_b  # birleşim
only_a = candidate_a - candidate_b  # fark

print(common_skills)
print(all_skills)
print(only_a)
