import streamlit as st

st.title("Compétences recherchées par les entreprises")

if "competences" not in st.session_state:
    st.session_state["competences"] = []

st.markdown("""
Ajoute ici les compétences que tu repères sur LinkedIn, Glassdoor, ou dans les offres d’emploi.  
Associe-les à une entreprise et une problématique business pour mieux cibler ta veille et tes formations.
""")

with st.form("add_competence"):
    competence = st.text_input("Compétence recherchée (ex : Data Engineering, Python, IA, Adaptabilité...)")
    entreprise = st.text_input("Entreprise (ex : BNP Paribas Fortis, Proximus, etc.)")
    probleme = st.text_area("Problématique business à laquelle répond cette compétence (ex : automatisation, conformité, innovation, etc.)")
    source = st.text_input("Source (LinkedIn, Glassdoor, offre d'emploi, etc.)")
    submitted = st.form_submit_button("Ajouter la compétence")
    if submitted and competence:
        st.session_state["competences"].append({
            "Compétence": competence,
            "Entreprise": entreprise,
            "Problématique": probleme,
            "Source": source
        })
        st.success(f"Compétence '{competence}' ajoutée !")

st.subheader("Tableau des compétences recensées")

if st.session_state["competences"]:
    for i, c in enumerate(st.session_state["competences"]):
        st.markdown(f"""
        **Compétence :** {c['Compétence']}  
        **Entreprise :** {c['Entreprise']}  
        **Problématique business :** {c['Problématique']}  
        **Source :** {c['Source']}
        """)
        if st.button(f"Supprimer", key=f"del_comp_{i}"):
            st.session_state["competences"].pop(i)
