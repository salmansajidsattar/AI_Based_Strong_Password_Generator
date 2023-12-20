from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv('api_key')

@app.route('/generate_password', methods=['GET'])
def generate_password():
    try:
        # Get the desired length of the password from the request
        length = int(request.values.get('lenght'))     
        # Generate a password using OpenAI prompt engineering
        prompt = f"Generate a secure password with {length} characters including 1 special chracter,2numbers and remaining alphabets with combination of small and capital letters:"
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the appropriate engine
            prompt=prompt,
            max_tokens=length,
            temperature=0.6  # You can adjust the temperature to control randomness
        )

        # Extract the generated password from the OpenAI response
        generated_password = response['choices'][0]['text'].strip()

        return jsonify({"password": generated_password})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
