

from email.mime import image
from flask import Blueprint, render_template, jsonify, request, redirect, flash
from flask_login import login_required, current_user
from .models import Game
from . import db


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    games = Game.query.all()
    return render_template('index.html', games=games)


@main.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html')


@main.route('/addgame', methods=['GET'])
@login_required
def addgame():
    return render_template('addgame.html')


@main.route('/api/addgame', methods=['POST'])
@login_required
def api_addgame():
    try:
        name = request.form['name']
        description = request.form['description']
        imageb64 = request.form['imageb64']
        game = Game(name=name, description=description, imageb64=imageb64)
        db.session.add(game)
        db.session.commit()
        return redirect('/')
    except:
        flash('Error while adding game')
        return redirect('/')


@main.route('/editgame/<int:id>', methods=['GET'])
@login_required
def editgame(id):
    game = Game.query.get(id)
    return render_template('editgame.html', game=game)


@main.route('/api/savegame/<int:id>', methods=['POST'])
@login_required
def api_savegame(id):
    try:
        name = request.form['name']
        description = request.form['description']
        imageb64 = request.form['imageb64']
        game = Game.query.get(id)
        game.name = name
        game.description = description
        game.imageb64 = imageb64
        db.session.commit()
        return redirect('/')
    except:
        flash('Error while saving game')
        return redirect('/')


@main.route('/api/deletegame/<int:id>', methods=['POST'])
@login_required
def api_deletegame(id):
    try:
        game = Game.query.get(id)
        db.session.delete(game)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(e)
        flash('Error while deleting game')
        return redirect('/')
