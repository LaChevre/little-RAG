# Import necessary libraries
from transformers import AutoModelForCausalLM, AutoTokenizer
import json
from corpus2rag import return_response


# Import the tokenizer and model from Hugging Face Hub
tokenizer_name = "stabilityai/stablelm-tuned-alpha-3b"
model_name = tokenizer_name
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


def trim_response(prompt, response):
    # Identify the start of new content by finding the end of the structured prompt in the response
    prompt_end = prompt.strip().split("\n")[-1]  # Get the last line of the prompt as the likely endpoint in the response
    end_index = response.find(prompt_end)
    if end_index != -1:
        # Adjust to start extracting right after the found prompt
        start_of_new_content = end_index + len(prompt_end)
        # Return everything from this point to the end of the response
        return response[start_of_new_content:].strip()
    return response  # Return the original if no prompt is found


# Define a function to handle user input and generate a response
def generate_response(user_input):
    relevant_document = return_response(user_input)
    prompt = f"""
    You are a bot that provides detailed technical advice about PC components. You respond with precise and concise information.
    This is the highlighted component: {relevant_document}
    The user input is: {user_input}
    Based on the highlighted component and the user's query, provide a tailored recommendation or detailed information that aligns with the user's specific needs or interests.
    """


    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    print("Generated text:", generated_text)

    response = trim_response(prompt, generated_text)
    return response


user_input = "what is a gpu?"
response = generate_response(user_input)
print("Response :" ,response)