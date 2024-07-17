# seed.py
from app import create_app, db
from app.models import User, Task

app = create_app()
app.app_context().push()

def seed():
    db.drop_all()
    db.create_all()

    # Create a user
    user = User(username='admin', email='admin@example.com')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()

    # Create tasks for the user
    task1 = Task(title='Task 1', description='Description 1', status='In Progress', user_id=user.id)
    task2 = Task(title='Task 2', description='Description 2', status='Completed', user_id=user.id)
    db.session.add(task1)
    db.session.add(task2)
    db.session.commit()

if __name__ == '__main__':
    seed()
