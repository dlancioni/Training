from blogapp import db
db.drop_all()
db.create_all()
from blogapp.models import User, Post

# Add data
db.session.add( User(username="David", email="david@demo.com") )
db.session.add( User(username="Renata", email="renata@demo.com") )
db.session.add( Post(title="Blog1", content="First post content from David", user_id = 1) )
db.session.add( Post(title="Blog2", content="Second post content from David", user_id = 1) )
db.session.add( Post(title="Blog1", content="First post content from Renata", user_id = 2) )
db.session.commit()

# Query data
User.query.all()
User.query.filter_by(username="David").all()
user = User.query.filter_by(username="David").first()
user = User.query.get(2)

# Get posts for each user (inner join equivalent)
User.query.get(2).posts
User.query.filter_by(username="Renata").first().posts
