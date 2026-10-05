# Business Requirements Document (BRD)
## โครงการ: ระบบแดชบอร์ดวิเคราะห์อุปสงค์-อุปทานและ Skill Mismatch สายงาน AI, Data Science & Statistics

---

### 1. บทนำและเป้าหมายของโครงการ (Project Overview & Objectives)
การศึกษาสายงาน **AI, Data Science และ Statistics** มีการเติบโตอย่างรวดเร็ว อย่างไรก็ตาม ยังคงมีความไม่สอดคล้องกันระหว่างทักษะที่สถาบันการศึกษาผลิต (Supply) และทักษะที่ภาคอุตสาหกรรมต้องการ (Demand) โครงการนี้จึงจัดทำขึ้นเพื่อพัฒนา **Interactive Analytics Dashboard** ผ่านแอปพลิเคชันแบบ Multi-tab เพื่อตอบโจทย์เป้าหมายหลัก 2 ด้าน ได้แก่:
1. การวิเคราะห์ฝั่งอุปทาน (Supply): ปริมาณผู้จบการศึกษา รายวิชาบังคับ อัตราการได้งานทำ และค่าธรรมเนียมการศึกษา
2. การวิเคราะห์ฝั่งอุปสงค์ (Demand): ปริมาณความต้องการจ้างงาน ทักษะที่ต้องการ บริษัทผู้จ้าง และระดับเงินเดือน
3. การวิเคราะห์ช่องว่างทางทักษะ (Skill Mismatch Analysis): การเปรียบเทียบเชิงลึกเพื่อระบุทักษะที่ขาดแคลนและเกินความต้องการ

---

### 2. ขอบเขตและเทคโนโลยีของระบบ (Technical Architecture & Requirements)

```
+-----------------------------------------------------------------------+
|                             USER INTERFACE                            |
|                  Dash / Streamlit Multi-Tab Dashboard                 |
+-----------------------------------------------------------------------+
|             TAB 1              |        TAB 2        |     TAB 3      |
|  Supply & Graduate Skills      |   Job Demand &      | Skill Mismatch |
|                                |   Skills Needed     |   Analytics    |
+-----------------------------------------------------------------------+
|                          CROSS-FILTERING ENGINE                       |
|           Dash Callbacks / Event Handlers (Cross-filtering)          |
+-----------------------------------------------------------------------+
|                               BACKEND                                 |
|               Python Backend (Pandas, NumPy, Flask/FastAPI)           |
+-----------------------------------------------------------------------+
|                               DATA SOURCE                             |
|          Open Data / Relational DB / Cleaned Data Warehouse           |
+-----------------------------------------------------------------------+
```

#### เทคโนโลยีที่กำหนด (Tech Stack):
* **Backend:** Python (Flask/FastAPI หรือ Built-in Python Data Engine บน Dash/Streamlit)
* **Dashboard & Data Visualization:** Plotly (Plotly Express / Graph Objects) เป็นแกนหลัก
* **Interactivity:** ทุกกราฟใน Tab เดียวกันต้องมี **Cross-filtering / Dynamic Interactivity** เชื่อมโยงกัน เมื่อ User คลิก/เลือก Filter ในกราฟใด กราฟอื่นจะอัปเดตข้อมูลตามทันที

---

### 3. รายละเอียดข้อกำหนดการพัฒนาราย Tab (Functional Requirements)

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│ TAB 1: ปริมาณคนจบและ Skills ที่เรียนมา (Graduate Supply & Academic Skills)         │
├───────────────────────────────────────────────────────────────────────────────────┤
│ [Global Filter Area]: ปีการศึกษา | สถาบันการศึกษา | สาขาวิชา (AI/Data Science/Stat)  │
├──────────────────────────────────┬────────────────────────────────────────────────┤
│ 1.1 Bar / Line Chart            │ 1.2 Sunburst / Treemap / Bar Chart             │
│ จำนวนผู้จบการศึกษาแยกตามหลักสูตร   │ รายวิชาบังคับที่ตรงกับสายงาน                 │
│ และแนวโน้มรายปี                  │                                                │
├──────────────────────────────────┼────────────────────────────────────────────────┤
│ 1.3 Stacked Bar / Grouped Bar   │ 1.4 Box Plot / Scatter Plot / Table            │
│ จำนวนบัณฑิตที่ได้งานทำ           │ ค่าธรรมเนียมการศึกษา (ค่าเทอม)                 │
│ (ปีที่ 1, ปีที่ 2, ปีที่ 3)       │ เปรียบเทียบตามหลักสูตร                         │
└──────────────────────────────────┴────────────────────────────────────────────────┘
```

#### **Tab 1: ปริมาณคนจบและ Skills ที่เรียนมา (Graduate Supply & Academic Skills)**
* **วัตถุประสงค์:** วิเคราะห์กำลังการผลิตบัณฑิตและหลักสูตรการศึกษา
* **ส่วนประกอบกราฟ (Plotly Visualizations):**
  1. **กราฟชื่อหลักสูตรและจำนวนผู้จบการศึกษา:** แสดงรายการหลักสูตรที่ผลิตบัณฑิตในสาขา AI, Data Science และ Statistics พร้อมสถิติการผลิตรายปี (ใช้ Plotly Bar Chart / Grouped Line Chart)
  2. **กราฟรายวิชาบังคับของหลักสูตร:** แสดงทักษะ/รายวิชาบังคับที่เปิดสอนในแต่ละหลักสูตรซึ่งตรงกับสายงาน (ใช้ Plotly Treemap / Sunburst หรือ Horizontal Bar Chart)
  3. **กราฟการได้งานทำของบัณฑิต:** แสดงจำนวนและสัดส่วนบัณฑิตที่ได้งานทำแยกตามช่วงเวลา ได้แก่ **ปีที่ 1, ปีที่ 2 และปีที่ 3** หลังจบการศึกษา (ใช้ Plotly Stacked Bar Chart)
  4. **กราฟค่าธรรมเนียมการศึกษา (ค่าเทอม):** แสดงการเปรียบเทียบค่าเทอมของแต่ละหลักสูตร/มหาวิทยาลัย (ใช้ Plotly Box Plot หรือ Scatter Plot)
* **Interactivity Constraint:** คลิกเลือกลูกคลื่นปีการศึกษาหรือหลักสูตรในกราฟที่ 1 จะไปเปลี่ยนข้อมูลรายวิชา อัตราการได้งาน และค่าเทอมในกราฟที่ 2-4 โดยอัตโนมัติ

---

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│ TAB 2: ปริมาณงานที่จ้างและ Skills ที่ต้องการ (Industry Demand & Market Skills)     │
├───────────────────────────────────────────────────────────────────────────────────┤
│ [Global Filter Area]: อุตสาหกรรม | ระดับตำแหน่งงาน | ประเทศ/ภูมิภาค                 │
├──────────────────────────────────┬────────────────────────────────────────────────┤
│ 2.1 Metric Cards + Donut Chart   │ 2.2 Horizontal Bar Chart / Word Cloud          │
│ ปริมาณตำแหน่งงานที่เปิดรับ (Vacancies)│ ทักษะที่ตลาดต้องการ (Required Skills)          │
├──────────────────────────────────┼────────────────────────────────────────────────┤
│ 2.3 Treemap / Bubble Chart       │ 2.4 Box Plot / Violin Plot                     │
│ บริษัทที่เปิดรับสมัครสูงสุด        │ อัตราเงินเดือนแบ่งตามระดับการทำงาน            │
│ (Top Hiring Companies)           │ (Entry / Mid / Senior / Expert)                │
└──────────────────────────────────┴────────────────────────────────────────────────┘
```

#### **Tab 2: ปริมาณงานที่จ้างและ Skills ที่ต้องการ (Industry Demand & Required Skills)**
* **วัตถุประสงค์:** วิเคราะห์ความต้องการของตลาดแรงงานและสภาวะการจ้างงาน
* **ส่วนประกอบกราฟ (Plotly Visualizations):**
  1. **กราฟปริมาณตำแหน่งงานที่เปิดรับ (Vacancies):** แสดงสถิติจำนวนประกาศรับสมัครงานที่เปิดว่างในแต่ละสาขาและภูมิภาค (ใช้ Plotly Metric Card + Donut Chart)
  2. **กราฟทักษะที่ต้องการ (Required Skills):** แสดงทักษะที่ถูกระบุไว้ในประกาศงาน (ใช้ Plotly Horizontal Bar Chart หรือ Bubble Chart)
  3. **กราฟบริษัทที่เปิดรับ:** แสดงรายชื่อและสัดส่วนองค์กร/บริษัทที่เปิดรับสมัครงานสายนี้สูงสุด (ใช้ Plotly Treemap หรือ Top-N Bar Chart)
  4. **กราฟเงินเดือนตามระดับการทำงาน:** แสดงโครงสร้างและช่วงเงินเดือน (Starting Salary & Ranges) แบ่งตามระดับสายงาน ได้แก่ Entry Level, Mid Level, Senior Level และ Expert (ใช้ Plotly Box Plot หรือ Violin Plot)
* **Interactivity Constraint:** การเลือกประเภททักษะ หรือระดับตำแหน่งงานในกราฟใดๆ จะ Filter บริษัทที่รับสมัคร และช่วงเงินเดือนให้สอดคล้องกันทันที

---

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│ TAB 3: การวิเคราะห์ Skill Mismatch (Skill Gap & Alignment Analytics)              │
├───────────────────────────────────────────────────────────────────────────────────┤
│ [Global Filter Area]: สาขาวิชาเปรียบเทียบ | ระดับตำแหน่งงานที่มุ่งหวัง            │
├──────────────────────────────────┬────────────────────────────────────────────────┤
│ 3.1 Overlay / Dual-Bar Chart     │ 3.2 Scatter Plot (Importance vs Coverage)      │
│ การเปรียบเทียบ Supply Skills     │ Skill Mismatch Quadrant                        │
│ vs Demand Skills                 │ (Missing, Surplus, Well-aligned Skills)        │
├──────────────────────────────────┴────────────────────────────────────────────────┤
│ 3.3 Interactive Gap Heatmap / Table                                               │
│ ตารางแสดงส่วนต่างเปอร์เซ็นต์ความต้องการและช่องว่างทักษะที่ต้องเร่งพัฒนา              │
└───────────────────────────────────────────────────────────────────────────────────┘
```

#### **Tab 3: การวิเคราะห์ Skill Mismatch (Skill Gap & Alignment Analytics)**
* **วัตถุประสงค์:** การเชื่อมโยงข้อมูลระหว่าง Tab 1 (Supply) และ Tab 2 (Demand) เพื่อหาช่องว่างทางทักษะ
* **ส่วนประกอบกราฟ (Plotly Visualizations):**
  1. **กราฟเปรียบเทียบทักษะ (Skills Supply vs Demand):** เปรียบเทียบสัดส่วนหลักสูตรที่สอนทักษะ X (จาก Tab 1) กับสัดส่วนที่ตลาดต้องการทักษะ X (จาก Tab 2) (ใช้ Plotly Overlay Bar Chart หรือ Radar Chart)
  2. **กราฟ Skill Mismatch Quadrant:** แบ่งประเภททักษะออกเป็น 4 กลุ่ม ได้แก่
     * *High Demand & High Supply* (ทักษะสอดคล้อง)
     * *High Demand & Low Supply* (ทักษะขาดแคลน - Critical Skill Gap)
     * *Low Demand & High Supply* (ทักษะเกินความต้องการ)
     * *Low Demand & Low Supply* (ทักษะ Niche)
     *(ใช้ Plotly Scatter Plot แบบกระจาย 4 Quadrants)*
  3. **ตาราง/Heatmap ข้อเสนอแนะการปรับปรุงหลักสูตร:** แสดงดัชนี Mismatch Index เพื่อให้สถาบันการศึกษานำไปปรับรายวิชาบังคับ

---

### 4. ข้อกำหนดด้านข้อมูลและการอัปเดต (Data Pipeline & Interactivity Specs)

1. **Data Model Structure:**
   * **Fact Table 1 (Graduate Fact):** `graduate_id`, `university`, `program_name`, `grad_year`, `employment_yr1`, `employment_yr2`, `employment_yr3`, `tuition_fee`
   * **Fact Table 2 (Job Vacancy Fact):** `job_id`, `company_name`, `job_title`, `experience_level`, `min_salary`, `max_salary`, `location`, `post_date`
   * **Bridge / Skill Mapping Tables:** `program_skills_bridge`, `job_skills_bridge`, `master_skills_dictionary`

2. **Cross-Filtering Callback Requirements (Plotly Events):**
   * ใช้ Event Handling ผ่าน `clickData`, `selectedData`, หรือ `relayoutData` ใน Plotly
   * เมื่อผู้ใช้คลิกเลือก Element บน Plotly Chart (เช่น คลิก Bar ของหลักสูตรหนึ่ง) ระบบจะส่ง `selected_program` เป็น parameter ไปกรอง Pandas DataFrame ใน Backend แล้ว re-render กราฟอื่นๆ ใน Tab นั้นแบบไร้รอยต่อ (Seamless Update)

---

### 5. เกณฑ์การประเมินความสำเร็จ (Acceptance Criteria)

| หัวข้อ | เกณฑ์ที่ต้องผ่าน |
| :--- | :--- |
| **Tab 1 Requirements** | แสดงผลครบ 4 ส่วน: หลักสูตร+จำนวนจบ, รายวิชาบังคับ, การได้งาน (ปี 1-3), และค่าเทอม |
| **Tab 2 Requirements** | แสดงผลครบ 4 ส่วน: ตำแหน่งงานว่าง, ทักษะที่ต้องการ, บริษัทที่รับ, และเงินเดือนตามระดับ |
| **Tab 3 Requirements** | มีกราฟวิเคราะห์ Skill Mismatch โดยคำนวณส่วนต่างระหว่าง Supply และ Demand ได้ถูกต้อง |
| **Interactivity** | ทุกกราฟใน Tab เดียวกันสามารถกดเลือกเพื่อ Cross-filter อัปเดตข้อมูลซึ่งกันและกันได้ |
| **Tech Stack Compliance** | พัฒนาด้วย Python + Plotly เป็นหลัก |
