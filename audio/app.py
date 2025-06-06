from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    temp_path = 'temp_audio.wav'
    audio_file.save(temp_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_path) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            text = "Could not understand the audio"
        except sr.RequestError as e:
            text = f"Error with speech recognition service: {e}"

    os.remove(temp_path)  # Clean up temporary file
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)