from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload',methods = ['POST','GET'])
def upload():
   if request.form['u'] == 'lobby' and request.form['p'] == 'dont store passwords like this!!!':
      return render_template('upload.html')
   else:
    return "incorrect password or user name"


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      file_name = f.filename
      extension = file_name.split(".")[1]
      

      f.save( "./video/new."+ extension)
      return 'file uploaded successfully'



if __name__ == '__main__':
    app.run(debug=True)
