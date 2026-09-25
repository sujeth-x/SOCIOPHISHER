<!-- Sociophisher -->

<div align="center">

  <h1>🛡️ SOCIOPHISHER</h1>

  <h3>Security Awareness Training Lab</h3>

  <p>
    <img src="https://img.shields.io/badge/Version-1.0-blue?style=for-the-badge">
    <img src="https://img.shields.io/github/license/sujeth-x/SOCIOPHISHER?style=for-the-badge">
    <img src="https://img.shields.io/github/stars/sujeth-x/SOCIOPHISHER?style=for-the-badge">
    <img src="https://img.shields.io/github/issues/sujeth-x/SOCIOPHISHER?color=red&style=for-the-badge">
    <img src="https://img.shields.io/github/forks/sujeth-x/SOCIOPHISHER?color=teal&style=for-the-badge">
  </p>

  <p>
    <img src="https://img.shields.io/badge/Author-sujeth--x-blue?style=flat-square">
    <img src="https://img.shields.io/badge/Open%20Source-Yes-darkgreen?style=flat-square">
    <img src="https://img.shields.io/badge/Maintained%3F-Yes-lightblue?style=flat-square">
    <img src="https://img.shields.io/badge/Written%20In-Python-yellow?style=flat-square">
    <img src="https://img.shields.io/badge/Framework-Flask-black?style=flat-square">
  </p>

  <p>
    <b>A security-awareness training lab for learning about phishing and social engineering.</b>
  </p>

</div>

<hr>

<h2 align="center">Disclaimer</h2>

<p>
  <i>
    <b>Sociophisher</b> is an educational security-awareness training project
    designed for authorized cybersecurity training, personal laboratories,
    demonstrations, and controlled environments.
  </i>
</p>

<p>
  <i>
    Do not use this project against systems, accounts, or individuals without
    explicit authorization.
  </i>
</p>

<p>
  <i>
    Sociophisher is designed as a training simulator and does not intentionally
    store password values.
  </i>
</p>

<p>
  <i>
    The author and contributors are not responsible for misuse of this project.
    Always obtain appropriate authorization before conducting any
    security-awareness exercise or security testing.
  </i>
</p>

<hr>

<h2>Features</h2>

<ul>
  <li>Security-awareness training environment</li>
  <li>Multiple training templates</li>
  <ul>
    <li>Instagram</li>
    <li>Facebook</li>
    <li>LinkedIn</li>
    <li>Google / Gmail</li>
  </ul>
  <li>Flask-based local training server</li>
  <li>Interactive CLI launcher</li>
  <li>Cloudflare Tunnel support</li>
  <li>ngrok Tunnel support</li>
  <li>Public training URLs for authorized demonstrations</li>
  <li>Training-event logging</li>
  <li>Password values are not stored</li>
  <li>Clean shutdown of services</li>
  <li>Beginner-friendly project structure</li>
  <li>Designed for cybersecurity education</li>
</ul>

<hr>

<h2>Installation</h2>

<ul>
  <li>
    Clone this repository:

    <pre><code>git clone --depth=1 https://github.com/sujeth-x/SOCIOPHISHER.git</code></pre>
  </li>

  <li>
    Go to the cloned directory:

    <pre><code>cd SOCIOPHISHER</code></pre>
  </li>

  <li>
    Create a Python virtual environment:

    <pre><code>python3 -m venv venv</code></pre>
  </li>

  <li>
    Activate the virtual environment:

    <pre><code>source venv/bin/activate</code></pre>
  </li>

  <li>
    Install the required dependencies:

    <pre><code>pip install flask colorama pyfiglet</code></pre>
  </li>
</ul>

<hr>

<h2>Running Sociophisher</h2>

<p>Start the main launcher:</p>

<pre><code>python3 sociophisher.py</code></pre>

<p>The CLI provides the following training templates:</p>

<pre><code>[01] Instagram
[02] Facebook
[03] LinkedIn
[04] Gmail

[99] About
[00] Exit</code></pre>

<p>
  Select a training template to start the Flask training environment.
</p>

<p>The local server runs on:</p>

<pre><code>http://127.0.0.1:5000</code></pre>

<hr>

<h2>Public Training Tunnels</h2>

<p>
  Sociophisher supports public tunneling for
  <b>authorized security-awareness demonstrations</b>.
</p>

<h3>Cloudflare Tunnel</h3>

<pre><code>cloudflared tunnel --url http://127.0.0.1:5000</code></pre>

<h3>ngrok</h3>

<pre><code>ngrok http 5000</code></pre>

<p>
  The <code>sociophisher.py</code> launcher can start the Flask server and
  configured tunnel processes together.
</p>

<blockquote>
  Public tunnels should only be used in environments where you have
  explicit authorization.
</blockquote>

<hr>

<h2>Training Templates</h2>

<h3>📸 Instagram</h3>

<pre><code>/instagram/</code></pre>

<h3>📘 Facebook</h3>

<pre><code>/facebook/</code></pre>

<h3>💼 LinkedIn</h3>

<pre><code>/linkedin/</code></pre>

<h3>📧 Google / Gmail</h3>

<pre><code>/gmail/</code></pre>

<hr>

<h2>Security &amp; Privacy</h2>

<p>
  Sociophisher is designed as a
  <b>security-awareness training simulator</b>.
</p>

<p>Training events may record:</p>

<pre><code>Template
Username / Identifier
Timestamp
Training Event</code></pre>

<p>
  Password values are intentionally <b>not stored</b>.
</p>

<p>Example:</p>

<pre><code>Password entered  : YES
Password value    : [REDACTED]</code></pre>

<hr>

<h2>Example Training Event</h2>

<pre><code>============================================================
          LOGIN ATTEMPT DETECTED
============================================================
Template          : LinkedIn
Username          : training-user@example.com
Password entered  : YES
Password value    : [REDACTED]
Time              : 2026-09-25 11:30:00
============================================================</code></pre>

<p>
  The purpose of this event is to demonstrate that a training interaction
  occurred without retaining the submitted password.
</p>

<hr>

<h2>Dependencies</h2>

<p><b>Sociophisher</b> requires:</p>

<ul>
  <li><code>python3</code></li>
  <li><code>pip</code></li>
  <li><code>git</code></li>
  <li><code>flask</code></li>
  <li><code>colorama</code></li>
  <li><code>pyfiglet</code></li>
</ul>

<p>Optional tunneling tools:</p>

<ul>
  <li><code>cloudflared</code></li>
  <li><code>ngrok</code></li>
</ul>

<hr>

<details>
  <summary><h2>Project Structure</h2></summary>

<pre><code>SOCIOPHISHER/
│
├── app.py
├── sociophisher.py
├── README.md
├── .gitignore
│
└── templates/
    ├── instagram/
    │   └── index.html
    │
    ├── facebook/
    │   └── index.html
    │
    ├── linkedin/
    │   └── index.html
    │
    ├── google1/
    │   └── index.html
    │
    └── google2/
        └── index.html</code></pre>

</details>

<hr>

<details>
  <summary><h2>Learning Objectives</h2></summary>

<ul>
  <li>Phishing awareness</li>
  <li>Social engineering</li>
  <li>Suspicious login-page identification</li>
  <li>Flask routing</li>
  <li>HTTP GET and POST requests</li>
  <li>HTML forms</li>
  <li>Redirects</li>
  <li>Linux command-line usage</li>
  <li>Public tunneling</li>
  <li>Security-event logging</li>
  <li>Git and GitHub workflow</li>
</ul>

</details>

<hr>

<h2 align="center"><i>:: Workflow ::</i></h2>

<div align="center">

<pre><code>                SOCIOPHISHER
                     │
                     ▼
              Select Template
                     │
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
      Instagram   LinkedIn    Gmail
          │          │          │
          └──────────┼──────────┘
                     │
                     ▼
              Training Page
                     │
                     ▼
            Training Interaction
                     │
                     ▼
             Security Event
                     │
                     ▼
          Password NOT Stored</code></pre>

</div>

<hr>

<h2>Technology Stack</h2>

<div align="center">

<img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask">
<img src="https://img.shields.io/badge/Cloudflare-Tunnel-orange?style=for-the-badge&logo=cloudflare">
<img src="https://img.shields.io/badge/ngrok-Tunnel-green?style=for-the-badge">
<img src="https://img.shields.io/badge/Linux-Environment-black?style=for-the-badge&logo=linux">
<img src="https://img.shields.io/badge/Git-Version%20Control-orange?style=for-the-badge&logo=git">

</div>

<hr>

<h2>Future Improvements</h2>

<ul>
  <li>Splunk integration</li>
  <li>Security-awareness dashboard</li>
  <li>Training analytics</li>
  <li>SIEM event forwarding</li>
  <li>Detection-rule demonstrations</li>
  <li>Event correlation</li>
  <li>Training-session reports</li>
  <li>Additional safe training scenarios</li>
  <li>Improved CLI interface</li>
  <li>Docker-based isolated deployment</li>
</ul>

<hr>

<h2>Responsible Use</h2>

<p>Sociophisher is intended only for:</p>

<ul>
  <li>Personal cybersecurity laboratories</li>
  <li>Security-awareness training</li>
  <li>Authorized demonstrations</li>
  <li>Controlled testing environments</li>
</ul>

<p>Do not use the project to:</p>

<ul>
  <li>Collect real credentials</li>
  <li>Store passwords</li>
  <li>Target users without permission</li>
  <li>Impersonate individuals</li>
  <li>Attack third-party systems</li>
  <li>Bypass security controls</li>
  <li>Conduct unauthorized phishing campaigns</li>
</ul>

<hr>

<h2>Find Me on</h2>

<p>
  <a href="https://github.com/sujeth-x">
    <img src="https://img.shields.io/badge/GitHub-sujeth--x-blue?style=for-the-badge&logo=github">
  </a>
</p>

<hr>

<div align="center">

<h2>🛡️ SOCIOPHISHER</h2>

<h3><i>Learn • Simulate • Detect • Defend</i></h3>

<p>
  Made for cybersecurity education and security awareness.
</p>

<p>⭐ If you find this project useful, consider starring the repository!</p>

</div>

<!-- // -->
