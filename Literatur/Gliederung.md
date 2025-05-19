# Prüfzifferverfahren – Mathematische Grundlagen und Anwendungen

## Inhaltsverzeichnis

1. [Einleitung](#1-einleitung)  
2. [Theoretische Grundlagen](#2-theoretische-grundlagen)  
3. [Klassifikation von Prüfzifferverfahren](#3-klassifikation-von-prüfzifferverfahren)  
4. [Ausgewählte Prüfzifferverfahren im Detail](#4-ausgewählte-prüfzifferverfahren-im-detail)  
5. [Mathematische Analyse der Verfahren](#5-mathematische-analyse-der-verfahren)  
6. [Anwendungsbeispiele und praktische Bedeutung](#6-anwendungsbeispiele-und-praktische-bedeutung)  
7. [Fazit und Ausblick](#7-fazit-und-ausblick)  
8. [Literaturverzeichnis](#8-literaturverzeichnis)  
9. [Anhang](#9-anhang)

---

## 1. Einleitung

### 1.1 Motivation und Bedeutung von Prüfziffern  
Prüfziffern dienen der Erkennung von Übertragungs- oder Eingabefehlern in Zahlenfolgen. Sie sind besonders relevant in Bereichen wie Zahlungsverkehr, Produktkennzeichnung oder Netzwerktechnik.

### 1.2 Zielsetzung der Arbeit  
Diese Arbeit stellt verschiedene mathematische Prüfzifferverfahren vor, erläutert ihre Grundlagen und analysiert ihre Stärken.

### 1.3 Aufbau der Arbeit  
Zunächst werden grundlegende mathematische Konzepte erläutert, gefolgt von einer Klassifikation gängiger Verfahren anhand ihrer Struktur. Anschließend werden einzelne Verfahren detailliert analysiert und in der Praxis eingeordnet.

---

## 2. Theoretische Grundlagen

- **Zahlensysteme und Codierung**  
- **Fehlerarten** (Einzelfehler, Ziffernvertauschung, Mehrfachfehler)  
- **Modulare Arithmetik**  
- **Polynomrechnung über \( \mathbb{F}_2 \)**  
- **Skalarprodukt und Gewichtungen**

---

## 3. Klassifikation von Prüfzifferverfahren

Dieses Kapitel stellt verschiedene Arten von Prüfzifferverfahren vor – jeweils mit einem typischen Beispiel und mathematischer Erläuterung.

### 3.1 Einfaches Modulo-Verfahren

**Prinzip:**  
Die Prüfziffer wird so gewählt, dass die gesamte Ziffernfolge einen bestimmten Modulus ergibt.

**Mathematisches Werkzeug:**  
Modulo-Rechnung, Division mit Rest

**Beispiel:**  
**Bankleitzahl (DE, veraltet)**  
- Eine 7-stellige Zahl + Prüfziffer → Gesamtsumme durch 10 teilbar  
- Beispiel: Prüfziffer von `1234567` ist `3`, da `12345673 mod 10 = 0`

---

### 3.2 Gewichtsverfahren

**Prinzip:**  
Jede Ziffer der Grundzahl wird mit einem festen Gewicht multipliziert, die Summe bestimmt die Prüfziffer.

**Mathematisches Werkzeug:**  
Skalarprodukt, lineare Kombination

**Beispiel:**  
**EAN-13 (Europäischer Artikelcode)**  
- Gewichtung: abwechselnd 1 und 3  
- Beispiel:  
  - Ziffern: `400638133393`  
  - Gewichtetes Produkt:  
    \( 4 \cdot 1 + 0 \cdot 3 + 0 \cdot 1 + 6 \cdot 3 + 3 \cdot 1 + 8 \cdot 3 + 1 \cdot 1 + 3 \cdot 3 + 3 \cdot 1 + 3 \cdot 3 + 9 \cdot 1 + 3 \cdot 3 = 93 \)  
  - Prüfziffer: \( (10 - (93 \mod 10)) \mod 10 = 7 \)  
  - Vollständiger Code: `4006381333937`

---

### 3.3 Verfahren mit Permutation

**Prinzip:**  
Ziffernpositionen werden systematisch vertauscht und gewichtet, um Fehler wie Zifferntausch zu erkennen.

**Mathematisches Werkzeug:**  
Permutation, bedingte Gewichtung

**Beispiel:**  
**Luhn-Algorithmus (Kreditkarten)**  
- Ziffern: `4992739871`  
- Verdoppeln jeder zweiten Ziffer von rechts (ungerade Positionen), ggf. Quersumme bilden:  
  \( 4, 18, 9, 14, 7, 6, 9, 4, 7, 2 \) → Quersummen: \( 4, 9, 9, 5, 7, 6, 9, 4, 7, 2 \)  
  Summe = 62 → Prüfziffer = \( (10 - (62 \mod 10)) = 8 \)  
  Vollständige Nummer: `49927398718`

---

### 3.4 Polynomielle Verfahren (z. B. CRC)

**Prinzip:**  
Zahl wird als Bitfolge interpretiert und durch ein Generatorpolynom über \( \mathbb{F}_2 \) dividiert. Der Rest ist die Prüfziffer.

**Mathematisches Werkzeug:**  
Polynomdivision im Körper \( \mathbb{F}_2 \)

**Beispiel:**  
**CRC-32 (z. B. in Netzwerken, ZIP-Dateien)**  
- Generatorpolynom z. B.:  
  \( G(x) = x^{32} + x^{26} + x^{23} + \dots + 1 \)  
- Eingabefolge = Nachricht als Binärzahl  
- Prüfziffer = Rest \( R(x) \) aus \( \frac{M(x) \cdot x^k}{G(x)} \)

---

## 4. Ausgewählte Prüfzifferverfahren im Detail

- 4.1 ISBN (Modulo-11 mit Gewichtung)  
- 4.2 IBAN (Modulo-97)  
- 4.3 GTIN-13 (s. o.)  
- 4.4 Luhn (s. o.)  
- 4.5 CRC-32 (s. o.)

---

## 5. Mathematische Analyse der Verfahren

- Fehlerarten: Erkennbarkeit von Einzelfehlern, Zifferntausch usw.  
- Theoretischer Nachweis der Fehlererkennung  
- Vergleich nach Erkennungsleistung, Komplexität, Stabilität

---

## 6. Anwendungsbeispiele und praktische Bedeutung

- Finanzwesen (IBAN, Kreditkarten)  
- Logistik und Handel (Barcodes)  
- IT und Netzwerke (CRC)  
- Datensicherheit und -validierung

---

## 7. Fazit und Ausblick

- Zusammenfassung der Verfahren  
- Grenzen der Erkennung  
- Ausblick auf kombinierte oder adaptive Prüfsysteme

---

## 8. Literaturverzeichnis

*(Beispielhafte Einträge)*  
- Duden Informatik – Prüfziffern  
- Knuth, D.E.: The Art of Computer Programming, Vol. 2  
- ISO/IEC Normen zu Barcodes und IBAN

---

## 9. Anhang

- Beispielrechnungen  
- Gewichtungstabellen  
- Pseudocode oder Python-Skripte zur Veranschaulichung
