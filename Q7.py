# 🧑‍🎓 Question 3: Movie Collection API
# -------------------------------------------------
# Task:
# Create a FastAPI app to manage a "movie collection".
#
# Endpoints to create:
# 1️⃣ POST /addmovie
#     - Accepts JSON body:
#       {
#         "name": "Inception",
#         "rating": 9
#       }
#     - Adds a new movie to the list.
#
# 2️⃣ GET /getmovies
#     - Returns all movies.
#
# 3️⃣ PUT /updatemovie/{index}
#     - Updates a movie's name or rating by index.
#
# 4️⃣ DELETE /deletemovie/{index}
#     - Deletes a movie by index.
#
# Requirements:
# - Each movie should have:
#     - "name" (string)
#     - "rating" (integer between 1 and 10)
# - If the rating is outside this range, return an error message.