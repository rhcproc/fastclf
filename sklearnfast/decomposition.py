from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

def pca(df, target, n_components=5):
    X_features = df.drop(target, axis=1)
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(X_features)
    pca = PCA(n_components=n_components)
    pca.fit(df_scaled)
    df_pca = pca.fit_transform(df_scaled)
    df_pca = pd.DataFrame(df_pca)
    df_pca[target] = df[target]
    return df_pca
    