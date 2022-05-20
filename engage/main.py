from flask import Flask, render_template
app = Flask(__name__, template_folder='template')
import os
picFolder = os.path.join('static', 'images')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/")
def index():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'home.jpg')
    return render_template("index.html", user_image=pic1)   
   ## return render_template('index.html')

if __name__  ==  "__main__":
    app.run(debug=True)