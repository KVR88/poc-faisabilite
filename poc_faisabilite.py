
import streamlit as st
from geopy.geocoders import Nominatim
import pandas as pd

# Configuration
st.set_page_config(page_title="POC Faisabilité Immobilière", layout="centered")
st.title("🏗️ POC – Analyse de Faisabilité Immobilière")

st.markdown("Saisis une adresse pour analyser la faisabilité potentielle du terrain.")

# Input utilisateur
adresse = st.text_input("🏠 Adresse du terrain", "23 rue des Lilas, Paris")

if adresse:
    # Géocodage avec Nominatim
    geolocator = Nominatim(user_agent="faisabilite_app")
    location = geolocator.geocode(adresse)

    if location:
        lat, lon = location.latitude, location.longitude
        st.success(f"📍 Coordonnées GPS : {lat:.5f}, {lon:.5f}")

        # Simulation de zone PLU (à remplacer plus tard par requête API Géoportail)
        zone_plu = "UA" if "Paris" in adresse else "UB"
        coef_occupation_sol = 0.6 if zone_plu == "UA" else 0.4
        surface_terrain = 650  # simulée

        surface_plancher = surface_terrain * coef_occupation_sol
        logements_possibles = int(surface_plancher / 120)

        st.markdown("### 📊 Résumé de la faisabilité")
        st.write(pd.DataFrame({
            "Critère": [
                "Zone PLU", "Surface terrain (m²)", "COS", 
                "Surface de plancher max (m²)", "Nb logements estimés"
            ],
            "Valeur": [
                zone_plu, surface_terrain, coef_occupation_sol, 
                round(surface_plancher), logements_possibles
            ]
        }))

        st.markdown("### 📎 Conclusion")
        st.success(f"Projet potentiellement viable : {logements_possibles} logements construisibles sur {surface_plancher:.0f} m².")
    else:
        st.error("Adresse introuvable. Merci de vérifier l'orthographe.")
