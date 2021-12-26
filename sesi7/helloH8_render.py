from flask import Flask, render_template

app = Flask(__name__)

#Rendering Templates
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):    
    # return render_template('hello.html', name=name)
    # return render_template('hello.html', template_name=name)
    # age = 22
    # pets = ['cat', 'dog', 'bird', 'fish'] # a list
    # pet_names = {'cat', 'aaa', 'dog', 'iii'} #a dictionary
    # return render_template('hello.html', 
    #                         template_name=name, 
    #                         age=age,
    #                         pet_list = pets,
    #                         pet_dicts = pet_names)

    return 'hi'

if __name__ == '__main__':
    # app.run()
    app.run(debug=True)