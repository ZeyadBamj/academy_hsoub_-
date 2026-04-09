from datetime import date


today = date.today()
high_season_start_date = date(today.year, month=7, day=1)
high_season_end_date = date(today.year, month=10, day=1)
regular_price = 200
low_season_rate = 1.2
high_season_rate = 2

# def hello_world():
#     string = 'Hello World!'
#     return string

def calculate_apartment_price(number_of_rooms, selected_date = today):
    check_number_of_rooms(number_of_rooms)

    check_selected_date(selected_date)

    if out_of_season(selected_date):
        price = out_of_the_season_price(number_of_rooms)

    elif selected_date > today:
        price = in_the_season_price(number_of_rooms)

    return price


def in_the_season_price(number_of_rooms):
    return number_of_rooms * regular_price * high_season_rate


def out_of_the_season_price(number_of_rooms):
    return number_of_rooms * regular_price * low_season_rate


def out_of_season(selected_date: date):
    return (selected_date > today and selected_date < high_season_start_date) or (
                selected_date > high_season_start_date)


def check_number_of_rooms(number_of_rooms):
    if number_of_rooms <= 0:
        raise ValueError("Number of rooms must be greater than zero.")


def check_selected_date(selected_date):
    if selected_date < today:
        raise Exception('Selected date should be in the future.')
