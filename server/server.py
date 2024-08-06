from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({'message': "Hello World!"})

if __name__ == "__main__":
    app.run(debug=True)
   
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"