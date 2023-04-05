import requests
import json

# Make a GET request to the API endpoint
response = requests.get('https://api.example.com/data')

# Extract the JSON data from the response
data = response.json()

# Print the JSON data to verify that it loaded correctly
print(json.dumps(data, indent=4))

# Extract the specific data you want and populate a new JSON object
new_data = {'name': data['name'], 'age': data['age'], 'email': data['email']}

# Print the new JSON object to verify that it was populated correctly
print(json.dumps(new_data, indent=4))
