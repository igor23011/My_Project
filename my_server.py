from flask import Flask, render_template
from my_avito import search_avito
app = Flask(__name__)

@app.route("/")

def index():
    title = "Китайский Авито"
    avito = search_avito()
    return render_template("index.html", page_title=title, avito=avito)

if __name__ =="__main__":
    app.run(debug=True)    