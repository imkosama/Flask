# Integrate Html with Flask
# HTTP verb GET and POST
# render _template help us to render HTMl page
# request will help us to read posted values
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
     return render_template("index.html")
 
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res='Passed'
    else:
        res="Failed"
    return render_template("results.html",result=res) # result will pass to results.html

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is " + str(score)
 


# result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form['science']) # id is given inside square bracket from index.html and 
        # converting into float bcz automatically is given into string thats why we are converting it
        maths=float(request.form['maths']) 
        c=float(request.form['c']) 
        data_science=float(request.form['datascience']) 
        total_score=(science+maths+c+data_science)/4
   
    return redirect(url_for('success',score=total_score))  
    
    
if __name__=="__main__":
    app.run(debug=True)