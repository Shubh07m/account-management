from flask import Flask, render_template, request, redirect, url_for
import ledger_bk

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view')
def view_all():
    rows = ledger_bk.viewall()
    return render_template('view.html', rows=rows)

@app.route('/add', methods=['POST'])
def add_account():
    name = request.form['name']
    user = request.form['user']
    password = request.form['password']
    category = request.form['category']
    cdate = request.form['cdate']
    ledger_bk.add(name, user, password, category, cdate)
    return redirect(url_for('view_all'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        name = request.form['name']
        user = request.form['user']
        password = request.form['password']
        category = request.form['category']
        rows = ledger_bk.search(name=name, user=user, password=password, category=category)
        return render_template('view.html', rows=rows)
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True)
