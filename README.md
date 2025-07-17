# 🦥💬 Chatbot with LangChain and Ollama (LLaMA2)

This is a **local AI chatbot app** built using:

* **LangChain** for prompt chaining
* **Ollama** for running LLaMA2 models locally
* **Streamlit** for interactive user interface

---

## 🚀 **Features**

✅ Ask any question to the LLaMA2 model
✅ Uses local Ollama installation (no external API cost)
✅ Clean and modular code for learning LangChain integrations

---

## 👥️ **Setup instructions**

### 1. **Clone the repository**

```bash
git clone https://github.com/yourusername/chatbot_langchain_ollama.git
cd chatbot_langchain_ollama
```

---

### 2. **Install Python dependencies**

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

Then install requirements:

```bash
pip install -r requirements.txt
```

---

### 3. **Install Ollama**

#### **On macOS**

```bash
brew install ollama
```

#### **On Linux**

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### **On Windows**

1. Install **WSL2 with Ubuntu**.
2. Inside Ubuntu terminal:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

### 4. **Pull the LLaMA2 model**

```bash
ollama pull llama2
```

---

### 5. **Run the app locally**

```bash
streamlit run main.py
```

Your app will open at `http://localhost:8501`.
