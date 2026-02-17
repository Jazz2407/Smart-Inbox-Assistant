# 📧 Smart Inbox Assistant

**A Full-Stack AI-Powered Email Client** built with **React**, **FastAPI**, and **Local LLMs (Ollama)**.

The Smart Inbox Assistant helps you declutter your digital life by automatically fetching emails from Gmail, summarizing them, categorizing them by priority, and generating context-aware replies using a local AI model (Llama 3.2).

<img width="1080" height="892" alt="2" src="https://github.com/user-attachments/assets/a1a8e0ce-0557-462c-a0f7-89c2b36074d8" />

<img width="1046" height="604" alt="1" src="https://github.com/user-attachments/assets/5a62f767-575c-4cb6-b8b3-52d9b8d0e39c" />


## 🚀 Key Features

* **📩 Gmail Integration:** Securely fetches emails using the Gmail API and stores them locally for fast access.
* **🧠 Local AI Intelligence:** Uses **Ollama (Llama 3.2)** to analyze email content without sending data to external third-party AI clouds.
* **✨ Auto-Summarization:** Instantly provides a 1-sentence summary of long threads.
* **🏷️ Smart Categorization:** automatically tags emails as *High Priority*, *Work*, *Promotions*, etc.
* **🤖 AI Auto-Reply:** Generates professional draft replies with a single click based on the email context.
* **📎 File Attachments:** Supports sending emails with attachments (PDFs, Images, Zips, etc.).
* **⚡ Modern UI:** A clean, responsive dashboard built with React, Tailwind CSS, and Lucide Icons.

---

## 🛠️ Tech Stack

### **Frontend**
* **React.js** (Vite)
* **Tailwind CSS** (Styling)
* **Framer Motion** (Animations)
* **Lucide React** (Icons)

### **Backend**
* **FastAPI** (Python)
* **SQLAlchemy & SQLite** (Database)
* **Gmail API** (Email Fetching)
* **SMTP** (Email Sending)
* **Ollama** (Local LLM Integration)

---

## ⚙️ Installation & Setup

### Prerequisites
* Node.js & npm installed
* Python 3.10+ installed
* [Ollama](https://ollama.com/) installed and running (`ollama run llama3.2`)
* Google Cloud Console Project with Gmail API enabled

### 1️⃣ Backend Setup

```bash
# Clone the repository
git clone [https://github.com/yourusername/smart-inbox-assistant.git](https://github.com/yourusername/smart-inbox-assistant.git)
cd smart-inbox-assistant/backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
