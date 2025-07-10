# 📰 Weekly Newsletter Blog
A dynamic Weekly Newsletter Blog application built using Flask, HTML, CSS, and JavaScript, designed to collect and manage newsletter subscriptions with a modern, responsive UI.

🚀 Features:
Clean and responsive front-end interface

Real-time subscription via email input field

Secure email storage and database interaction

Cloud-based deployment and MySQL integration

🛠 Tech Stack:
Backend: Python, Flask (for routing, server logic, and template rendering)

Frontend: HTML5, CSS3, JavaScript (for styling and interactivity)

Database: MySQL (Cloud hosted via Aiven)

Database Tools: MySQL Workbench (for local queries and table management)

Version Control: Git (with GitHub repository management)

Cloud IDE: Replit (used for full-cycle development and testing)

Deployment: Render (for deploying Flask app with MySQL backend)

📦 Key Functionalities:
Newsletter subscription form

Email validation and duplicate check

Automatic storage in cloud MySQL table email_list (with fields: id, email)

Ready for scaling and additional features like authentication, newsletter publishing, etc.

📁 Folder Structure:
bash
Copy
Edit
/project-root
├── static/               # CSS and JS files
├── templates/            # HTML templates (Jinja2)
├── database.py           # MySQL connection logic
├── main.py               # Flask app routes
├── schema.sql            # SQL schema for creating `email_list` table
├── requirements.txt      # Python dependencies
└── README.md             # Project overview
✅ Future Improvements:
Admin dashboard to view and manage subscribers

Scheduled newsletter delivery system

Integration with email services (like Mailchimp or SMTP servers)
