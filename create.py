import requests

# URL of the Juice Shop instance (update this if your Juice Shop runs on a different URL)
JUICE_SHOP_URL = "http://0.0.0.0:3000"

# Define the registration endpoint
register_url = f"{JUICE_SHOP_URL}/api/Users"

# User details
user_data = {
    "email": "w3af@holm.com",
    "password": "w3aftesting",
    "passwordRepeat": "w3aftesting",
    "securityQuestion": {
        "id": 1,  # Assuming the first security question is selected, change if necessary
        "answer": "myAnswer"
    }
}

# Send a POST request to create the new user
response = requests.post(register_url, json=user_data)

# Check if the user was created successfully
# Check if the user was created successfully
if response.status_code == 201:
    print("User created successfully.")
    
    # Log in with the new credentials

