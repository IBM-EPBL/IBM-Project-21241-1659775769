from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
def firstpage():
    return render_template("index.html")

@app.route("/register",methods=['POST'])
def register():
    email=request.form['inputemail']
    password=request.form['inputpass']
    

if __name__=="__main__":
    app.run(debug=True)