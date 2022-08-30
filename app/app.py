from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return "<h1>¡Estoy aprendiendo python :D!</h1>"
    courses = ['PHP', 'Python', 'Java', 'Kotlin', 'Dart', 'JavaScript']
    data = {
        'title': 'Index123',
        'welcome': '¡Saludos!',
        'courses': courses,
        'courses_number': len(courses),
    }
    return render_template('index.html', data=data)


@app.route('/contact/<name>/<int:age>')
def contact(name, age):
    data = {
        'title': 'Contacto',
        'name': name,
        'age': age
    }
    return render_template('contact.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
