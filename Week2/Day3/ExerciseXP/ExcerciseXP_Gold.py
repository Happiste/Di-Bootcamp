from datetime import date
import holidays

# il_holiday = holidays.IL()
fr_holiday2 = holidays.country_holidays('FR', 2024)
now = date.today()
print(now)
print(fr_holiday2)

for holiday_date, holiday_name in sorted(fr_holiday2.items()):
    if holiday_date >= now:
        print(f"{holiday_date}: {holiday_name}")