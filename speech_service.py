"""
Azure Speech Service Integration
Speech-to-Text dan Text-to-Speech menggunakan Azure Cognitive Services

Author: Edhot Purwoko - Microsoft Indonesia
License: MIT - Free to use
Disclaimer: Provided "as is" without warranty. Use at your own risk.
"""

import os
import threading
import time
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

class SpeechService:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Initialize Speech configuration
        self.speech_key = os.getenv("AZURE_SPEECH_KEY")
        self.speech_region = os.getenv("AZURE_SPEECH_REGION")
        
        if not self.speech_key or not self.speech_region:
            raise ValueError("Azure Speech key dan region harus diset di file .env")
        
        # Create speech config
        self.speech_config = speechsdk.SpeechConfig(
            subscription=self.speech_key, 
            region=self.speech_region
        )
        
        # Set language untuk recognition (Indonesia/English)
        self.speech_config.speech_recognition_language = "id-ID"  # Indonesian
        
        # Set voice untuk synthesis (Indonesian female voice)
        self.speech_config.speech_synthesis_voice_name = "id-ID-ArdiNeural"  # Indonesian male voice
        
        # Audio configs
        self.audio_config_mic = speechsdk.audio.AudioConfig(use_default_microphone=True)
        self.audio_config_speaker = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        
        # Initialize recognizer and synthesizer
        self.speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config, 
            audio_config=self.audio_config_mic
        )
        
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=self.speech_config, 
            audio_config=self.audio_config_speaker
        )
        
        # State management
        self.is_listening = False
        self.recognition_done = False
        self.recognized_text = ""
        
    def recognize_speech_once(self):
        """Recognize speech once from microphone"""
        try:
            print("🎤 Mendengarkan... Silakan berbicara!")
            
            # Start recognition
            speech_recognition_result = self.speech_recognizer.recognize_once_async().get()
            
            # Process result
            if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                recognized_text = speech_recognition_result.text
                print(f"👤 Anda berkata: {recognized_text}")
                return recognized_text
            elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                error_msg = "❌ Tidak ada suara yang terdeteksi. Silakan coba lagi."
                print(error_msg)
                return None
            elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_recognition_result.cancellation_details
                error_msg = f"❌ Speech recognition dibatalkan: {cancellation_details.reason}"
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    error_msg += f"\nError details: {cancellation_details.error_details}"
                print(error_msg)
                return None
                
        except Exception as e:
            print(f"❌ Error saat mengenali suara: {str(e)}")
            return None
    
    def start_continuous_recognition(self, callback=None):
        """Start continuous speech recognition"""
        def recognition_callback(evt):
            if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
                self.recognized_text = evt.result.text
                print(f"👤 Terdeteksi: {self.recognized_text}")
                if callback:
                    callback(self.recognized_text)
        
        def session_stopped_callback(evt):
            print("🔇 Sesi pengenalan suara dihentikan")
            self.is_listening = False
            self.recognition_done = True
        
        def canceled_callback(evt):
            print(f"❌ Pengenalan suara dibatalkan: {evt.reason}")
            self.is_listening = False
            self.recognition_done = True
        
        # Connect callbacks
        self.speech_recognizer.recognized.connect(recognition_callback)
        self.speech_recognizer.session_stopped.connect(session_stopped_callback)
        self.speech_recognizer.canceled.connect(canceled_callback)
        
        try:
            print("🎤 Mulai mendengarkan secara berkelanjutan...")
            self.is_listening = True
            self.recognition_done = False
            self.speech_recognizer.start_continuous_recognition()
            
            return True
        except Exception as e:
            print(f"❌ Error memulai pengenalan berkelanjutan: {str(e)}")
            return False
    
    def stop_continuous_recognition(self):
        """Stop continuous speech recognition"""
        try:
            if self.is_listening:
                self.speech_recognizer.stop_continuous_recognition()
                self.is_listening = False
                print("🔇 Pengenalan suara dihentikan")
        except Exception as e:
            print(f"❌ Error menghentikan pengenalan: {str(e)}")
    
    def speak_text(self, text):
        """Convert text to speech and play it"""
        try:
            print(f"🔊 Mengucapkan: {text}")
            
            # Synthesize speech
            speech_synthesis_result = self.speech_synthesizer.speak_text_async(text).get()
            
            # Check result
            if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                print("✅ Audio berhasil diputar")
                return True
            elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_synthesis_result.cancellation_details
                error_msg = f"❌ Speech synthesis dibatalkan: {cancellation_details.reason}"
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    error_msg += f"\nError details: {cancellation_details.error_details}"
                print(error_msg)
                return False
                
        except Exception as e:
            print(f"❌ Error saat mengucapkan teks: {str(e)}")
            return False
    
    def speak_text_async(self, text):
        """Convert text to speech asynchronously"""
        def speak_in_thread():
            self.speak_text(text)
        
        thread = threading.Thread(target=speak_in_thread)
        thread.daemon = True
        thread.start()
        return thread
    
    def set_language(self, language_code):
        """Change recognition language"""
        try:
            self.speech_config.speech_recognition_language = language_code
            
            # Update recognizer with new config
            self.speech_recognizer = speechsdk.SpeechRecognizer(
                speech_config=self.speech_config, 
                audio_config=self.audio_config_mic
            )
            
            print(f"🌐 Bahasa diubah ke: {language_code}")
            return True
        except Exception as e:
            print(f"❌ Error mengubah bahasa: {str(e)}")
            return False
    
    def set_voice(self, voice_name):
        """Change synthesis voice"""
        try:
            self.speech_config.speech_synthesis_voice_name = voice_name
            
            # Update synthesizer with new config
            self.speech_synthesizer = speechsdk.SpeechSynthesizer(
                speech_config=self.speech_config, 
                audio_config=self.audio_config_speaker
            )
            
            print(f"🗣️ Suara diubah ke: {voice_name}")
            return True
        except Exception as e:
            print(f"❌ Error mengubah suara: {str(e)}")
            return False
    
    def get_available_voices(self):
        """Get list of available voices (simplified list)"""
        return {
            "Indonesian": {
                "id-ID-ArdiNeural": "Ardi (Male, Indonesian)",
                "id-ID-GadisNeural": "Gadis (Female, Indonesian)"
            },
            "English": {
                "en-US-JennyNeural": "Jenny (Female, US English)",
                "en-US-GuyNeural": "Guy (Male, US English)",
                "en-US-AriaNeural": "Aria (Female, US English)",
                "en-US-DavisNeural": "Davis (Male, US English)"
            }
        }
    
    def test_speech_services(self):
        """Test both speech recognition and synthesis"""
        print("🧪 Testing Speech Services...")
        
        # Test TTS
        print("\n1. Testing Text-to-Speech:")
        success = self.speak_text("Halo! Ini adalah tes text to speech.")
        
        if success:
            print("✅ Text-to-Speech berfungsi dengan baik!")
        else:
            print("❌ Text-to-Speech mengalami masalah")
            return False
        
        # Test STT
        print("\n2. Testing Speech-to-Text:")
        print("Silakan ucapkan sesuatu...")
        
        recognized = self.recognize_speech_once()
        if recognized:
            print(f"✅ Speech-to-Text berfungsi! Terdeteksi: '{recognized}'")
            return True
        else:
            print("❌ Speech-to-Text mengalami masalah")
            return False