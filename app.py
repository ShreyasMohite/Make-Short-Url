from flask import Flask,render_template,url_for,request,send_from_directory
import pyshorteners
import os





app=Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'logo591.ico',mimetype='image/vnd.microsoft.icon')



@app.route("/",methods=['GET','POST'])
def home():
    datas=None
    if request.method=='POST':
        urls=request.form['urls']
        s = pyshorteners.Shortener()
        datas=s.tinyurl.short(urls)
    return render_template("home.html",title="Url Shortner",urlx=datas)



@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__=="__main__":
    app.run(debug=True,host="192.168.1.204")