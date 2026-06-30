import streamlit as st
import json
import os

FICHIER_DONNEES = "registre_crushs.json"

# --- CHARGEMENT DES DONNÉES ---
if os.path.exists(FICHIER_DONNEES):
    with open(FICHIER_DONNEES, "r") as fichier:
        registre_crushs = json.load(fichier)
else:
    registre_crushs = {}

# --- INTERFACE WEB ---
st.title("❤️ Crush Matcher")
st.write("Trouve discrètement si ton crush t'aime en retour !")

# Cases à remplir
nom_utilisateur = st.text_input("Quel est ton nom / pseudo ?").strip().lower()
nom_crush = st.text_input("Quel est le nom de ton crush ?").strip().lower()

# Bouton de validation
if st.button("Vérifier le Match"):
    if nom_utilisateur and nom_crush:

        # Sécurité : On vérifie si l'utilisateur existe déjà
        if nom_utilisateur in registre_crushs:
            ancien_crush = registre_crushs[nom_utilisateur]
            st.error(
                f"⚠️ {nom_utilisateur.capitalize()}, tu as déjà enregistré un crush ({ancien_crush.capitalize()}) ! Impossible de changer. 🤫")

        else:
            # Enregistrement du nouveau crush
            registre_crushs[nom_utilisateur] = nom_crush
            with open(FICHIER_DONNEES, "w") as fichier:
                json.dump(registre_crushs, fichier)

            st.success("Ton choix a été enregistré secrètement ! 🤫")

            # Algorithme de Match
            if nom_crush in registre_crushs and registre_crushs[nom_crush] == nom_utilisateur:
                st.balloons()  # Animation de ballons !
                st.success(
                    f"😍 INCROYABLE ! C'est un MATCH entre {nom_utilisateur.capitalize()} et {nom_crush.capitalize()} ! ❤️")
            else:
                st.info("Pas encore de match. Attends que ton crush s'inscrive ! 👀")
    else:
        st.warning("S'il te plaît, remplis les deux cases.")

# --- BOUTON ADMIN (En bas de page) ---
st.write("---")
if st.button("🧹 Vider la base de données (Admin)"):
    registre_crushs = {}
    with open(FICHIER_DONNEES, "w") as fichier:
        json.dump(registre_crushs, fichier)
    st.success("Base de données vidée ! Tout est remis à zéro.")
    st.rerun()