# AI, Data Science & Statistics Workforce Dashboard

## Project Overview & Objectives
An Interactive Analytics Dashboard analyzing the supply, demand, and skill mismatch in the **AI, Data Science, and Statistics** fields. This project aims to bridge the gap between academic output (graduates and their skills) and industry needs (job vacancies, required skills, and salary benchmarks).

### Key Objectives
1. **Supply Analysis:** Track graduates, academic skills, employment rates, and tuition fees across universities.
2. **Demand Analysis:** Monitor job vacancies, market skills required, top hiring companies, and salary structures.
3. **Skill Mismatch Analytics:** Identify gaps between academic supply and industry demand to highlight critical shortages or surpluses.

---

## Technical Architecture & Tech Stack
- **Dashboard UI:** Multi-tab layout built with Dash, Streamlit, or Modern Web Technologies (Chart.js/D3.js + Tailwind CSS).
- **Backend Framework:** Python (Flask/FastAPI) or integrated data engine (Pandas/NumPy).
- **Visualizations:** Plotly (Express & Graph Objects) as the core charting library.
- **Interactivity:** Seamless cross-filtering within tabs. Clicking an element in one chart dynamically updates the others.

---

## Dashboard Structure (Functional Specs)

### Tab 1: Graduate Supply & Academic Skills
- **KPIs/Charts:** Graduates by program, required courses (Sunburst/Treemap), employment rates (Stacked Bar), and tuition fees (Box Plot).
- **Interactivity:** Filtering by academic year, institution, or program dynamically updates all visualizations.

### Tab 2: Industry Demand & Required Skills
- **KPIs/Charts:** Total job vacancies (Metric Cards/Donut), required skills (Horizontal Bar/Word Cloud), top hiring companies (Treemap), and salary ranges by level (Violin Plot/Box Plot).
- **Interactivity:** Selecting a skill or career level filters the top hiring companies and corresponding salary ranges.

### Tab 3: Skill Mismatch Analytics
- **KPIs/Charts:** Supply vs. Demand skills overlay, Skill Mismatch Quadrant (High/Low Demand vs. High/Low Supply), and Gap Heatmap/Table.

---

## Core Datasets & Data Schema
1. **Graduates Supply:** Estimated yearly graduates in Statistics/Math, Data Science, and AI/Robotics.
2. **Salary & Regional Benchmarks:** Entry to expert salary structures across regions (Thailand, Singapore, USA, Europe).
3. **Top Employers:** Leading enterprises, global tech companies, and consulting firms hiring data professionals.
4. **Skill Matrix (3-Tier Structure):**
   - **Tier 1 (Entry/Junior):** Python, R, SQL, Power BI, Tableau, Basic ML.
   - **Tier 2 (Mid/Senior):** Advanced ML, PyTorch, TensorFlow, Cloud (AWS/GCP), MLOps.
   - **Tier 3 (Expert/Lead):** GenAI, LLM Fine-Tuning, Enterprise Architecture, AI Ethics.

---

## UI/UX Guidelines
- **Color Palette:** Deep Indigo / Slate (`#1e293b`, `#4f46e5`) with Emerald Green, Cyan, and Purple accents.
- **Widgets:** KPI Cards, Bar Charts, Interactive Tables with search/filter, Tiered Skill Cards.
- **Features:** Export capabilities (JSON/CSV/PDF), responsive design, and modern styling.
