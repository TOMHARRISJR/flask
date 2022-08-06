from flask import Flask ,render_template
app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html",color="pink",num =3)

@app.route('/play/<int:num>')
def box1(num):
    return render_template("index.html",num=num,color="blue")

@app.route('/play/<int:num>/<string:color>')
def box(color,num):
    return render_template("index.html",color=color,num=num)




if __name__ == "__main__":   
    app.run(debug=True)    
