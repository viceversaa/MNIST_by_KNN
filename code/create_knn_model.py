knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)