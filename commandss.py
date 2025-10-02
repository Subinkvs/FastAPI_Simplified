"""
FastAPI Overview
================

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ 
based on standard Python type hints.

Key Features:
-------------

1. Asynchronous-Friendly:
   - FastAPI supports asynchronous programming using `async` and `await`.
   - This means it can handle multiple HTTP requests at the same time without blocking.
   - Example: Multiple users hitting the API simultaneously can be served concurrently,
     even if some requests involve time-consuming tasks like database queries or 
     external API calls.

2. Automatic Data Validation:
   - Uses Pydantic models to validate request data automatically.
   - Reduces boilerplate code for input validation.

3. Automatic Documentation:
   - Generates interactive API docs using Swagger UI and ReDoc.
   - Docs are automatically updated based on your endpoints and type hints.

4. High Performance:
   - Built on Starlette (for async support) and Pydantic (for data validation).
   - Comparable speed to NodeJS and Go for typical web APIs.

5. Easy Integration:
   - Can be integrated with databases, background tasks, authentication, and more.
   - Supports both synchronous and asynchronous endpoints.

6. Type Hints and Editor Support:
   - Python type hints enable better code completion and error checking in IDEs.
   - Helps catch errors before running the application.

Asynchronous Behavior:
---------------------

- In a synchronous API, each request is handled one by one. 
  Slow requests can block others.
- In FastAPI (async):
  - Using `async def` endpoints and `await`, multiple requests can be processed concurrently.
  - Example:
      @app.get("/wait")
      async def wait_seconds():
          await asyncio.sleep(5)
          return {"message": "Done waiting!"}

- Benefits:
  1. Faster response times under heavy load
  2. Efficient handling of I/O-bound operations
  3. Non-blocking execution for multiple clients

Conclusion:
-----------

FastAPI makes building modern APIs easier, faster, and more reliable by leveraging Python's 
async capabilities, automatic validation, and built-in documentation.
"""

# 1️⃣ Install FastAPI
# pip install fastapi

# 2️⃣ Install Uvicorn (ASGI server to run FastAPI apps)
# pip install "uvicorn[standard]"

# 3️⃣ Create a Python file, e.g., main.py
# (Use any text editor or IDE to create this file)

# 4️⃣ Run the FastAPI app using Uvicorn
# uvicorn main:app --reload
# Explanation:
# - main → Python file name (main.py)
# - app → FastAPI instance name
# - --reload → Automatically reloads server on code changes

# 5️⃣ Open API in browser:
# Root endpoint: http://127.0.0.1:8000/
# Path parameter example: http://127.0.0.1:8000/hello/YourName