# 🔬 SciVis 2025 – AlloyExplorer

## 📖 Documentation

### 🔍 Overview

**AlloyExplorer** is a data-driven visualization project developed for the **IEEE SciVis 2025 Contest**. The goal is to explore and visually analyze a massive dataset of simulated aluminum alloy compositions derived from recycled engine pistons. These high-performance materials are evaluated on their structural, thermal, and mechanical properties to aid the discovery of new, sustainable alloys.

The project features:
- Multidimensional analysis of input–output relationships
- Dimensionality reduction techniques for pattern recognition
- Interactive visual exploration dashboards (Streamlit)
- Potential for integration with alloy optimization algorithms

---

### 🏗️ System Architecture

- **Notebook Layer**
  - Used for exploration, correlation mapping, and PCA/UMAP analysis
  - Identifies sensitivity of outputs to composition variations

- **Interactive Dashboard (Streamlit)**
  - Enables material scientists to compare alloy candidates
  - Filters by performance traits like strength, phase stability, solidification
  - Visualizes microstructure–composition–property links

- **(Optional) Optimization Hooks**
  - Future integration with visual steering and optimizer-guided exploration

---

## 📁 Project Structure

```
2025-IEEE_SciVis-Contest-Mughees/
│
├── Data/
│   └── Dataset_VisContest_Rapid_Alloy_development_v3.txt
│
├── Output/
│
├── app/
│   └── streamlit_dashboard.py
│ 
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── scripts/
│   └── load_and_clean_data.py
│
├── README.md
```



## 📊 Dataset

**Title:** Dataset – SciVisContest – Materials Discovery Challenge  
**DOI:** [10.5281/zenodo.15189444](https://doi.org/10.5281/zenodo.15189444)  
**Published by:** K. Bugelnig and G. Requena, Nov 14, 2024  
**Size:** ~223MB  
**Format:** Text file containing over 100 features related to alloy composition, phase changes, and mechanical properties.

> ⚠️ Do not upload this file to GitHub. Reference the Zenodo link above instead.

---

## 🔗 Core Tasks (from Contest)

### 🧪 Challenge 1: Alloy Space Exploration
- Visualize high-dimensional input-output relationships
- Use dimensionality reduction (e.g., PCA, UMAP)
- Map correlations across scrap mixtures and mechanical properties

### 🧬 Challenge 2: Optimization & Visual Steering
- Develop visual tools for guiding alloy composition changes
- Identify stable vs. volatile input regions
- Support exploratory decision-making through interaction

---

