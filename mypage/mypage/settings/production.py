from .base import *
from dotenv import load_dotenv
load_dotenv()
#noqa
DEBUG = False
ALLOWED_HOSTS = [".vercel.app", "127.0.0.1"]
SECRET_KEY = os.getenv("SECRET_KEY")