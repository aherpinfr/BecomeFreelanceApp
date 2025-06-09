import streamlit as st

st.title("Fiche Entreprise & Stratégie Personnalisée")

# Exemple de base de données simple (à remplacer par une vraie base ou un fichier CSV plus tard)
entreprises = {
    "BNP Paribas Fortis": {
        "secteur": "Banque",
        "strategie": "Accélérer la digitalisation, optimiser l’expérience client, renforcer la sécurité et l’inclusion numérique.",
        "problemes": [
            "Transformation digitale des parcours clients",
            "Automatisation des processus",
            "Conformité réglementaire et gestion des risques",
            "Gestion et valorisation de la donnée"
        ],
        "stack": ["Azure", "AWS", "API", "Big Data", "Java", "Python", "Power BI"],
        "competences": ["Data engineering", "Sécurité", "Cloud", "Automatisation", "Gestion de projet agile"],
        "contacts": ["Manager Data: Jean Dupont (LinkedIn)", "RH: Sophie Martin (LinkedIn)"],
        "pourquoi_recrute": "Transformation digitale, nouveaux services, conformité, innovation",
        "comment_parler": "Mettre en avant ton expertise data, cloud, automatisation, conformité, expérience client."
    },
    "Bijouterie Altenloh": {
        "secteur": "Bijouterie",
        "strategie": "Développer la visibilité en ligne et digitaliser la gestion des ventes.",
        "problemes": [
            "E-commerce",
            "Gestion de stock",
            "Fidélisation client"
        ],
        "stack": ["Shopify", "WooCommerce", "ERP léger", "CRM"],
        "competences": ["Data visualisation", "Automatisation des ventes", "Gestion base de données client"],
        "contacts": ["Propriétaire: Marie Altenloh", "Webmaster: info@altenloh.be"],
        "pourquoi_recrute": "Optimisation des ventes en ligne, analyse clientèle, gain de temps.",
        "comment_parler": "Proposer des solutions concrètes pour mieux connaître leurs clients et automatiser la gestion."
    }
}

# Sélection de l'entreprise
nom_entreprise = st.selectbox("Choisis une entreprise à analyser :", list(entreprises.keys()))

fiche = entreprises[nom_entreprise]

# Affichage structuré
st.subheader(f"Secteur : {fiche['secteur']}")
st.markdown(f"**Stratégie actuelle** : {fiche['strategie']}")

st.markdown("**Problématiques business :**")
for pb in fiche["problemes"]:
    st.write(f"- {pb}")

st.markdown("**Stack IT & outils :**")
st.write(", ".join(fiche["stack"]))

st.markdown("**Compétences recherchées :**")
st.write(", ".join(fiche["competences"]))

st.markdown("**Contacts clés :**")
for contact in fiche["contacts"]:
    st.write(f"- {contact}")

st.markdown(f"**Pourquoi ils recrutent ?** : {fiche['pourquoi_recrute']}")
st.markdown(f"**Comment leur parler / ton pitch personnalisé :** {fiche['comment_parler']}")

# Zone pour tes notes et actions personnalisées
st.markdown("**Tes notes/actions personnalisées :**")
notes = st.text_area("Prends des notes ou prépare ton pitch ici…")

