# Task:
# Create a FastAPI app that manages a simple "student grades" system.
# Students can:
# 1️⃣ Add a student's grade using POST
# 2️⃣ Retrieve all students and their grades using GET
# 3️⃣ Determine pass/fail automatically based on logic
#
# Details:
# - Each student should have:
#     - "name" (string)
#     - "score" (integer, 0-100)
# - Logic:
#     - If score >= 50, the student has "passed"
#     - If score < 50, the student has "failed"
# - Store students in a temporary Python list
#
# Endpoints to create:
# 1. POST /addstudent
#    - Accepts JSON body:
#        {
#            "name": "John",
#            "score": 75
#        }
#    - Determines "status" (pass/fail) based on score
#    - Adds the student to the list with status
#    - Returns a message including the student’s name and status
#
# 2. GET /getstudents
#    - Returns all students and their scores along with pass/fail status
#    - Example response:
#        {
#            "students": [
#                {"name": "John", "score": 75, "status": "passed"},
#                {"name": "Alice", "score": 40, "status": "failed"}
#            ]
#        }
#