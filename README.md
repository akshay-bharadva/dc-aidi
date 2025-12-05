# AI & Web Development Project Portfolio

This repository is a curated collection of projects that demonstrate my skills and experience in Artificial Intelligence, Machine Learning, Data Science, and Full-Stack Web Development. Each project is self-contained within its own directory and includes specific documentation to guide you through its setup and features.

## 📂 Projects Overview

### 1. Banking Chatbot (`aidi-1003-capstone-1`)

A full-stack AI chatbot application developed for a fictional bank, "HooBank". This capstone project features a Python backend that processes user queries using NLP techniques and a modern React frontend.

*   **Description:** The backend, built with Flask, uses NLTK for text processing and `fuzzywuzzy` for string matching to provide answers from a predefined knowledge base. All user-chatbot interactions are logged to an SQLite database for monitoring and future analysis. The frontend is a responsive and visually appealing landing page built with React and Tailwind CSS.
*   **Key Technologies:** Python, Flask, SQLite, NLTK, React, Tailwind CSS, JavaScript.

---

### 2. QueryGenius: RAG Chrome Extension (`ask-me-anything`)

An intelligent Chrome extension that functions as a personal research assistant. It leverages a Retrieval-Augmented Generation (RAG) architecture to answer questions about the content of the user's active webpage.

*   **Description:** The extension's frontend is built with React and TypeScript. It communicates with a Python backend server powered by Flask and LangChain, which uses the OpenAI API to analyze the webpage content and generate contextually relevant answers.
*   **Key Technologies:** Python, Flask, LangChain, OpenAI, React, TypeScript, Chrome Extension APIs.

---

### 3. Fish Species Predictor (`fish-market-ml-predict`)

A classic machine learning deployment project where a trained model is served via a web application. The application predicts fish species based on physical measurements provided by the user.

*   **Description:** A Random Forest Classifier model was trained on the Fish Market dataset using Scikit-learn. The trained model is deployed using a lightweight Flask web server, allowing users to input fish characteristics through a simple HTML form and receive an instant species prediction.
*   **Key Technologies:** Python, Flask, Scikit-learn, Pandas, Joblib, HTML.

---

### 4. Knowledge & Expert Systems Assignments (`knx-assignment-*`)

A series of assignments for a Knowledge and Expert Systems course, showcasing a progression in building AI-powered applications with Streamlit and LangChain.

*   **Description:** These projects demonstrate rapid application development for AI. They include a ChatGPT-like clone that interacts with the OpenAI API and a document-querying application that implements a RAG pipeline (LangChain, ChromaDB, OpenAI) to answer questions based on an uploaded text file.
*   **Key Technologies:** Python, Streamlit, LangChain, OpenAI, ChromaDB.

---

### 5. Data Science Labs (`aidi-2004-*`)

A collection of data science labs focusing on core skills such as Exploratory Data Analysis (EDA), model building, and version control.

*   **Description:** These labs include an EDA on an NBA player dataset and a project to build and compare different classification models for the Wisconsin Diagnostic Breast Cancer (WDBC) dataset. This work also highlights proficiency in using Git for branching and merging different model development efforts.
*   **Key Technologies:** Python, Pandas, Scikit-learn, Jupyter Notebook, Git.

---

### 6. House Price Prediction (`predict-house-price`)

A machine learning project aimed at predicting housing prices based on a comprehensive set of features.

*   **Description:** This project involves the end-to-end process of building a predictive model. It includes data cleaning, feature engineering, and training a regression model to predict the final sale price of a house using variables like square footage, location, and condition.
*   **Key Technologies:** Machine Learning, Regression Modeling, Data Analysis, Pandas.

---

### 7. NBA Statistics Scraper (`scrape-nba-stats`)

A Python script developed to automate the process of scraping NBA player statistics from web sources.

*   **Description:** This utility script is designed to efficiently gather and structure data from sports websites, preparing it for further analysis, visualization, or use in other machine learning applications.
*   **Key Technologies:** Python, Web Scraping (e.g., BeautifulSoup, Scrapy).