from flask import Flask, request, jsonify, render_template
from transformers import MarianMTModel, MarianTokenizer, PegasusForConditionalGeneration, PegasusTokenizer
from langdetect import detect

app = Flask(__name__)

# Translation function
def translate_text(text, source_lang, target_lang):
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# Summarization function
def summarize_text(text):
    model_name = "google/pegasus-xsum"
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    model = PegasusForConditionalGeneration.from_pretrained(model_name)

    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary = model.generate(**inputs)
    return tokenizer.decode(summary[0], skip_special_tokens=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_article():
    data = request.json
    article = data.get("article")
    target_language = data.get("target_language", "en")
    
    if not article:
        return jsonify({"error": "No article provided"}), 400

    source_language = detect(article)
    translated = article
    if source_language != target_language:
        translated = translate_text(article, source_language, target_language)
    summary = summarize_text(translated)

    return jsonify({
        "translated_text": translated,
        "summary": summary
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
