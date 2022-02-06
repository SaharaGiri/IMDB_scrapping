# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:01:40 2022

@author: giris
"""
from bs4 import BeautifulSoup;
from flask import Flask, render_template, request
import requests
   
app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def search():
    if request.method == "POST":
        inputNumber = request.form["mNumber"]
        sourceUrl = "https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count="
        details = requests.get(sourceUrl + inputNumber)
        soup = BeautifulSoup(details.text, 'lxml')
        movies_list = soup.find_all("div", {"class": "lister-item mode-advanced"})      
        return render_template("Result.html", allMovies=movies_list)
    else:
        return render_template('Request.html')
if __name__ == '__main__':
  app.run()

 

    
    
    
    
    
    
    
