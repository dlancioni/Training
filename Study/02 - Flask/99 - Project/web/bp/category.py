from flask.blueprints import Blueprint
from src.models.category import Category

bp_category = Blueprint('bp_category', __name__, template_folder='templates', static_folder='static')

@bp_category.route('/category_list')
def category_list():
  category = Category.query.filter_by(name="Food").first()
  return "Test: Category %s " % category.name