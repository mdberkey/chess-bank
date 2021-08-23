from flask import Blueprint, render_template, request, flash
from flask_login import current_user
from . import db
from .models import Game
import re

# starts blueprint
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/dashboard')
def dashboard():
    games = current_user.games
    return render_template('dashboard.html', name=current_user.name, data=games, stats=get_stats())


@main.route('/dashboard', methods=['POST', 'GET'])
def dashboard_add():
    games = current_user.games
    try:
        link = request.form.get('link')

        if not check_url(link):
            flash('Please enter a valid link. Example: https://lichess.org/F7vL9PtciyjI')
            return render_template('dashboard.html', name=current_user.name, data=games, stats=get_stats())
        elif not Game.query.filter_by(link=link).first() == None:
            flash('That link has already been submitted to your collection. Please submit a different link.')
            return render_template('dashboard.html', name=current_user.name, data=games, stats=get_stats())

        name = request.form.get('name')
        outcome = request.form.get('outcome')
        notes = request.form.get('notes')
        game = Game(link=link, name=name, outcome=outcome, notes=notes, player=current_user)
        db.session.add(game)
        db.session.commit()
    except Exception as e:
        print('Failed to add game.')
        print(e)
    games = current_user.games
    return render_template('dashboard.html', name=current_user.name, data=games, stats=get_stats())


@main.route('/delete', methods=['POST'])
def dashboard_delete():
    link = request.form.get('link')
    game = Game.query.filter_by(link=link).first()
    db.session.delete(game)
    db.session.commit()
    games = current_user.games
    return render_template('dashboard.html', name=current_user.name, data=games, stats=get_stats())


def check_url(link):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, link) is not None


def get_stats():
    games = Game.query.filter_by(player=current_user)
    wins = 0
    losses = 0
    stales = 0
    total = 0
    for game in games:
        if game.outcome == 0:
            wins += 1
        elif game.outcome == 1:
            losses += 1
        else:
            stales += 1
        total += 1
    win_perc = round(wins / total * 100, 2)
    loss_perc = round(losses / total * 100, 2)
    stale_perc = round(stales / total * 100, 2)
    return [wins, losses, stales, win_perc, loss_perc, stale_perc, total]
