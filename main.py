from flask import Flask, request, render_template

from availability_scheduler import availability_calculator, month_parser
import spotipysongsegmentor
import pyperclip
from datetime import datetime
import time
app = Flask(__name__)
import availability_scheduler

#static images in static folder
#html+css files in templates
#shift refresh clears site cache - so static files reload
#can edit html in chrome in devtool - js - document.body.contenteditable=true and then save html file
    # can del files by devtool chrome - select tool - backspace




# timer = 0
# @app.route('/')
# def my_form():
#     global timer
#     event = "Workout"
#     current_year = datetime.now().year
#     for i in range(10):
#         timer += 1
#         time.sleep(1)
#         #timer makes more since in JS (jquery)
#         #import jquery with script tag and CDN link
#         #write code in script tag
#
#     return render_template('my-form.html', event_name= event, current_year = current_year, timer = timer)
#

# @app.route('/')
# def twentyfiveminutes():
#     return render_template("twentyfiveminutes.html")
variables = 1

@app.route('/')
def render_website():
    return render_template('index.html')

    # text = request.form['text']

@app.route('/', methods=['POST'])
def my_form_post():
    days_list = []
    days_string = ""
    copied = False
    # request form is immutable (unchangeable) multi dict (dict designed to handle multiple of same key)
    # name: value (button name or input value)
    text = request.form['text']
    try:
        month_abbreviated = month_parser(text)
        days_liszt, days_string = availability_calculator(month_abbreviated)
        error_occurred = False
    except Exception as error:
        error_occurred = True
        print(error)
    if "Copy To Clipboard" in request.form:
        pyperclip.copy(days_string)
        copied = True
    return render_template('index.html', app_data = days_list, text_input= text, copied= copied, error_occurred= error_occurred)

@app.route('/spotify')
def render_spotify():
    return render_template('my-spotify-form.html')

@app.route('/spotify', methods=['POST'])
def spotify_triggered():
    spotipysongsegmentor.app()
    return render_template('my-spotify-form.html')







# dev server - off when pushed to production (python anywhere)
if __name__ == "__main__": #checks if this is imported module
    app.run(debug= True) #flask run in terminal same as this