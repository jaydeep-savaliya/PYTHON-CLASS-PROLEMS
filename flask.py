import flask as fl
# from flask import jsonify

app = fl(__name__)

@app.route('/')
def hello_world():
    return 'hello world !'

if __name__ == "__main__":
    app.run(debug = True)
