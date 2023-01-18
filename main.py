from sklearnfast.test import classifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

model = RandomForestClassifier()
result = classifier(model, df, 'target')
print(result)
