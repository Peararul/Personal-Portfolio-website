from flask import Flask, render_template, request

import os



app= Flask(__name__)

picfolder=os.path.join('static','pics')
app.config['UPLOAD_FOLDER']=picfolder

@app.route("/")
def home():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True,port=7384)