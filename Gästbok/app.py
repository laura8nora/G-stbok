from flask import Flask, request, render_template_string
import os

from datetime import datetime


app = Flask(__name__)

APPEND_FILE = 'append_demo.txt'

HTML = '''
<!doctype html>
<title>Append File</title>
<h2>Append to File???</h2>
<form method="post" action="/append">
    <input type="text" name="line3" size="40" placeholder="Name"><br><br>
    <input type="text" name="line" size="40" placeholder="Enter text to append"><br><br>
    <input type="text" name="line2" size="40" placeholder="Email"><br><br>
    <input type="submit" value="Append">
</form>
<h2>File Contents</h2>
<pre>{{ file_content }}</pre>
'''

@app.route('/', methods=['GET'])
def append_demo():
    content = ''
    if os.path.exists(APPEND_FILE):
        with open(APPEND_FILE, 'r', encoding='utf-8') as f: 
            content = f.read()
    return render_template_string(HTML, file_content=content)

@app.route('/append', methods=['POST'])
def append():
    line = request.form.get('line', '').strip()
    line2 = request.form.get('line2', '').strip()
    line3 = request.form.get('line3', '').strip()

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(APPEND_FILE, 'a', encoding='utf-8') as f:
        f.write(f"Time: {now}\n")

        if line:
            f.write(f"Text: {line}\n")
        if line2:
            f.write(f"Email: {line2}\n")
        if line3:
            f.write(f"Name: {line3}\n")
        f.write('-' * 20 + '\n')


    with open(APPEND_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    return render_template_string(HTML, file_content=content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
