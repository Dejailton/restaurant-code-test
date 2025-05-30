from flask import Blueprint, render_template, request, redirect, url_for
from app.restaurant import RestaurantApp

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        pedido = request.form.get('pedido')
        restaurant = RestaurantApp()
        dishes = restaurant.process_order(pedido)

        return render_template("homepage.html", dishes=dishes)
    return render_template("homepage.html")