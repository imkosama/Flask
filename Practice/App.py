from flask import Flask

app=Flask(__name__) # WSGI Application 

@app.route('/')
def welcome():
    return "Welcome to my show Hope you enjoy it!!"




if __name__=="__main__":
    app.run()
 