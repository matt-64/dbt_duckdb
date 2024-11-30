# 📊 Projet d'initiation : dbt + DuckDB + Streamlit

<p align="center">
  <img src="https://www.getdbt.com/ui/img/dbt-logo.svg" alt="dbt Logo" width="200">
  <img src="https://duckdb.org/assets/logo.png" alt="DuckDB Logo" width="200">
  <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit Logo" width="200">
</p>

## 🚀 Objectif du projet
Ce projet a pour but de découvrir et maîtriser les bases des outils **dbt**, **DuckDB**, et **Streamlit**. À la fin de ce guide, vous aurez construit un pipeline analytique complet en local, avec une interface de visualisation interactive.

---

## 🛠️ Technologies utilisées
- **dbt** : Modélisation et gestion des transformations de données en SQL.
- **DuckDB** : Moteur SQL léger et performant pour traiter vos données localement.
- **Streamlit** : Framework Python pour créer des applications web de visualisation interactive.

---

## 📋 Étapes du projet

### 1️⃣ Pré-requis
Avant de commencer, assurez-vous d’avoir :
- Python 3.8+ installé sur votre machine.
- Un éditeur de texte/code comme VS Code ou PyCharm.
- Un dataset en format CSV à utiliser pour vos transformations (exemple : [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)).

---

### 2️⃣ Mise en place de l’environnement

1. **Créez un environnement virtuel Python :**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Pour Mac/Linux
   venv\Scripts\activate      # Pour Windows

