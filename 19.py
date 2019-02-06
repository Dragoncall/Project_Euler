days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
months = {0: 31, 1: -1, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}
start = 0
start_day = 0

number_of_days_per_year = 30 * 4 + 28 + 31 * 7


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def amount_of_leap_years(start_year, end_year):
    return sum([1 for year in range(start_year, end_year + 1) if is_leap_year(year)])


def amount_of_days(start_year, end_year):
    return number_of_days_per_year * (end_year - start_day + 1) + amount_of_leap_years(start_year, end_year)


def days_on_first(start_year, end_year):
    # Which day is januari 1 in our start year
    januari_1_day = number_of_days_per_year * (start_year - 1900) % 7
    current_weekday = januari_1_day
    current_month = 0
    current_year = start_year
    sunday_on_first_day = 0

    while True:
        # Get month length
        month_length = months[current_month]
        if current_month == 1:
            month_length = 29 if is_leap_year(current_year) else 28

        # Update weekdays and month
        current_weekday = (current_weekday + month_length) % 7
        current_month = (current_month + 1) % 12

        # Update year and stop at end year
        if current_month == 0:
            current_year += 1
            if current_year == end_year:
                return sunday_on_first_day

        # Update the variable we are searching for
        if current_weekday == 6:
            sunday_on_first_day += 1


if __name__ == '__main__':
    print(days_on_first(1901, 2001))
