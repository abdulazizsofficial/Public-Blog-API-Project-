# 📚 Public Blog API (Django REST Framework)

A **Public Blog API** built using **Django REST Framework** where all blog data is publicly accessible.  
Users can **view and manage posts, categories, authors, and comments without authentication**.

This project demonstrates **REST API development, relational database models, and CRUD operations** using Django.

---

# 🚀 Project Goal

The goal of this project is to build a **RESTful API for a blog platform** where:

- Anyone can **view blog posts**
- Anyone can **create comments**
- Blog data such as **authors, categories, and posts** are publicly accessible
- No **login or authentication system** is required

---

# 🏗 Project Setup

| Item | Name |
|-----|-----|
| Project Name | `{YourName}_{YourID}_BlogAPI` |
| Example | `Rahim_221_BlogAPI` |
| Django App | `blog_app` |

---

# 🧩 Models Overview

The API contains **four main models**:

```
Author → Post → Comment
        ↓
     Category
```

---

# 👤 AuthorModel

Stores information about blog authors.

| Field | Type | Description |
|------|------|-------------|
| name | String | Author's full name |
| email | String | Author's email address |

---

# 📂 CategoryModel

Used to organize blog posts into categories.

| Field | Type | Description |
|------|------|-------------|
| name | String | Category name |
| description | Text | Details about the category |

---

# 📝 PostModel

Represents a blog post written by an author.

| Field | Type | Description |
|------|------|-------------|
| title | String | Title of the blog post |
| content | Text | Full blog content |
| category | ForeignKey → CategoryModel | Category of the post |
| published_date | DateTime | Date when the post was published |
| author | ForeignKey → AuthorModel | Author of the post |

---

# 💬 CommentModel

Stores comments for blog posts. Anyone can add comments.

| Field | Type | Description |
|------|------|-------------|
| post | ForeignKey → PostModel | Post being commented on |
| author_name | String | Name of the commenter |
| content | Text | Comment message |
| created_at | DateTime | Auto generated timestamp |

---

# 🔗 Example API Endpoints

| Method | Endpoint | Description |
|------|------|-------------|
| GET | `/authors/` | List all authors |
| POST | `/authors/` | Create a new author |
| GET | `/categories/` | List all categories |
| POST | `/categories/` | Create a category |
| GET | `/posts/` | List all posts |
| POST | `/posts/` | Create a new post |
| GET | `/comments/` | View all comments |
| POST | `/comments/` | Add a comment |

---

# ⚙️ Technologies Used

- Python
- Django
- Django REST Framework
- SQLite (default database)

---

# ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/blog-api-project.git
```

### 2️⃣ Go to the project directory

```bash
cd YourName_YourID_BlogAPI
```

### 3️⃣ Create a virtual environment

```bash
python -m venv venv
```

### 4️⃣ Activate virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 5️⃣ Install dependencies

```bash
pip install django djangorestframework
```

### 6️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7️⃣ Start the development server

```bash
python manage.py runserver
```

---

# ✨ Key Features

- Public REST API
- CRUD operations for all models
- Blog post categorization
- Comment system without authentication
- Clean relational database design

---

# 📄 License

This project is created for **educational purposes**.
