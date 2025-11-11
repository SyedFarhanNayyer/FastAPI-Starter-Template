# 🚀 FastAPI Starter Template

A **starter template** for building modern Python web applications or RestAPI using **FastAPI**. This template includes commonly used tools and best practices, so you can quickly start building APIs or web apps. ✨


## ⚡ Features

- **FastAPI** - Modern, fast (high-performance) Python web framework   
- **Pydantic** - Data validation and settings management using Python type annotations 
- **MongoDB (pymongo)** - NoSQL database integration 
- **Argon2** - Secure password hashing 🔒 
- **python-dotenv** - Load environment variables from `.env` files 
- **Jinja2** - Templating engine for rendering HTML pages 
- Ready-to-use **project structure** for API and web development 

---

## 📁 Project Structure
```
fastapi-starter/
│
├─ app/
│  ├─ main.py          # FastAPI entry point
│  ├─ routes/          # API route definitions
│  ├─ schema/          # Pydantic schemas
│  ├─ helper/          # Helper functions
│  ├─ static/          # Static CSS / JS files
│  ├─ auth/            # Argon2 auth utilities
│  ├─ config/          # MongoDB connection
│  └─ templates/       # Jinja2 HTML templates
│
├─ .env                # Environment variables
├─ requirements.txt    # Python dependencies
└─ README.md
```
# ⚙️ Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SyedFarhanNayyer/FastAPI-Starter-Template.git
cd fastapi-starter

Create a virtual environment

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

Install dependencies
pip install -r requirements.txt

Run the FastAPI server
fastapi dev main.py
