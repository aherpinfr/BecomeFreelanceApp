import streamlit as st

st.title("Groupes & Communautés")

if "groupes" not in st.session_state:
    st.session_state["groupes"] = []

with st.form("add_groupe"):
    nom = st.text_input("Nom du groupe ou communauté")
    description = st.text_area("Description")
    lien = st.text_input("Lien (site, LinkedIn, Meetup...)")
    submitted = st.form_submit_button("Ajouter le groupe")
    if submitted and nom:
        st.session_state["groupes"].append({
            "Nom": nom,
            "Description": description,
            "Lien": lien
        })
        st.success(f"Groupe '{nom}' ajouté !")

st.subheader("Liste des groupes enregistrés")
if st.session_state["groupes"]:
    for i, groupe in enumerate(st.session_state["groupes"]):
        st.markdown(f"**{groupe['Nom']}**  \n{groupe['Description']}  \n[Lien]({groupe['Lien']})" if groupe['Lien'] else f"**{groupe['Nom']}**  \n{groupe['Description']}")
        if st.button(f"Supprimer {groupe['Nom']}", key=f"del_{i}"):
            st.session_state["groupes"].pop(i)
            st.experimental_rerun()
else:
    st.info("Aucun groupe enregistré pour l’instant.")
