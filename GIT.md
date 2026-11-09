# Ściąga: workflow Git (gałąź → PR → merge)

Zasada: **nigdy nie commituj prosto na `main`**. Każda zmiana idzie przez osobną gałąź i pull request.

## Pełny cykl krok po kroku

| # | Komenda / akcja | Po co |
|---|-----------------|-------|
| 1 | `git switch main` | Wracam na główną gałąź |
| 2 | `git pull` | Pobieram najnowszy stan z GitHuba |
| 3 | `git switch -c nazwa-galezi` | Tworzę nową gałąź i przełączam się na nią |
| 4 | *(pracuję: edytuję pliki)* | Zmiany powstają tylko na gałęzi |
| 5 | `git status` | Sprawdzam, co się zmieniło (Untracked / Modified) |
| 6 | `git diff` | Oglądam zmiany przed dodaniem |
| 7 | `git add plik` lub `git add folder` | Wrzucam wybrane zmiany do staging area |
| 8 | `git commit -m "Krótki opis zmiany"` | Zapisuję migawkę w lokalnej historii |
| 9 | `git push -u origin nazwa-galezi` | Wypycham gałąź na GitHuba (`-u` tylko za pierwszym razem) |
| 10 | GitHub: **Compare & pull request** → **Create pull request** | Otwieram PR (base: `main` ← compare: moja gałąź) |
| 11 | GitHub: zakładka **Files changed** | Przeglądam zmiany przed mergem |
| 12 | GitHub: **Merge pull request** → **Confirm merge** | Zmiany trafiają do `main` w chmurze |
| 13 | GitHub: **Delete branch** | Kasuję gałąź zdalną (albo `git push origin --delete nazwa-galezi`) |
| 14 | `git switch main` | Wracam na `main` lokalnie |
| 15 | `git pull` | Pobieram zmergowane zmiany na swój komputer |
| 16 | `git branch -d nazwa-galezi` | Kasuję gałąź lokalną |
| 17 | `git push origin --delete nazwa-galezi` | Kasuję gałąź zdalnego repo (to samo mozna osiągnąć ustawiajac w Github w opcjach, ze po merge sam kasuje) |
| 18 | `git branch -a` | Sprawdzam, czy zostało tylko `main` i `remotes/origin/main` |

## Wersja skrócona (do skopiowania)

```powershell
git switch main
git pull
git switch -c nazwa-galezi
# ...praca...
git status
git add .
git commit -m "Opis zmiany"
git push -u origin nazwa-galezi
# GitHub: PR -> Merge -> Delete branch
git switch main
git pull
git branch -d nazwa-galezi
```

## Przydatne pojedyncze komendy

| Komenda | Co robi |
|---------|---------|
| `git branch` | Lista gałęzi lokalnych (gwiazdka = aktualna) |
| `git branch -a` | Lokalne i zdalne |
| `git log --oneline -5` | Ostatnie 5 commitów w skrócie |
| `git diff --staged` | Zmiany już dodane przez `git add` |
| `git fetch --prune` | Czyści lokalne wpisy o skasowanych gałęziach zdalnych |

## Pułapki, które już się zdarzyły

- **`git branch -d` kasuje tylko lokalnie.** Gałąź zdalną usuwa się osobno.
- **Po mergu na GitHubie lokalny `main` jest stary**, dopóki nie zrobisz `git pull`.
- **Przed `git add` zawsze `git status`.** Upewnij się, że jesteś na właściwej gałęzi.
- **Sekretów (`.env`, klucze) nie commitujemy.** Są w `.gitignore`.
- **VS Code i konflikt wersji pliku:** gdy plik został zmieniony na dysku, wybierz *Revert File* albo *Compare*, nie *Overwrite*.

## Nazwy gałęzi i commitów

- Gałąź: krótko, małymi literami, myślnikami, np. `postman-more-tests`, `httpx-get`.
- Commit: jedno zdanie w trybie rozkazującym, np. „Dodaj testy do kolekcji”, „Popraw literówkę w README”.
