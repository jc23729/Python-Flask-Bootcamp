from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #my_variable is = some_variable= Jose, you can use Jinja to put that anywhere in the html
    # some_variable = 'Jose'
    # return render_template('basic.html', my_variable = some_variable)
    #EXAMPLE OF PASSING IN A STRING, LIST, AND DICTIONARY
    #MAIN IDEA IS YOU GET TO CREATE WHATEVER VARIABLES YOU WANT WITH PYTHON CODE YOUR FAMILIAR WITH
    #THEN YOU SETUP A TEMPLATE NAME THAT USUALLY SHARES THE SAME NAME, AND YOU CAN INJECT THEM WITH JINJA {{}}
    name= "Jose"
    letters = list(name)
    pup_dictionary= {'pup_name':'Sammy'}
    return render_template('basic.html', name=name, letters=letters,
                           pup_dictionary= pup_dictionary)

if __name__ == '__main__':
    app.run(debug= True)



"""
FLASK BASICS 
#one view function which is our main page
@app.route('/')
def index():
  return '<h1>Hello Puppy!</h1>'

## this will bring page another page
@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1>"

##Dynamic routes are routes where you may want a page per user
# Dyamic routes have a variable passed in, and parmaeter passed in function

@app.route('/some_page/<name>')
def other_page(name):
    #Later we will see how to use 
    #this parameter with templates!
    return 'User: {}'.format(name)
    
@app.route('/puppy/<name>')
def puppy(name):
    return "100th letter: {}".format(name[100])

@app.route('/puppy_name/<name>')
def puppylatin(name):

    pupname = ''
    if name [-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'

    return "<h1>Your Puppy latin name is: {}".format(pupname)

if __name__ == '__main__':
    app.run(debug= True)

"""



