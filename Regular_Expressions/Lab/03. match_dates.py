import re

dates = input()

pattern = r"(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})"
correct_dates = re.findall(pattern, dates)

for date in correct_dates:
    day = date[0]
    # separator = date[1]
    month = date[2]
    year = date[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")
