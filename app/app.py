import os
import psycopg2
from flask import Flask, request, redirect

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'postgres-service'),
        database=os.environ.get('POSTGRES_DB', 'tododb'),
        user=os.environ.get('POSTGRES_USER', 'todouser'),
        password=os.environ.get('POSTGRES_PASSWORD', 'todopass')
    )

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            task TEXT NOT NULL
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def home():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT id, task FROM todos ORDER BY id')
    todos = cur.fetchall()
    cur.close()
    conn.close()

    items = ''.join(
        f'<li style="margin:8px 0">{t[0]}. {t[1]} '
        f'<a href="/done/{t[0]}" style="color:green">done</a></li>'
        for t in todos
    )
    return f'''
    <html>
    <body style="font-family:Arial; max-width:500px; margin:40px auto">
        <h2>To-Do App v3 - CI/CD Works!</h2>
        <form method="POST" action="/add">
            <input name="task" placeholder="Enter a task"
                style="padding:8px; width:300px"/>
            <button type="submit" style="padding:8px 16px">Add</button>
        </form>
        <ul style="margin-top:20px">{items}</ul>
    </body>
    </html>
    '''

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        conn = get_db()
        cur = conn.cursor()
        cur.execute('INSERT INTO todos (task) VALUES (%s)', (task,))
        conn.commit()
        cur.close()
        conn.close()
    return redirect('/')

@app.route('/done/<int:task_id>')
def done(task_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM todos WHERE id = %s', (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

with app.app_context():
    try:
        init_db()
    except Exception as e:
        print(f"DB init failed: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)