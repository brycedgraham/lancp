📝 LAN Clipboard Server
A lightweight, FastAPI-powered clipboard for your local network. Share text between devices using a browser or API. Backed by Redis, containerized with Docker.

🚀 Features
- 📋 Shared clipboard accessible across LAN
- 🌐 Simple web UI with textarea + update button
- ⚙️ REST API for custom clients and automation
- 🪄 FastAPI + Redis for snappy performance
- 🐳 Dockerized with Compose for easy setup

📦 Tech Stack
| Component | Role | 
| FastAPI | API backend and templating | 
| Redis | In-memory clipboard store | 
| Jinja2 | Renders HTML templates | 
| Docker | Containerization and orchestration | 

📁 Folder Structure
network-clipboard/
├── app/
│   ├── main.py
│   └── templates/
│       └── index.html
├── Dockerfile
├── requirements.txt
├── docker-compose.yml

⚙️ Setup
# Clone the repo
git clone https://github.com/<yourname>/network-clipboard.git
cd network-clipboard

# Build and run
docker compose up --build

# Access from LAN
http://<raspberrypi-ip>:8000

📋 API Endpoints
GET /
Returns current clipboard content via rendered HTML.
POST /update
Updates clipboard value via form submission.
curl -X POST -F "value=Hello LAN!" http://<raspberrypi-ip>:8000/update

🛠️ Troubleshooting
- TemplateNotFound: Make sure index.html is in app/templates.
- Form processing: Ensure python-multipart is included in requirements.txt.

✅ Todo / Extensions
- 🧠 Add clipboard history (Redis list)
- 🌈 HTMX / AJAX for live updates
- 🔐 User auth or IP whitelisting
- 🧰 CLI / tray client integration
- 📄 Markdown + file support