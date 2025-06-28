# -*- encoding: utf-8 -*-

from apps.charts import blueprint
from flask import render_template
from apps.models import Product

@blueprint.route('/charts')
def charts():
    products = [{'name': product.name, 'price': product.price} for product in Product.get_list()]
    return render_template('charts/index.html', parent="apps", segment='charts', products=products)