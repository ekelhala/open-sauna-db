from os import getenv
from mongoengine import connect
from dotenv import load_dotenv

def init():
    """
    Initializes the database connection 
    by first configuring environment variables with `config_dotenv`, 
    and then connects to the MongoDB database by using the environment 
    variable `MONGODB_URI`
    """
    load_dotenv()
    connect(db="db", host=getenv("MONGODB_URI"))
