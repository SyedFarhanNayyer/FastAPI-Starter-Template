from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_PASSWORD")

URI = ""
CLIENT = MongoClient("")
DB = CLIENT["Test"]
COLLECTION = DB["Plants"]
COLLECTION_USER = DB["Users"]