from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import APIRouter

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
        <html>
            <head>
                <title>FastAPI with Swagger UI</title>
                <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css" />
            </head>
            <body>
                <h1>FastAPI with Swagger UI</h1>
                <div id="swagger-ui"></div>

                <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
                <script>
                    SwaggerUIBundle({
                        url: "/openapi.json",
                        dom_id: '#swagger-ui',
                    });
                </script>
            </body>
        </html>
    """

# Route for serving the OpenAPI schema
@app.get("/openapi.json")
def get_open_api_endpoint():
    return JSONResponse(get_openapi(title="FastAPI with Swagger UI", version="1.0", routes=app.routes))

# Additional routes for your API
router = APIRouter()

@router.get("/items/")
def read_items():
    return {"Hello": "World"}

app.include_router(router, prefix="/api")

# Serve static files (e.g., the Swagger UI) from the '/static' directory
app.mount("/static", StaticFiles(directory="/app/static"), name="static")
