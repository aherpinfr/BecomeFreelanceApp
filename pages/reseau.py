import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.title("Réseau & Contacts professionnels")

# Connexion à Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)
worksheet = "reseau"  # À adapter selon le nom de ta feuille

def load_data():
    df = conn.read(worksheet=worksheet)
    if df is None or df.empty:
        df = pd.DataFrame(columns=[
            "Nom", "Fonction", "Entreprise", "Relation", "Compétences", "Contact", "Notes"
        ])
    return df

def save_data(df):
    conn.update(worksheet=worksheet, data=df)

def add_contact(nom, fonction, entreprise, relation, competences, contact, notes):
    df = load_data()
    new_row = pd.DataFrame([{
        "Nom": nom,
        "Fonction": fonction,
        "Entreprise": entreprise,
        "Relation": relation,
        "Compétences": competences,
        "Contact": contact,
        "Notes": notes
    }])
    df = pd.concat([df, new_row], ignore_index=True)
    save_data(df)

def delete_contact(index):
    df = load_data()
    df = df.drop(index).reset_index(drop=True)
    save_data(df)

def update_contact(df, index, col, value):
    df.at[index, col] = value
    save_data(df)

df = load_data()

with st.form("add_contact"):
    nom = st.text_input("Nom et prénom")
    fonction = st.text_input("Fonction (ex: Freelancer, Recruteur, Manager...)")
    entreprise = st.text_input("Entreprise / Organisation")
    type_relation = st.selectbox(
        "Type de contact",
        ["Freelance Data", "Recruteur", "Manager", "Partenaire", "Autre"]
    )
    competences = st.text_input("Compétences (séparées par des virgules)")
    contact_direct = st.text_input("Contact direct (email, LinkedIn, téléphone...)")
    notes = st.text_area("Notes (ex: comment tu l’as rencontré, intérêts communs, etc.)")
    submitted = st.form_submit_button("Ajouter le contact")
    if submitted and nom:
        add_contact(nom, fonction, entreprise, type_relation, competences, contact_direct, notes)
        st.success(f"Contact '{nom}' ajouté à ton réseau !")
        df = load_data()  # Recharger les données
        st.cache_data.clear()
        st.rerun()  # Rafraîchir la page

st.subheader("Liste de tes contacts réseau")
if not df.empty:
    for i, c in df.iterrows():
        st.markdown(f"""
        **{c['Nom']}**  
        *{c['Fonction']}* chez *{c['Entreprise']}*  
        **Type :** {c['Relation']}  
        **Compétences :** {c['Compétences']}  
        **Contact :** {c['Contact']}  
        **Notes :** {c['Notes']}
        """)
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Modifier les notes", key=f"edit_notes_{i}"):
                st.session_state["edit_notes_index"] = i  # On stocke l'index à modifier
        with col2:
            if st.button(f"Supprimer {c['Nom']}", key=f"del_{i}"):
                delete_contact(i)
                st.cache_data.clear()
                st.rerun()  # Rafraîchir la page

        # Formulaire pour modifier les notes
        if "edit_notes_index" in st.session_state and st.session_state["edit_notes_index"] == i:
            with st.form(f"edit_notes_form_{i}"):
                new_notes = st.text_area("Nouvelles notes", value=c["Notes"])
                if st.form_submit_button("Enregistrer"):
                    update_contact(df, i, "Notes", new_notes)
                    del st.session_state["edit_notes_index"]  # On retire l'index de la session
                    st.cache_data.clear()
                    st.rerun()  # Rafraîchir la page

        st.markdown("---")
else:
    st.info("Aucun contact enregistré pour l’instant.")
