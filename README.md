# Del 2 – Inloggningsfunktion (Selenium WebDriver)

Detta projekt innehåller automatiserade testfall för inloggningsfunktionen på [SauceDemo](https://www.saucedemo.com/).  
Testerna är skrivna i **Python** med hjälp av **Selenium WebDriver**.

---

## 📋 Kravspecifikation
### Grundläggande test (G)
- Lyckad inloggning med korrekta uppgifter (`standard_user` / `secret_sauce`).
- Verifiering: Användaren hamnar på startsidan (`/inventory.html`) och rubriken *Products* visas.

### Utökade tester (VG)
- Felaktigt användarnamn → felmeddelande visas.
- Felaktigt lösenord → felmeddelande visas.

---

## 🛠️ Installation
1. Klona repot:
   ```bash
   git clone https://github.com/alialsaade96/Del_2_Inloggningsfunktion.git
   cd Del_2_Inloggningsfunktion
