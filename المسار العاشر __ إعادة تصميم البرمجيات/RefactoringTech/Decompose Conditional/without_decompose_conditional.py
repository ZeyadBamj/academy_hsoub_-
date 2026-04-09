from datetime import date

today = date.today()
high_season_start_date = date(today.year, month=7, day=1)
high_season_end_date = date(today.year, month=10, day=1)
regular_price = 200
low_season_rate = 1.2
high_season_rate = 2

def calculate_room_price(number_of_rooms, selected_date):
    price = 0
    if number_of_rooms <= 0:
        raise ValueError("Invalid Number of Rooms")

    if selected_date > today and selected_date < high_season_start_date or selected_date > high_season_end_date:
        price = number_of_rooms * regular_price * low_season_rate
    elif selected_date > today:
        price = number_of_rooms * regular_price * high_season_rate
    else:
        raise Exception("Selected Date Should Be in The Future.")

    return price

if __name__ == "__main__":
    price = calculate_room_price(1, date(year=2026, month=8, day=1))
    print(price)