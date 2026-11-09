# Postępy nauki: API / REST API

Legenda: `[x]` zrobione · `[ ]` do zrobienia · ➡️ aktualny punkt

## 📍 Punkt startowy (dla nowej sesji)
- **Moduł:** M0, M1, M2 i M3 ukończone ✅. Następny: **M4. Uwierzytelnianie**.
- **Koncept:** M4, „API key”. Jeszcze nie zaczęty. Uczeń zna z M1 nagłówki HTTP, z M3 `httpx.get/post`, `params=`, `headers=` jeszcze nie używał (pokazać), `try/except`, `raise_for_status()`, retry z backoffem, paginację, zapis JSON i CSV (`csv.DictWriter`). Do ćwiczenia wybrać darmowe API z kluczem (np. pogoda); sprawdzić aktualną dokumentację wybranego API i httpx w context7. Klucz trzymać w `.env` poza repo (to temat osobnego konceptu, ale od początku nie wklejać kluczy do kodu). Słabszy punkt: literówki, odpowiedzi czasem mijają się z pytaniem (czytać pytanie dokładnie), wklejanie `params=` w tekst URL. Niezacommitowane: `m3_*.py`, `posts.json`, `posts.csv`, `pyproject.toml`, `uv.lock`, `GIT.md`, zmiany w `.md`, przypomnieć o gałęzi i PR (decyzja, czy `posts.*` trafiają do repo).
- **Pytanie czekające na odpowiedź:** brak. Zacznij od pierwszego konceptu M3.
- **Ustalenia:** narzędzie automatyzacji to Power Automate (nie n8n). Po każdym koncepcie pytanie rekrutacyjne do `INTERVIEW.md`. **Zamiast czystego venv używamy `uv`** (uczeń zainstalował uv 0.13.7, `.venv` utworzony przez `uv venv` w `E:\Projects\API`). Pełny workflow uv (`uv init`, `uv add`, `uv run`) pokazać przy pierwszej instalacji biblioteki (httpx w M3), składnię sprawdzić w context7 (/astral-sh/uv). Python 3.15.2, Git 2.56 zainstalowane. Postman zainstalowany.

## M0. Setup
- [x] Python 3.12+ i venv (uv)
- [x] VS Code
- [x] Git + konto GitHub, konfiguracja
- [x] Repo projektu (git init, .gitignore, commit, push)
- [x] Postman

## M1. Fundamenty HTTP i REST (bez kodu)
- [x] Klient, serwer i API
- [x] Request i response
- [x] Budowa URL (ścieżka, query params)
- [x] Metody HTTP (GET, POST, PUT, PATCH, DELETE)
- [x] Kody statusu (2xx, 4xx, 5xx)
- [x] Nagłówki (headers)
- [x] JSON
- [x] Zasady REST (zasoby, bezstanowość)
- [x] Idempotentność

## M2. Konsumowanie API ręcznie: Postman
- [x] Pierwsze zapytania do publicznego API
- [x] Kolekcje
- [x] Zmienne i środowiska
- [x] Testy (asercje) w Postmanie
- [x] Git w praktyce: gałęzie (branch) i pull request
- [x] **Mini-projekt:** kolekcja z testami na GitHubie

## M3. Konsumowanie API z kodu: Python + httpx
- [x] GET z kodu, parsowanie JSON
- [x] POST z kodu
- [x] Obsługa błędów i timeouty
- [x] Paginacja
- [x] Rate limiting i retry
- [x] **Mini-projekt:** skrypt raportu (API → CSV/JSON)

## M4. Uwierzytelnianie
- [ ] ➡️ API key
- [ ] Bearer token
- [ ] OAuth2 (koncepcja i flow)
- [ ] JWT
- [ ] Sekrety w `.env` i `.gitignore`
- [ ] **Ćwiczenie:** wywołanie API z kluczem (pogoda lub LLM)

## M5. Własne REST API: FastAPI
- [ ] Pierwszy endpoint i Uvicorn
- [ ] Path i query params
- [ ] Modele Pydantic i walidacja
- [ ] Kody statusu i obsługa błędów
- [ ] CRUD
- [ ] OpenAPI / Swagger (`/docs`)
- [ ] **Mini-projekt:** Tasks/Tickets API (dane w pamięci)

## M6. Baza danych i struktura projektu
- [ ] SQLite + SQLModel
- [ ] Routery i podział projektu
- [ ] Konfiguracja (settings)
- [ ] Zabezpieczenie API (klucz lub JWT)

## M7. Testowanie API
- [ ] pytest: podstawy
- [ ] TestClient z FastAPI
- [ ] Testy pozytywne i negatywne
- [ ] Fixtures
- [ ] Mockowanie zewnętrznych API
- [ ] Newman (Postman z CLI)
- [ ] GitHub Actions: CI uruchamiający pytest po każdym pushu

## M8. Integracja systemów
- [ ] Webhooki: odbieranie
- [ ] Webhooki: wysyłanie
- [ ] Async w Pythonie i httpx
- [ ] Integracja z API LLM (backend chatbota)
- [ ] Power Automate: akcja HTTP wywołująca Twoje API
- [ ] Power Automate: trigger „When an HTTP request is received” (flow jako webhook)
- [ ] Power Automate: Custom Connector z pliku OpenAPI Twojego FastAPI

## M9. Projekt portfolio: „Ticket/Lead API z asystentem AI”
- [ ] REST API + DB + auth
- [ ] Webhook przyjmujący zgłoszenia
- [ ] Klasyfikacja i odpowiedź przez LLM
- [ ] Testy pytest
- [ ] Kolekcja Postmana
- [ ] Docker
- [ ] README (uruchomienie, Swagger)

---

## Dziennik sesji
| Data | Co zrobione | Następny krok |
|------|-------------|---------------|
| 2026-11-06 | Plan nauki, CLAUDE.md, PROGRESS.md | M1: Klient, serwer i API (czeka na odpowiedź) |
| 2026-11-07 | **M1 ukończony**: 9 konceptów HTTP/REST, 9 pytań w INTERVIEW.md. Słabszy punkt: przy PATCH uczeń wpisał wartość w URL zamiast w body (poprawione). | M0 Setup, potem M2 Postman |
| 2026-11-08 | **M0 ukończony**: Python 3.15.2 + uv (`.venv`), VS Code, Git (konfiguracja), repo `api-learning` na GitHubie, Postman. 6 pytań dodanych do INTERVIEW.md. Plan uzupełniony o gałęzie/PR (M2) i GitHub Actions (M7). | M2: pierwsze zapytania w Postmanie |
| 2026-11-08 | **M2 ukończony**: Postman (pierwsze zapytania, kolekcje, zmienne i środowiska, testy asercji), Git: gałęzie, PR #1 i #2, merge, sprzątanie gałęzi. Kolekcja z testami w `postman/` na GitHubie, README. 5 pytań dodanych do INTERVIEW.md. Słabszy punkt: literówki (`usersId`). | M3: GET z kodu (httpx, uv) |
| 2026-11-09 | **M3 ukończony**: httpx GET/POST, `json()`, błędy i timeouty (`raise_for_status`, `try/except`), paginacja (`_page`/`_limit`), retry z exponential backoff, mini-projekt `m3_report.py` (API → JSON + CSV). 5 pytań dodanych do INTERVIEW.md. Słabszy punkt: `params=` wklejane w URL, logika `not []`, odpowiedzi mijające się z pytaniem. | M4: API key |
