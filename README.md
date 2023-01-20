# sklearnfast

### Description

sklearnfast is a python package that allows you to test your scikit-learn models with a single line of code. It is designed to be used in Jupyter Notebooks and is inspired by the [fastai](https://github.com/fastai/fastai) library.

### Installation

```bash
pip install sklearnfast
pip install scikit-learn, pandas
```

### Usage

```python
from sklearnfast.modelinfo import classification_info
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

# {'f1': 0.972972972972973,
#  'accuracy': 0.9649122807017544,
#  'precision': 0.9722222222222222,
#  'recall': 0.9736842105263158}
```

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

### License

[MIT](https://choosealicense.com/licenses/mit/)
