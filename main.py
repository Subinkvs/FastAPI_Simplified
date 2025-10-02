"""
📌 FastAPI Example: POST & GET with Permanent Storage Using JSON File

This example demonstrates how to:
- Create simple GET and POST endpoints using FastAPI.
- Accept JSON data from a POST request.
- Store data permanently in a JSON file.
- Retrieve all stored data using a GET request.

Author: Your Name
"""

from fastapi import FastAPI, Request
import json
import os

# Create a FastAPI instance
app = FastAPI()

# File to store items permanently
DATA_FILE = "items.json"

# ------------------ Helper Functions ------------------
def load_items():
    """Load items from the JSON file; create file if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_items(items):
    """Save items to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(items, f, indent=4)

# ------------------ API Endpoints ------------------

@app.post("/additems")
async def add_items(request: Request):
    """
    Add a new item to the JSON file.

    URL: http://127.0.0.1:8000/additems
    Method: POST
    Body (JSON):
        {
            "item": "Apple"
        }

    Steps:
    - Read the incoming JSON body.
    - Extract the value of "item".
    - Load existing items from JSON file.
    - Append the new item.
    - Save the updated list back to the file.
    """
    # Read the request body as JSON
    data = await request.json()

    # Extract the item from the JSON body
    item = data.get("item")

    # Load existing items
    items = load_items()

    # Add the new item
    items.append(item)

    # Save the updated list
    save_items(items)

    # Return a success message
    return {"message": f"Successfully added item {item}"}


@app.get("/getitems")
def get_items():
    """
    Retrieve all stored items from the JSON file.

    URL: http://127.0.0.1:8000/getitems
    Method: GET

    Returns:
        A JSON list of all items stored permanently.
    """
    items = load_items()
    return {"items": items}



