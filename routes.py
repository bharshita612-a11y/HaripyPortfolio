from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, ContactMessage

# Main blueprint for the portfolio pages.
main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in all fields before sending your message.", "error")
        return redirect(url_for("main.home"))

    new_message = ContactMessage(name=name, email=email, message=message)
    db.session.add(new_message)
    db.session.commit()

    flash("Your message has been saved successfully!", "success")
    return redirect(url_for("main.home"))
