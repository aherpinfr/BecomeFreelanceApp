import streamlit as st
from datetime import date

st.title("Suivi des Événements Freelance & Data")

if "evenements" not in st.session_state:
    st.session_state["evenements"] = []

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
        st.session_state["evenements"].append({
            "Nom": nom,
            "Groupe": groupe,
            "Date": date_event,
            "Lieu": lieu,
            "Description": description,
            "Planifié": planifie,
            "Participe": participe
        })
        st.success(f"Évènement '{nom}' ajouté !")

st.subheader("Liste des évènements enregistrés")
if st.session_state["evenements"]:
    for i, event in enumerate(st.session_state["evenements"]):
        st.markdown(f"**{event['Nom']}** ({event['Date']}) - {event['Lieu']}")
        st.markdown(f"Groupe : {event['Groupe']}" if event['Groupe'] else "")
        st.markdown(event["Description"])
        st.markdown(f"Planifié : {'✅' if event['Planifié'] else '❌'} | Participé : {'✅' if event['Participe'] else '❌'}")
        # Boutons pour modifier le statut
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Marquer comme planifié", key=f"plan_{i}"):
                event["Planifié"] = True
                st.experimental_rerun()
        with col2:
            if st.button("Marquer comme participé", key=f"part_{i}"):
                event["Participe"] = True
                st.experimental_rerun()
        with col3:
            if st.button("Supprimer", key=f"del_event_{i}"):
                st.session_state["evenements"].pop(i)
                st.experimental_rerun()
        st.markdown("---")
else:
    st.info("Aucun évènement enregistré pour l’instant.")
