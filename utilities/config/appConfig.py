from dotenv import load_dotenv
import os

class AppConfig:

    # Load environment variables from .env file
    load_dotenv()
    env = os.getenv("ENV")
    BASE_URL = f"https://app{env}.neodove.com/login"




