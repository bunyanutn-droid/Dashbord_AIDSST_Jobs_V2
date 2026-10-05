# 🚀 Handoff Specification: AI, Data Science & Statistics Workforce Dashboard

**Target Tool/System:** Antigravity  
**Author:** AI Assistant  
**Date:** October 5, 2026  
**Status:** Ready for Development / Dashboard Generation  

---

## 📌 1. Project Context & Objectives
เอกสารฉบับนี้จัดทำขึ้นเพื่อส่งต่อสเปกและข้อมูลให้ **Antigravity** นำไปสร้าง Interactive Dashboard สำหรับแสดงภาพรวมของสายงาน **AI, Data Science และ Statistics** โดยเน้นข้อมูล 4 มิติหลัก:
1. ปริมาณผู้จบการศึกษา (Graduate Supply)
2. โครงสร้างเงินเดือนเริ่มต้น และความต้องการในตลาดแรงงาน (Salary & Market Demand)
3. รายชื่อบริษัทชั้นนำที่เปิดรับสมัคร (Hiring Companies)
4. โครงสร้างทักษะแบ่งตามระดับประสบการณ์ (Career Level & Skill Matrix)

---

## 📊 2. Data Schema & Core Datasets

### Dataset A: Graduates Supply (สถิตินักศึกษาจบใหม่ต่อปีในไทย - ประมาณการ)
| Field | Category | Graduates_Per_Year | Notes |
| :--- | :--- | :--- | :--- |
| `cat_stats` | สถิติ / คณิตศาสตร์ประยุกต์ | 3,500 | ฐานเดิมจากคณะวิทยาศาสตร์/สถิติ |
| `cat_ds` | วิทยาการข้อมูล (Data Science) | 1,800 | หลักสูตรตรงที่เปิดเพิ่มใน 5 ปีหลัง |
| `cat_ai` | ปัญญาประดิษฐ์ (AI / ML Direct) | 600 | หลักสูตรเฉพาะทาง AI/Robotics |

---

### Dataset B: Starting Salary & Regional Benchmark
| Region | Qualification | Entry_Salary_Min_THB | Entry_Salary_Max_THB | Currency_Local | Local_Range |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Thailand** | ป.ตรี / ป.โท | 25,000 | 45,000 | THB | 25,000 - 45,000 / month |
| **Singapore** | Bachelor / Master | 100,000 | 170,000 | SGD | $4,000 - $6,500 / month |
| **USA** | BS / MS / PhD | 230,000 | 350,000 | USD | $85,000 - $130,000 / year |
| **Europe (Germany)** | B.Sc. / M.Sc. | 140,000 | 210,000 | EUR | €48,000 - €70,000 / year |

---

### Dataset C: Top Employers Matrix
* **Thailand Enterprise & Tech:** SCB 10X, KBTG, Agoda, Central Group, True Digital Group, Sertis, Coral, Amity
* **Global Tech & AI Labs:** Google, Microsoft, Meta, OpenAI, NVIDIA, Amazon AWS, DeepMind
* **Consulting & Data Partners:** McKinsey QuantumBlack, BCG GAMMA, Accenture, Seven Peaks Software

---

### Dataset D: Skill Matrix (Business Card Portfolio Levels)

#### 🟢 Tier 1: Entry / Junior (0 - 2 Years)
* **Core Tools:** Python, R, SQL
* **Data & Stats:** Descriptive & Inferential Statistics, Exploratory Data Analysis (EDA)
* **Visualization:** Power BI, Tableau, Looker Studio
* **Machine Learning:** Basic ML (Scikit-Learn, Linear/Logistic Regression, Decision Trees)

#### 🔵 Tier 2: Mid-Level / Senior (2 - 5 Years)
* **Advanced ML:** Feature Engineering, XGBoost, A/B Testing, Causal Inference
* **Deep Learning:** PyTorch, TensorFlow, Computer Vision, NLP
* **Engineering & Cloud:** Big Data (PySpark, Databricks), Cloud Infrastructure (AWS/GCP/Azure)
* **Practices:** MLOps, CI/CD for Machine Learning

#### 🟣 Tier 3: Expert / Principal / Lead (5+ Years)
* **Generative AI:** RAG Architecture, LLM Fine-Tuning, Model Quantization & Deployment
* **Enterprise Architecture:** End-to-End Enterprise Data Stack Design, Edge AI
* **Governance & Strategy:** AI Ethics, Data Governance, Technical Roadmap Creation
* **Leadership:** Technical Team Management, Cross-functional Business Impact Alignment

---

## 🔗 3. Open Data Reference Sources (External Links)

1. **Thailand Government Open Data Portal:** [data.go.th](https://data.go.th)  
   * *Use case:* ดึงสถิติบัญชีข้อมูลภาครัฐ สถิติบัญชีจบใหม่
2. **Kaggle Datasets:** [kaggle.com/datasets](https://www.kaggle.com/datasets)  
   * *Use case:* ชุดข้อมูล Data Science Job Salaries
3. **National Statistical Office (NSO):** [nso.go.th](https://www.nso.go.th)  
   * *Use case:* สถิติภาวะการทำงานของประชากร
4. **UCI Machine Learning Repository:** [archive.ics.uci.edu](https://archive.ics.uci.edu)  
   * *Use case:* ชุดข้อมูลมาตรฐานสำหรับวิจัย AI/ML

---

## 🎨 4. Layout & UI/UX Guidelines for Antigravity

1. **Color Palette Theme:**
   * Primary: Deep Indigo / Slate (`#1e293b`, `#4f46e5`)
   * Accents: Emerald Green for Salaries (`#10b981`), Cyan for Open Data (`#06b6d4`), Purple for Senior Tier (`#a855f7`)
2. **Dashboard Widgets Required:**
   * **KPI Cards:** แสดงสรุปจำนวนบัณฑิตรวม และช่วงเงินเดือนเฉลี่ย
   * **Bar Chart:** เปรียบเทียบผู้จบการศึกษาตามแต่ละสายวิชา
   * **Interactive Data Table:** แสดงอัตราเงินเดือนจำแนกตามประเทศ/วุฒิการศึกษา พร้อม Search/Filter
   * **Tiered Card Grid:** แสดงทักษะสำคัญ 3 ระดับ (Junior, Mid, Expert)
3. **Interactivity Requirements:**
   * รองรับ Filter ตามภูมิภาค/ประเทศ
   * รองรับการ Export ข้อมูลเป็น JSON/CSV หรือ PDF Report

---

## 🤖 5. Antigravity Prompt / Execution Command

```text
Please ingest the provided Markdown specification and build a modern, responsive, interactive dashboard. 
Use Chart.js or D3.js for visual rendering, and ensure all table items and skill cards reflect the 3-tier structure (Entry, Mid, Expert). 
Maintain clean styling using Tailwind CSS, and keep data structures modular so API endpoints can easily hydrate the components later.
```