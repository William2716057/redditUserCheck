import requests
from bs4 import BeautifulSoup

# Read usernames from file
with open('userlist.txt', 'r') as file:
    usernames = file.read().splitlines()

# Base URL for profiles
base_url = "https://www.reddit.com/user/"

# Iterate over each username
for user in usernames:
    # Construct URL
    URL = base_url + user
    
    # Make HTTP request to the URL
    response = requests.get(URL)
    
    # Check if the request successful
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Check if user profile exists based on specific element presence
        user_exists = soup.find('p', {'class': 'm-0 text-14 text-neutral-content-weak font-semibold'})
        
        if user_exists:
            print(f"User '{user}' exists.")