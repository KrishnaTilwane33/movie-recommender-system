# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built with **Python**, **Streamlit**, and **Machine Learning**. The application recommends movies similar to the one selected by the user and displays their posters using the TMDB API.

---

## 🚀 Demo

**Live App:** *https://mvrs-oakdev.streamlit.app/*

**GitHub Repository:** *https://github.com/KrishnaTilwane33/movie-recommender-system*

---

## 📌 Features

* 🎥 Content-based movie recommendations
* 🖼️ Displays movie posters using the TMDB API
* 🔍 Search and select movies from a dropdown
* ⚡ Fast recommendation generation
* 🌐 Interactive web interface built with Streamlit

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Pickle**
* **Requests API**

---

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
```

### 2. Navigate to the project

```bash
cd Movie-Recommendation-System
```

### 3. Create a virtual environment (Optional)

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## 🔑 TMDB API

This project uses **The Movie Database (TMDB)** API to fetch movie posters.

Create a free API key and store it securely using Streamlit Secrets when deploying.

Example:

```toml
TMDB_API_KEY="YOUR_API_KEY"
```

---

## 📊 Machine Learning Approach

This project uses a **Content-Based Recommendation System**.

Workflow:

1. Movie metadata preprocessing
2. Feature extraction using vectorization
3. Cosine similarity computation
4. Recommend the Top 5 most similar movies

---

## 📷 Screenshots

Add screenshots of:
<img width="1085" height="782" alt="image" src="https://github.com/user-attachments/assets/bd8f92d8-8b35-4e15-b3fb-fdae4306e8fb" />

* Home page
* Movie selection
* Recommendation results

---

## 📦 Deployment

This application can be deployed on **Streamlit Community Cloud**.

Steps:

1. Push the project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Create a new app.
4. Select your repository.
5. Deploy.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**OakDev**

Artificial Intelligence & Data Science Engineer

GitHub: https://github.com/krishnatilwane33

LinkedIn: https://linkedin.com/in/krishnatilwane620128
