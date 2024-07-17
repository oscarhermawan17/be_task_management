# seed.py
from app import create_app, db
from app.models import User, Task

app = create_app()

with app.app_context():
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()

    # Create initial users
    admin = User(username='admin')
    admin.set_password('admin')
    oscar = User(username='oscar')
    oscar.set_password('oscar')

    # Add users to the session
    db.session.add(admin)
    db.session.add(oscar)
    db.session.commit()

    # Create tasks for admin
    task1_admin = Task(title='Task 1', description='Task Admin', status='Pending', user_id=admin.id)
    task2_admin = Task(title='Task 2', description='Task Admin On Progress', status='In Progress', user_id=admin.id)

    # Create tasks for oscar
    task1_oscar = Task(title='Task Oscar 1', description='Javascript', status='Completed', user_id=oscar.id)
    task2_oscar = Task(title='Task Oscar 2', description='Python', status='In Progress', user_id=oscar.id)

    # Add tasks to the session
    db.session.add(task1_admin)
    db.session.add(task2_admin)
    db.session.add(task1_oscar)
    db.session.add(task2_oscar)

    # Commit the session
    db.session.commit()

    print("Database seeded with initial data!")
