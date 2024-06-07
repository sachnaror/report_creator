## JSON Extractor from  spreadsheet uplaod

## API Documentation with Swagger

This repository is jango with API endpoints documented using Swagger (check views.py and load your own xlsx sheet to run and see the JSON results). This `README.md` file explains how to set up and use Swagger to document our Django API.

## Setup

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/sachnaror/report_creator.git
    ```

2. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

## Usage

1. API endpoints in the Django project's `urls.py` file.

2. Created a separate YAML or JSON file to hold our Swagger/OpenAPI configuration. You can name this file `swagger.yaml`.

3. Defined the paths, operations, request/response formats, parameters, and headers in your Swagger configuration file. Refer to the [Swagger Specification](https://swagger.io/specification/) for details on how to structure this configuration.

4. Because i'm using Swagger UI, Swagger Editor, or ReDoc to generate API documentation, I'm referencing this Swagger configuration file in the tool's settings or configuration.

5. Start Django development server and navigate to the API documentation URL (e.g., `http://localhost:8000/swagger/`) to view the interactive API documentation generated from this Swagger configuration.

## Example

Here's an example of how you might define a file upload endpoint in Swagger YAML format:

```yaml
openapi: 3.0.0
info:
  title: My API
  version: 1.0.0
paths:
  /api/upload/:
    post:
      summary: Upload a file
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
      responses:
        '201':
          description: File uploaded successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  file_url:
                    type: string
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string



