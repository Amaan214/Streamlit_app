# 🧠 LyfeHub – Medical Image Analysis App

**LyfeHub** is a powerful, user-friendly Streamlit application designed to provide AI-powered medical image analysis and suggest potential treatment options using Google Generative AI. This guide will walk you through the setup and usage.

---

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Features](#features)
- [Safety Settings](#safety-settings)
- [License](#license)

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/lyfehub.git
cd lyfehub

## 🔧 Installation

### 2. Install Dependencies

Ensure you have **Python 3.8+** installed, then run:

```bash
pip install -r requirements.txt

### 🔑 API Key Configuration

- Obtain an API key from **Google Generative AI**.
- Create a file named `api_key.py` in the root directory and add the following:

```python
api_key = "YOUR_API_KEY"

## 🚀 Usage

### ▶️ Run the Application

```bash
streamlit run app.py
### 🧭 Using the Interface

1. Open the provided Streamlit URL in your browser.
2. Upload a medical image (`.png`, `.jpeg`, or `.jpg`).
3. Click **"Click to generate analysis"** to get AI-powered diagnostic insights.

---

## ⚙️ Configuration

- **Temperature**: Adjusts the creativity of the AI model.
  - _Lower values_ → more focused, deterministic output.
  - _Higher values_ → more diverse, creative responses.

- **Safety Settings**: Ensures content is medically appropriate and adheres to AI safety standards.

---

## ✨ Features

- **📤 Image Upload**: Upload medical images in supported formats.
- **📑 AI-Powered Analysis**: Get comprehensive results including:
  - Clinical findings  
  - Potential diagnoses  
  - Treatment suggestions
- **🔒 Built-in Safety**: Configured to block unsafe or misleading outputs.

---

## 🔐 Safety Settings

To ensure responsible AI usage, the following safety thresholds are enforced:

```python
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

## 📄 License
This project is licensed under the MIT License.
See the LICENSE file for details.

## 🤝 Contributing
We welcome contributions and feedback!
For bug reports, feature requests, or improvements, please visit the GitHub repository.

Thank you for using LyfeHub.
We hope this tool helps in delivering efficient and accurate medical insights.
Stay healthy and informed! 🩺
