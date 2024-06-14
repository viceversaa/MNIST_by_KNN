num_samples = 10
indices = np.random.choice(range(len(X_test_scaled)), num_samples, replace=False)

for i, idx in enumerate(indices):
    image = X_test_scaled[idx].reshape(28, 28)
    predicted_label = y_pred[idx]
    true_label = y_test[idx]

    plt.subplot(2, num_samples // 2, i + 1)
    plt.imshow(image, cmap='gray', interpolation='none')
    plt.title(f'Predict: {predicted_label}\nTrue: {true_label}')
    plt.axis('off')

plt.tight_layout()
plt.show()