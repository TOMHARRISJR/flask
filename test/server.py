from flask import Flask  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/hello/<name>/<int:num>')
def hi(name,num):
    return f"<p>{ name }</p>" * num

# @app.route('/repeat/<int:num>/<string>')



if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)   