# 🏡 Florida Housing Market – End-to-End Machine Learning & Azure MLOps
Author: Sanjana Patnam
Status: Self-Initiated, Independently Built


This project builds an end-to-end ML pipeline to predict Florida home values, discover market segments via clustering, deploy the model on Azure ML, and visualize insights through Tableau dashboards.

---

## 🔍 **Project Overview**
- Performed comprehensive EDA, data cleaning, and feature engineering on 20+ housing attributes.
- Built & compared multiple ML models (Lasso, Ridge, Random Forest, XGBoost).
- Applied **K-Means clustering** to segment the Florida housing market.
- Selected **Lasso Regression** as the final model based on stability & accuracy.
- Deployed the model using **Azure ML Batch Endpoints** for scalable inference.
- Delivered interactive **Tableau visualizations** for business insights.

---

## 📁 **Repository Structure**
```
├── 01_EDA_and_Feature_Engineering.ipynb
├── 02_Clustering_Analysis.ipynb
├── 03_Value_Prediction.ipynb
├── 05_Model_Deployment.ipynb
├── models/
├── data/
├── deployment/
│   └── score.py
├── model_comparison.csv
├── undervalued_properties.csv
└── requirements.txt
```

---

## 📊 **Modeling Summary**
- **Baseline:** Decision Tree  
- **Advanced Models:** Random Forest, XGBoost  
- **Final Model:** **Lasso Regression**  
  - Most stable coefficients  
  - Strong generalization  
  - High performance and interpretability  

---

## 🧭 **Clustering Summary – Market Segments Identified**
Using K-Means, four distinct market segments were discovered:

1. **Affordable starter homes**  
2. **Mid-range suburban family homes**  
3. **Large premium homes**  
4. **High-end luxury properties**

These clusters helped identify which regions/properties are undervalued.

---

## ☁ **Azure Deployment – MLOps**
- Registered model in Azure ML Workspace.
- Created batch deployment using `score.py`.
- Automated:
  - Model loading  
  - Input CSV processing  
  - Price prediction  
- Verified endpoint results using sample input files.

---

## 📊 **Tableau Dashboard**
Dashboard includes:
- Price-per-square-foot trends  
- Market segmentation maps  
- City-level comparisons  
- Actual vs predicted pricing  

---

## ▶ **How to Run**
1. Clone the repository  
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run notebooks in numeric order.

---

## 🛠 **Tech Stack**
**Python**, Pandas, NumPy  
**Scikit-learn**, XGBoost  
**Azure Machine Learning**, Batch Endpoints  
**Tableau**, MLflow  

---
📬 Contact
If you'd like to collaborate or have questions about the dataset or workflow, feel free to reach out:

Sanjana Patnam
📧 [patnamsanjana128@gmail.com]
