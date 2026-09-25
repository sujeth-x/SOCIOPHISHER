# SOCIOPHISHER

## Security Awareness Training Lab

Sociophisher is a **security-awareness training simulator** built with Python and Flask.

The project is designed to demonstrate how realistic-looking login pages can be used in social-engineering scenarios and help users understand how to identify suspicious authentication pages.

> ⚠️ **Educational & Authorized Use Only**
>
> Sociophisher is intended for cybersecurity education, security-awareness training, and authorized lab environments.
> Do not use it against systems, accounts, or users without permission.

---

## 🎯 Project Objective

The main objective of Sociophisher is to provide a controlled environment for learning about:

- Phishing awareness
- Social engineering techniques
- Suspicious login-page identification
- Security-awareness training
- Web application routing
- Public tunneling for authorized demonstrations
- Basic security-event logging

---

## 🚀 Features

- Flask-based training server
- Multiple security-awareness templates
- Instagram training page
- Facebook training page
- LinkedIn training page
- Google/Gmail training page
- Google training flow
- Cloudflare Tunnel integration
- ngrok Tunnel integration
- CLI-based launcher
- Public training URLs
- Training-event logging
- Password values are **not stored**
- Manual browser opening
- Clean shutdown of Flask and tunnel processes

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Flask | Web application/backend |
| HTML/CSS | Training interfaces |
| Cloudflare Tunnel | Authorized public tunnel |
| ngrok | Authorized public tunnel |
| Git | Version control |
| GitHub | Source-code repository |

---

## 📁 Project Structure

```text
SOCIOPHISHER/
│
├── app.py
├── sociophisher.py
├── README.md
├── .gitignore
│
├── templates/
│   ├── instagram/
│   │   └── index.html
│   │
│   ├── facebook/
│   │   └── index.html
│   │
│   ├── linkedin/
│   │   └── index.html
│   │
│   ├── google1/
│   │   └── index.html
│   │
│   └── google2/
│       └── index.html
│
└── venv/
    └── (local virtual environment - not committed)
