# 🧑‍🎓 Question 1: Book Management API
# -------------------------------------------------
# Task:
# Create a FastAPI app to manage a simple "book collection".
# Implement full CRUD operations as described below:
#
# Endpoints to create:
# 1️⃣ POST /addbook
#     - Accepts JSON body:
#       {
#         "title": "Book Name",
#         "author": "Author Name"
#       }
#     - Adds the book to a temporary list.
#
# 2️⃣ GET /getbooks
#     - Returns all stored books.
#
# 3️⃣ PUT /updatebook/{index}
#     - Updates a book's details (title or author) by index.
#
# 4️⃣ DELETE /deletebook/{index}
#     - Deletes a book from the list by index.
#
# Requirements:
# - Each book should have:
#     - "title" (string)
#     - "author" (string)
# - Store all books in a Python list.

