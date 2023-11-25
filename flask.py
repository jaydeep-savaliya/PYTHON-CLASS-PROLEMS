import flask as fl
app = fl(__name__)

@app.route('/')
def hello_world():
    return 'hello world !'

if __name__ == "__main__":
    app.run(debug = True)
