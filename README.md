# 🧳 Rasa Chatbot - Travel Agency (Arabic)

A smart Arabic-speaking travel assistant chatbot built with [Rasa](https://rasa.com). This chatbot helps users book flights and hotels, select and confirm travel options, and interact with a travel agency—all in natural Arabic language.

## 🚀 Features

- Book flight tickets ✈️
- Book hotels 🏨
- Confirm or modify reservations
- Arabic language support (NLU + dialogue)
- Suggest travel options based on user input
- Deployed on a local interface with web chat

## 🛠️ Tech Stack

- Python 3.8+
- Rasa (NLU + Core)
- TensorFlow (Rasa-compatible version)
- HTML (for embedding the chatbot)
- Custom actions (API call simulation)

## 🔧 Setup & Usage

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rasa_chatbot_travel-agency.git
cd rasa_chatbot_travel-agency
```

### 2. Create a virtual environment

```bash
# Linux/macOS
python -m venv venv
source venv/bin/activate
```

```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Rasa

```bash
pip install rasa
```

### 4. Train the model

```bash
rasa train
```

### 5. Run the assistant

```bash
rasa run actions & rasa shell
```
