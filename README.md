
# Snake Game in Pygame

Dieses Snake-Spiel ist in Python unter Verwendung des Pygame-Frameworks implementiert. Es enthält grundlegende Funktionen wie Bewegung, das Sammeln von Punkten (Futter), und Power-ups, die die Snake schneller oder langsamer machen. Außerdem gibt es eine Highscore-Funktion, die den höchsten erreichten Punktestand speichert.

## Features

- Bewegung der Snake mit WASD oder Pfeiltasten
- Sammeln von Punkten
- Power-ups (z. B. Speed Boost und Verlangsamung)
- Highscore-Speicherung
- Variable Hintergrundfarben und Snake-Farben
- Anpassbare Geschwindigkeitserhöhung basierend auf der Punktzahl
- FPS-Anzeige im Fenstertitel (Debug-Modus)

## Installation

1. Klone das Repository:
   ```bash
   git clone <repository-url>
   ```
2. Installiere die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```
3. Führe das Spiel aus:
   ```bash
   python snake_game.py
   ```

## Steuerung

- **Bewegung**: WASD oder Pfeiltasten
- **Neustart**: Leertaste
- **Beenden**: Escape-Taste

## To-Do Liste

1. **Highscore-Funktion fixen**: 
   - Der Highscore sollte korrekt gespeichert und geladen werden. 
   - Überprüfen, warum der Highscore manchmal nicht aktualisiert wird, wenn ein neuer Rekord erreicht wird.

2. **Mehr Power-ups hinzufügen**:
   - Weitere Power-ups wie Unverwundbarkeit oder Doppelpunktzahl implementieren.
   - Power-ups visuell von den normalen Futter-Items unterscheiden.

3. **Snake-Geschwindigkeit balancieren**:
   - Die Geschwindigkeitserhöhung der Snake alle 5 Punkte funktioniert, aber die Balance muss überprüft werden.
   - Maximalgeschwindigkeit anpassen, damit das Spiel nicht zu schwer wird.

4. **Bessere Grafiken und Soundeffekte**:
   - Optionale Grafiken hinzufügen (z. B. eine bessere Darstellung der Snake und der Power-ups).
   - Soundeffekte für das Einsammeln von Punkten und Power-ups hinzufügen.

5. **Pause-Funktion implementieren**:
   - Spieler sollten das Spiel pausieren und fortsetzen können (z. B. mit der `P`-Taste).

6. **Erweiterung des Spielfelds**:
   - Möglichkeit hinzufügen, die Größe des Spielfelds dynamisch zu ändern.
   - Spielmodi für verschiedene Spielfeldgrößen (z. B. kleines, mittleres, großes Spielfeld).

7. **Power-up Timer-Anzeige**:
   - Eine Anzeige hinzufügen, die zeigt, wie lange ein Power-up noch aktiv ist.
   - Visuelle Hinweise auf Power-ups, um dem Spieler zu signalisieren, dass ein Power-up aktiv ist.

8. **Mehrere Schwierigkeitsgrade**:
   - Schwierigkeitsgrade wie "Leicht", "Mittel" und "Schwer" implementieren, die unterschiedliche Startgeschwindigkeiten und Power-up-Frequenzen haben.

## Debug-Modus

Der Debug-Modus kann aktiviert werden, um die FPS im Fenstertitel anzuzeigen:
```python
debug_mode = True
```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Details finden sich in der [LICENSE](LICENSE) Datei.
