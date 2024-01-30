from flask import Flask, render_template, request
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from io import BytesIO
from PIL import Image
import requests
import textwrap


app = Flask(__name__)

# your_api_key = '2628e23eff5524c8910f98b38bb64f12b547f16d836b06d26845e93ba8088072e3dc1616a3ad311ac1220ff3793ac8e9'

# Define global variables for model and tokenizer
model = None
tokenizer = None
device_poem = None

# tf.config.set_env('TF_ENABLE_ONEDNN_OPTS', '0')

def generate_poem(prompt, max_length=100, num_return_sequences=1):
    global model
    global tokenizer
    global device_poem

    model.eval()

    generated = tokenizer.encode(prompt, return_tensors="pt").to(device_poem)

    while True:
        sample_outputs = model.generate(
            generated,
            max_length=max_length,
            num_return_sequences=num_return_sequences,
            temperature=0.9,
            pad_token_id=model.config.eos_token_id,
            do_sample=True,
        )

        poems = [tokenizer.decode(output, skip_special_tokens=True) for output in sample_outputs]

        if poems[0].endswith('.') or poems[0].endswith('!') or poems[0].endswith('?'):
            break

    return poems
def get_model_directory(poet, genre):
    base_directory = "All models/"

    if poet == "shakespeare":
        if genre == "angry":
            return base_directory + "angry_shakespeare"
        elif genre == "love":
            return base_directory + "love_shakespeare"
        elif genre == "sad":
            return base_directory + "sad_shakespeare"
    elif poet == "keats":
        if genre == "angry":
            return base_directory + "angry_keats"
        elif genre == "love":
            return base_directory + "love_keats"
        elif genre == "sad":
            return base_directory + "sad_keats"

    # Default to Keats and Sad if input is invalid
    return base_directory + "sad_keats"

@app.route('/', methods=['GET', 'POST'])
def index():
    global model
    global tokenizer
    global device_poem
    
    image_generated = False
    original_prompt_generated = "" 

    if request.method == 'POST':
        title = request.form['title']
        poet = request.form['poet']
        genre = request.form['genre']

        model_directory = get_model_directory(poet, genre)

        tokenizer = GPT2Tokenizer.from_pretrained(model_directory)
        model = GPT2LMHeadModel.from_pretrained(model_directory)
        device_poem = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device_poem)

        original_prompt_generated = generate_poem(title, 300, 1)[0]
        cropped_poem = ' '.join(textwrap.wrap(original_prompt_generated, width=40)[:40])

        prompt_for_image = f'"{cropped_poem}"'

        r = requests.post('https://clipdrop-api.co/text-to-image/v1',
                          files={'prompt': (None, prompt_for_image, 'text/plain')},
                          headers={'x-api-key': 'e43effb77b348c0bb7f168ed5e26563486a2d8e8856212900e067f8084b38cccb769bfd627e577159f7be67411dc604f'})

        if r.ok:
            image_generated = True
            image = Image.open(BytesIO(r.content))
            image.save('static/generated_image.png')
        else:
            r.raise_for_status()

    return render_template('index.html', image_generated=image_generated, original_poem=original_prompt_generated)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
