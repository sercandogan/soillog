from os.path import join, dirname
from dotenv import load_dotenv
from src.models import create_tables

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)

# Create DB and tables
create_tables()
