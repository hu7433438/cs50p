months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input('Date: ').strip()
    if ' ' in date:
        if ',' in date:
            dates = date.split(' ')
        else:
            continue
    else:
        dates = date.split('/')
        if dates[0] in months:
            continue
    try:
        month = months.index(dates[0].title()) + 1 if dates[0] in months else int(dates[0])
        day = int(dates[1].replace(',', ''))
        year = dates[2]
    except ValueError:
        pass
    else:
        if 0 < month < 13 and 0 < day < 32:
            print(f'{year}-{month:02d}-{int(day):02}')
            break
