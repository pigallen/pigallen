# Prompting the user for input
hours_str = input("Enter hours worked: ")
rate_str = input("Enter hourly rate: ")
h = float(hours_str)
r = float(rate_str)

if h <= 40:
    gross_pay = hours * r
else:
    regular_pay = 40 * r
    overtime_pay = (h - 40) * (r * 1.5)
    gross_pay = regular_pay + overtime_pay

print(f"{gross_pay:.2f}")