<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📊 Projet d'initiation : dbt + DuckDB + Streamlit</title>
</head>
<body>
    <h1>📊 Projet d'initiation : dbt + DuckDB + Streamlit</h1>
    <p align="center">
        <img src="https://www.getdbt.com/ui/img/dbt-logo.svg" alt="dbt Logo" width="200">
        <img src="https://duckdb.org/assets/logo.png" alt="DuckDB Logo" width="200">
        <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit Logo" width="200">
    </p>
    
    <hr>

    <h2>🚀 Objectif du projet</h2>
    <p>
        Ce projet vise à fournir une <strong>introduction pratique</strong> à trois outils puissants : 
        <strong>dbt</strong>, <strong>DuckDB</strong>, et <strong>Streamlit</strong>. 
        Vous apprendrez à construire un pipeline analytique local pour manipuler, transformer et visualiser des données, tout en découvrant les rôles spécifiques de ces technologies.
    </p>

    <hr>

    <h2>🛠️ Technologies utilisées et leur rôle</h2>
    <h3>1️⃣ dbt (Data Build Tool)</h3>
    <ul>
        <li><strong>Rôle</strong> : Gérer la transformation des données de manière modulaire et reproductible.</li>
        <li><strong>Pourquoi utiliser dbt ?</strong>
            <ul>
                <li>Centralise vos transformations SQL dans un environnement structuré.</li>
                <li>Génère automatiquement de la documentation des modèles.</li>
                <li>Gère des dépendances claires entre vos modèles (via un DAG - Directed Acyclic Graph).</li>
            </ul>
        </li>
        <li><strong>Cas d'usage dans le projet</strong> :
            <ul>
                <li>Importation du dataset Iris.</li>
                <li>Transformation des données : agrégations (moyenne des longueurs et largeurs de pétales/sépales).</li>
                <li>Création de vues SQL exploitables dans DuckDB.</li>
            </ul>
        </li>
    </ul>

    <h3>2️⃣ DuckDB</h3>
    <ul>
        <li><strong>Rôle</strong> : Fournir un moteur SQL local ultra-rapide.</li>
        <li><strong>Pourquoi utiliser DuckDB ?</strong>
            <ul>
                <li>Idéal pour les analyses rapides sans dépendre d'une base de données distante.</li>
                <li>Compatible avec dbt pour stocker les résultats des transformations.</li>
                <li>Léger et facile à intégrer à des projets Python.</li>
            </ul>
        </li>
        <li><strong>Cas d'usage dans le projet</strong> :
            <ul>
                <li>Stockage du dataset Iris dans un fichier <code>.duckdb</code>.</li>
                <li>Hébergement des vues générées par dbt.</li>
                <li>Fourniture des données agrégées à Streamlit.</li>
            </ul>
        </li>
    </ul>

    <h3>3️⃣ Streamlit</h3>
    <ul>
        <li><strong>Rôle</strong> : Offrir une interface utilisateur interactive pour visualiser les données.</li>
        <li><strong>Pourquoi utiliser Streamlit ?</strong>
            <ul>
                <li>Permet de créer des dashboards rapidement avec Python.</li>
                <li>Se connecte directement aux résultats DuckDB générés par dbt.</li>
                <li>Rend les pipelines data accessibles même aux non-techniciens.</li>
            </ul>
        </li>
        <li><strong>Cas d'usage dans le projet</strong> :
            <ul>
                <li>Lecture des données agrégées depuis DuckDB.</li>
                <li>Affichage sous forme de tableau et de graphiques interactifs.</li>
                <li>Mise en avant du pipeline dbt / DuckDB / Streamlit.</li>
            </ul>
        </li>
    </ul>

    <hr>

    <h2>📋 Étapes du projet</h2>
    <h3>1️⃣ Mise en place de l’environnement</h3>
    <ol>
        <li><strong>Créez un environnement virtuel :</strong>
            <pre>
python3 -m venv venv
source venv/bin/activate   # Pour Mac/Linux
venv\Scripts\activate      # Pour Windows
            </pre>
        </li>
        <li><strong>Installez les dépendances nécessaires :</strong>
            <pre>
pip install dbt-duckdb duckdb streamlit pandas
            </pre>
        </li>
        <li><strong>Configurez dbt :</strong>
            <p>Ajoutez un fichier <code>profiles.yml</code> :</p>
            <pre>
first_dbt_test:
  outputs:
    dev:
      type: duckdb
      path: data/dev.duckdb
      threads: 1
  target: dev
            </pre>
        </li>
    </ol>

    <h3>2️⃣ Pipeline dbt : Transformations des données</h3>
    <ol>
        <li><strong>Ajoutez votre source :</strong>
            <p>Placez le fichier CSV dans le dossier <code>data/</code>.</p>
            <p>Déclarez votre source dans dbt (<code>schema.yml</code>) :</p>
            <pre>
sources:
  - name: iris_source
    tables:
      - name: iris
            </pre>
        </li>
        <li><strong>Créez des modèles dbt :</strong>
            <p>Exemple de transformation (<code>aggregated_iris.sql</code>) :</p>
            <pre>
SELECT
    Species,
    AVG(SepalLengthCm) AS avg_sepal_length,
    AVG(SepalWidthCm) AS avg_sepal_width
FROM {{ source('iris_source', 'iris') }}
GROUP BY Species
            </pre>
        </li>
        <li><strong>Générez les vues DuckDB :</strong>
            <pre>
dbt run
            </pre>
        </li>
    </ol>

    <h3>3️⃣ Streamlit : Visualisation interactive</h3>
    <ol>
        <li><strong>Créez une application Streamlit (<code>app.py</code>) :</strong>
            <pre>
import streamlit as st
import duckdb

st.set_page_config(page_title="Pipeline dbt + DuckDB + Streamlit", layout="wide")
st.title("🚀 Pipeline dbt + DuckDB + Streamlit")

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
st.dataframe(result)
st.bar_chart(result.set_index("Species"))
            </pre>
        </li>
        <li><strong>Exécutez l’application :</strong>
            <pre>
streamlit run app.py
            </pre>
        </li>
    </ol>

    <hr>

    <h2>🎯 Points clés à retenir</h2>
    <p>
        Avec ce projet, vous avez appris à intégrer et exploiter trois technologies complémentaires, chacune jouant un rôle clé dans un pipeline analytique moderne :
    </p>
    <ul>
        <li><strong>dbt</strong> : Transformations SQL modulaire.</li>
        <li><strong>DuckDB</strong> : Base SQL locale rapide.</li>
        <li><strong>Streamlit</strong> : Visualisation interactive.</li>
    </ul>
</body>
</html>
