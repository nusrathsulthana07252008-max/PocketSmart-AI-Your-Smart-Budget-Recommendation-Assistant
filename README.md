# PocketSmart AI

AI-powered budget planning and recommendation assistant for home interiors, parties and jewelry shopping, based on the supplied project documentation.

## Stack
- FastAPI + Jinja2
- SQLite (zero setup)
- Google Gemini through the official `google-genai` SDK
- JWT authentication with HTTP-only cookies
- Responsive HTML/CSS/vanilla JavaScript
- Optional outfit-image analysis for jewelry planning

## Features
- Register/login/logout
- Home Interior Budget Planner
- Party Budget Planner
- Jewelry Budget Planner with optional outfit image
- Gemini JSON recommendations with a deterministic demo fallback
- India/INR-oriented shopping links
- Recommendation history and detail pages
- Health endpoint and API docs

## VS Code setup
1. Extract the ZIP and open the `PocketSmartAI` folder in VS Code.
2. Install Python 3.11+.
3. Create a virtual environment:
   - Windows: `py -m venv .venv`
   - macOS/Linux: `python3 -m venv .venv`
4. Activate it:
   - Windows PowerShell: `.venv\\Scripts\\Activate.ps1`
   - Windows CMD: `.venv\\Scripts\\activate.bat`
   - macOS/Linux: `source .venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Copy `.env.example` to `.env`.
7. For live AI, add your Gemini API key to `GEMINI_API_KEY`. Without it, demo recommendations are returned so the full UI can still be tested.
8. Start: `uvicorn app.main:app --reload`
9. Open `http://127.0.0.1:8000`.

## Testing
Run `pytest -q`.

## API
- `GET /health`
- `POST /api/register`
- `POST /api/login`
- `POST /api/logout`
- `GET /api/me`
- `POST /api/home-budget`
- `POST /api/party-budget`
- `POST /api/jewelry-budget`
- `GET /api/recommendation-history`
- `GET /api/recommendation/{id}`
- `GET /docs`

## Notes
The supplied documentation contains UI screenshots and OCR-unreliable code fragments. This implementation preserves the documented product concepts and flows while replacing broken/incomplete snippets with a clean working implementation. It does not claim to reproduce undocumented backend infrastructure such as AWS services; the local application uses SQLite and can be migrated to cloud services later.
