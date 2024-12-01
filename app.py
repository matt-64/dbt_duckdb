import streamlit as st
import duckdb
import pandas as pd

# Logo et titre principal
st.set_page_config(page_title="Pipeline dbt / DuckDB / Streamlit", layout="wide")
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/2/28/DBT_logo.png",
    width=150,
)
st.title("🚀 Pipeline dbt / DuckDB / Streamlit")
st.markdown(
    """
    ### Cette application montre le bon fonctionnement du pipeline :
    - **dbt** : Gestion et transformation des données.
    - **DuckDB** : Stockage et interrogation rapide des données.
    - **Streamlit** : Interface utilisateur interactive.
    """
)

# Connexion à DuckDB
st.header("📊 Résultat de l'agrégation des données")
st.markdown("Les données sont chargées depuis **DuckDB** après transformation via **dbt**.")
try:
    con = duckdb.connect("data/dev.duckdb")
    query = """
    SELECT
        Species,
        AVG(SepalLengthCm) AS avg_sepal_length,
        AVG(SepalWidthCm) AS avg_sepal_width
    FROM main.iris_source
    GROUP BY Species
    """
    result = con.execute(query).fetchdf()

    # Affichage des données avec style
    st.dataframe(result.style.format(precision=2).highlight_max(axis=0, color="lightgreen"))

    # Graphique pour visualiser les données
    st.subheader("📈 Visualisation des données")
    st.bar_chart(result.set_index("Species"))
except Exception as e:
    st.error(f"Une erreur est survenue : {e}")

# Footer avec lien vers dbt, DuckDB, et Streamlit
st.markdown("---")
st.markdown(
    """
    🛠️ Développé avec [dbt](https://www.getdbt.com/), [DuckDB](https://duckdb.org/), et [Streamlit](https://streamlit.io/).
    """
)
