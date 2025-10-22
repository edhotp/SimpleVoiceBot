#!/usr/bin/env python3
"""
Simple Web Chatbot using Flask
Aplikasi chatbot web sederhana menggunakan Flask dan Azure OpenAI dengan Voice Features

Author: Edhot Purwoko - Microsoft Indonesia
License: MIT - Free to use
Disclaimer: Provided "as is" without warranty. Use at your own risk.
"""

from flask import Flask, render_template, request, jsonify, Response
from chatbot import SimpleChatbot
import json

app = Flask(__name__)
bot = SimpleChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get response from chatbot
        response = bot.get_response(user_message, stream=False)
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chat/stream', methods=['POST'])
def chat_stream():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        def generate():
            for chunk in bot.get_response(user_message, stream=True):
                yield f"data: {json.dumps({'chunk': chunk})}\n\n"
            yield f"data: {json.dumps({'done': True})}\n\n"
        
        return Response(generate(), mimetype='text/plain')
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/clear', methods=['POST'])
def clear_history():
    try:
        bot.clear_history()
        return jsonify({'status': 'success', 'message': 'History cleared'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/voice/chat', methods=['POST'])
def voice_chat():
    """Voice chat endpoint - listen and respond with voice"""
    try:
        if not bot.speech_enabled:
            return jsonify({'error': 'Speech services tidak tersedia'}), 400
        
        result = bot.voice_chat(speak_response=True)
        
        if result and isinstance(result, dict):
            return jsonify({
                'status': 'success',
                'user_input': result['user_input'],
                'bot_response': result['bot_response']
            })
        else:
            return jsonify({'error': result or 'Gagal memproses voice chat'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/voice/listen', methods=['POST'])
def voice_listen():
    """Listen to speech input and return text"""
    try:
        if not bot.speech_enabled:
            return jsonify({'error': 'Speech services tidak tersedia'}), 400
        
        speech_text = bot.listen_for_input()
        
        if speech_text:
            return jsonify({
                'status': 'success',
                'text': speech_text
            })
        else:
            return jsonify({'error': 'Tidak ada suara yang terdeteksi'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/voice/speak', methods=['POST'])
def voice_speak():
    """Speak the given text"""
    try:
        if not bot.speech_enabled:
            return jsonify({'error': 'Speech services tidak tersedia'}), 400
        
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        success = bot.speak_response(text)
        
        if success:
            return jsonify({'status': 'success', 'message': 'Text berhasil diucapkan'})
        else:
            return jsonify({'error': 'Gagal mengucapkan teks'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/voice/test', methods=['POST'])
def voice_test():
    """Test speech services"""
    try:
        if not bot.speech_enabled:
            return jsonify({'error': 'Speech services tidak tersedia'}), 400
        
        success = bot.test_speech_services()
        
        return jsonify({
            'status': 'success' if success else 'error',
            'message': 'Speech services berfungsi dengan baik' if success else 'Ada masalah dengan speech services'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/voice/voices', methods=['GET'])
def get_voices():
    """Get available voices"""
    try:
        if not bot.speech_enabled:
            return jsonify({'error': 'Speech services tidak tersedia'}), 400
        
        voices = bot.get_available_voices()
        return jsonify({'voices': voices})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/voice/set-voice', methods=['POST'])
def set_voice():
    """Set speech synthesis voice"""
    try:
        if not bot.speech_enabled:
            return jsonify({'error': 'Speech services tidak tersedia'}), 400
        
        data = request.get_json()
        voice_name = data.get('voice_name', '')
        
        if not voice_name:
            return jsonify({'error': 'No voice name provided'}), 400
        
        success = bot.set_speech_voice(voice_name)
        
        if success:
            return jsonify({'status': 'success', 'message': f'Suara diubah ke: {voice_name}'})
        else:
            return jsonify({'error': f'Gagal mengubah suara ke: {voice_name}'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/voice/set-language', methods=['POST'])
def set_language():
    """Set speech recognition language"""
    try:
        if not bot.speech_enabled:
            return jsonify({'error': 'Speech services tidak tersedia'}), 400
        
        data = request.get_json()
        language_code = data.get('language_code', '')
        
        if not language_code:
            return jsonify({'error': 'No language code provided'}), 400
        
        success = bot.set_speech_language(language_code)
        
        if success:
            return jsonify({'status': 'success', 'message': f'Bahasa diubah ke: {language_code}'})
        else:
            return jsonify({'error': f'Gagal mengubah bahasa ke: {language_code}'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/voice/status', methods=['GET'])
def voice_status():
    """Get voice service status"""
    return jsonify({
        'speech_enabled': bot.speech_enabled,
        'status': 'available' if bot.speech_enabled else 'unavailable'
    })

if __name__ == '__main__':
    print("🌐 Starting Flask Web Chatbot...")
    print("📱 Open your browser and go to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)