century = int(input())
years = century * 100
days = years * 365.2422
hours = days * 24
minutes = hours * 60

print(f"{century} centuries = {years:.0f} years = "
      f"{int(days)} days = {hours:.0f} hours = {minutes:.0f} minutes")
