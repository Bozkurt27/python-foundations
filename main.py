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