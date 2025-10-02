# Task:
# Create a FastAPI app that allows users to:
# 1️⃣ Add a "task" to a temporary list using POST
# 2️⃣ Retrieve all tasks using GET
#
# Details:
# - Each task should have:
#     - "title" (string)
#     - "completed" (boolean)
# - Store tasks in a simple Python list (temporary storage)
#
# Endpoints to create:
# 1. POST /addtask
#    - Accepts JSON body:
#        {
#            "title": "Buy groceries",
#            "completed": false
#        }
#    - Adds the task to the list
#    - Returns a success message with the task title
#
# 2. GET /gettasks
#    - Returns all tasks currently in the list
#    - Example response:
#        {
#            "tasks": [
#                {"title": "Buy groceries", "completed": false},
#                {"title": "Walk the dog", "completed": true}
#            ]
#        }
#