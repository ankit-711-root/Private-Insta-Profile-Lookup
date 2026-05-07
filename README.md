# 🛡️ Private-Insta Profile Lookup
**Advanced OSINT Tool for Private Instagram Post**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-1.1+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Cybersecurity](https://img.shields.io/badge/Security-OSINT-red?style=for-the-badge&logo=hackthebox&logoColor=white)]()

---

## 📝 Description
**Private-Insta Profile Lookup** is an advanced OSINT tool designed for ethical hackers and security researchers. It identifies and displays posts from private Instagram profiles only when those posts are collaborated with a public Instagram profile.
The tool uses advanced TLS fingerprint impersonation techniques to bypass standard Instagram browser restrictions and intercept raw media data. It supports single-image posts, videos, and carousel (sidecar) posts, then securely serves the extracted media through a proxy-based delivery system.

---

## 🔥 Key Features
* **🚀 Anti-Bot Bypass:** Uses `curl_cffi` to mimic real Chrome browser TLS signatures.
* **📂 Carousel Extraction:** Automatically breaks down multi-image/video posts into individual downloadable assets.
* **⚡ Media Proxying:** Built-in server-side proxy to bypass CORS and IG hotlinking protections.
* **🎬 High-Res Downloads:** Supports high-definition `.jpg` and `.mp4` extraction.
* **🎨 Glassmorphic UI:** Clean, dark-mode dashboard with premium Instagram-style gradients.

---

## 🛠️ Tech Stack & Requirements
* **Languages:** Python 3.9+
* **Framework:** Flask (Backend)
* **Networking:** `curl_cffi` (Impersonation Library)
* **Frontend:** HTML5, CSS3 (Advanced Flexbox & Glassmorphism)

---

## 🚀 Installation & Setup

### 📥 Clone Repository

```bash
git clone https://github.com/ankit-711-root/Private-Insta-Profile-Lookup.git

cd Private-Insta-Profile-Lookup
```
## ⚙️ Installation

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run the Tool

```bash
python app.py
```

---

## 🐧 Linux Setup (Kali/Ubuntu)

### 🔄 Update System

```bash
sudo apt update && sudo apt install python3-pip git -y
```

### 📥 Clone Repository & Install Requirements

```bash
git clone https://github.com/ankit-711-root/Private-Insta-Profile-Lookup.git

cd Private-Insta-Profile-Lookup
```

### 📦 Install Dependencies

```bash
pip3 install -r requirements.txt
```

### ▶️ Run the Tool

```bash
python3 app.py
```
