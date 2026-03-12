# 🔐 Password Strength Analyzer

A Python project that checks how strong a password is.
Uses **regex** to detect character types and gives a **score out of 10**.

---

## Files

```
password_analyzer/
├── analyzer.py       ← Core logic (regex checks + scoring)
├── main.py           ← Terminal / CLI version
├── app.py            ← Web server (Flask)
├── tests.py          ← Tests
├── requirements.txt  ← Python packages needed
└── static/
    └── index.html    ← Web UI (open in browser)
```

---

## How to Run

### Terminal version (no install needed)
```bash
python main.py
```

### Web version
```bash
pip install flask
python app.py
# Open http://localhost:5000
```

### Tests
```bash
python tests.py
```

---

## Scoring System

| Check              | Points |
|--------------------|--------|
| Password length    | 0–3    |
| Has uppercase      | 1      |
| Has lowercase      | 1      |
| Has numbers        | 1      |
| Has special chars  | 2      |
| No common patterns | 1      |
| **Total**          | **9 → scaled to 10** |

**Strength labels:**
- 0–3 → Weak
- 4–6 → Medium
- 7–8 → Strong
- 9–10 → Very Strong

---

## Deploy Online (Free)

### Render.com (easiest)
1. Push code to GitHub
2. Go to render.com → New Web Service
3. Connect your repo
4. Build command: `pip install flask`
5. Start command: `python app.py`
6. Get a public URL like `https://yourapp.onrender.com`

### PythonAnywhere
1. Create free account at pythonanywhere.com
2. Upload your files
3. Create a Flask web app pointing to `app.py`
4. Free URL: `yourname.pythonanywhere.com`

### Quick local share (no deploy)
```bash
python app.py
# Share your IP address with people on the same WiFi
# e.g. http://192.168.1.100:5000
```

---

## Key Concepts Used

- `re.search(r"[A-Z]", password)` — regex to find uppercase letters
- `re.search(r"[0-9]", password)` — regex to find numbers
- `re.search(r"(.)\1{2,}", password)` — regex to detect repeated chars
- Functions returning dictionaries with score + feedback
- A `while True` loop for the interactive CLI
- Flask `@app.route` for the web API

---

*Built with Python · No external libraries for core logic · Flask optional for web*
