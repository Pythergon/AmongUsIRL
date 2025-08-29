import json

data = {
    "name": "John Doe",
    "age": 30,
    "isStudent": False,
    "courses": [
        {"title": "History", "credits": 3},
        {"title": "Math", "credits": 4}
    ]
}

# Open a file in write mode
with open('data.json', 'w') as f:
    # Use json.dump() to write the data with an indent of 4 spaces
    json.dump(data, f, indent=4)