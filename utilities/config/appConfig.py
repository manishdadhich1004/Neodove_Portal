import os

class AppConfig:

    env = os.getenv('ENV')
    BASE_URL = f"https://app{env}.neodove.com/login"