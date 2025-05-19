# import requests
# def get_time_by_timezone(timezone):
#     url = f"http://worldtimeapi.org/api/timezone/{timezone}"
#     response = requests.get(url)
#     if response.staus_code == 200:
#         data = response.json()
#         return data['datetime']
#     else:
#         return "Error:couldn't fetch time check the timezone"
    
# user_timezone = input("Enter the timezone (e.g., Asia/Kolkata, America/Los_Angeles, America/New_York): ")
# current_time = get_time_by_timezone(user_timezone)
# print(f"Current time in {user_timezone}: {current_time}")

import requests

def get_time_by_city(city):
    url = f"https://timeapi.io/api/Time/current/zone?timeZone={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"{data['date']} {data['time']}"
    else:
        return "❌ Error: Could not fetch time."

# You must use full timezone format (similar to worldtimeapi)
user_input = input("Enter timezone (e.g., Asia/Kolkata, America/Los_Angeles, America/New_York): ")

time = get_time_by_city(user_input)
print(f"Current time in {user_input}: {time}")
