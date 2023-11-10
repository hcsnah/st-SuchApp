import streamlit as st

# Grundkonfiguration der App
st.set_page_config(page_title="Such-App")
st.header("Such-App")
st.write("Lade eine .txt Datei hoch, gib einen Suchbegriff ein und lass dir anzeigen wie oft dieser vorkommt.")

# Sidebar zum Upload einer .txt Datei
with st.sidebar:
    st.write("Upload-Bereich")
    dokument = st.file_uploader(label="Upload-File")

# Eingabebereich des Suchbegriffs
suchbegriff = st.text_input("Gib den Suchbegriff ein")

if dokument != None:
    
    # Suche im String des Dokumentinhalts
    dokumentInhalt = str(dokument.read())
    if suchbegriff != "":
        zaehler = dokumentInhalt.count(suchbegriff)
    else:
        zaehler = 0

    # Ausgabebereich für die Anzahl der Treffer
    st.write("Folgende Daten sind in dem Dokument: ", dokumentInhalt)
    st.write("Der Suchbegriff ist: ", suchbegriff)
    st.write("Der Suchbegriff wurde ", zaehler, " mal gefunden.")
else:
    st.write("Bitte laden Sie ein .txt Dokument hoch. ")