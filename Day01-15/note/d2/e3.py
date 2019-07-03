while(True):
    text = input('plz input year')
    if (text == 'x'):
        break
    year = int(text)
    is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
    print('is leap year: %s' % is_leap)
