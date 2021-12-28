from models.user import User
from flask.blueprints import Blueprint

mod_user = Blueprint('mod_user', __name__, template_folder='templates', static_folder='static')

@mod_user.route('/user_list')
def test():
  user = User.query.filter_by(username="Tom").first()
  return "Test: Username %s " % user.username