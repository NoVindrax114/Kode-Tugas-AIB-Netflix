from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import model as Model
from wtforms import Form, IntegerField

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('submit'))

def findRating(year):
    rating = (Model.model.coef_ * year) + Model.model.intercept_
    return rating

class SubmitForm(Form):
    year = IntegerField('Year')

@app.route('/submit', methods=['GET','POST'])
def submit():
    form = SubmitForm(request.form)
    if request.method == 'POST':
        SubmitForm.year = form.year.data
        if form.year.data == '':
            return render_template('submit.html', message='Please enter required field')
        return redirect(url_for('result'))
    return render_template('submit.html',form=form)

@app.route('/result')
def result():
    year = SubmitForm.year
    res = findRating(year)
    return render_template('result.html', res=res, year=year)

if __name__ == '__main__':
    app.debug=True
    app.run()