from flask import Flask,render_template,request
import download
import email_send
from makezip import create_zip
import pickle
app = Flask(__name__)

@app.route('/')
def main_page():
    if request.method == "POST":
        keyword = request.form['keyword'].replace(' ','').lower()
        emailid = request.form['emailid']
        limit = int(request.form['limit'])
        download_song(keyword,limit)
        create_zip()
        send_mail(emailid)
        # print(keyword,emailid,limit)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)