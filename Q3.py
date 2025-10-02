# Task:
# Create a FastAPI app that allows users to:
# 1️⃣ Add a "contact" to a temporary list using POST
# 2️⃣ Retrieve all contacts using GET
#
# Details:
# - Each contact should have:
#     - "name" (string)
#     - "phone" (string)
#     - "email" (string)
# - Store contacts in a simple Python list (temporary storage)
#
# Endpoints to create:
# 1. POST /addcontact
#    - Accepts JSON body:
#        {
#            "name": "Alice",
#            "phone": "1234567890",
#            "email": "alice@example.com"
#        }
#    - Adds the contact to the list
#    - Returns a success message with the contact name
#
# 2. GET /getcontacts
#    - Returns all contacts currently in the list
#    - Example response:
#        {
#            "contacts": [
#                {"name": "Alice", "phone": "1234567890", "email": "alice@example.com"},
#                {"name": "Bob", "phone": "9876543210", "email": "bob@example.com"}
#            ]
#        }
#