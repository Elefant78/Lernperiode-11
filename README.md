# Lernperiode 11

### 22.8 bis 26.9.2024

## Grob-Planung

1. Erklären Sie Ihre Projekt-Idee in einem Satz, als müssen Sie einen Investor davon überzeugen. Ein RaiseTheBrainrot, bei dem man Charaktere wie TRALALERO TRALALA grossziehen muss. 
2. Erklären Sie, welche technischen Herausforderungen Sie in Ihrem Projekt erwarten. Design Schwierigkeiten
3. Beschreiben Sie, welche nicht-technischen Aspekte Sie in diesem Projekt besonders üben möchten. das Designen
4. Wie unterscheidet sich dieses Projekt von Ihrem Projekt in 335; und wo ergänzen sich diese Projekte?

## 22.8

- [X] Arbeitspaket 1 Bewerbungswebsite überarbeiten
- [X] Arbeitspaket 2 Bei SNB anrufen und nach dem Bewerbungsstand nachfragen, weitere Stellen anschreiben 
- [ ] Arbeitspaket 3 Layout für RaiseMyBrainrot erstellen

Ich habe zwei Arbeitspakete erfolgreich abgeschlossen: Die Bewerbungswebsite wurde überarbeitet und ich habe bei der SNB nach dem Bewerbungsstand nachgefragt sowie weitere Stellen kontaktiert. Das dritte Arbeitspaket, das Layout für RaiseMyBrainrot zu erstellen, konnte ich leider nicht umsetzen. Insgesamt gute Fortschritte erzielt.

☝️ Vergessen Sie nicht, einen ersten Code und Skizze auf github hochzuladen!

## 29.8

- [ ] Arbeitspaket 1 Layout für RaiseMyBrainrot erstellen
#### Als Team-Leiter
möchte ich ein Layout für die Handyapplikation 
damit ich weitere Schritte richtung Programmierung planen kann
- [ ] Arbeitspaket 2 Mini GPT verstehen und selber auch implementieren
#### Als Lernender 
möchte ich ein tieferes verständins aus dem Mini Gpt gewinn 
damit kann ich selber auch so eine  programmieren erstellen

def lade_korpus(dateipfad):
    gesamter_text = []
    with open(dateipfad, "r", encoding="utf-8") as datei:
        inhalt = datei.read()

    for zeile in inhalt.split("\n"):
        try:
            gesamter_text.append(zeile.split("\t")[1])
        except IndexError:
            print(f"Fehler in Zeile: '{zeile}'")

    return " ".join(gesamter_text)


text = lade_korpus("deu-ch_newscrawl_2012_10K-sentences.txt")


def vorverarbeiten(text):
    text = text.lower()
    # Nur Buchstaben, Ziffern, Punkt und Leerzeichen behalten
    gefiltert = "".join(ch for ch in text if ch.isalnum() or ch in [".", " "])
    gefiltert = gefiltert.replace(".", " . ")
    woerter = [wort.strip() for wort in gefiltert.split() if wort]
    return woerter


woerter = vorverarbeiten(text)


def berechne_trigramme(woerter):
    trigramme = {}
    for i in range(len(woerter) - 2):
        triple = (woerter[i], woerter[i+1], woerter[i+2])
        trigramme[triple] = trigramme.get(triple, 0) + 1
    return trigramme


trigramme = berechne_trigramme(woerter)


def vorhersage(eingabe_woerter, trigramme):
    kandidaten = {
        tri: haeufigkeit
        for tri, haeufigkeit in trigramme.items()
        if tri[0] == eingabe_woerter[0] and tri[1] == eingabe_woerter[1]
    }

    if not kandidaten:
        return None

    bestes = max(kandidaten, key=kandidaten.get)
    return bestes[2]


user_input = input("Gib zwei Wörter ein: ")
user_input = vorverarbeiten(user_input)

if len(user_input) >= 2:
    wort = vorhersage(user_input, trigramme)
    print(wort if wort else "Keine Vorhersage möglich.")
else:
    print("Bitte mindestens zwei Wörter eingeben.")

- [ ] Arbeitspaket 3 Game Konzept erstellen
#### Als Investor 
möchte ich einen Game Konzept haben
damit ich weiss ob die Idee eine Zukunft hat und es sich Lohnt in es zu investieren
- [ ] Arbeitspaket 4 Präsentation für SNB erstellen(Arbeitspaket in Riederregel)
#### Als Mitarbeiter der SNB
möchte ich einen bessern Einblick im Leben von Tim Tafolli bekommen
damit kann ich mir ein Bild von ihm erschaffen



Heute habe ich einen guten Arbeitstag gehabt, vor allem hatte ich viel abwechslung, somit hatte ich keine Langweille und konnte effektiv arbeiten. Meine Leiblingsaufgabe ware es den Code zu verstehen und selber zu überarbeiten. Leider konnte ich einer der vier User-Storys nicht machen. Das ist das Ziek für nächste Woche. Ich denke diese User Story kann ich gut in der Rieder-Riegel Block berabeiten.

## 29.8

#### Als Team-Leiter
möchte ich ein Layout für die Handyapplikation 
damit ich weitere Schritte richtung Programmierung planen kann
- [ ] Arbeitspaket 2 Mini GPT verstehen und selber auch implementieren
☝️ Vergessen Sie nicht, Ihren Code auf github hochzuladen
