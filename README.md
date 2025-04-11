# ☕ Cafe RESTful API

A professional, secure, and fully-documented RESTful API for managing cafes — complete with filtering, authentication, and Postman collection support.

---

## 🚀 What This Project Includes

- ✅ Flask REST API with modular Blueprint structure
- ✅ Full CRUD capabilities: Create, Read, Update, Delete
- ✅ Filtering, sorting, and pagination on cafe listings
- ✅ Secure PATCH and DELETE endpoints using API key authentication
- ✅ Built-in `/docs` endpoint providing live API documentation in JSON format
- ✅ CORS enabled for frontend integrations
- ✅ Fully tested and demo-ready via Postman Collection

---

## 🧠 What I Learned

- How to structure a real-world REST API using Flask and Flask-Restful
- Implementing secure endpoints with API key-based protection
- Enabling CORS to make backend APIs frontend-friendly
- Using Blueprints for scalable, clean Flask architecture
- Writing developer-focused API documentation with a `/docs` route
- Testing and organizing APIs using Postman

---

## 🛠️ Technologies Used

- Python 3.12
- Flask
- Flask-Restful
- Flask-SQLAlchemy
- Flask-CORS
- SQLite (as the database)
- Postman (for testing & documentation)

---

## 📦 Postman Collection

You can find the complete collection to demo and test this API in the file:

```
cafe-api.postman_collection.json
```

Import it into Postman to try every endpoint with example data.

---

## 🧪 How to Run Locally

1. Create and activate a virtual environment:

```
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
python run.py
```

4. Explore the endpoints (e.g. `http://127.0.0.1:5000/cafes`, `/random`, `/add`, etc.)

---

## 📄 API Documentation

Visit [`/docs`](http://127.0.0.1:5000/docs) after running the app to see the full live API spec.

---

## 🔐 Secure Endpoints

- `PATCH /cafes/<id>/update-price` and `DELETE /cafes/<id>` require the following header:

```
x-api-key: TopSecretAPIKey
```

---

## 📁 Project Structure

```
restful_api_project/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── cafes.py
│   └── utils/
│       └── auth.py
│
├── run.py
├── requirements.txt
├── cafes.db
└── cafe-api.postman_collection.json
```

---

## ✅ Status

✨ Project Complete and Production-Ready