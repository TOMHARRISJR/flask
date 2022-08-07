
from flask import Flask, render_template,session,redirect
app = Flask(__name__)
app.secret_key = "omgahhh"

@app.route('/')
def counter():
    if "count" in session:
        session["count"]+= 1
    else:
        session["count"]= 1
    return render_template("index.html")

@app.route('/addTwo', methods=["post"])
def addTwoClicks():
    if "count" in session:
        session["count"]+= 1
    else:
        session["count"] = 1
    return redirect("/")

@app.route("/destroy",methods=["post"])
def removeCounter():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)





