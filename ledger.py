from flask import Flask, render_template, request, redirect, url_for, session
import ledger_bk  # Assuming your database functions are in ledger_bk.py

app = Flask(__name__)
app.secret_key = 'your_secret_key' 
ADMIN_PASSWORD = "Karan@143"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        password = request.form['password']
        if password == ADMIN_PASSWORD:
            session['is_admin'] = True  # Set session variable for admin access
            return redirect(url_for('admin_actions'))
        else:
            return "Invalid password. Please try again."
    return render_template('admin_login.html')

@app.route('/admin_actions')
def admin_actions():
    if not session.get('is_admin'):
        return redirect(url_for('admin_login'))  # Redirect to login if not admin
    return render_template('admin_actions.html')

@app.route('/logout')
def logout():
    session.pop('is_admin', None)  # Remove admin session
    return redirect(url_for('home'))

@app.route('/add', methods=['GET', 'POST'])
def add_account():
    if request.method == 'POST':
        name = request.form['name']
        user = request.form['user']
        password = request.form['password']
        category = request.form['category']
        cdate = request.form['cdate']
        ledger_bk.add(name, user, password, category, cdate)  # Call the add function from ledger_bk
        return redirect(url_for('home'))  # Redirect to home after adding
    return render_template('add.html')

@app.route('/view')
def view_all():
    rows = ledger_bk.viewall()
    return render_template('view.html', rows=rows)

@app.route('/update', methods=['GET', 'POST'])
def update_account():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        user = request.form['user']
        password = request.form['password']
        category = request.form['category']
        cdate = request.form['cdate']
        ledger_bk.update(id, name, user, password, category, cdate)  # Call the update function from ledger_bk
        return redirect(url_for('view_all'))  # Redirect to view all accounts after updating
    return render_template('update.html')  # Render update form

@app.route('/delete', methods=['GET', 'POST'])
def delete_account():
    if request.method == 'POST':
        id = request.form['id']
        ledger_bk.delete(id)  # Call the delete function from ledger_bk
        return redirect(url_for('view_all'))  # Redirect to view all accounts after deleting
    return render_template('delete.html')  # Render delete form

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_value = request.form['search_value']  # Get the search value from the form
        search_type = request.form['search_type']  # Get the search type from the form
        rows = ledger_bk.search(search_value, search_type)  # Call the search function
        return render_template('view.html', rows=rows)  # Render the results
    return render_template('search.html')

if __name__ == '__main__':
    ledger_bk.create()  # Ensure the database and table are created
    app.run(debug=True)