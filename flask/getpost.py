from flask import Flask, render_template, request
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

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

if __name__ == "__main__": #Entry point of any py file - Execution Starts from here
    app.run(debug = True)