# ai-userstory-generator

# 🤖 AI-Assisted User Story Generator

Welcome to the **AI-Assisted User Story Generator**! This project is built as part of the Agile Project Management module, delivering a digital solution under the theme **"AI DevOps Assistant for Software Teams"**. 

This application helps software product teams quickly transform rough feature ideas into professional, standard Agile User Stories and detailed Acceptance Criteria using advanced AI.

---

## 🚀 Live Demo & Deliverables
* **Live Web Application:** 👉 https://ai-userstory-generator-fb24zshsngeyjedswgkpix.streamlit.app/
* **GitHub Project Board (Scrum):** 👉 https://github.com/YashikaVelma/ai-userstory-generator/issues

---

## 📋 Agile & Scrum Framework
This project was developed strictly following Scrum methodologies and iterative software development lifecycle (SDLC) practices:
* **Product Backlog:** User Stories were planned, prioritized, and broken down into task cards.
* **Kanban Board:** Progress was continuously tracked through `Todo`, `In Progress`, and `Done` cycles.
* **MVP Approach:** Built a Minimum Viable Product first, then iteratively integrated AI features and deployment configurations.

---

## 🛠 Technical Architecture
* **Frontend Interface:** Built with **Streamlit** (Python Framework) for a clean, interactive user experience.
* **AI Core Engine:** Powered by **Groq API** utilizing the `llama-3.3-70b-versatile` model for lightning-fast text processing and domain-expert outputs.
* **Security & Configuration:** High-security implementation using `Streamlit Secrets` to hide API tokens, ensuring credentials are never exposed in source code.

---

## 🚀 DevOps & CI/CD Pipeline
To demonstrate modern DevOps engineering principles, this repository includes an automated pipeline:
* **Continuous Integration (CI):** Powered by **GitHub Actions** (`.github/workflows/main.yml`).
* **Automated Linting:** Every `push` or `pull_request` triggers an isolated virtual machine to install dependencies and run syntax compiling checks on `app.py`.
* **Continuous Deployment (CD):** Connected seamlessly with Streamlit Community Cloud for automatic updates on code changes.

---

## 📦 How to Run Locally

If you want to test this project on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YashikaVelma/ai-userstory-generator.git
   cd ai-userstory-generator

   
2. ##Install requirements:
   pip install -r requirements.txt

3. ##run the application 
   streamlit run app.py


