

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        print("We received GET")
        print("We're looking for contact.html page!!!!!")
        info = "Wyślij wiadomość"
        return render_template("contact.html", infos=info)
    elif request.method == 'POST':
        print("We received POST")
        myinfo = request.form['massege']
        print(f"We received massage: {myinfo}!!!!")
        print(f"Type of massage: {type(myinfo)}!")
        return redirect("/contact")
    

@app.route('/me', methods=['GET'])
def me():
    print("We're looking for me.html page!!!!!")
    return render_template("me.html")



