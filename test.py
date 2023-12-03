from flask import Flask

app = Flask(__name__)

@app.route('/welcome/<nama>')
def welcome(nama):
    return f"Selamat datang {nama}!"
@app.route("/welcome/")
@app.route("/welcome")
def slash_agnostic():
    return "Anonymous"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000, threaded=True)
