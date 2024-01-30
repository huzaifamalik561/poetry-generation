**Poem Generator**

**Overview**

The Poem Generator is a web application built using Flask and the Transformers library that generates poems based on user input. The application uses pre-trained GPT-2 models for different poets (Shakespeare and Keats) and genres (Angry, Love, Sad) to create unique and creative poems. Additionally, the application utilizes an external service to convert generated text into an image.

**Table of Contents**

Getting Started

Usage

File Structure

Dependencies

Docker Support

Acknowledgments

License

Getting Started

**Clone the repository:**

git clone https://github.com/your-username/poem-generator.git

**Install the required dependencies:**

cd poem-generator

pip install -r requirements.txt

**Run the application:**

python main.py

The application will be accessible at http://localhost:5000.

**Usage**
Open your web browser and navigate to http://localhost:5000.

Enter a title, select a poet (Shakespeare or Keats), and choose a genre (Angry, Love, Sad).

Click the "Generate Poem and Image" button.

View the generated poem and associated image.

File Structure

-All models: Directory containing pre-trained GPT-2 models for different poets and genres.
---Angry_shakespeare

---Angry_keats

---Sad_keats

---Sad_shakespeare

---Love_keats

---Love_shakespeare

-Templates: HTML templates for the Flask application.

---index.html

-Static: Static files such as stylesheets.

---style.css

-main.py: Flask application code for generating poems and handling user input.

-Dockerfile: Docker configuration file for containerizing the application.

-requirements.txt: List of Python dependencies.

**Dependencies**

-torch==2.1.2

-torchvision==0.16.2

-Flask==3.0.1

-transformers==4.35.0

-pandas==2.1.4

-Pillow==9.4.0

-Docker Support

This application can be containerized using Docker. Ensure you have Docker installed, then follow these steps:

**Build the Docker image:**

docker build -t poem-generator:latest .

**Run the Docker container:**

docker run -p 5000:5000 poem-generator:latest

The application will be accessible at http://localhost:5000.

**Acknowledgments**

This project uses the GPT-2 models from the Transformers library by Hugging Face.

**License**

This project is licensed under the MIT License.

Feel free to contribute, report issues, or suggest improvements. For accessing the pre-trained GPT-2 models, please download them from the following Google Drive link: https://drive.google.com/drive/folders/1jUYsMms-kXp-a8XLCAnd1TtXzm_xdkxi?usp=sharing
