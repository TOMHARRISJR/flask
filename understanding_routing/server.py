from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html",name="hello world",num = 1)

@app.route("/dojo")
def dojo():
    return render_template('index.html',name='Dojo!',num = 1)

@app.route("/say/<name>")    
def names(name):
    return "Hi, " + name
    
@app.route("/repeat/<int:num>/<name>")
def repeat(num,name):
    return  render_template("index.html",name = name,num = num)   

if __name__ == "__main__":
    app.run(debug=True)






