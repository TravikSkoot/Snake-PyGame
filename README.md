
# 🐍 Snake Game in Pygame
Dieses Snake-Spiel ist in Python unter Verwendung des Pygame-Frameworks implementiert. Es enthält grundlegende Funktionen wie Bewegung, das Sammeln von Punkten (Futter), und Power-ups, die die Snake schneller oder langsamer machen. Außerdem gibt es eine Highscore-Funktion, die den höchsten erreichten Punktestand speichert.

## 🌟 Features
- **Klassisches Snake-Gameplay**: Steuere die Schlange und sammle Essen, um Punkte zu erhalten.
- **Anpassbare Farben**: Hintergrund und Schlange haben anpassbare Farben, um die Spielerfahrung zu personalisieren.
- **Power-Ups**:
  - **Speed Boost**: Erhöht die Geschwindigkeit der Schlange für eine begrenzte Zeit.
  - **Slowness**: Verringert die Geschwindigkeit für präziseres Manövrieren.
  - **Unsterblichkeit**: Die Schlange kann für kurze Zeit Kollisionen ignorieren.
- **Highscore-System**: Der höchste Punktestand wird gespeichert, um immer wieder neue Herausforderungen zu bieten.
- **FPS-Anzeige**: Debug-Modus mit FPS-Anzeige, um die Leistung zu überwachen.

## 🎮 Steuerung
- **Bewegen**: Verwende die Pfeiltasten oder `W`, `A`, `S`, `D`, um die Schlange zu steuern.
- **Neustart**: Drücke `Space`, um das Spiel neu zu starten.
- **Beenden**: Drücke `ESC`, um das Spiel zu beenden.

## 📥 Installation für Endbenutzer
Lade die neueste Version des Spiels über die GitHub-Releases herunter:

- [Download Snake Game v1.0.0 (.exe für Windows)](https://github.com/TravikSkoot/Snake-PyGame/releases/download/v1.0/snake_game.exe)
- [Download Snake Game v1.0.0 (.zip für Windows, entpacken und `.exe` ausführen)](https://github.com/TravikSkoot/Snake-PyGame/releases/download/v1.0/snake_game.zip)

Falls du Probleme mit Windows Defender hast, verwende die `.zip`-Datei. Entpacke sie und führe die `.exe`-Datei im entpackten Ordner aus.

## 📝 To-Do Liste
Die vollständige Roadmap und geplante Features sind in der [ROADMAP.md](ROADMAP.md) dokumentiert.

- [x] **Highscore-Funktion fixen**:
  - Der Highscore sollte korrekt gespeichert und geladen werden. 
  - Überprüfen, warum der Highscore manchmal nicht aktualisiert wird, wenn ein neuer Rekord erreicht wird.

- [x] **Mehr Power-ups hinzufügen**:
  - Weitere Power-ups wie Unverwundbarkeit oder Doppelpunktzahl implementieren.
  - Power-ups visuell von den normalen Futter-Items unterscheiden.

- [x] **Power-up Timer-Anzeige**:
  - Eine Anzeige hinzufügen, die zeigt, wie lange ein Power-up noch aktiv ist.
  - Visuelle Hinweise auf Power-ups, um dem Spieler zu signalisieren, dass ein Power-up aktiv ist.

- [x] **Mehrere Schwierigkeitsgrade**:
  - Schwierigkeitsgrade wie "Leicht", "Mittel" und "Schwer" implementieren, die unterschiedliche Startgeschwindigkeiten und Power-up-Frequenzen haben.

- [x] **Snake-Geschwindigkeit balancieren**:
  - Die Geschwindigkeit der Snake sollte sich alle 5 Punkte erhöhen, allerdings muss die Balance überprüft werden.
  - Maximalgeschwindigkeit anpassen, damit das Spiel nicht zu schwer wird.
 
- [ ] **Bessere Grafiken und Soundeffekte**:
  - Optionale Grafiken hinzufügen (z. B. eine bessere Darstellung der Snake und der Power-ups).
  - Soundeffekte für das Einsammeln von Punkten und Power-ups hinzufügen.

- [ ] **Pause-Funktion implementieren**:
  - Spieler sollten das Spiel pausieren und fortsetzen können (z. B. mit der `P`-Taste).

- [ ] **Erweiterung des Spielfelds**:
  - Möglichkeit hinzufügen, die Größe des Spielfelds dynamisch zu ändern.
  - Spielmodi für verschiedene Spielfeldgrößen (z. B. kleines, mittleres, großes Spielfeld).

## 🛠️ Installation für Entwickler
1. Klone das Repository:
   ```bash
   git clone https://github.com/TravikSkoot/Snake-PyGame.git
   ```
2. Installiere die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```
3. Führe das Spiel aus:
   ```bash
   python snake_game.py
   ```

## 📜 Lizenz
> Dieses Projekt steht unter der MIT-Lizenz. Weitere Details finden sich in der [LICENSE](LICENSE.md) Datei.
