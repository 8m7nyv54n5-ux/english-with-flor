# app/forms.py
# Defines the forms used across the site using Flask-WTF (which wraps WTForms).
# Each class is a form. Fields are class attributes, and validators are rules
# that must pass before the form is considered valid.

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp, Optional


class RegistrationForm(FlaskForm):
    """Form for creating a new user account."""
    # Validator message strings are translation keys — the template looks them up in t[]
    # so the error displays in the user's chosen language.
    first_name = StringField("First Name", validators=[
                     DataRequired(message="error_field_required"),
                     Length(min=2, max=80, message="error_name_length")])
    last_name  = StringField("Last Name",  validators=[
                     DataRequired(message="error_field_required"),
                     Length(min=2, max=80, message="error_name_length")])
    email      = StringField("Email",      validators=[
                     DataRequired(message="error_field_required"),
                     Email(message="error_invalid_email")])
    username   = StringField("Username",   validators=[
                     DataRequired(message="error_field_required"),
                     Length(min=3, max=80, message="error_username_length")])
    password   = PasswordField("Password", validators=[
                     DataRequired(message="error_field_required"),
                     Length(min=8, message="error_password_too_short")])
    confirm    = PasswordField("Confirm Password", validators=[
                     DataRequired(message="error_field_required"),
                     EqualTo("password", message="error_passwords_must_match")])
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
                      ("a1", "A1 English"),
                      ("a2", "A2 English"),
                      ("b1", "B1 English"),
                      ("b2", "B2 English"),
                      ("c1", "C1 English"),
                      ("c2", "C2 English"),
                  ], validators=[DataRequired()])

    # Argentina fields — required only if user_type is "argentina".
    # Optional() lets the field pass when blank (the route handles required-ness).
    # CUIT/CUIL format: 2 digits, dash, 8 digits, dash, 1 digit (e.g. 20-12345678-9)
    cuit_cuil   = StringField("CUIT / CUIL", validators=[
                      Optional(),
                      Regexp(r"^\d{2}-\d{8}-\d$", message="error_invalid_cuit")])
    # DNI is 7 or 8 digits
    dni         = StringField("DNI", validators=[
                      Optional(),
                      Regexp(r"^\d{7,8}$", message="error_invalid_dni")])

    # International fields — required only if user_type is "international"
    passport_no = StringField("Passport Number", validators=[
                      Optional(),
                      Length(max=30, message="error_passport_length")])

    submit = SubmitField("Enrol")


class EditProfileForm(FlaskForm):
    """Form for updating personal details from the dashboard.
    Same validators as RegistrationForm but without username or password —
    those are handled separately."""
    first_name = StringField("First Name", validators=[
                     DataRequired(message="error_field_required"),
                     Length(min=2, max=80, message="error_name_length")])
    last_name  = StringField("Last Name",  validators=[
                     DataRequired(message="error_field_required"),
                     Length(min=2, max=80, message="error_name_length")])
    email      = StringField("Email",      validators=[
                     DataRequired(message="error_field_required"),
                     Email(message="error_invalid_email")])
    submit     = SubmitField("Save")


class ChangePasswordForm(FlaskForm):
    """Form for changing password from the dashboard.
    Requires the current password to verify identity before allowing the change."""
    current_password = PasswordField("Current Password", validators=[
                           DataRequired(message="error_field_required")])
    new_password     = PasswordField("New Password", validators=[
                           DataRequired(message="error_field_required"),
                           Length(min=8, message="error_password_too_short")])
    confirm          = PasswordField("Confirm New Password", validators=[
                           DataRequired(message="error_field_required"),
                           EqualTo("new_password", message="error_passwords_must_match")])
    submit           = SubmitField("Change Password")


class DeleteAccountForm(FlaskForm):
    """Form for confirming account deletion.
    Requires the user's password to prevent accidental or unauthorised deletion."""
    password = PasswordField("Password", validators=[
                   DataRequired(message="error_field_required")])
    submit   = SubmitField("Delete My Account")


class ContactForm(FlaskForm):
    """Form for sending a message via the contact page."""
    name    = StringField("Name", validators=[
                  DataRequired(message="error_field_required"),
                  Length(min=2, max=160, message="error_name_length")])
    email   = StringField("Email", validators=[
                  DataRequired(message="error_field_required"),
                  Email(message="error_invalid_email")])
    message = TextAreaField("Message", validators=[
                  DataRequired(message="error_field_required"),
                  Length(min=10, max=2000, message="error_message_length")])
    submit  = SubmitField("Send")
