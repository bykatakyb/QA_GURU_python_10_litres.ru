import os

from dotenv import load_dotenv

load_dotenv()
base_url = "https://api.litres.ru/foundation/api"
email = os.getenv('CUSTOMER_EMAIL')
password = os.getenv('RIGHT_CUSTOMER_PASSWORD')
wrong_password = os.getenv('WRONG_CUSTOMER_PASSWORD')
