from django import forms
from . models import NeuralNet, Regression, \
    KMeansCluster, LogisticRegression, Perceptron

class NuralNetCreateForm(forms.ModelForm):
    class Meta:
        model = NeuralNet
        fields = ('title','model_description', 'features_input', 'labels_input')

class NeuralNetPredictionForm(forms.Form):
    new_data_point = forms.CharField(label='features')

#forms for regression
class RegressionCreateForm(forms.ModelForm):
    class Meta:
        model = Regression
        fields = ('title','degree', 'features_input', 'labels_input')

class RegressionPredictionForm(forms.Form):
    new_data_point = forms.CharField(label='features')

#forms for K Means
class KMeansCreateForm(forms.ModelForm):
    class Meta:
        model = KMeansCluster
        fields = ('title','no_of_clusters', 'features_input')

class KMeansPredictionForm(forms.Form):
    new_data_point = forms.CharField(label='features')


#forms for Logistic regression
class LogisticRegressionCreateForm(forms.ModelForm):
    class Meta:
        model = LogisticRegression
        fields = ('title', 'features_input', 'labels_input')

class LogisticRegressionPredictionForm(forms.Form):
    new_data_point = forms.CharField(label='features')


#forms for Perceptron
class PerceptronCreateForm(forms.ModelForm):
    class Meta:
        model = Perceptron
        fields = ('title', 'features_input', 'labels_input')

class PerceptronPredictionForm(forms.Form):
    new_data_point = forms.CharField(label='features')