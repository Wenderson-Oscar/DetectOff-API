import joblib
from sklearn.feature_extraction.text import TfidfVectorizer


class OffensiveTextClassifier:

    def __init__(self, model_path, vectorizer_path):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)


    def predict_offensive_texts(self, new_texts):
        new_vectors = self.vectorizer.transform(new_texts)
        new_vectors_dense = new_vectors.toarray()
        new_predictions = self.model.predict(new_vectors_dense)
        labels = self.model.classes_
        predicted_labels = new_predictions

        results = []
        for text, prediction in zip(new_texts, predicted_labels):
            results.append((text, prediction))
        return results

