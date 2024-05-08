from flask import Flask, render_template, request

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

@app.get('/')
def index():
  return render_template('index.html')

@app.get('/hello')
def hello():
  return render_template('hello.html', name=request.args.get('name'))

@app.errorhandler(404)
def handle_404(e):
    return '<h1>404</h1><p>File not found!</p><img src="https://httpcats.com/404.jpg" alt="cat in box" width=400>', 404


if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0', debug=True, port=8080)