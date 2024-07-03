from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_PORT = '5440'
DB_HOST = 'localhost'
DB_PASSWORD = 'postgres'
DB_USER = 'postgres'
DB_NAME = 'lecture'
DIALECT_DRIVER = 'postgresql+psycopg'

sync_engine = create_engine(f'{DIALECT_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=True)
session_factory = sessionmaker(sync_engine)
