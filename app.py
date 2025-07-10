from flask import Flask, render_template, jsonify, request
from database import load_books, add_email_to_email_list

app = Flask(__name__)

# ✅ Single route that handles both GET and POST for the one-page site
@app.route("/", methods=["GET", "POST"])
def home():
    success = False

    if request.method == "POST":
        email = request.form["email"]
        add_email_to_email_list(email)
        success = True

    books = load_books()
    return render_template("blog.html", books=books, success=success)

# ✅ Separate route to serve API if needed
@app.route("/api/books")
def list_books():
    books = load_books()
    return jsonify(books)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
