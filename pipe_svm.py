pipe_svm = Pipeline([
    ('scaler', StandardScaler()),
    ('SVC', SVC())
])
