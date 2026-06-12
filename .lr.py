from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=100)
model.fit(X_train_vector, y_train)

output = model.predict([vector])
probability = model.predict_proba([vector])
