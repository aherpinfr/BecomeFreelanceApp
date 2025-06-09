import streamlit as st

st.title("Négociation")

# --- Section : Rémunérations moyennes en Belgique ---
st.header("Rémunérations moyennes Data Analyst en Belgique")
st.markdown("""
- **Salaire médian (Stepstone, 2025) :** 39 000 € brut/an[2][3][4]
- **Fourchette (Stepstone) :** 32 200 € à 47 800 € brut/an[2][4]
- **Salaire débutant (Randstad) :** 40 778 € brut/an[5]
- **Salaire moyen (Jooble) :** ~46 620 € brut/an (3 885 €/mois)[7]
- **Salaire à Bruxelles (Jooble) :** 45 720 € brut/an (3 810 €/mois)[8]
- **Salaire expérimenté (Randstad) :** jusqu’à 60 000 € brut/an[5]
""")

# --- Section : Calculateur de rémunération ---
st.header("Calculateur de rémunération")
st.markdown("""
Ce calculateur te permet d’estimer rapidement la rémunération nette à partir du brut, en utilisant un taux d’imposition moyen simplifié (environ 40% de charges sociales et fiscales en Belgique).
**À titre indicatif uniquement : les montants réels dépendent de ta situation personnelle.**
""")

brut_annuel = st.number_input("Salaire brut annuel (€)", min_value=20000, value=39000, step=1000)
taux_imposition = st.slider("Taux d’imposition et charges (%)", min_value=30, max_value=50, value=40)

net_annuel = brut_annuel * (1 - taux_imposition/100)
net_mensuel = net_annuel / 12

st.subheader("Résultats")
col1, col2 = st.columns(2)
col1.metric("Brut annuel", f"{brut_annuel:,.0f} €")
col2.metric("Net annuel (estimation)", f"{net_annuel:,.0f} €")
col1.metric("Brut mensuel", f"{brut_annuel/12:,.0f} €")
col2.metric("Net mensuel (estimation)", f"{net_mensuel:,.0f} €")
