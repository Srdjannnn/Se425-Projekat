# Dokumentacija Projekta: Sistem za Prodaju Karata za Klub

## Uvod u Temu i Motivacija

Ovaj projekat se bavi razvojem jednostavnog web sistema za prodaju karata za klub. Motivacija je stvaranje funkcionalne demonstracione aplikacije koja simulira prodaju ulaznica za muzičke događaje u klubu, omogućavajući korisnicima pregled događaja i odabir sedišta.

## Opis Problema

Klubovi često imaju potrebu za efikasnim sistemom prodaje karata kako bi upravljali rezervacijama sedišta za različite događaje. Postojeći sistemi mogu biti skupi ili prekomplikovani, pa je potreban jednostavan demo sistem koji pokazuje osnovne funkcionalnosti.

## Stejkholderi

- **Vlasnik kluba**: Koristi sistem za upravljanje prodajom karata.
- **Posetioci kluba**: Kupuju karte i biraju sedišta.
- **Administrator sistema**: Održava i ažurira događaje.

## Ciljni Korisnici

Glavni ciljni korisnici su posetioci kluba koji žele da kupe karte za događaje. Sistem je dizajniran da bude jednostavan za korišćenje.

## Glavni Ciljevi Projekta

- Kreirati web aplikaciju za pregled događaja.
- Omogućiti odabir sedišta za događaje.
- Simulirati kupovinu karata (bez realne transakcije).

## Analiza Zahteva

### Funkcionalni Zahtevi

- Prikaz liste događaja.
- Prikaz detalja događaja sa mapom sedišta.
- Odabir dostupnog sedišta.
- Potvrda kupovine karte.

### Nefunkcionalni Zahtevi

- Sistem mora biti brz i responzivan.
- Jednostavan UI/UX.
- Bezbednost: Osnovna validacija.

## Use Case Scenariji

1. **Pregled Događaja**: Korisnik otvara početnu stranu i vidi listu događaja.
2. **Odabir Sedišta**: Korisnik bira događaj, vidi mapu sedišta i klikne na dostupno sedišće.
3. **Kupovina Karte**: Korisnik potvrđuje kupovinu i dobija potvrdu.

## Tehnike Prioritizacije Zahteva (MoSCoW)

- **Must Have**: Prikaz događaja, odabir sedišta, potvrda kupovine.
- **Should Have**: Jednostavan UI.
- **Could Have**: Dodatne funkcije kao što su login.
- **Won't Have**: Realne transakcije, baza podataka.

## Definicija MVP-a (Minimum Viable Product)

MVP uključuje osnovne funkcionalnosti: pregled događaja, odabir sedišta i simulacija kupovine. Sistem koristi in-memory podatke bez baze.

## Potrebni Dijagrami

### Use Case Dijagram

- Akteri: Korisnik
- Use Cases: Pregled Događaja, Odabir Sedišta, Kupovina Karte

### Activity Dijagram

1. Korisnik otvara aplikaciju.
2. Birа događaj.
3. Odabira sedišće.
4. Potvrđuje kupovinu.

### Dijagram Arhitekture Sistema

- Frontend: HTML/CSS/JS
- Backend: Flask (Python)
- Podaci: In-memory (liste)

## Tehnologije Koje će Biti Korišćene

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Verzionisanje**: Git
- **Organizacija**: Trello

## Plan Implementacije i Vremenska Linija

- **Faza 1 (P1 N1)**: Dokumentacija (trenutno).
- **Faza 2 (P1 N2)**: Prototip (implementiran).
- **Faza 3 (P2 N1)**: Finalna dokumentacija.
- **Faza 4 (P2 N2)**: Funkcionalna aplikacija (proširenje prototipa).

Vremenska linija: 2 nedelje po fazi.

## Reference i Prilozi

- Flask dokumentacija: https://flask.palletsprojects.com/
- Git: https://git-scm.com/