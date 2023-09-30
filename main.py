from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import torch
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline

app = Flask("Name")
CORS(app)

# Load environment variables from .env file into the script's environment
load_dotenv()

# Access environment variables using the os module
api_token = os.getenv("HF_HOME") #create a .env file and add your HF token

# Now you can use these variables in your code
print(f"API Key: {api_token}")


tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf",token=api_token)
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf",
                                             device_map='auto',
                                             torch_dtype=torch.float16,
                                             token=api_token,
                                             )


print("Listening on port 5000...")
@app.route('/getResponse', methods=['POST'])
def upload():
    try:
        data = request.get_json()
        print(data)
        
        # Create a text generation pipeline
        text_generation_pipeline = pipeline("text-generation", tokenizer=tokenizer, model=model)

        sequences = text_generation_pipeline(data['text'],
                                             do_sample=True,
                                             top_k=10,
                                             top_p=data['top_p'],
                                             num_return_sequences=1,
                                             eos_token_id=tokenizer.eos_token_id,
                                             max_length=data['max_length'],
                                             temperature=data['temperature'],)
        
        response = sequences[0]['generated_text']
        # Check if s starts with p
        if response.startswith(data['text']):
            response = response[len(data['text']):].strip()  # remove prefix
        return jsonify({"response": response})
    except Exception as e:
        # return jsonify({"error": "As an AI language model, I am abide to the code of conduct and won't give you the answer."})
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)