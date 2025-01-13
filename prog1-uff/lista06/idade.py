def daysOfAge(years, months, days):
    totalDays = days
    totalDays += years*365
    totalDays += months*30

    return totalDays

years = int(input('Digite a quantidade de anos: '))
months = int(input('Digite a quantidade de meses: '))
days = int(input('Digite a quantidade de dias: '))

print(f'Dias totais de vida: {daysOfAge(years, months, days)}')