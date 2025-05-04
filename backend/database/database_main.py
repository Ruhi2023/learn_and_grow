# this file will connect to database
from sqlalchemy import create_engine
from ..utils.cred_utils import Credentials_helper
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQL_ALCHMY_DATABASE_URL = '[type_of_database]://<username>:<password>@<host>:<port>/<database_name>'
cre_hlp = Credentials_helper()
SQL_ALCHMY_DATABASE_URL = cre_hlp.get_postgres_connection_string()

engine = create_engine(SQL_ALCHMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

