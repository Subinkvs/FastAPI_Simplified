# 🧑‍🎓 Question 2: Task Manager API
# -------------------------------------------------
# Task:
# Build a FastAPI CRUD API to manage a "to-do task list".
#
# Endpoints to create:
# 1️⃣ POST /addtask
#     - Accepts JSON body:
#       {
#         "title": "Do homework",
#         "status": "pending"
#       }
#     - Adds a new task to the list.
#
# 2️⃣ GET /gettasks
#     - Returns all tasks.
#
# 3️⃣ PUT /updatetask/{index}
#     - Updates a task's title or status by index.
#
# 4️⃣ DELETE /deletetask/{index}
#     - Deletes a task from the list.
#
# Requirements:
# - Each task should have:
#     - "title" (string)
#     - "status" (string) — must be either "pending" or "completed".
# - Validate that the status value is valid before adding or updating.