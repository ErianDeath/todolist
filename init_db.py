from app import app
from models import db, user, task

print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])

with app.app_context():
    db.create_all()
    print('Database initialised!')
    print('Tables:', db.engine.table_names())