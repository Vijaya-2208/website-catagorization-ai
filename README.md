# 🔍 Website Categorization AI (Flask + Transformers)

A simple AI-powered web app that classifies websites into categories (like News, Tech, Finance, etc.) using the content of the page. It uses a zero-shot classification model from Hugging Face (`facebook/bart-large-mnli`) and works offline after setup.

---

## 🚀 Features

- Enter any website URL
- Extracts and cleans the visible text
- Predicts category using a local transformer model
- Built with Flask, BeautifulSoup (or Selenium), and Hugging Face Transformers
- Zero-shot classification — no custom training needed

---

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/website-categorizer.git
cd website-categorizer

2. Set up a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Download the transformer model
python download_model.py
This will automatically create a model/ folder and save the BART model files locally.

▶️ Run the App
python app.py
Then open your browser at:
http://127.0.0.1:5000
Enter a website URL and view the predicted category.

To deactivate your Python virtual environment:
deactivate
