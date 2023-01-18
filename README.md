# sklearnfast

### Description

sklearnfast is a python package that allows you to test your scikit-learn models with a single line of code. It is designed to be used in Jupyter Notebooks and is inspired by the [fastai]('www.fast.ai') library.

### Installation

```bash
pip install sklearnfast
```

### Usage

```python
from sklearnfast.test import Classifier
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

model = RandomForestClassifier()
result = Classifier(model, df, 'target')
print(result)
```

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

### License

[MIT](https://choosealicense.com/licenses/mit/)
