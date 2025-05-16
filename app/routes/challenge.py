from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import Challenge, ChallengeCompletion
from app.extensions import db
from flask_login import login_required, current_user

challenge_bp = Blueprint('challenge', __name__, url_prefix='/challenges')

@challenge_bp.route('/')
@login_required
def today_challenge():
    challenge = Challenge.query.order_by(Challenge.id.desc()).first()
    completed = ChallengeCompletion.query.filter_by(user_id=current_user.id, challenge_id=challenge.id).first() if challenge else None
    return render_template('challenges/today.html', challenge=challenge, completed=completed)

@challenge_bp.route('/complete/<int:challenge_id>', methods=['POST'])
@login_required
def complete_challenge(challenge_id):
    completion = ChallengeCompletion(user_id=current_user.id, challenge_id=challenge_id)
    db.session.add(completion)
    db.session.commit()
    flash('Challenge marked as completed!')
    return redirect(url_for('challenge.today_challenge'))
