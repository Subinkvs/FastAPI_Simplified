# 🧠 FastAPI Practice Task – Path Parameters & GET Requests
#
# 📌 Your Task:
# Create a FastAPI application with the following routes:
#
# 1️⃣ Root Endpoint ("/")
#    - Return a welcome message like:
#      {"message": "Welcome to the Math API!"}
#
# 2️⃣ Multiplication Endpoint ("/multiply/{number}")
#    - Accept a number from the URL path.
#    - Return the result of that number multiplied by 5.
#    - Example:
#        Request: GET /multiply/6
#        Response: {"number": 6, "result": 30}
#
# 3️⃣ Square Endpoint ("/square/{number}")
#    - Accept a number from the URL path.
#    - Return the square of that number.
#    - Example:
#        Request: GET /square/4
#        Response: {"number": 4, "result": 16}
#
# ✅ Hints:
# - Use @app.get() for both endpoints.
# - Use path parameters {number} and type hints (int).
# - Return a dictionary so FastAPI will automatically convert it to JSON.
