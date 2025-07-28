import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the T5 model and tokenizer
model_name = "t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Function to translate English to German
def translate_to_german(english_text):
    # Add task prefix for translation
    input_text = "translate English to German: " + english_text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output_ids = model.generate(input_ids, max_length=100, num_beams=5, early_stopping=True)
    german_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return german_text

# Main block
if __name__ == "__main__":
    english_input = input("Enter English sentence to translate into German:\n")
    german_output = translate_to_german(english_input)
    print("\nGerman Translation:\n", german_output)
