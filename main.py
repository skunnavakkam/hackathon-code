from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html', message="")
    if request.method == 'POST':
        text = request.form["handle"].strip()
        
        if text != "":
            return redirect(url_for('politician', handle=text))
        else:
            return render_template('index.html', message="The handle cannot be blank")

@app.route('/politician/<handle>')
def politician(handle):
    return render_template('politician.html', handle=handle)