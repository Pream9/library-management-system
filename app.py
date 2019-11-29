from flask import Flask, g, escape, session, redirect, render_template, request, jsonify, Response


app = Flask(__name__)
app.secret_key = '#$ab9&^BB00_.'

# Setting DAO Class
from Models.DAO import DAO

DAO = DAO(app)

# Registering blueprints
from routes.user import user_view as user_routes
from routes.admin import admin_view as admin_routes

app.register_blueprint(user_routes)
app.register_blueprint(admin_routes)