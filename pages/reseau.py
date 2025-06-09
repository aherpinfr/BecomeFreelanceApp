import streamlit as st

st.title("Réseau & Contacts professionnels")

# Initialisation de la session pour stocker les contacts temporairement
if "contacts" not in st.session_state:
    st.session_state["contacts"] = []

# Formulaire pour ajouter un contact
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
        st.session_state["contacts"].append({
            "Nom": nom,
            "Fonction": fonction,
            "Entreprise": entreprise,
            "Relation": type_relation,
            "Compétences": competences,
            "Contact": contact_direct,
            "Notes": notes
        })
        st.success(f"Contact '{nom}' ajouté à ton réseau !")

# Affichage de la liste des contacts
st.subheader("Liste de tes contacts réseau")
if st.session_state["contacts"]:
    for i, c in enumerate(st.session_state["contacts"]):
        st.markdown(f"""
        **{c['Nom']}**  
        *{c['Fonction']}* chez *{c['Entreprise']}*  
        **Type :** {c['Relation']}  
        **Compétences :** {c['Compétences']}  
        **Contact :** {c['Contact']}  
        **Notes :** {c['Notes']}
        """)
        if st.button(f"Supprimer {c['Nom']}", key=f"del_{i}"):
            st.session_state["contacts"].pop(i)
            st.experimental_rerun()
        st.markdown("---")
else:
    st.info("Aucun contact enregistré pour l’instant.")
