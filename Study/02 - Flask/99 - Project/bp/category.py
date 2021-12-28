from models.category import Category
from flask.blueprints import Blueprint

bp_category = Blueprint('bp_category', __name__, template_folder='templates', static_folder='static')

@bp_category.route('/category_list')
def fn1():
  category = Category.query.filter_by(name="Food").first()
  return "Test: Category %s " % category.name