from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def logreg_giridSearch_crossValid(X_train, y_train, X_test, y_test):

    # Define hyperparameter values to be tuned
    param_grid = {'penalty': ['l1', 'l2'],
                'C': [0.01, 0.1, 1],
                'solver': ['liblinear', 'saga'],
                'class_weight': [None, 'balanced']}

    # Create a logistic regression model
    logreg = LogisticRegression()

    # Create a GridSearchCV object to perform hyperparameter tuning
    grid_search = GridSearchCV(logreg, param_grid, cv=5, scoring='accuracy',n_jobs=10)
    grid_search.fit(X_train, y_train)

    # Get the best hyperparameter
    best_params = grid_search.best_params_
    print("Best Hyperparameters: ", best_params)

    # Fit the logistic regression model with best hyperparameter to the training data
    best_logreg = LogisticRegression(**best_params)
    best_logreg.fit(X_train, y_train)

    # Predict the churn value for the test set
    y_pred = best_logreg.predict(X_test)

    # Evaluate the model performance
    report = classification_report(y_test, y_pred)
    print(report)

def randomForest_giridSearch_crossValid(X_train, y_train, X_test, y_test):

    # Let's build a random forest model

    # Define hyperparameter values to be tuned
    param_grid = {
        "n_estimators": [100, 500],
        "max_depth": [5, 10],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2],
    }
    # Create a random forest model
    rf = RandomForestClassifier()

    # Create a GridSearchCV object to perform hyperparameter tuning
    grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy',n_jobs=10)
    grid_search.fit(X_train, y_train)

    # Get the best hyperparameter
    best_params = grid_search.best_params_
    print("Best Hyperparameters: ", best_params)

    # Fit the random forest model with best hyperparameter to the training data
    best_rf = RandomForestClassifier(**best_params)
    best_rf.fit(X_train, y_train)

    # Predict the churn value for the test set
    y_pred = best_rf.predict(X_test)

    # Evaluate the model performance
    report = classification_report(y_test, y_pred)
    print(report)