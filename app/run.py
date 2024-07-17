from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index() :
    return "Главная страничка"


app.run(host='127.0.0.21', port=80)