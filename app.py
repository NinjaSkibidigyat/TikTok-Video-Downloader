from __future__ import unicode_literals
import yt_dlp
from yt_dlp import YoutubeDL
import re
import os
import sys
from flask import Flask, jsonify, flash, request, render_template, redirect, copy_current_request_context
import time

# Configure Application
app = Flask(__name__)
app.secret_key = "####74123698"

@app.route('/', methods=['GET', 'POST'])
def download():

    if request.method == 'GET':
        
        return render_template('index.html')
    
    else:
        link = request.form.get('link')
        ## if empty input 
        if not request.form.get('link'):
            flash(u'Empty input! Please enter a valid TikTok url','danger')
            return redirect('/')
        ## if not valid TikTok Link
        elif request.form['download'] == 'Download':            
            myRegex = r"^https[:][/][/]w{3}[.]\b(tiktok)[.]\b(com)[/][@]([A-Za-z0-9\.\_]+)[/]\b(video)[/]([A-Za-z0-9\.\_\?\=\&]+)"
            while not re.match(myRegex, link):
                flash('Enter a valide URL \n Like : https://www.tiktok.com/@username/video/71263533154907.....', 'danger')
                return redirect('/')
        
        # ydl options for trimming the title
        # if the title is too long maybe some devices won't support it
        ## IMPORTANT : the title is not 10 characters
        ydl_opts = {
            #'outtmpl':"C:/videostktk/%(title)s.%(ext)s%(title).5s %(id)s.%(ext)s",
            'outtmpl':"c:/tktkvideos/saved/%(title).5s.%(ext)s",
            'throttled':'100k'
            }
        # IMPORTANT above 
        start_time = time.time()
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                # showing the user where his video was saved
                directory=os.getcwd()
                directory_file = 'File Location: '+ directory 
                # flash video after the video was successfully downloaded
                flash('Video Downloaded successfully.','success')
                # time stamp
                t3 = ('Speed: ',time.time() - start_time)
        # catching an error if the user inputs a demi url
        except yt_dlp.utils.DownloadError:
            flash('An exception occured please make sure your link is valid','danger')
        return render_template('index.html',link=link,directory_file=directory_file,t3=t3)
# catching 500 internal server error
@app.errorhandler(500)
def internal_error(error):
    flash('Error! Invalid TikTok post','danger')
    return render_template("500error.html")

if __name__=='__main__':
    app.run(debug=True)






                






