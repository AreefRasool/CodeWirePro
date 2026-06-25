# ⚡ CodeWire Pro — Engineering Compliance Hub

**CodeWire Pro** is an all-in-one electrical engineering dashboard that turns manual cable-sizing and compliance calculations into an instant, visual, and shareable web app. Built with **Gradio** and **Plotly**, it brings together voltage drop analysis, wire sizing, conduit design, box fill, ampacity lookups, material estimation, and one-click executive PDF reports — all wrapped in a sleek, dark, glassmorphism-inspired interface with a live-updating KPI dashboard.

Whether you're a student validating textbook formulas or an engineer sanity-checking a quick design, CodeWire Pro gives you instant, visual feedback instead of spreadsheets and manual lookups.

![Status](https://img.shields.io/badge/status-active-success)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Gradio](https://img.shields.io/badge/built%20with-Gradio-orange)

---

## 🎯 Features

- **⚡ Voltage Drop Analysis** — Calculates voltage drop, percentage loss, and a live engineering health score with a dynamic gauge chart.
- **🔌 Wire Sizing** — Recommends AWG wire size based on load current.
- **📦 Conduit Design** — Calculates conduit fill percentage and recommends conduit size with a bar chart.
- **📐 Box Fill Calculator** — Computes required box volume from conductors, devices, and grounds.
- **🔥 Ampacity Lookup** — Quick reference ampacity ratings for standard wire sizes.
- **📋 Material Estimator** — Estimates wire and conduit material requirements with a donut chart breakdown.
- **📊 Executive Analytics** — Compliance meter and auto-generated executive summary, side-by-side.
- **📂 Project Manager** — Save and reload multiple project calculations by name.
- **📄 Executive PDF Reports** — One-click professional PDF report generation using ReportLab.
- **🎨 Modern UI** — Glassmorphism dark theme with live-updating KPI dashboard cards.

---

## 📸 Preview

### Hero Section & Live KPI Dashboard
![Hero Dashboard](assets/01-hero-dashboard.png)

### Executive Dashboard — Engineering Health Gauge
![Executive Dashboard Gauge](assets/02-executive-dashboard-gauge.png)

### ⚡ Voltage Drop Analysis
![Voltage Analysis](assets/03-voltage-analysis.png)

### 🔌 Wire Sizing
![Wire Sizing](assets/04-wire-sizing.png)

### 📦 Conduit Design
![Conduit Design](assets/05-conduit-design.png)

### 📐 Box Fill Calculator
![Box Fill](assets/06-box-fill.png)

### 🔥 Ampacity Lookup
![Ampacity](assets/07-ampacity.png)

### 📋 Material Estimator
![Material Estimator](assets/08-material-estimator.png)

### 📊 Executive Analytics — Compliance Meter & Summary
![Executive Analytics](assets/09-executive-analytics.png)

### 📂 Project Manager — Save Project
![Project Manager Save](assets/10-project-manager-save.png)

### 📄 Executive PDF Report Generation
![PDF Report Generation](assets/11-project-manager-pdf-report.png)

---

## 🖥️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Gradio](https://www.gradio.app/) | Web UI framework |
| [Plotly](https://plotly.com/python/) | Interactive charts (gauges, bar, pie) |
| [ReportLab](https://www.reportlab.com/) | PDF report generation |
| Python 3.9+ | Core logic |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python codewire_pro.py
```

The app will launch locally and also generate a temporary public link (via Gradio's `share=True`).

> 💡 **Running in Google Colab / Kaggle?** Just upload `codewire_pro.py`, install dependencies with `!pip install -r requirements.txt`, and run the script — Gradio will give you a shareable public link.

---

## 📂 Project Structure

```
.
├── codewire_pro.py       # Main application file
├── requirements.txt      # Python dependencies
├── assets/               # Screenshots used in README
│   ├── 01-hero-dashboard.png
│   ├── 02-executive-dashboard-gauge.png
│   ├── 03-voltage-analysis.png
│   ├── 04-wire-sizing.png
│   ├── 05-conduit-design.png
│   ├── 06-box-fill.png
│   ├── 07-ampacity.png
│   ├── 08-material-estimator.png
│   ├── 09-executive-analytics.png
│   ├── 10-project-manager-save.png
│   └── 11-project-manager-pdf-report.png
├── .gitignore
└── README.md
```

---

## 🧠 How It Works

The app uses a simple engineering health-score model:

```
Health Score = 100 − (Voltage Drop % × 8)
```

- **Score ≥ 90** → ✅ PASS
- **Score 70–89** → ⚠️ WARNING
- **Score < 70** → ❌ FAIL

Wire sizing follows standard AWG current-capacity tiers, and all calculations update the live dashboard KPI cards in real time.

---

## 📌 Future Improvements

- Add user authentication for multi-user project storage
- Export project history to Excel/CSV
- Add support for 3-phase voltage drop calculations
- Persist projects to a database instead of in-memory storage

---

## 👤 Author

**Areef Rasool**
BSAI Student | AI, Computer Vision & Networking Enthusiast

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
