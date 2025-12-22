pipe_lasso = Pipeline([
    ('scaler', StandardScaler()),
    ('feature_selection', SelectFromModel(LassoCV(cv=5, random_state=42))),
    ('regressor', Ridge(random_state=42))
])
