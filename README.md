# 🏡 HomeHunter – Wyszukiwarka domów i mieszkań

HomeHunter to aplikacja do wyszukiwania nieruchomości w Polsce, która agreguje oferty z wielu popularnych portali nieruchomościowych (Otodom, OLX, Nieruchomości-Online).

## ✨ Funkcje

- 🔍 **Wyszukiwanie ofert** z wielu źródeł jednocześnie
- ❤️ **System ulubionych** z możliwością dodawania notatek
- 🗺️ **Widok mapy** z lokalizacją ofert
- 💾 **Lokalna baza danych SQLite** do przechowywania ulubionych
- 🎨 **Elegancki interfejs** z minimalistycznym designem
- 🍎 **Pakiet jako aplikacja macOS** (.app)

## 📦 Instalacja

### Wymagania

- Python 3.8 lub nowszy
- macOS (dla pakietu .app)

### Instalacja zależności

```bash
pip install -r requirements.txt
```

## 🚀 Uruchomienie

### Szybki start

1. **Zainstaluj zależności:**
```bash
pip install -r requirements.txt
```

2. **Uruchom aplikację:**
```bash
streamlit run app.py
```

Aplikacja automatycznie otworzy się w przeglądarce pod adresem `http://localhost:8501`.

### Testowanie

Przed pierwszym uruchomieniem możesz przetestować moduły:

```bash
python3 test_app.py
```

### Pakowanie jako aplikacja macOS

1. Zainstaluj py2app (jeśli jeszcze nie masz):
```bash
pip install py2app
```

2. Zbuduj aplikację:
```bash
python build_mac_app.py py2app
```

3. Uruchom aplikację:
```bash
open dist/HomeHunter.app
```

**Uwaga:** Przed pakowaniem upewnij się, że:
- Masz plik `assets/icon.icns` jako ikonę aplikacji
- Wszystkie pliki źródłowe są w odpowiednich katalogach

## 📁 Struktura projektu

```
homehunter/
├── app.py                              # Główna aplikacja Streamlit
├── database.py                         # Moduł bazy danych SQLite
├── launcher.py                         # Skrypt uruchamiający dla macOS
├── build_mac_app.py                    # Skrypt budujący aplikację macOS
├── requirements.txt                     # Zależności Python
├── scrapers/                           # Moduł scraperów
│   ├── __init__.py
│   ├── otodom_scraper.py              # Scraper Otodom (mock)
│   ├── olx_scraper.py                 # Scraper OLX (mock)
│   └── nieruchomosci_online_scraper.py # Scraper Nieruchomości-Online (mock)
└── assets/                             # Zasoby graficzne
    ├── logos/                          # Loga źródeł
    │   ├── otodom.png
    │   ├── olx.png
    │   └── nieruchomosci.png
    └── icon.icns                       # Ikona aplikacji macOS
```

## 🎯 Jak używać

### 1. Wyszukiwanie ofert

1. Wybierz lokalizację (domyślnie: Wrocław)
2. Ustaw promień wyszukiwania
3. Wybierz zakres cenowy
4. Wybierz typ nieruchomości
5. Kliknij **"Szukaj ofert"**

Aplikacja równolegle pobierze dane ze wszystkich źródeł i wyświetli wyniki.

### 2. Przeglądanie wyników

- **Widok listy**: Karty z obrazkami, ceną, powierzchnią i lokalizacją
- **Widok mapy**: Wizualizacja na mapie (wymaga danych geograficznych)

### 3. Zarządzanie ulubionymi

- Kliknij **"❤️ Dodaj do ulubionych"** na dowolnej ofercie
- Przejdź do zakładki **"❤️ Ulubione"** w pasku bocznym
- Dodaj notatki do ulubionych ofert
- Usuń oferty z listy ulubionych

## 🔧 Rozwój

### Scrapery (obecnie mock)

Obecnie wszystkie scrapery zwracają losowe dane mock. Aby zaimplementować prawdziwe scrapery:

1. Otwórz odpowiedni plik w katalogu `scrapers/`
2. Zaimplementuj funkcję `fetch_*()` używając biblioteki do scrapingu (np. `requests`, `beautifulsoup4`, `selenium`)
3. Zwróć listę słowników zgodnie ze standardowym formatem

**Uwaga:** Pamiętaj o przestrzeganiu regulaminów stron i zasad etycznego scrapingu (robots.txt, rate limiting).

### Dodawanie nowych źródeł

1. Utwórz nowy plik `scrapers/new_source_scraper.py`
2. Zaimplementuj funkcję `fetch_new_source()` z tym samym interfejsem
3. Dodaj import i wywołanie w `app.py`
4. Dodaj logo do `assets/logos/new_source.png`

## 📝 Licencja

Ten projekt został stworzony do celów edukacyjnych i demonstracyjnych.

## ⚠️ Uwagi prawne

- Scrapery są obecnie w trybie mock (zwracają losowe dane)
- Przed implementacją prawdziwych scraperów sprawdź regulaminy stron
- Przestrzegaj zasad etycznego scrapingu i rate limiting
- Nie używaj aplikacji do celów komercyjnych bez odpowiednich licencji

## 🐛 Rozwiązywanie problemów

### Problem: Aplikacja nie uruchamia się

- Sprawdź, czy wszystkie zależności są zainstalowane: `pip install -r requirements.txt`
- Upewnij się, że używasz Python 3.8+

### Problem: Brak ikon/logo

- Utwórz pliki PNG dla logo w `assets/logos/`
- Utwórz plik `.icns` dla ikony aplikacji (możesz użyć narzędzia jak `iconutil` na macOS)

### Problem: Błąd podczas pakowania macOS

- Upewnij się, że py2app jest zainstalowane: `pip install py2app`
- Sprawdź, czy wszystkie ścieżki do plików są poprawne
- Na pierwsze uruchomienie py2app może wymagać dodatkowych uprawnień

## 📧 Kontakt

W razie pytań lub problemów, utwórz issue w repozytorium projektu.

---

Made with ❤️ for finding your dream home 🏡

