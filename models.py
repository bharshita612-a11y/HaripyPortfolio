from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy instance used by the app and routes.
db = SQLAlchemy()


class ContactMessage(db.Model):
    """Stores portfolio contact submissions in SQLite."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(220), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    def __repr__(self):
        return f"<ContactMessage {self.name}>"
