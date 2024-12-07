from flask import Flask, render_template, url_for, request, redirect, session, jsonify, abort
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from models import db, user, task
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt
from sqlalchemy.exc import SQLAlchemyError


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' 
# 3 slashes is relative path, 4 slashes is absolute path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

@app.route('/', methods=['POST', 'GET'])
@login_required
def index():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'content' not in data:
            abort(400, description="Invalid task data. 'content' field is required.")

        new_task = task(content=data['content'], user_id=current_user.id, completed=0)

        try:
            db.session.add(new_task)
            db.session.commit()
            return jsonify({
                "id": new_task.id, 
                "content": new_task.content, 
                "completed": new_task.completed, 
                "date_created": new_task.date_created.date()
                }), 201
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, description=f"There was an issue adding your task: {str(e)}")
    else:
        tasks = task.query.filter_by(user_id=current_user.id).all()
        return render_template('index.html', tasks=tasks)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password').encode('utf-8')

        user_data = user.query.filter_by(username=username).first()

        if user_data:
            if bcrypt.checkpw(password, user_data.password):
                login_user(user_data)
                return redirect('/')
            else:
                abort(401, description="Invalid password")
        else:
            abort(404, description="User not found")
        
    return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password').encode('utf-8')
        confirmation = request.form.get('confirmation').encode('utf-8')

        if password != confirmation:
            abort(400, description="Passwords do not match")

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password, salt)
        new_user = user(username=username, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
        
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, description=f"There was an issue creating your account: {str(e)}")
        
    return render_template('signup.html')

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/api/tasks/<int:id>', methods=['DELETE'])
@login_required
def delete_task(id):
    task_to_delete = task.query.get_or_404(id)
    if task_to_delete and task_to_delete.user_id != current_user.id:
        abort(403, description="Unauthorized to delete this task")
       
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return 'Task deleted', 204
    except SQLAlchemyError as e:
        db.session.rollback()
        abort(500, description=f"There was an issue deleting the task: {str(e)}")      

@app.route('/api/tasks/<int:id>', methods=['PUT'])
@login_required
def toggle_task(id):
    task_to_toggle = task.query.get_or_404(id, description="Task not found")
    if task_to_toggle.user_id != current_user.id:
        abort(403, description="Unauthorized to update this task")

    data = request.get_json()
    if not data or 'completed' not in data:
        abort(400, description="Invalid task data. 'completed' field is required.")
    
    try:
        task_to_toggle.completed = data['completed']
        db.session.commit()
        return jsonify({
            'message': 'Task updated', 
            'task_id': task_to_toggle.id,
            'completed': task_to_toggle.completed
            }), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        abort(500, description=f"There was an issue updating the task: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)