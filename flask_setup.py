from flask import Flask, request, redirect
import requests

app = Flask(__name__)

def exchange_code(code):
    a = 9

@app.route('/')
def index():
    code = request.args.get('code')    
    if not code:
        error = request.args.get('error')
        return error
    else:
        return code
    # code = request.args.get('code')
    # error = request.args.get('error')
    # return "Hello, World!"

if __name__ == "__main__":
    app.run(debug = True, port = 8080)


