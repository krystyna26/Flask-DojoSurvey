from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def survey():
	return render_template('index.html') 


@app.route('/result', methods=['GET', 'POST'])
def takeSurveyResults():
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   # display in terminal
   print name, location, language, comment
   return render_template("result.html", name=name, location=location, language = language, comment= comment)


app.run(debug=True)