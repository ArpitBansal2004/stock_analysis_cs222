# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

def load_data():
    # Load the dataset (dataset is yet to be pulled in from yfinance)
    data = load_iris()
    X, y = data.data, data.target
    return train_test_split(X, y, test_size=0.2, random_state=42)

def evaluate_algorithms(X_train, y_train):
    # Define the models
    models = [
        ("Logistic Regression", LogisticRegression(max_iter=10000)),
        ("Decision Tree", DecisionTreeClassifier()),
        ("Random Forest", RandomForestClassifier()),
        ("Support Vector Machine", SVC()),
        ("K-Nearest Neighbors", KNeighborsClassifier()),
        ("Naive Bayes", GaussianNB())
    ]

    results = []
    for name, model in models:
        score = cross_val_score(model, X_train, y_train, cv=5, scoring="accuracy").mean()
        results.append((name, score))

    # Sort models based on score
    results.sort(key=lambda x: x[1], reverse=True)

    return results

def test_best_model(X_train, y_train, X_test, y_test, best_model_name, models):
    best_model = dict(models)[best_model_name]
    best_model.fit(X_train, y_train)
    test_score = best_model.score(X_test, y_test)
    return test_score

if __name__ == "__main__":
    # Load data
    X_train, X_test, y_train, y_test = load_data()

    # Evaluate algorithms
    results = evaluate_algorithms(X_train, y_train)

    # Print results
    print("Cross-validation results:")
    for name, score in results:
        print(f"{name}: {score:.4f}")

    # Test the best model
    best_model_name, _ = results[0]
    test_score = test_best_model(X_train, y_train, X_test, y_test, best_model_name, dict(results))

    # Print test results
    print(f"\nTest accuracy of the best model ({best_model_name}): {test_score:.4f}")

