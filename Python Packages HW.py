#!/usr/bin/env python
# coding: utf-8

# In[9]:


#SCIKIT-LEARN (sklearn)

#Scikit-learn is one of the most widely used open-source machine
#learning libraries in Python. It provides simple and efficient tools 
#for data preprocessing, feature engineering, model training, 
#evaluation, and prediction.

#Scikit-learn supports:
#Classification (e.g., predicting hospital readmission)
#Regression
#Clustering
#Dimensionality reduction
#Model selection
#Preprocessing and pipelines


#GitHub repository:
#https://github.com/scikit-learn/scikit-learn

#Citation
#Pedregosa et al. (2011). Scikit-learn: Machine Learning in Python.
#Journal of Machine Learning Research.

#ADVANTAGES OF SCIKIT-LEARN

#1. Simple and consistent API for all models.
#2. Really useful for prototyping and applied machine learning.
#3. Supports lots of classifiers (Logistic Regression, Random Forest, 
   #Gradient Boosting, SVM, etc.).
#4. Works cohesively with Pandas and NumPy.
#5. Built-in tools for scaling, splitting, cross-validation, metrics.

#LIMITATIONS OF SCIKIT-LEARN

#1. Not optimized for very large datasets or deep learning 
#2. Does not use GPUs.
#3. Primarily focused on classical ML, not neural networks or NLP.
#4. Requires data to be numeric (categorical must be encoded manually).


#EXAMPLE: PREDICTING HOSPITAL READMISSION USING
#AGE, GENDER, AND RACE FROM THE DIABETES 130-US DATASET


import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


# Load Data
df = pd.read_csv("diabetic_data.csv")

# Select variables
features = ["age", "race", "gender"]
target = "readmitted"
df = df[features + [target]]

# Clean missing values
df = df.replace("?", pd.NA).dropna()

# Convert target to binary because scikit cannot process non-integers
df["readmitted"] = df["readmitted"].apply(lambda x: 1 if x == "<30" else 0)


X = pd.get_dummies(df[features], drop_first=True)


# Train and test split
split_point = int(0.8 * len(df))
X_train = X.iloc[:split_point]
X_test = X.iloc[split_point:]
y_train = df["readmitted"].iloc[:split_point]
y_test = df["readmitted"].iloc[split_point:]

# -----------------------------
# Train log Regression
# -----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

preds = model.predict(X_test)

# Predicted probabilities 
probs = model.predict_proba(X_test)[:, 1]   # probability of readmission (<30 days)


# Evaluate
accuracy = (preds == y_test).mean()
print("Accuracy:", accuracy)

# Results Table
results = X_test.copy()
results["actual"] = y_test.values
results["predicted"] = preds
results["probability_readmission"] = probs   


# Plot Creation
plt.hist(results["probability_readmission"], bins=20)
plt.xlabel("Predicted Probability of Readmission")
plt.ylabel("Number of Patients")
plt.title("Distribution of Readmission Risk")
plt.show()


# In[ ]:




