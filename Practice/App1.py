# Building URL dynamically
# Variable Rule and URL B


from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return " Welcome to my Channel"
# In Success Url i want to print score as integer,
# if im not putting <int:score> like this then score will considered as string


@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is " + str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is " + str(score)


@app.route('/results/<int:marks>')
def report(marks):
    result = ""
    if marks > 50:
        result = "pass"
    else:
        result = "fail"
    return redirect(url_for(result, score=marks))


if __name__ == "__main__":
    app.run(debug=True)
