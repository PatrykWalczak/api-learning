# Pytania rekrutacyjne: API / REST

Jedno pytanie na każdy opanowany koncept. Przed rozmową o pracę powtórz na głos: zasłoń odpowiedź i odpowiedz sam.

## M1. Fundamenty HTTP i REST

### Czym jest API?
> API (Application Programming Interface) to kontrakt, który określa, jak jeden program może komunikować się z drugim: jakie zapytania można wysłać, w jakim formacie i jaką odpowiedź się dostanie. Ukrywa wewnętrzną implementację i udostępnia tylko to, co dozwolone. Dzięki temu systemy napisane w różnych technologiach mogą się integrować.

### Z czego składa się request i response HTTP?
> Request ma metodę (np. GET, POST), URL, nagłówki i opcjonalnie body. Response ma kod statusu, nagłówki i opcjonalnie body. Nagłówki niosą metadane, np. autoryzację i typ treści (`Content-Type`), a body niesie właściwe dane, najczęściej w JSON.

### Jaka jest różnica między path parameter a query parameter?
> Path parameter jest częścią ścieżki i wskazuje konkretny zasób, np. `/tickets/42`, więc zwykle jest wymagany. Query parameter stoi po `?` i modyfikuje sposób pobrania: filtruje, sortuje albo stronicuje, np. `/tickets?status=open&sort=date`, i zwykle jest opcjonalny. Krótka zasada: path mówi „co”, query mówi „jak”.

### Jaka jest różnica między PUT a PATCH?
> PUT zastępuje cały zasób: wysyłasz wszystkie pola, a pole, którego nie podasz, może zostać wyczyszczone. PATCH zmienia tylko te pola, które wyślesz, np. `{"status": "closed"}`. PUT jest idempotentny. PATCH zwykle też jest, ale specyfikacja HTTP tego nie gwarantuje.

### Jaka jest różnica między kodem 401 a 403?
> 401 Unauthorized oznacza brak uwierzytelnienia: serwer nie wie, kim jesteś, bo brakuje tokenu albo jest nieprawidłowy. 403 Forbidden oznacza brak autoryzacji: serwer wie, kim jesteś, ale nie masz uprawnień do tego zasobu. Przy 401 pomaga zalogowanie się albo poprawny klucz, przy 403 nie, bo potrzebne są inne uprawnienia.

### Czym różni się nagłówek Content-Type od Accept?
> `Content-Type` określa format body, które wysyłam. W requeście mówi serwerowi, jak odczytać moje dane, np. `application/json`. W odpowiedzi serwer ustawia go dla swojego body. `Accept` to prośba klienta: w jakim formacie chcę dostać odpowiedź. Krótko: Content-Type mówi „to wysyłam”, Accept mówi „to chcę dostać”.

### Czym jest JSON i dlaczego jest standardem w REST API (zamiast XML)?
> JSON to lekki, tekstowy format danych oparty na parach klucz–wartość, z typami: string, number, boolean, null, object i array. Jest czytelniejszy i krótszy niż XML, szybciej się go parsuje, a prawie każdy język ma wbudowaną obsługę (w Pythonie moduł `json`, gdzie object to `dict`, a array to `list`). XML nadal spotyka się w starszych systemach i w SOAP.

### Co oznacza, że REST API jest bezstanowe (stateless)?
> Serwer nie przechowuje stanu sesji klienta między zapytaniami. Każdy request musi zawierać wszystko, co potrzebne do jego obsługi: token uwierzytelniający, dane i kontekst. Dzięki temu API łatwo skalować, bo każdy request może obsłużyć dowolna instancja serwera. Przykład: przy API LLM wysyłasz za każdym razem całą historię rozmowy.

### Co to jest idempotentność i które metody HTTP są idempotentne?
> Operacja jest idempotentna, gdy wykonanie jej wiele razy daje ten sam stan na serwerze co wykonanie raz. Liczy się stan, nie identyczna odpowiedź. Idempotentne są GET, PUT, DELETE (a także HEAD i OPTIONS). POST nie jest, bo każde wywołanie tworzy nowy zasób. Ma to znaczenie przy retry: metodę idempotentną można bezpiecznie ponowić, a przy POST stosuje się np. nagłówek `Idempotency-Key`, żeby uniknąć duplikatów.

## M0. Setup

### Do czego służy wirtualne środowisko (venv) w Pythonie i dlaczego warto używać uv?
> Venv to izolowane środowisko z własną kopią Pythona i bibliotek dla jednego projektu. Zapobiega konfliktom wersji między projektami i nie zaśmieca systemowego Pythona. Środowisko odtwarza się z pliku zależności (`pyproject.toml` i lockfile, dawniej `requirements.txt`), więc zespół i nowy komputer mają identyczny zestaw bibliotek. uv to szybkie narzędzie w Rust, które zastępuje pip i venv: tworzy środowisko, instaluje zależności i generuje lockfile.

### Jak przygotowujesz środowisko pracy nad nowym projektem w Pythonie i co trafia do repozytorium?
> Tworzę repozytorium i wirtualne środowisko (u mnie `uv venv`), a w edytorze, np. VS Code, wybieram interpreter z `.venv`, żeby podpowiedzi i debugger widziały właściwe biblioteki. Do repozytorium trafia kod oraz pliki zależności (`pyproject.toml`, lockfile), a folder `.venv` i sekrety z `.env` trafiają do `.gitignore`. Dzięki temu każdy w zespole odtwarza to samo środowisko jedną komendą.

### Jaka jest różnica między Gitem a GitHubem?
> Git to rozproszony system kontroli wersji, który działa lokalnie i zapisuje historię zmian w kodzie (commity, gałęzie). GitHub to platforma w chmurze, która hostuje repozytoria Gita i dodaje do nich współpracę: pull requesty, code review, issues i CI/CD (GitHub Actions). Gita można używać bez GitHuba. Są też alternatywy dla GitHuba, np. GitLab i Bitbucket.

### Jak chronisz sekrety (klucze API, hasła) w projekcie i co robisz, gdy sekret trafi do repozytorium?
> Sekrety trzymam w pliku `.env` lub zmiennych środowiskowych, a `.env` dodaję do `.gitignore`. W repozytorium zostaje tylko `.env.example` bez wartości. Jeśli sekret trafi do repo, samo usunięcie pliku nie wystarcza, bo zostaje w historii commitów. Trzeba natychmiast unieważnić i wygenerować nowy klucz (rotacja), dopiero potem ewentualnie czyścić historię. Boty skanują GitHuba w poszukiwaniu kluczy w ciągu minut.

### Czym jest staging area (index) w Gicie i po co jest osobny krok `git add` przed `git commit`?
> Staging area to przechowalnia między katalogiem roboczym a historią. `git add` wybiera, które zmiany trafią do następnego commita, a `git commit` zapisuje je jako migawkę w lokalnej historii. Dzięki temu mogę z wielu zmian zrobić kilka małych, logicznych commitów (np. osobno poprawkę błędu i refaktoryzację) i przed zapisem sprawdzić `git status` i `git diff --staged`. Commit zostaje lokalny, dopiero `git push` wysyła go na zdalne repozytorium.

### Czym jest remote i `origin` w Gicie oraz czym różni się `git push` od `git pull`?
> Remote to zapisany w lokalnym repo adres zdalnego repozytorium, np. na GitHubie. `origin` to domyślna nazwa (alias) nadawana głównemu remote'owi, wygodniejsza niż pełny URL. `git push` wysyła moje lokalne commity do remote, a `git pull` pobiera cudze zmiany z remote i scala je z moją gałęzią (to `git fetch` plus `merge`). Przed pushem warto zrobić pull, żeby uniknąć konfliktów.

### Czym jest Postman i do czego służy w pracy z API?
> Postman to narzędzie do ręcznego wysyłania zapytań HTTP i oglądania odpowiedzi bez pisania kodu. Pozwala ustawić metodę, URL, nagłówki, body i uwierzytelnianie, grupować zapytania w kolekcje, używać zmiennych i środowisk (dev, test, prod) oraz pisać testy-asercje w JavaScripcie. Kolekcje można uruchamiać z terminala przez Newmana albo Postman CLI, np. w CI. Używam go do eksploracji API, debugowania i testów, a do automatyzacji w kodzie biblioteki typu `httpx` lub `requests`.
