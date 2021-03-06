#Team KateLin
#Kaitlin Wan + Kevin Lin
#SoftDev1 pd6
#K 14: Do I Know You?
#2018-10-01

from flask import Flask,request,render_template,session,url_for,redirect
import json,urllib.request
from random import randint

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!


@app.route('/')
def hello():
    x = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=SFVhYXCLPaL8AiaRP6JfTlcPSCF6c90qCF3cLQiA')
    x = x.read()
    #print(x)
    p = json.loads(x)
    #print(p)
    #print("=======")
    #print(p.keys())
    new = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&api_key=SFVhYXCLPaL8AiaRP6JfTlcPSCF6c90qCF3cLQiA'
    y = urllib.request.urlopen(new).read()
    y = json.loads(y)
    listPic = y['photos']
    lenPics = len(listPic)
    chosen = randint(0,24)
    finalpic = listPic[chosen]
    print(finalpic)
    id = finalpic['id']
    str = "Taken by Rover: "
    rovname = finalpic['rover']['name']
    str = str + rovname
    date = finalpic['earth_date']
    str = str + " on " + date
    imgad = finalpic['img_src']



    return render_template("template.html", img = p['url'], ex1 = p['title'], coolpic = imgad, imgInfo = str, id = id)


if __name__ == '__main__':
    app.debug = True
    app.run()
