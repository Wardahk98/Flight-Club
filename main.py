from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from user_email import UserEmail

print("*******WELCOME TO FLIGHT CLUB********")
print("Destination to find cheapest flights.")
first_name = input("What is your first name: ")
last_name = input("What is your last name: ")
email = input("Enter your email: ")
email_verify = input("ReEnter your email: ")
if email != email_verify:
    print("Please recheck your credentials!")

else:
    print("*******Welcome*******\nYou are part of our Flight Club")
    u_email = UserEmail(first_name, last_name, email)
    u_data = u_email.data
    print(u_data)

data = DataManager()
sheet_data = data.data

id_search = 1
listed_data = []
for x in range(len(sheet_data)):
    if sheet_data[x]['iataCode'] == "":
        id_search = sheet_data[x]['id']
        city = sheet_data[x]["city"]
        value = FlightSearch(city)
        find_iata = value.data_iata
        # print(f"Found no data for location: {city}")
        put = data.put_request(find_iata, id_search)
        data_price = FlightSearch(find_iata)
        prices = data_price.find_price()
        listed_data.append(data_price.c_data)

    else:
        data_price = FlightSearch(sheet_data[x]['iataCode'])
        prices = data_price.find_price()
        listed_data.append(data_price.c_data)

# --------------------Notifications----------------------------
for x in range(len(listed_data)):
    if sheet_data[x]["price"] >= listed_data[x]["price"]:
        body = (f"Reduced Prices ~ For Rs.{listed_data[x]['price']}, "
                f"fly from {listed_data[x]['departure city']}-{listed_data[x]['departure iata']} to "
                f"{listed_data[x]['arrival city']}-{listed_data[x]['arrival iata']}, "
                f"from {listed_data[x]['date']}")
        sms = NotificationManager(body)
        print(sms.message.sid)
