from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/<page_name>')
# @app.route('/shop')
# @app.route('/food')
# @app.route('/shoes')
def hello_world(page_name):    
    # return 'Hello World! <br> <h1>Hello World!</h1>'
    html = 'Hello World! <br> <h1>This is hello home</h1>'
    html += '<h2>This is {} page</h2>'.format(page_name)
    # html += '<h2>This is {page_name} page</h2>'
    return html


@app.route('/hello')
def hello():    
    return 'Hello World! <br> <h1>This is hello home</h1>'

if __name__ == '__main__':    
    app.run()


# #HTML Escaping
# @app.route("/<name>")
# def hello(name):    
#     return f"Hello, {escape(name)}!"


# #Routing
# @app.route('/')
# def index():    
#     return 'Index Page'

# @app.route('/hello')
# def hello():    
#     return 'Hello, World'


