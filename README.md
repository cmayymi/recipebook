# RecipeBook

> A web app that automatically pulls a recipe out of a messy webpage (or pasted text) and turns it into clean, structured data — ingredients, steps, and servings, ready to search and scale.

## Why I'm building this

I save a lot of recipes from TikTok and cooking sites, and I almost never find them again when I actually want to cook. Most recipe pages bury the actual recipe inside a long blog post, and TikTok captions are even messier. This project is my attempt to fix that for myself: paste a link or some text in, get a clean recipe out.

## 🚧 Status: work in progress

This is an active learning project — I'm building it while learning full-stack web development. Nothing here is production-ready yet, and that's on purpose: I'm documenting the process as I go rather than only publishing a finished result.

| Feature | Status |
|---|---|
| Flask backend + routing | ✅ Done |
| Basic HTML pages (Flask templates) | ✅ Done |
| SQLite database (recipes, ingredients, steps) | 🔜 In progress |
| Recipe extraction from URLs (HTML / schema.org JSON-LD) | 🔜 In progress |
| LLM-based extraction fallback (for messy/unstructured text) | 🔜 In progress |
| Search | 🔜 Planned |
| Serving-size scaler (1x / 2x / 3x) | 🔜 Planned |
| Polished frontend | 🔜 Planned |
| One-click "save this page" browser extension | 💭 Future idea |

## Tech stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Recipe parsing:** HTML parsing + schema.org JSON-LD, with an LLM fallback for unstructured sources (planned)
- **Frontend:** HTML/CSS/JS (Flask templates for now; may move to React later)

## Project structure

```
recipebook/
├── .github/              # Workflow / automation files
├── apps/
│   ├── backend/
│   │   ├── app.py          # Main Flask server
│   │   ├── database.py     # SQLite connection & queries
│   │   ├── ai_parser.py    # LLM-based extraction logic
│   │   └── templates/      # HTML pages rendered by Flask
│   │       ├── index.html
│   │       └── receitas.html
│   ├── frontend/
│   │   ├── static/         # CSS / JS
│   │   └── views/          # Additional UI components
│   └── libs/              # Shared utility modules
├── design_files/          # DB schema diagrams, screen prototypes
├── requirements.txt        # Project dependencies
└── README.md
```

## Getting started

```bash
git clone https://github.com/<your-username>/recipebook.git
cd recipebook
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python apps/backend/app.py
```

## Roadmap

1. Finish URL-based extraction using schema.org JSON-LD (most recipe sites embed this)
2. Add an LLM fallback for pasted text / sites without structured data
3. Build search and the serving-size scaler
4. Polish the frontend
5. Explore a browser extension for one-click saving

## About

Built by Caroline Saito — Computer Science student at UNIOESTE, learning full-stack development one messy recipe at a time.