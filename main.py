print("Merhaba")
print("Python temllerini öğreniyorum.")

print(type(10))
print(type(10.5))
print(type("Merhaba"))
print(type(True))

name = input("Adınız: ")
weekly_hours = float(input("Haftalık çalışma süreniz: "))
completed_lessons = int(input("Tamamlanan ders sayısı: "))

monthly_hours = weekly_hours * 4

print(f"Öğrenci: {name}")
print(f"Haftalık çalışma: {weekly_hours} saat")
print(f"Aylık tahmini çalışma: {monthly_hours} saat")
print(f"Tamamlanan ders: {completed_lessons}")