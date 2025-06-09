import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.title("Compétences recherchées par les entreprises")

# Connexion à Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Nom de la feuille (worksheet) à utiliser
worksheet = "competences"  # adapte si besoin

# Charger les données depuis Google Sheet
def load_data():
    df = conn.read(worksheet=worksheet)
    if df is None or df.empty:
        # Crée un DataFrame vide avec les bonnes colonnes si la feuille est vide
        df = pd.DataFrame(columns=["Compétence", "Entreprise", "Problématique", "Source"])
    return df

# Ajouter une compétence
def add_competence(competence, entreprise, probleme, source):
    df = load_data()
    new_row = pd.DataFrame([{
        "Compétence": competence,
        "Entreprise": entreprise,
        "Problématique": probleme,
        "Source": source
    }])
    df = pd.concat([df, new_row], ignore_index=True)
    conn.update(worksheet=worksheet, data=df)

# Supprimer une compétence (par index)
def delete_competence(index):
    df = load_data()
    df = df.drop(index).reset_index(drop=True)
    conn.update(worksheet=worksheet, data=df)

competences = load_data()

st.markdown("""
Ajoute ici les compétences que tu repères sur LinkedIn, Glassdoor, ou dans les offres d’emploi.  
Associe-les à une entreprise et une problématique business pour mieux cibler ta veille et tes formations.
""")

with st.form("add_competence"):
    competence = st.text_input("Compétence recherchée (ex : Data Engineering, Python, IA, Adaptabilité...)")
    entreprise = st.text_input("Entreprise (ex : BNP Paribas Fortis, Proximus, etc.)")
    probleme = st.text_area("Problématique business à laquelle répond cette compétence (ex : automatisation, conformité, innovation, etc.)")
    source = st.text_input("Source (LinkedIn, Glassdoor, offre d’emploi, etc.)")
    submitted = st.form_submit_button("Ajouter la compétence")
    if submitted and competence:
        add_competence(competence, entreprise, probleme, source)
        st.success(f"Compétence '{competence}' ajoutée !")
        st.cache_data.clear()
        st.rerun()  # Rafraîchir la page

st.subheader("Tableau des compétences recensées")

if not competences.empty:
    for i, c in competences.iterrows():
        st.markdown(f"""
        **Compétence :** {c['Compétence']}  
        **Entreprise :** {c['Entreprise']}  
        **Problématique business :** {c['Problématique']}  
        **Source :** {c['Source']}
        """)
        if st.button(f"Supprimer", key=f"del_comp_{i}"):
            delete_competence(i)
            st.success("Compétence supprimée !")
            st.cache_data.clear()
            st.rerun()
else:
    st.info("Aucune compétence enregistrée pour l’instant.")
