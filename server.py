from flask import Flask, render_template,  request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Obtuviste Información")
    print(request.form)
    return redirect('/')
#Obtuviste Información
#ImmutableMultiDict([('name', 'Octavio '), ('email', 'octaviochavez154@gmail.com')])
if __name__ == "__main__":
    app.run(debug=True)

