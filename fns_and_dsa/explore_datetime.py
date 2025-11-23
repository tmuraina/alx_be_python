from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Format the date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Display the formatted output
    print(f"Current date and time: {formatted_date}")


def calculate_future_date():
    # Ask the user for a number of days
    days = int(input("Enter the number of days to add to the current date: "))

    # Get today's date
    current_date = datetime.now()

    # Add the specified number of days
    future_date = current_date + timedelta(days=days)

    # Display the future date in YYYY-MM-DD format
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


def main():
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()

