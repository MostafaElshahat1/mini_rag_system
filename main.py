from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env") # Load environment variables from the .env file. This allows us to keep sensitive information like API keys and database credentials out of our codebase and instead store them in a separate file that can be easily managed and secured. By calling load_dotenv(".env"), we ensure that all the environment variables defined in the .env file are available to our application, making it easier to configure and maintain our application across different environments (development, staging, production).

from routes import base

app = FastAPI()

app.include_router(base.base_router)
