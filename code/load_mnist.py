mnist = fetch_openml('mnist_784', version=1)
X, y = mnist.data, mnist.target

if isinstance(X, pd.DataFrame):
    X = X.to_numpy()
y = y.to_numpy()