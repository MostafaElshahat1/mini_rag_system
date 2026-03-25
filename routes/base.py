from fastapi import FastAPI, APIRouter
import os

base_router = APIRouter(
    prefix="/api/v1", # Add a prefix to all routes in this router this prefix is writen in the api before the / in the app.get and also for better organization and versioning and this will help in future when we want to add new versions of the API without breaking existing clients. It also makes it clear that these routes belong to version 1 of the API.
    tags=["api_v1"]
)

@base_router.get("/")
def welcome():
    app_name =os.getenv("APP_NAME") # Get the application name from environment variables, with a default value of "FastAPI Application" if not set. This allows us to easily configure the application name without hardcoding it in the code, making it more flexible and adaptable to different environments.
    app_version = os.getenv("APP_VERSION") # Get the application version from environment variables, with a default value of "1.0.0" if not set. This allows us to easily manage and update the application version without modifying the code, making it easier to maintain and track changes across different versions of the application
    
    return {"app_name": app_name, "app_version": app_version}