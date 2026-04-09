# Extract Method, Change Signature, Inline

from datetime import date

today = date.today()
high_season_start_date = date(today.year, month=7, day=1)
high_season_end_date = date(today.year, month=10, day=1)
regular_price = 200
low_season_rate = 1.2
high_season_rate = 2

def calculate_room_price(number_of_rooms, selected_date):
    check_number_of_rooms(number_of_rooms)
    check_selected_date(selected_date)
    return out_of_the_season_price(number_of_rooms) if out_of_the_season(selected_date) else in_the_season_price(
        number_of_rooms)


def check_selected_date(selected_date):
    if selected_date < today:
        raise Exception("Selected Date Should Be in The Future.")


def in_the_season_price(number_of_rooms):
    return number_of_rooms * regular_price * high_season_rate


def out_of_the_season_price(number_of_rooms):
    return number_of_rooms * regular_price * low_season_rate


def out_of_the_season(selected_date):
    return selected_date > today and selected_date < high_season_start_date or selected_date > high_season_end_date


def check_number_of_rooms(number_of_rooms):
    if number_of_rooms <= 0:
        raise ValueError("Invalid Number of Rooms")


if __name__ == "__main__":
    price = calculate_room_price(1, date(year=2026, month=3, day=1))
    print(price)