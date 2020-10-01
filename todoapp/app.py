# Import Flask and SQLAlchemy to allow Python access to script to the database with Object Relational Mapping
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Set the flask instance to an app variable for later use
app = Flask(__name__)
# Defind the SQLAlchemy database connection string syntax postgresql://username:password@URL:port/databasename
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/todoapp'
# Flask debug mode for live reloading in development mode
app.run(debug=True)

# Set a db instance to link the SQLAlchemy library to interact with the database
db = SQLAlchemy(app)

# Set a todo class to inherit from db.Model, with attributes mapped to the tablename and columns
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

# Detect models and create tables for them (if they don't exist already)
db.create_all()

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all()
    )

@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.form.get('description', '')
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__': 
 app.run()