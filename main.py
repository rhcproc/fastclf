from sklearnfast.modelinfo import classification_info
from sklearnfast.decomposition import pca
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from pprint import pprint
import pandas as pd

data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

model = RandomForestClassifier()
(model, info) = classification_info(model, df, 'target')
pprint(info)

df_pca = pca(df, 'target', n_components=7)
(model, info) = classification_info(model, df_pca, 'target')
pprint(info)
