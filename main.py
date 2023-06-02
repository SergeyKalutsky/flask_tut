# HTML, CSS, Маршруты(статические), Разного рода запросы GET и POST
# 1 Динамическая маршрутизация
# 2 JINJA 2
# 3 БД


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/contacts")
def contacts():
    return render_template('contacts.html')


@app.route("/items")
def items():
    return render_template('items.html')


@app.route("/login", methods=['GET', 'POST'])
def login_form():
    login = 'admin'
    password = '12345'
    if request.method == 'POST':
        if request.form['login'] == login and request.form['password'] == password:
            return redirect(url_for('hello_world'))
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)

# Создать директорию проекта
# Установить Flask
# Запустить файл
