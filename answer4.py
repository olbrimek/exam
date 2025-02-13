from flask import Flask, request, render_template_string, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection function
def connect_db():
    conn = sqlite3.connect('exam2.db')
    return conn

# HTML template for the form
form_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Reader Registration</title>
    </head>
    <body>
        <h2>Register Reader</h2>
        {% if error %}
            <p style="color:red;">{{ error }}</p>
        {% endif %}
        <form method="POST" action="/">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name"><br><br>

            <label for="email">Email:</label><br>
            <input type="text" id="email" name="email"><br><br>

            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
'''

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']


        if not name:
            error = "Name cannot be empty."
            return render_template_string(form_html, error=error)
        if '@' not in email:
            error = "Email must contain an '@' sign."
            return render_template_string(form_html, error=error)


        try:
            conn = connect_db()
            cursor = conn.cursor()


            cursor.execute("INSERT INTO Readers (name, email) VALUES (?, ?)", (name, email))


            conn.commit()
            conn.close()


            return redirect(url_for('register'))

        except sqlite3.Error as e:
            error = f"Database error: {str(e)}"
            return render_template_string(form_html, error=error)


    return render_template_string(form_html, error=None)

if __name__ == '__main__':
    app.run(debug=True)