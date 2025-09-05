def lade_korpus(dateipfad):
    """Lädt den Textkorpus aus einer Datei."""
    saetze = []
    with open(dateipfad, "r", encoding="utf-8") as datei:
        for zeile in datei:
            teile = zeile.strip().split("\t")
            if len(teile) > 1:
                saetze.append(teile[1])
    return " ".join(saetze)


def vorverarbeiten(text):
    """Bereitet den Text auf: Kleinbuchstaben, Sonderzeichen filtern, Wörterliste zurückgeben."""
    text = text.lower()
    text = "".join(ch for ch in text if ch.isalnum() or ch in [".", " "])
    text = text.replace(".", " . ")
    return [wort for wort in text.split() if wort]


def baue_trigramme(woerter):
    """Erstellt ein Wörterbuch mit Trigrammen und deren Häufigkeit."""
    trigramme = {}
    for i in range(len(woerter) - 2):
        triple = (woerter[i], woerter[i+1], woerter[i+2])
        trigramme[triple] = trigramme.get(triple, 0) + 1
    return trigramme


def vorhersage(zwei_woerter, trigramme):
    """Gibt das wahrscheinlichste nächste Wort zurück, basierend auf zwei eingegebenen Wörtern."""
    kandidaten = {
        tri: freq for tri, freq in trigramme.items()
        if tri[0] == zwei_woerter[0] and tri[1] == zwei_woerter[1]
    }
    if not kandidaten:
        return None
    bestes = max(kandidaten, key=kandidaten.get)
    return bestes[2]


# --- Hauptprogramm ---
if __name__ == "__main__":
    text = lade_korpus("deu-ch_newscrawl_2012_10K-sentences.txt")
    woerter = vorverarbeiten(text)
    trigramme = baue_trigramme(woerter)

    benutzereingabe = input("Bitte zwei Wörter eingeben: ")
    eingabe_woerter = vorverarbeiten(benutzereingabe)

    if len(eingabe_woerter) >= 2:
        vorhersage_wort = vorhersage(eingabe_woerter, trigramme)
        if vorhersage_wort:
            print(f"Vorhersage für das nächste Wort: {vorhersage_wort}")
        else:
            print("Keine Vorhersage möglich für diese Kombination.")
    else:
        print("Bitte mindestens zwei Wörter eingeben.")
