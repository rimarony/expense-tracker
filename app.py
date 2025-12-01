from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

DB = 'expenses.db'

def init_db():
    if not os.path.exists(DB):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute('''CREATE TABLE expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            description TEXT,
            date TEXT
        )''')
        conn.commit()
        conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = c.fetchall()
    conn.close()
    return render_template('index.html', expenses=rows)

@app.route('/add', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    category = request.form['category']
    description = request.form['description']
    date = request.form['date']
    
@app.route('/delete/<int:id>')
def delete_expense(id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')


    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
              (amount, category, description, date))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

