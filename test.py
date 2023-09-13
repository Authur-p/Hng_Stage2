import requests
import json

# Define the base URL of your Spring Boot application
base_url = 'http://authur.pythonanywhere.com/api/user'

# Function to send a POST request to create a person
def create_person(name):
    data = {'name': name}
    response = requests.post(f'{base_url}', json=data)  # Append the create endpoint
    return response

# Function to send a GET request to read a person by ID
def read_person(name):
    response = requests.get(f'{base_url}/{name}')  # Append the ID as a path variable
    return response

# Function to send a PUT request to update a person by ID
def update_person(name, new_name):
    data = {'name': new_name}
    response = requests.put(f'{base_url}/{name}', json=data)  # Append the ID as a path variable
    return response

# Function to send a DELETE request to delete a person by ID
def delete_person(name):
    response = requests.delete(f'{base_url}/{name}')  # Append the ID as a path variable
    return response

# Test the create endpoint
create_response = create_person('example1')
print('Create Person Response:')
print(create_response.status_code)
print(create_response.text)
print('\n')

# Test the read endpoint
read_response = read_person('example1')
print('Read Person Response:')
print(read_response.status_code)
print(read_response.text)
print('\n')

# Test the update endpoint
update_response = update_person('example1', 'User1')
print('Update Person Response:')
print(update_response.status_code)
print(update_response.text)
print('\n')

# Test the delete endpoint
delete_response = delete_person('User1')
print('Delete Person Response:')
print(delete_response.status_code)
print(delete_response.text)