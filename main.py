from sklearnfast.test import classification_test
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from pprint import pprint
import pandas as pd

data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

model = RandomForestClassifier()
result = classification_test(model, df, 'target')
pprint(result)