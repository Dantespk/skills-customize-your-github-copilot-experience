# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern REST APIs using the FastAPI framework. You'll create endpoints that handle HTTP requests, work with request/response data, and implement data validation using Pydantic models.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI and Create Your First Endpoint

#### Description
Initialize a FastAPI application and create a simple GET endpoint that returns data. This task introduces you to FastAPI's basic structure and how to run a web server locally.

#### Requirements
Completed program should:

- Import FastAPI and uvicorn
- Create a FastAPI application instance
- Define at least one GET endpoint that returns a JSON response
- Run the server using `uvicorn main:app --reload`
- Successfully respond to requests at `http://localhost:8000/`

### 🛠️ Task 2: Build Multiple Endpoints with Different HTTP Methods

#### Description
Expand your API by adding multiple endpoints that handle different HTTP methods (GET, POST, PUT, DELETE). This task teaches you how to manage different types of requests and perform CRUD operations.

#### Requirements
Completed program should:

- Include at least one GET endpoint to retrieve data
- Include at least one POST endpoint to create data
- Include at least one PUT endpoint to update data
- Include at least one DELETE endpoint to remove data
- Return appropriate HTTP status codes for each operation
- Include a simple in-memory data structure (list or dictionary) to store/retrieve data

### 🛠️ Task 3: Implement Data Validation with Pydantic Models

#### Description
Create Pydantic models to validate request and response data. This task teaches you how to ensure data integrity by defining schemas and handling validation errors automatically.

#### Requirements
Completed program should:

- Define at least two Pydantic models for request and response data
- Use these models in endpoint function parameters and return types
- Validate incoming request data automatically
- Return appropriate error messages (400 Bad Request) when validation fails
- Use type hints throughout the code

### 🛠️ Task 4: Add Error Handling and Documentation (Stretch Goal)

#### Description
Enhance your API with proper error handling and auto-generated documentation. FastAPI automatically generates interactive API documentation that makes testing and understanding your API easier.

#### Requirements
Completed program should:

- Implement custom exception handlers for common errors
- Use HTTP exception handling with appropriate status codes
- Access the auto-generated interactive docs at `http://localhost:8000/docs`
- Include docstrings for all endpoints (they'll appear in the docs)
- Handle edge cases gracefully (e.g., requesting a non-existent item returns 404)
