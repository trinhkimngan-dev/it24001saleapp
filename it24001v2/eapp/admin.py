from flask_admin.contrib.sqla import ModelView

from eapp.models import Category,Product

from eapp import app, db
from flask_admin import Admin

admin = Admin(app=app, name="E-Commerce's Admin")

class ProductView(ModelView):
    column_list = ['id', 'name', 'active', 'category_id']
    column_searchable_list = ['name']
    can_export = True
    edit_modal =  True
    column_editable_list = ['name']
    column_filters = ['name', 'price']

admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))