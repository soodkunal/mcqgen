# 🧠 MCQ Generator Application - Powered by LangChain & Streamlit

This is a simple Streamlit-based MCQ generator that uses LangChain and LLMs to create quizzes from uploaded text or PDF files.

---

## 🚀 Deploy on AWS EC2 (Ubuntu)

Follow these steps to deploy and run the application on an Ubuntu-based EC2 instance.

---

### ✅ Step 1: Launch EC2

1. Log in to the [AWS Console](https://aws.amazon.com/console/)
2. Search for and launch an **EC2 instance**
3. Choose **Ubuntu** as the OS
4. Configure instance settings, choose key pair, and launch

---

### 🛠️ Step 2: Set Up Ubuntu Instance

SSH into your instance, then run the following commands to update and prepare your environment:

```bash
sudo apt update
sudo apt-get update
sudo apt upgrade -y
sudo apt install git curl unzip tar make sudo vim wget -y

---

### 📦 Step 3: Clone the Repository

git clone https://github.com/soodkunal/mcqgen.git
cd mcqgen

---

### 🐍  Step 4: Install Python & Requirements

sudo apt install python3-pip -y
pip3 install -r requirements.txt

---

### 🔑 Step 5: Add OpenAI API Key (Optional)

If your app uses OpenAI or another API key, create a .env file:

  touch .env
  vi .env

Inside the file, press i to insert, then paste:

  OPENAI_API_KEY=your_openai_key_here

Then press Esc, type :wq, and hit Enter to save.

---

### ▶️ Step 6: Run the App

python3 -m streamlit run streamlit_app.py

---

### 🌐 Step 7: Access in Browser

1. Go to your EC2 Dashboard → Security Groups

2. Edit Inbound Rules:
  
   Add Custom TCP Rule
    
   Port: 8501
    
   Source: Anywhere (0.0.0.0/0)

Then open your browser and visit:

  http://<your-ec2-public-ip>:8501
