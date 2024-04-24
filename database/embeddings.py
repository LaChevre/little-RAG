import json
import torch
from transformers import BertModel, BertTokenizer

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_embeddings(text, tokenizer, model):
    # Encode text to get token ids and attention masks
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True, padding='max_length')
    # Get embeddings from BERT
    with torch.no_grad():
        outputs = model(**inputs)
    # Use the mean of the last hidden state as the embedding
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
    return embeddings

# Load the pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Load your JSON data
data = load_json('little-RAG/database/data.json')

# Iterate over each entry and generate embeddings
for entry in data:
    entry['embedding'] = get_embeddings(entry['contenu'], tokenizer, model)

# Save the data back to JSON with embeddings
save_json(data, 'little-RAG/database/updated_data.json')

print("Embeddings generated and saved successfully.")
