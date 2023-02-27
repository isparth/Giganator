from flask import Flask, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),"templates")
jinja_env = jinja2.Environment(loader = jinja2.File.SystemLoader(template_dir))

app = Flask(__name__)

#route to the index
@app.route('/')
def index():
    return render_template('login.html')
      #return render_template('index.html', README=readme.read(), requirements=req.read())

