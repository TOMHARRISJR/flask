from flask import Flask, render_template,session,redirect,request
app = Flask(__name__)
app.secret_key = "omgahhh"

@app.route("/")
def display_form():
    return render_template("index.html")


@app.route("/process", methods=["post"])
def form():
    session["Name"] = request.form["Name"]
    session["Language"] = request.form["Language"]
    session["Location"] = request.form["Location"]
    session["Comment"] = request.form["Comment"]
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("index1.html")


if __name__ == "__main__":
    app.run(debug=True)

