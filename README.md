
# 🧠 Custom AI Chatbot with Fine-Tuned GPT-2

A lightweight chatbot app powered by a fine-tuned DistilGPT-2 model trained on your own question-answer pairs. This project supports both exact/fuzzy matching and intelligent fallback using language generation. It also includes a responsive Flask-based web UI.

---

## 🌟 Demo

![Chat UI](assets/chat_ui.png)

---

## 📦 Features

- ✅ Fine-tuning GPT-2 on custom Q&A dataset
- 🔍 Fuzzy matching with fallback to language generation
- 💬 Clean web UI for chat via Flask
- 📁 Lightweight, runs in Google Colab or locally
- 🔄 Easily extendable with more training data

---

## 🗂 Project Structure

```
custom-chatbot/
├── dataset.json           # Custom Q&A pairs
├── train_model.py         # Fine-tune GPT-2 on dataset
├── chatbot.py             # Core logic (match + generation)
├── app.py                 # Flask API & UI
├── requirements.txt       # Python dependencies
├── model/                 # Fine-tuned GPT-2 model (via Git LFS)
├── assets/
│   └── chat_ui.png        # UI screenshot (used in README)
└── README.md              # This file
```

---

## 🚀 How to Run

### 🔧 Setup (Local or Colab)
1. Clone this repo:
   ```bash
   git clone https://github.com/tejash-300/build-custom-chatbot.git
   cd build-custom-chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Enable Git LFS for model files:
   ```bash
   git lfs install
   git lfs pull
   ```

---

### 🧠 Train the Model

```bash
python train_model.py
```

- This fine-tunes `distilgpt2` on your Q&A pairs from `dataset.json`.
- The trained model is saved under `/model`.

---

### 💬 Start Chat UI

```bash
python app.py
```

Then open `http://localhost:5000` in your browser. You’ll see a live chatbot UI where you can start chatting.

---

## 📥 Customize

- Add more Q&A entries to `dataset.json`
- Style the UI (in `app.py`) using HTML/CSS
- Replace GPT-2 with other Hugging Face models if needed

---

## 📸 Screenshot

Add this image to your repo at `assets/chat_ui.png`:

![Chat UI](assets/chat_ui.png)

> Screenshot of the chatbot web UI running via Flask and ngrok.

---

## 📌 Requirements

- Python 3.8+
- `transformers`, `torch`, `flask`, `pyngrok`, `datasets`

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Made with ❤️ by [Tejas Pandey](https://github.com/tejash-300)

```

---

### ✅ What to do now:

1. Save your uploaded screenshot as:
   ```
   assets/chat_ui.png
   ```
2. Copy and paste the full `README.md` content into a file at the root of your project.
3. Commit both:
   ```bash
   git add README.md assets/chat_ui.png
   git commit -m "Add README with UI screenshot"
   git push origin main
   ```

Let me know if you also want a **video demo section**, **Colab badge**, or **GitHub Pages deployment** added.


