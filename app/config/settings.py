import os

from dotenv import load_dotenv

# Reads DB credentials from a local .env file (never committed to git).
load_dotenv()

MYSQL_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME", "trade_pipeline_db"),
}
