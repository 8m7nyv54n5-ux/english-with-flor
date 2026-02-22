# app/forms.py
# Defines the forms used across the site using Flask-WTF (which wraps WTForms).
# Each class is a form. Fields are class attributes, and validators are rules
# that must pass before the form is considered valid.

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    """Form for creating a new user account."""
    full_name  = StringField("Full Name",  validators=[DataRequired(), Length(min=2, max=150)])
    email      = StringField("Email",      validators=[DataRequired(), Email()])  # Email() checks format
    username   = StringField("Username",   validators=[DataRequired(), Length(min=3, max=80)])
    password   = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm    = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])  # must match password
    submit     = SubmitField("Register")


class LoginForm(FlaskForm):
    """Form for logging into an existing account."""
    username = StringField("Username",  validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit   = SubmitField("Log In")


class EnrolmentForm(FlaskForm):
    """Form for enrolling on a course.
    Shows different ID fields depending on whether the student is from Argentina
    or is an international student — this conditional logic is handled in auth.py."""
    user_type   = SelectField("I am", choices=[
                      ("argentina", "Argentina resident / citizen"),
                      ("international", "International student")
                  ], validators=[DataRequired()])
    course      = SelectField("Course", choices=[
                      ("english_all_levels", "English for All Levels")
                  ], validators=[DataRequired()])

    # Argentina fields — required only if user_type is "argentina"
    cuit_cuil   = StringField("CUIT / CUIL")
    dni         = StringField("DNI")

    # International fields — required only if user_type is "international"
    passport_no = StringField("Passport Number")

    submit = SubmitField("Enrol")
