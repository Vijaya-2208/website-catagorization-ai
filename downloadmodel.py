import os
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "facebook/bart-large-mnli"
save_path = "./model"

# Create folder if it doesn't exist
os.makedirs(save_path, exist_ok=True)

# Download and save model
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)

print(f"✅ Model saved to: {save_path}")

