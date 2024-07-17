import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = 'SECRETKEY'
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin_task_management:admintaskmanagement@localhost/task_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'JWTSECRET'
