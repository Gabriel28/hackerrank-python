def time_conversion(data):
    period = data[-2:]
    time = data[:-2]

    hours, minutes, seconds = map(int, time.split(':'))

    if period == 'AM':
        if hours == 12:
            hours = 0
    else:
        if hours != 12:
            hours += 12

    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    print(time_conversion('07:05:45PM'))