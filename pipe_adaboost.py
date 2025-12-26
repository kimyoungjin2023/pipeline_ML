pipe_ada = Pipeline([
    ('scaler', StandardScaler()),
    ('ada', AdaBoostClassifier(random_state=42))
])
