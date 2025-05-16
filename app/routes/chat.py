from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User, Message, Conversation
from app.extensions import db
from flask_login import login_required, current_user

chat_bp = Blueprint('chat', __name__, url_prefix='/chat')

@chat_bp.route('/')
@login_required
def chat_home():
    conversations = Conversation.query.filter(Conversation.users.any(id=current_user.id)).all()
    return render_template('chat/home.html', conversations=conversations)

@chat_bp.route('/start', methods=['GET', 'POST'])
@login_required
def start_conversation():
    if request.method == 'POST':
        username = request.form.get('username')
        user = User.query.filter_by(username=username).first()
        if user:
            conv = Conversation(users=[current_user, user])
            db.session.add(conv)
            db.session.commit()
            return redirect(url_for('chat.view_conversation', conv_id=conv.id))
        flash('User not found.')
    return render_template('chat/start.html')

@chat_bp.route('/<int:conv_id>', methods=['GET', 'POST'])
@login_required
def view_conversation(conv_id):
    conv = Conversation.query.get_or_404(conv_id)
    if request.method == 'POST':
        msg = Message(sender_id=current_user.id, conversation_id=conv_id, content=request.form.get('content'))
        db.session.add(msg)
        db.session.commit()
    messages = Message.query.filter_by(conversation_id=conv_id).all()
    return render_template('chat/conversation.html', conversation=conv, messages=messages)
