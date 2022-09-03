#TikTok Video Downloader

## Video Demo : https://youtu.be/XdRuaZu-fRo

## Description : 
*In a time where phones are much more used
than Computers where 68.1% of all website visits in 2020 
came from mobile devices it's hard to find certain options
for Desktops so i decided to make a website to help desktop
users to download videos from TikTok, The most used app.

My project is made to facilitate users interaction with TikTok
to be more specific by using my website you can download
any TikTok video from the URL specified By TikTok
which looks like this : https://www.tiktok.com/@username/video/712635......*
**it's also free to use and will always be free Enjoy.**

## myCode

First we import all the denepndencies then we create an instance of
a Flask app next we create a Python decorator `@app.route` that Flask
uses to connect URL endpoints with code contained in functions.

After the steps above we define a function called `download()`
and inside of it if the user requested our page we will render 
our template once on our website we made a regular expression
that matches what a tiktokt link look like but as websites
are continuasly changing i didn't want to match all the entire
length of the link...

##Second part
We call the ydl options that will make the title of the video shorter
because if the title is too big certain devices won't save the video,
I also called throttled to make the downloading process faster.

After We put our code in a try block to catch any unwanted error
specifically `yt_dlp.utils.DownloadError` that can be raised if the
link is correct but the video couldn't be found.
I also created another Python decorator that catches error 500

#Finnaly 
you're ready to go and use this sublime web app that is
very powerful and clean. 
