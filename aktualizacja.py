import requests

url = r"""https://www.ur.edu.pl/files/user_directory/305/RATOWNICTWO%20MEDYCZNE/PLANY%20ZAJ%C4%98%C4%86/1%20rok%20Ratownictwo%20medyczne%20semestr%201%20zimowy%202026.2027%209.10.xlsx"""

nazwa_pliku = "plan.xlsx"

# Nagłówek informujący serwer, że zapytanie idzie z normalnej przeglądarki
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Pobieranie pliku z uwzględnieniem nagłówka
response = requests.get(url, headers=headers)

# Sprawdzenie czy się udało
if response.status_code == 200:
    with open(nazwa_pliku, "wb") as f:
        f.write(response.content)
    print("Plik został pomyślnie pobrany!")
else:
    print(f"Nadal występuje błąd. Kod statusu: {response.status_code}")