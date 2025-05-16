from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import MovieSuggestion
from app.extensions import db
from flask_login import login_required, current_user

movies_bp = Blueprint('movies', __name__, url_prefix='/movies')

@movies_bp.route('/', methods=['GET', 'POST'])
@login_required
def suggest_movie():
    if request.method == 'POST':
        title = request.form.get('title')
        if title:
            suggestion = MovieSuggestion(user_id=current_user.id, title=title)
            db.session.add(suggestion)
            db.session.commit()
            flash('Movie suggested!')
    suggestions = MovieSuggestion.query.order_by(MovieSuggestion.id.desc()).all()
    return render_template('movies/suggestions.html', suggestions=suggestions)
