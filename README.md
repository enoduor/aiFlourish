
# MyInsightIQ AI Tools API Service

## Overview

The Tools API Service is a microservice designed to manage and provide information about various tools and their categories. It allows users to browse tools, view detailed descriptions, and access links to external resources. This service is built using Django Rest Framework (DRF) and follows RESTful principles.

## Features

- Browse and filter tools by category.
- View detailed descriptions of tools.
- Access external links to tool websites and video use cases.
- Built-in support for microservices architecture.

## Installation

### Prerequisites

- Python 3.6 or higher
- Django 3.2 or higher
- Django Rest Framework
- PostgreSQL (or any other database of your choice)

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/tools-api.git
   cd tools-api
   ```

2. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:

   Ensure your database settings are configured in `settings.py`. Run the following commands to create the database tables:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser** (optional):

   To access the admin panel, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

   The API will be accessible at `http://localhost:8000`.

## API Endpoints

### Tools

- **GET /api/tools/**
  - Retrieve a list of all tools.
  
- **GET /api/tools/{id}/**
  - Retrieve detailed information about a specific tool.
  
- **POST /api/tools/**
  - Create a new tool (Admin only).
  
- **PUT /api/tools/{id}/**
  - Update an existing tool (Admin only).
  
- **DELETE /api/tools/{id}/**
  - Delete a tool (Admin only).

### Categories

- **GET /api/categories/**
  - Retrieve a list of all categories.
  
- **GET /api/categories/{id}/**
  - Retrieve detailed information about a specific category.

## Testing the API Endpoints

You can test the following API endpoints using **cURL** or **Postman**:

### 1. Browse Tools
**GET** `/api/tools/`

```bash
curl -X GET http://localhost:8000/api/tools/
```
*Expected Response:* A list of all tools in JSON format.

### 2. View Tool Details
**GET** `/api/tools/<tool_id>/`

```bash
curl -X GET http://localhost:8000/api/tools/1/
```
*Expected Response:* Details of the tool with ID 1 in JSON format.

### 3. Filter Tools by Category
**GET** `/api/tools/?category=<category_id>`

```bash
curl -X GET "http://localhost:8000/api/tools/?category=1"
```
*Expected Response:* A list of tools filtered by the specified category ID in JSON format.

### 4. Search Tools
**GET** `/api/tools/?search=<query>`

```bash
curl -X GET "http://localhost:8000/api/tools/?search=example"
```
*Expected Response:* A list of tools matching the search query in JSON format.

### 5. Create New Tool
**POST** `/api/tools/`

```bash
curl -X POST http://localhost:8000/api/tools/ \
-H "Content-Type: application/json" \
-d '{
    "name": "New Tool",
    "description": "Description of the new tool",
    "category": 1,
    "website": "https://example.com",
    "video": "https://youtube.com/example"
}'
```
*Expected Response:* The created tool's details in JSON format, including a unique ID.

### 6. Edit Existing Tool
**PUT** `/api/tools/<tool_id>/`

```bash
curl -X PUT http://localhost:8000/api/tools/1/ \
-H "Content-Type: application/json" \
-d '{
    "name": "Updated Tool Name",
    "description": "Updated description of the tool",
    "category": 1,
    "website": "https://example.com",
    "video": "https://youtube.com/example"
}'
```
*Expected Response:* The updated tool's details in JSON format.

### 7. Delete Tool
**DELETE** `/api/tools/<tool_id>/`

```bash
curl -X DELETE http://localhost:8000/api/tools/1/
```
*Expected Response:* A confirmation message indicating that the tool has been deleted (e.g., `{"message": "Tool deleted successfully."}`).

### 8. Fetch Categories
**GET** `/api/categories/`

```bash
curl -X GET http://localhost:8000/api/categories/
```
*Expected Response:* A list of all categories in JSON format.

## Testing

To run the tests, use the following command:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### How to Save:
1. Open your text editor or IDE.
2. Find your `README.md` file in your project.
3. Replace the existing content with the updated content above.
4. Save the file.