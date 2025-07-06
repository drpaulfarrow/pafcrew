```plaintext
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Feedback form using WTForms
class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Length(min=5, max=100)])
    feedback = TextAreaField('Feedback', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Submit Feedback')

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        # Process the feedback (e.g., store in database or send via email)
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('thank_you'))
    return render_template('feedback.html', form=form)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)