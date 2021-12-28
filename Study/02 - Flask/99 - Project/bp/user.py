from models.user import User
from flask.blueprints import Blueprint

bp_user = Blueprint('bp_user', __name__, template_folder='templates', static_folder='static')

@bp_user.route('/user_list')
def user_list():
  try:
      users = User.query.all()
      users = [user.username for user in users]
  except Exception:
      users = "Something went wrong"
      
  return "Userlist: %s " % users