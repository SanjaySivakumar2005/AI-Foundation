import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
model_name = "t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
# Function to generate text based on input
def generate_text(input_text):
    # Encode the input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    # Generate output
    output_ids = model.generate(input_ids, max_length=150, num_beams=5, early_stopping=True)
    # Decode the output text
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output_text
# Example usage
if __name__ == "__main__":
    input_text = "Translate English to French: How are you?"
    output_text = generate_text(input_text)
    print("Input:", input_text)
    print("Output:", output_text)