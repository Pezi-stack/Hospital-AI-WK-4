# Predictive Analytics for Resource Allocation
## Breast Cancer Priority Prediction

This Jupyter notebook implements a complete machine learning pipeline to predict patient priority levels (High/Medium/Low) for hospital resource allocation using the Breast Cancer Wisconsin Dataset.

## Features

- ✅ **Data Preprocessing**: Complete data cleaning, feature engineering, and labeling
- ✅ **Priority Classification**: Creates priority labels based on cancer characteristics
- ✅ **Random Forest Model**: Trains a robust classifier for priority prediction
- ✅ **Performance Evaluation**: Comprehensive metrics including Accuracy and F1-Score
- ✅ **Visualizations**: Confusion matrices, feature importance, and performance charts

## Dataset

The notebook uses the **Wisconsin Breast Cancer Diagnostic Dataset** (available in sklearn, also available on Kaggle). This dataset contains:
- 569 samples
- 30 features (mean, worst, and standard error values of various diagnostic measurements)
- Target: Malignant (0) or Benign (1)

## Priority Levels

The model predicts three priority levels for resource allocation:
- **High Priority**: Malignant cases with severe risk factors (mean radius > 18, worst area > 1000, etc.)
- **Medium Priority**: Early malignant cases or benign cases requiring monitoring
- **Low Priority**: Clearly benign cases with low-risk features

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Launch Jupyter Notebook:
```bash
jupyter notebook breast_cancer_priority_prediction.ipynb
```

## Model Performance

The Random Forest classifier typically achieves:
- **Accuracy**: >90% on test set
- **F1-Score (Macro)**: >0.90
- **Per-class F1-Scores**: Balanced performance across all priority levels

## Notebook Structure

1. **Data Loading**: Load and explore the breast cancer dataset
2. **Data Preprocessing**: 
   - Clean and validate data
   - Create priority labels
   - Feature selection and scaling
   - Train/test split (80/20)
3. **Model Training**: Random Forest classifier with hyperparameters
4. **Evaluation**: 
   - Accuracy and F1-Score metrics
   - Confusion matrices
   - Classification reports
   - Feature importance analysis
5. **Summary**: Performance metrics and recommendations

## Usage

Simply run all cells in the notebook sequentially. The notebook is self-contained and will:
1. Load the dataset automatically
2. Perform all preprocessing steps
3. Train the model
4. Display comprehensive performance metrics and visualizations

## Output

The notebook generates:
- Performance metrics (Accuracy, F1-Score)
- Confusion matrices for training and testing sets
- Feature importance visualization
- Classification reports with precision, recall, and F1-score per class
- Performance comparison charts

## Requirements

- Python 3.7+
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- jupyter

See `requirements.txt` for specific versions.

## Notes

- The dataset is automatically loaded from sklearn's built-in datasets
- To use Kaggle's version, uncomment and modify the data loading cell
- The model uses stratified train/test split to maintain class distribution
- Feature scaling is applied for consistency (though Random Forest handles unscaled data)

## Applications

This model can be used in hospital systems for:
- **Resource Allocation**: Prioritize patients based on predicted urgency
- **Workload Management**: Allocate medical staff and equipment efficiently
- **Risk Assessment**: Early identification of high-priority cases
- **Decision Support**: Assist healthcare professionals in triage decisions

