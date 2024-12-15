from flask import Flask, render_template, request

app = Flask(__name__)

students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 95},
    {"name": "David", "score": 88},
]

@app.route("/")
def index():
    top_student = max(students, key=lambda x: x['score'])
    return render_template("index.html", students=students, top_student=top_student)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
