from fastapi import FastAPI, Request

# ✅ Create a FastAPI instance
app = FastAPI()

# ✅ Temporary storage to hold added items (simulating a database)
items = []


@app.post("/additems")
async def add_items(request: Request):
    """
    📩 Add a new item to the list.

    - Expects a JSON body: {"item": "<item_name>"}
    - Appends the item to the global 'items' list.

    Example Request Body:
    {
        "item": "Apple"
    }
    """
    # Read JSON data from the request body asynchronously
    data = await request.json()

    # Extract the value of "item" from the JSON data
    item = data.get("item")

    # Add the new item to the list
    items.append(item)

    return {"message": f"✅ Successfully added item '{item}'"}


@app.get("/getitems")
def get_items():
    """
    📤 Retrieve all items from the list.

    - Returns a JSON list of all stored items.
    - No request body required.
    """
    return {"items": items}



@app.put("/updateitems/{index}")
async def update_items(index: int, request: Request):
    """
    ✏️ Update an existing item by its index.

    - Path Parameter: index (int) → Position of the item in the list.
    - Expects a JSON body: {"item": "<new_value>"}
    - Updates the item at the given index with the new value.

    Example Request:
    PUT /updateitems/0
    {
        "item": "Orange"
    }
    """
    # Validate the index
    if index < 0 or index >= len(items):
        return {"error": "❌ Invalid index"}

    # Read the new item value from the request body
    data = await request.json()
    new_item = data.get("item")

    # Update the item at the specified index
    items[index] = new_item

    return {"message": f"✅ Successfully updated item at index {index} to '{new_item}'"}


@app.delete("/deleteitems/{index}")
async def delete_items(index: int):
    """
    🗑️ Delete an item from the list by its index.
    - Path Parameter: index (int) → Position of the item to remove.
    - Removes the item and returns a success message.

    Example Request:
    DELETE /deleteitems/1
    """
    # Validate the index
    if index < 0 or index >= len(items):
        return {"error": "❌ Invalid index"}

    # Remove the item at the given index
    removed_item = items.pop(index)

    return {"message": f"✅ Successfully removed item '{removed_item}'"}
