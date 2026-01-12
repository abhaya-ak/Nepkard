<<<<<<< HEAD
# Nepkard
The E-commerse website with full implimentation of backend (auth, session based auth ) and production ready enviroment
=======
# 🛒 Nepkard

**Nepkard** is a Nepal-focused, secure, and minimal e-commerce platform built with Django.  
It supports physical products, session-based cart, and QR-based manual payment verification.

This project is built using **production-grade patterns**, not as a demo.

---

## 🚀 Features

### Customer
- Email-based authentication
- Product browsing
- Session-based cart
- Secure checkout
- QR-based payment
- Transaction ID submission
- Order history & order tracking

### Admin (Superadmin)
- Product management
- Order management
- Manual payment verification
- Transaction ID audit (DB + TXT file)

---

## 💳 Payment System (Nepal Context)

- QR-based payment only
- Customer pays externally (eSewa / Khalti / etc.)
- Customer submits **Transaction ID**
- Transaction ID is stored:
  - In database (linked to order)
  - In a `.txt` file for manual verification
- Admin manually verifies payments

❗ No payment gateway integration (by design)

---

## 🧱 Tech Stack

| Layer | Technology |
|-----|-----------|
| Backend | Django (Python) |
| Frontend | HTML5, Bootstrap 5, ES6 |
| Database | PostgreSQL |
| Auth | Django Authentication (Email-based) |
| Cart | Session-based |
| Deployment Target | Render |

---

## 🔐 Security Practices

- CSRF protection everywhere
- Secure sessions
- Ownership checks (IDOR prevention)
- Server-side validation only
- Environment-based secrets (`.env`)
- No sensitive data committed to GitHub

---

## 🗂️ Project Structure

```text
Nepkard/
├── accounts/
├── cart/
├── core/
├── orders/
├── products/
├── templates/
├── static/
├── nepkard/
├── manage.py
├── requirements.txt
└── README.md
>>>>>>> 2ceb950b23896267f0d44f3bfd04620301d40f63
