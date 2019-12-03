from flask import Flask, g, escape, session, redirect, render_template, request, jsonify, Response


app = Flask(__name__)
app.secret_key = '#$ab9&^BB00_.'

# Setting DAO Class
from Models.DAO import DAO

DAO = DAO(app)

# Registering blueprints
from routes.user import user_manager
from routes.book import book_manager
from routes.admin import admin_manager

app.register_blueprint(user_manager)
app.register_blueprint(book_manager)
app.register_blueprint(admin_manager)