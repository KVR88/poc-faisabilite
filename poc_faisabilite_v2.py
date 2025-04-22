
import streamlit as st
import pandas as pd
from shapely.geometry import Polygon
import random

st.set_page_config(page_title="POC Faisabilité Immobilière v2", layout="centered")

st.title("🏗️ POC - Faisabilité Immobilière (v2)")

# Entrée utilisateur
adresse = st.text_input("🏡 Adresse ou nom du terrain (fictif ou réel)")

col1, col2 = st.columns(2)
with col1:
    surface_terrain = st.number_input("📏 Surface du terrain (m²)", min_value=50, max_value=10000, value=500)
with col2:
    forme = st.selectbox("📐 Forme de la parcelle", ["Rectangulaire", "En L", "Irrégulière"])

# Simuler des règles d’urbanisme selon forme (inspiré de typologies)
typologies = {
    "Rectangulaire": {"COS": 0.5, "Hauteur max": 9, "Recul": 4},
    "En L": {"COS": 0.4, "Hauteur max": 7, "Recul": 5},
    "Irrégulière": {"COS": 0.35, "Hauteur max": 6, "Recul": 6}
}

if adresse:
    st.markdown("### 📊 Résultats de la simulation")
    regles = typologies[forme]
    surf_constructible = surface_terrain * regles["COS"]

    st.write(f"**Adresse analysée** : {adresse}")
    st.write(f"**Forme typologique** : {forme}")
    st.write(f"**Surface terrain** : {surface_terrain:.0f} m²")
    st.write(f"**Coefficient d’occupation du sol (COS)** : {regles['COS']}")
    st.write(f"**Surface constructible estimée** : {surf_constructible:.0f} m²")
    st.write(f"**Hauteur max autorisée** : {regles['Hauteur max']} m")
    st.write(f"**Recul à respecter** : {regles['Recul']} m")

    # Estimation d'un potentiel de logements
    logements_estimés = int(surf_constructible / 75)
    st.success(f"🏘️ Nombre de logements estimés : {logements_estimés} logements (moyenne 75m²/logt)")
