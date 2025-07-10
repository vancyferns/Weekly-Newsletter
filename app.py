from flask import Flask, render_template, jsonify
from database import engine, load_books
from sqlalchemy import text

app = Flask(__name__)

@app.route('/')
def hello_blog():
    books=load_books()
    return render_template('blog.html',books=books)

@app.route('/api/books')
def list_books():
    books=load_books()
    return jsonify(books)
    
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
