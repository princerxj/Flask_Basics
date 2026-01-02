### Building URL dynamically 
### Variable Rule 
### Jinja2 Template Engine 

### Jinja2 Template Engine
'''
{{ }} expressions to print output in html
{%...%} conditional statements, for loops
{#..#} this is used for writing comments
'''

from flask import Flask, render_template, request, redirect, url_for
'''
It creates the instance of the Flask Class, 
which will be our WSGI (Web Server Gateway Interface) application.
'''
#### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome() :
    return "<html><h1>Welcome to the flask Course.</h1></html>"

@app.route("/index", methods = ['GET'])
def welcomeIndex() :
    return render_template('index.html')

@app.route("/about")
def about() :
    return render_template('about.html')

# @app.route('/submit', methods = ['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form['name']
#         return f"Hello {name}!"
#     return render_template('form.html')

##Variable Rule
@app.route("/successres/<int:score>")
def successres(score) :
    res = ""
    if score >= 50:
        res = "PASS"
    else :
        res = "FAIL"

    exp = {'score' : score, 'res' : res}

    return render_template('result1.html', results = exp)

## If condition 
@app.route("/successif/<int:score>")
def successif(score) :
    return render_template('resultif.html', results = score)

@app.route('/fail/<int:score>')
def fail(score):

    return render_template('resulif.html', results = score)

@app.route('/submit', methods =['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science) / 4
    else :
        return render_template('getresult.html')

    return redirect(url_for('successres', score = total_score))

if __name__ == "__main__": #Entry point of any py file - Execution Starts from here
    app.run(debug = True)