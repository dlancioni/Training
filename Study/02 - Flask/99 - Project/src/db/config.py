# https://docs.sqlalchemy.org/en/14/orm/queryguide.html#select-statements

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

sqlite_url = "sqlite:///src/db/ecommerce.dat"
sqlite_path = "src/db/ecommerce.dat"