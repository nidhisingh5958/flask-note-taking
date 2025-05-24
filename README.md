# 📝 Flask Note-Taking App

A simple and lightweight **Note-Taking Web Application** built with **Flask**, designed to help users create, view, and delete personal notes. Ideal for learning Flask basics and deploying a minimal full-stack Python application.

## 🚀 Features

* Create and save notes
* Delete existing notes
* View all your saved notes
* Clean and minimal web interface
* Lightweight and easy to set up

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS (Jinja templates)
* **Database:** SQLite (via SQLAlchemy)

---

## 📂 Project Structure

```
flask-note-taking/
│
├── static/               # Static files (CSS, JS)
│
├── templates/            # HTML templates
│   └── index.html
│
├── app.py                # Main Flask application
├── models.py             # Database models
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/nidhisingh5958/flask-note-taking.git
cd flask-note-taking
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python app.py
```

5. **Visit in browser**

```
http://127.0.0.1:5000/
```

---

## 🗃️ Database Setup

The app uses SQLite and SQLAlchemy ORM. When you run the app for the first time, it will automatically create the database file (`notes.db`) and required tables.

---

## ✨ Usage

* Visit the homepage.
* Enter a new note and submit.
* See the note appear in the list.
* Click the delete button to remove a note.

---

## 🙋‍♀️ Author

Made with ❤️ by [Nidhi Singh](https://github.com/nidhisingh5958)
