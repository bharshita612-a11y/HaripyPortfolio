# Jacob Aiden Portfolio

A complete portfolio website built with Python, Flask, SQLite, HTML, CSS, and JavaScript.
The design uses a dark glassmorphism aesthetic and includes a frontend hero section, services, portfolio examples, and a contact form with backend storage.

## Architecture Overview

- `app.py` - Flask application factory that initializes the app and database.
- `models.py` - SQLAlchemy model definitions for storing contact submissions.
- `routes.py` - Main Flask blueprint with the homepage and contact form route.
- `templates/index.html` - Single template for the portfolio landing page.
- `static/css/style.css` - Custom styling for the dark glassmorphism portfolio UI.
- `static/js/main.js` - Frontend animation and visibility behavior.
- `portfolio.db` - SQLite database file created automatically.
- `requirements.txt` - Required Python packages.

## Features

- Modern portfolio layout matching the requested image style
- Sticky top navigation and hero section with call-to-action buttons
- Services and portfolio showcase sections
- Contact form with server-side validation and SQLite persistence
- Flask backend with SQLAlchemy ORM
- Virtual environment support using `venv`

## Setup Instructions

1. Open PowerShell in the project folder:

```powershell
cd "C:\Users\HP\Desktop\python..H\HaripyPortfolio"
```

2. Create and activate the virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

4. Run the app:

```powershell
python app.py
```

5. Open the app in your browser:

```text
http://127.0.0.1:5000/
```

## Database Details

- SQLite is used as the local database.
- `portfolio.db` is created automatically when the app starts.
- Contact form submissions are stored in the `ContactMessage` table.

## Customization

- Update `templates/index.html` to change headings, sections, and content.
- Change colors and layout in `static/css/style.css`.
- Add more portfolio items or services in the HTML structure.
- Replace the placeholder contact email with your real contact address.

## Notes

- The app already includes a `venv` folder in the repository.
- If you need to reset the database, delete `portfolio.db` and restart the app.
- Use the `flash` messages at the top of the contact form to show success or error notifications.
