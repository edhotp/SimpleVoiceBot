"""
Simple Chatbot with Voice Integration
Core chatbot class menggunakan Azure OpenAI dan Azure Speech Services

Author: Edhot Purwoko - Microsoft Indonesia
License: MIT - Free to use
Disclaimer: Provided "as is" without warranty. Use at your own risk.
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from speech_service import SpeechService

class SimpleChatbot:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Initialize Azure OpenAI client
        self.client = AzureOpenAI(
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        )
        
        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
        
        # Initialize Speech Service
        try:
            self.speech_service = SpeechService()
            self.speech_enabled = True
        except Exception as e:
            print(f"⚠️ Speech service tidak tersedia: {e}")
            self.speech_service = None
            self.speech_enabled = False
        
        # Initialize conversation history
        self.conversation_history = [
            {
                "role": "system",
                "content": "You are a helpful assistant. You can answer questions and have conversations in Indonesian or English."
            }
        ]
    
    def get_response(self, user_message, stream=False):
        """Get response from Azure OpenAI"""
        # Add user message to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        try:
            if stream:
                return self._get_streaming_response()
            else:
                return self._get_regular_response()
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _get_regular_response(self):
        """Get regular (non-streaming) response"""
        response = self.client.chat.completions.create(
            messages=self.conversation_history,
            max_completion_tokens=1000,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            model=self.deployment
        )
        
        assistant_message = response.choices[0].message.content
        
        # Add assistant response to conversation history
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def _get_streaming_response(self):
        """Get streaming response (generator)"""
        response = self.client.chat.completions.create(
            stream=True,
            messages=self.conversation_history,
            max_completion_tokens=1000,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            model=self.deployment,
        )
        
        full_response = ""
        for update in response:
            if update.choices and update.choices[0].delta.content:
                chunk = update.choices[0].delta.content
                full_response += chunk
                yield chunk
        
        # Add complete response to conversation history
        self.conversation_history.append({
            "role": "assistant",
            "content": full_response
        })
    
    def clear_history(self):
        """Clear conversation history except system message"""
        self.conversation_history = [self.conversation_history[0]]  # Keep only system message
    
    def get_conversation_history(self):
        """Get current conversation history"""
        return self.conversation_history
    
    def voice_chat(self, speak_response=True):
        """Voice chat mode - listen from microphone and optionally speak response"""
        if not self.speech_enabled:
            return "Speech service tidak tersedia. Pastikan Azure Speech service sudah dikonfigurasi."
        
        try:
            # Listen for speech input
            print("🎤 Mendengarkan input suara...")
            user_speech = self.speech_service.recognize_speech_once()
            
            if not user_speech:
                return None
            
            # Get response from chatbot
            bot_response = self.get_response(user_speech, stream=False)
            
            # Speak the response if requested
            if speak_response and bot_response:
                print("🔊 Mengucapkan respons...")
                self.speech_service.speak_text(bot_response)
            
            return {
                "user_input": user_speech,
                "bot_response": bot_response
            }
            
        except Exception as e:
            error_msg = f"Error dalam voice chat: {str(e)}"
            print(f"❌ {error_msg}")
            return error_msg
    
    def listen_for_input(self):
        """Listen for speech input and return text"""
        if not self.speech_enabled:
            return None
        
        return self.speech_service.recognize_speech_once()
    
    def speak_response(self, text):
        """Speak the given text"""
        if not self.speech_enabled:
            return False
        
        return self.speech_service.speak_text(text)
    
    def set_speech_language(self, language_code):
        """Set speech recognition language"""
        if not self.speech_enabled:
            return False
        
        return self.speech_service.set_language(language_code)
    
    def set_speech_voice(self, voice_name):
        """Set speech synthesis voice"""
        if not self.speech_enabled:
            return False
        
        return self.speech_service.set_voice(voice_name)
    
    def get_available_voices(self):
        """Get available speech voices"""
        if not self.speech_enabled:
            return {}
        
        return self.speech_service.get_available_voices()
    
    def test_speech_services(self):
        """Test speech services"""
        if not self.speech_enabled:
            return False
        
        return self.speech_service.test_speech_services()