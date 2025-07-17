# ⏳ Time Machine

**Time Machine** is a web application that transports you back in time.

Choose any date, and you'll discover:

- ✨ Notable **births**
- 🕯️ Important **deaths**
- 📜 Historic **events**

All data is powered by [Wikimedia’s “On This Day” API](https://api.wikimedia.org/wiki/Feed_API/Reference/On_this_day), bringing real historical records to life from Wikipedia.

## 🛠️ Getting Started

### 📦 Prerequisites

- Node.js
- Python 3.9+
- pip
- (Optional) Docker + Docker Compose

## 🖥️ Local Development

### 1. Clone the Repository

```bash
git clone https://github.com/TodayNightt/time-machine.git
cd time-machine
```

### 2. Frontend Setup

```bash
cd frontend
npm install
npm run build
```

### 3. Backend Setup

```bash
cd ../backend
pip install -r requirements.txt
```

### 4. Run Backend Server

- Windows:

```bash
 waitress-serve --port 5000 main:app
```

- Linux/macOS:

```bash
 gunicorn --bind 0.0.0.0:5000 --workers 4 main:app
```

## 🐳 Run with Docker

- Docker compose

```bash
docker compose up
```

- Prebuilt Docker image

```bash
docker load time-machine.tar
```
