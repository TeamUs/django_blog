# titanic_predictor/views.py
from django.shortcuts import render
from .forms import ModelChoiceForm
from .gradient_boosting import GradientBoostingModel
from .polynomial_regression import PolynomialRegressionModel
from .rnn import RNNModel
import pandas as pd
from django.http import HttpResponse
import numpy as np

def choose_model(request):
    if request.method == 'POST':
        form = ModelChoiceForm(request.POST)
        if form.is_valid():
            # Load training data from a CSV file
            train_data = pd.read_csv('titanic_data.csv')
            train_data = train_data[train_data['is_test'] == 0]
            X_train = train_data.drop(columns=['Survived', 'is_test'])
            y_train = train_data['Survived']
            X_train = X_train.astype('float32')

            model_choice = form.cleaned_data['model']
            if model_choice == 'gradient_boosting':
                model = GradientBoostingModel()
            elif model_choice == 'polynomial_regression':
                model = PolynomialRegressionModel()
            elif model_choice == 'rnn':
                # Normalize continuous features
                X_train['Fare'] = (X_train['Fare'] - X_train['Fare'].mean()) / X_train['Fare'].std()
                X_train['Age'] = (X_train['Age'] - X_train['Age'].mean()) / X_train['Age'].std()
                model = RNNModel(X_train)

            # Train the model
            model.train(X_train, y_train)

            # Load test data from a CSV file
            test_data = pd.read_csv('titanic_data.csv')
            test_data = test_data[test_data['is_test'] == 1]
            X_test = test_data.drop(columns=['Survived', 'is_test'])
            X_test = X_test.astype('float32')

            # Get predictions
            predictions = model.predict(X_test)
            if model_choice == 'rnn':
                predictions = np.round(predictions).astype(int).flatten()

            # Create a DataFrame with the results
            results_df = pd.DataFrame({'Sex': test_data['Sex'], 'Fare': test_data['Fare'], 'Age': test_data['Age'], 'Predicted': list(predictions)})

            # Save results to a CSV file
            results_csv = results_df.to_csv(index=False)

            # Create an HTTP response for downloading the file
            response = HttpResponse(results_csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="results.csv"'
            return response
    else:
        form = ModelChoiceForm()
    return render(request, 'choose_model.html', {'form': form})