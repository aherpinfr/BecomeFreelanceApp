import streamlit as st
from datetime import date
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.title("Suivi des Événements Freelance & Data")

# Connexion à Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)
worksheet = "evenements"  # À adapter selon le nom de ta feuille

def load_data():
    df = conn.read(worksheet=worksheet)
    if df is None or df.empty:
        df = pd.DataFrame(columns=["Nom", "Groupe", "Date", "Lieu", "Description", "Planifié", "Participe"])
    # Convertir les dates si elles sont stockées en string
    if "Date" in df.columns and df["Date"].dtype == "object":
        df["Date"] = pd.to_datetime(df["Date"]).dt.date
    return df

def save_data(df):
    conn.update(worksheet=worksheet, data=df)

def add_event(nom, groupe, date_event, lieu, description, planifie, participe):
    df = load_data()
    new_row = pd.DataFrame([{
        "Nom": nom,
        "Groupe": groupe,
        "Date": date_event,
        "Lieu": lieu,
        "Description": description,
        "Planifié": planifie,
        "Participe": participe
    }])
    df = pd.concat([df, new_row], ignore_index=True)
    save_data(df)

def update_event(df, index, col, value):
    df.at[index, col] = value
    save_data(df)

def delete_event(index):
    df = load_data()
    df = df.drop(index).reset_index(drop=True)
    save_data(df)

df = load_data()

with st.form("add_event"):
    nom = st.text_input("Nom de l'évènement")
    groupe = st.text_input("Groupe/Communauté associé (optionnel)")
    date_event = st.date_input("Date", value=date.today())
    lieu = st.text_input("Lieu")
    description = st.text_area("Description")
    planifie = st.checkbox("Planifié ?", value=True)
    participe = st.checkbox("J’y ai participé ?", value=False)
    submitted = st.form_submit_button("Ajouter l'évènement")
    if submitted and nom:
        add_event(nom, groupe, date_event, lieu, description, planifie, participe)
        st.success(f"Évènement '{nom}' ajouté !")
        df = load_data()  # Recharger les données
        st.cache_data.clear()
        st.rerun()  # Rafraîchir la page

st.subheader("Liste des évènements enregistrés")
if not df.empty:
    for i, event in df.iterrows():
        st.markdown(f"**{event['Nom']}** ({event['Date']}) - {event['Lieu']}")
        st.markdown(f"Groupe : {event['Groupe']}" if event['Groupe'] else "")
        st.markdown(event["Description"])
        st.markdown(f"Planifié : {'✅' if event['Planifié'] else '❌'} | Participé : {'✅' if event['Participe'] else '❌'}")

        # Boutons pour modifier le statut
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("Planifié", key=f"plan_{i}"):
                update_event(df, i, "Planifié", True)
                st.cache_data.clear()
                st.rerun()  # Rafraîchir la page
        with col2:
            if st.button("Participé", key=f"part_{i}"):
                update_event(df, i, "Participe", True)
                st.cache_data.clear()
                st.rerun()  # Rafraîchir la page
        with col3:
            if st.button("Modifier la description", key=f"edit_desc_{i}"):
                st.session_state["edit_desc_index"] = i  # On stocke l'index à modifier

        with col4:
            if st.button("Supprimer", key=f"del_event_{i}"):
                delete_event(i)
                st.cache_data.clear()
                st.rerun()  # Rafraîchir la page

        # Formulaire pour modifier la description
        if "edit_desc_index" in st.session_state and st.session_state["edit_desc_index"] == i:
            with st.form(f"edit_desc_form_{i}"):
                new_desc = st.text_area("Nouvelle description", value=event["Description"])
                if st.form_submit_button("Enregistrer"):
                    update_event(df, i, "Description", new_desc)
                    del st.session_state["edit_desc_index"]  # On retire l'index de la session
                    st.cache_data.clear()
                    st.rerun()  # Rafraîchir la page
        st.markdown("---")
else:
    st.info("Aucun évènement enregistré pour l’instant.")
