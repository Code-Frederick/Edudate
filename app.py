from flask import Flask, render_template
from data import get_data

app = Flask(__name__)

Tutors = get_data()

@app.route('/')
def index():
    return render_template('index.html', tutors = Tutors)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/category/<string:category>/')
def category(category):
    mastered_tutors = []
    cap_cat = category.capitalize()
    if (category == "languages"):
        print("Yay")
        cap_cat = "Foreign Language"
    if (category == "standardized"):
        cap_cat = "Standardized Testing"
    if (category == "cs"):
        cap_cat = "Computer Science"
    for tutor in Tutors:
        if (tutor.subject.find(cap_cat) >= 0):
            mastered_tutors.append(tutor)
    return render_template('category.html', tutors = mastered_tutors, category = cap_cat)

@app.route('/tutors/<string:id>/')
def tutor(id):
    index = int(id) - 1
    return render_template('tutor.html', id = id, tutor = Tutors[index])

if __name__ == '__main__':
    app.run(debug=True)