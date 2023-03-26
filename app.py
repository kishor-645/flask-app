from Flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey hello world'

@app.route('/health')
def health():
    return 'Server is up and running :)'