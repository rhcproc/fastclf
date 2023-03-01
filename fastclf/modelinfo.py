from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score

"""
Returns a tuple of (model, result) where result is a dictionary with the following keys
f1_score: f1_score
precision: precision_score
recall: recall_score
accuracy: accuracy_score
"""
def classification_info(
    model, 
    df, 
    target, 
    test_size=0.2, 
    random_state=42, 
    f1_average='weighted'):

    X = df.drop(target, axis=1)
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return (model, {
        'f1_score': f1_score(y_test, y_pred, average=f1_average),
        'precision': precision_score(y_test, y_pred, average=f1_average),
        'recall': recall_score(y_test, y_pred, average=f1_average),
        'accuracy': accuracy_score(y_test, y_pred)
    })

def classification_predict(model, X):
    y_pred = model.predict(X)
    return y_pred
    
def classification_predict_proba(model, X):
    y_pred_proba = model.predict_proba(X)
    return y_pred_proba
