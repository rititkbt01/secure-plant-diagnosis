# 🌿 Secure Plant Disease Diagnosis App
### Group 31 | Taylor's University | Capstone Project I (PRJ63504)

---

## 📌 Project Overview

A secure mobile application that allows farmers to photograph a diseased plant leaf and receive an instant AI-powered diagnosis with expert-verified treatment recommendations — all within 3 seconds.

**Three crops supported:** Tomato 🍅 | Potato 🥔 | Bell Pepper 🫑

---

## 🎯 Key Features

- **AI Diagnosis** — Vision Transformer (DeiT-Tiny) trained via knowledge distillation
- **Safe Treatment Advice** — Rule-based engine from FAO-verified database (zero AI hallucination)
- **Full Security** — JWT Authentication + TLS 1.3 encryption + Magic Byte validation
- **Cross-Platform** — Flutter mobile app for Android

---

## 👥 Team

| Member | Role | Responsibility |
|--------|------|---------------|
| **Ritik Budhathoki** | Project Leader + Security Lead | FastAPI backend, JWT, TLS 1.3, Magic Byte validation |
| **Yashraj Shrestha** | AI Lead | ResNet50 teacher training, DeiT-Tiny knowledge distillation |
| **Rishi Kumar Kushwaha** | Data Engineering Lead | Dataset preparation, augmentation pipeline |
| **Jeshik Neupane** | App Development Lead | Flutter mobile app, camera integration |
| **Rishav Dhakal** | Model Optimization Lead | Benchmarking, latency testing, accuracy validation |

**Supervisor:** Rabin Thapa (rabin@iimscollege.edu.np)

---

## 📊 Project Status

| Stage | Task | Status |
|-------|------|--------|
| ✅ Complete | Proposal submitted | Done |
| ✅ Complete | GitHub repository setup | Done |
| ✅ Complete | Python environment + libraries | Done |
| ✅ Complete | PlantVillage dataset downloaded | Done |
| ✅ Complete | Data filtered to 3 crops (15 classes) | Done |
| ✅ Complete | Data split into train/val/test | Done |
| 🔄 In Progress | Train ResNet50 teacher model | Starting |
| ⏳ Upcoming | Train DeiT-Tiny student model | Pending |
| ⏳ Upcoming | Build FastAPI backend + security | Pending |
| ⏳ Upcoming | Build Flutter mobile app | Pending |
| ⏳ Upcoming | System integration | Pending |
| ⏳ Upcoming | Final demo | Pending |

---

## 🏗️ System Architecture

```
📱 Flutter App (Mobile Client)
        ↓ HTTPS / TLS 1.3
🔐 FastAPI Backend (JWT Auth + Rate Limiting)
        ↓
✅ Security Layer (Magic Byte Validation)
        ↓
🤖 DeiT-Tiny Model (Disease Classification)
        ↓
🗄️ PostgreSQL (Rule-Based Treatment Engine)
        ↓
📱 Result: Disease Name + Confidence + Treatment
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Flutter | Cross-platform mobile app |
| FastAPI | Backend REST API |
| PyTorch | AI model training |
| DeiT-Tiny | Plant disease classification |
| ResNet50 | Teacher model for distillation |
| PostgreSQL | Treatment database |
| JWT | User authentication |
| TLS 1.3 | Data encryption |

---

## 📁 Repository Structure

```
secure-plant-diagnosis/
│
├── 📄 README.md              → Project overview (this file)
├── 📄 .gitignore             → Ignores dataset, venv, secrets
├── 📄 requirements.txt       → All Python libraries
│
├── 📂 data/                  → Data preparation scripts
│   ├── prepare_data.py       → Filters dataset to 3 crops
│   ├── split_data.py         → Splits into train/val/test
│   └── verify_data.py        → Verifies data integrity
│
├── 📂 ai-model/              → AI model files (Yashraj)
│   └── README.md
│
├── 📂 notebooks/             → Kaggle training notebooks (Yashraj)
│   └── README.md
│
├── 📂 backend/               → FastAPI server (Ritik)
│   └── README.md
│
├── 📂 mobile/                → Flutter app (Jeshik)
│   └── README.md
│
├── 📂 docs/                  → Reports and documentation
│   └── README.md
│
└── 📂 deliverables/          → Final submission files
    └── README.md
```

> ⚠️ Dataset images and trained model files are NOT stored in this repository due to size.
> They are stored locally on each team member's laptop.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 (NOT 3.11, 3.12 or 3.13)
- Git
- Kaggle account with API token

### 1. Clone the Repository
```bash
git clone https://github.com/rititkbt01/secure-plant-diagnosis.git
cd secure-plant-diagnosis
```

### 2. Create Virtual Environment
```bash
py -3.10 -m venv venv
venv\Scripts\activate
```

### 3. Install Libraries
```bash
pip install -r requirements.txt
```

### 4. Download Dataset
```bash
kaggle datasets download -d abdallahalidev/plantvillage-dataset
tar -xf plantvillage-dataset.zip
```

### 5. Prepare Data
```bash
python data/prepare_data.py
python data/split_data.py
python data/verify_data.py
```

---

## 📊 Dataset Information

- **Source:** PlantVillage (raw, unprocessed)
- **Total Images:** 22,787
- **Classes:** 15 disease classes across 3 crops
- **Split:**

| Set | Images | Purpose |
|-----|--------|---------|
| Train | 15,944 (70%) | AI learns from this |
| Val | 3,411 (15%) | AI checks itself during training |
| Test | 3,432 (15%) | Final accuracy verification |

---

## 🎯 Target Performance

| Metric | Target |
|--------|--------|
| Accuracy | ≥ 85% |
| Precision | ≥ 0.85 |
| Recall | ≥ 0.85 |
| F1-Score | ≥ 0.88 |
| Response Time | < 3 seconds |

---

## 📅 Timeline

| Phase | Duration | Focus |
|-------|----------|-------|
| Capstone 1 | Weeks 1–5 | Planning + Proposal + Data |
| Capstone 2 | Weeks 6–15 | Build + Test + Demo |

---

*Taylor's University | School of Computer Science*
*Bachelor of Computer Science (Honours)*
*Module: Capstone Project I — PRJ63504*
*Supervisor: Rabin Thapa | February 2026*