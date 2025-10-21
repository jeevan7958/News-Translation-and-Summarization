# News Translation and Summarization Web App

This project is a Flask-based web application that allows users to translate and summarize news articles in multiple languages using state-of-the-art Transformer models from Hugging Face. The system automatically detects the source language of the input text, translates it into the target language (if needed), and generates a concise summary of the translated article.

## Project Overview

The application leverages two key models from the Hugging Face Transformers library. For translation, it uses the Helsinki-NLP MarianMT model, which supports a wide range of language pairs. For summarization, it employs Google's Pegasus model, specifically the "google/pegasus-xsum" variant, optimized for abstractive summarization. The combination of these models ensures high-quality translation and context-aware summarization results.

## How It Works

When a user submits a news article, the system first detects its language using the langdetect library. If the source language differs from the target language, the text is translated using the appropriate MarianMT model. The translated text is then passed to the Pegasus summarization model to generate a coherent summary. The Flask backend handles incoming requests and returns the translated and summarized text as JSON responses, making it easy to integrate into web or mobile interfaces.

## File Structure

The project consists of two main scripts. The first script defines the Flask server with routes for handling translation and summarization requests. The second script can be used as a standalone Python module to translate and summarize articles without running the web server. Both scripts rely on Hugging Face Transformers, langdetect, and PyTorch as their primary dependencies.

## Setup Instructions

1. Install Python version 3.8 or higher.
2. Create a virtual environment using venv or conda.
3. Install the required dependencies from the requirements.txt file by running the command:
   pip install -r requirements.txt
4. Run the Flask server with the command:
   python app.py
5. Open a web browser and go to http://127.0.0.1:5000 to access the application interface.

## Example Usage

You can use the web interface to paste or upload a news article. Specify the target language (for example, English "en" or French "fr"), and click the process button. The system will return both the translated text and its summary. You can also test the backend using tools such as curl or Postman by sending a POST request to the /process endpoint with a JSON body containing the article and target language.

## Author

Developed by Jeevan Reddy. Built with Flask, Transformers, and PyTorch for intelligent multilingual text processing.

## License

This project is open source and distributed under the MIT License.
