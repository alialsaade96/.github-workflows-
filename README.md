Del 2 – Inloggningsfunktion (Selenium WebDriver)
Detta projekt innehåller automatiserade testfall för inloggningsfunktionen på SauceDemo. Testerna är skrivna i Python med hjälp av Selenium WebDriver och täcker både grundläggande (G) och utökade (VG) krav.

📋 Kravspecifikation
Grundläggande test (G):

Lyckad inloggning med korrekta uppgifter (standard_user / secret_sauce).

Verifiering: Användaren hamnar på startsidan (/inventory.html) och rubriken Products visas.

Utökade tester (VG):

Felaktigt användarnamn → felmeddelande visas: Epic sadface: Username and password do not match any user in this service

Felaktigt lösenord → samma felmeddelande visas.

🧪 Testfall
Del_2_test_login_success.py → Lyckad inloggning.

Del_2_test_login_invalid_username.py → Felaktigt användarnamn.

Del_2_test_login_invalid_password.py → Felaktigt lösenord.

👉 För att underlätta observation har en 10 sekunders paus (time.sleep(10)) lagts in i testerna. Detta gör att webbläsarfönstret inte stängs direkt, utan hålls öppet så att man hinner läsa felmeddelandet eller se att inloggningen lyckats innan fönstret stängs automatiskt.

🛠️ Installation
Klona repot:

bash
git clone https://github.com/alialsaade96/Del_2_Inloggningsfunktion.git
cd Del_2_Inloggningsfunktion
Installera beroenden:

bash
pip install -r requirements.txt
▶️ Kör testerna
Använd pytest:

bash
pytest
✅ Sammanfattning
Projektet uppfyller både G‑ och VG‑kraven:

Lyckad inloggning verifieras.

Felaktigt användarnamn och lösenord ger korrekt felmeddelande.

Testerna är strukturerade, automatiserade och observerbara tack vare pausen på 10 sekunder.
