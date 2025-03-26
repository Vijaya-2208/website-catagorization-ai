from transformers import pipeline

# Load from the local model folder
classifier = pipeline(
    "zero-shot-classification",
    model="./model",
    tokenizer="./model"
)

# Predefined categories
CATEGORIES = [
    "News", "Technology", "E-Commerce", "Finance", "Adult",
    "Entertainment", "Education", "Health", "Travel", "Social Media"
]

def predict_category(text):
    result = classifier(text, CATEGORIES)
    return result["labels"][0]

