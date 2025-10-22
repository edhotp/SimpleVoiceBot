#!/usr/bin/env python3
"""
Demo Script untuk Voice Chatbot
Menunjukkan semua fitur yang tersedia

Author: Edhot Purwoko - Microsoft Indonesia
License: MIT - Free to use
Disclaimer: Provided "as is" without warranty. Use at your own risk.
"""

from chatbot import SimpleChatbot
import time

def demo_text_chat(bot):
    """Demo text chatting"""
    print("\n" + "="*50)
    print("🔤 DEMO: Text Chat")
    print("="*50)
    
    # Test text chat
    test_questions = [
        "Halo, siapa nama kamu?",
        "Jelaskan tentang Indonesia",
        "What can you do?"
    ]
    
    for question in test_questions:
        print(f"\n👤 User: {question}")
        response = bot.get_response(question, stream=False)
        print(f"🤖 Bot: {response}")
        time.sleep(1)

def demo_speech_features(bot):
    """Demo speech features"""
    print("\n" + "="*50)
    print("🎤 DEMO: Speech Features")
    print("="*50)
    
    if not bot.speech_enabled:
        print("❌ Speech services tidak tersedia")
        return
    
    # Test TTS
    print("\n1. Testing Text-to-Speech:")
    test_text = "Halo! Ini adalah demo text to speech menggunakan Azure Speech Service."
    print(f"🔊 Mengucapkan: {test_text}")
    success = bot.speak_response(test_text)
    
    if success:
        print("✅ TTS berhasil!")
    else:
        print("❌ TTS gagal")
    
    time.sleep(2)
    
    # Show available voices
    print("\n2. Available Voices:")
    voices = bot.get_available_voices()
    for language, voice_list in voices.items():
        print(f"\n{language}:")
        for voice_code, voice_name in voice_list.items():
            print(f"  • {voice_code}: {voice_name}")
    
    # Test voice change
    print("\n3. Testing Voice Change:")
    print("🗣️ Mengubah ke suara perempuan Indonesia...")
    success = bot.set_speech_voice("id-ID-GadisNeural")
    if success:
        bot.speak_response("Halo, sekarang saya menggunakan suara perempuan.")
    
    time.sleep(2)
    
    # Change back to male voice
    print("🗣️ Mengubah kembali ke suara laki-laki...")
    bot.set_speech_voice("id-ID-ArdiNeural")
    bot.speak_response("Dan sekarang kembali ke suara laki-laki.")

def demo_voice_interaction(bot):
    """Demo interactive voice chat"""
    print("\n" + "="*50)
    print("🗣️ DEMO: Voice Interaction")
    print("="*50)
    
    if not bot.speech_enabled:
        print("❌ Speech services tidak tersedia")
        return
    
    print("🎤 Demo voice interaction akan dimulai...")
    print("Anda bisa berbicara setelah mendengar bunyi 'beep'")
    
    # Simulate voice conversation
    bot.speak_response("Halo! Saya siap untuk demo voice chat. Silakan berbicara setelah bunyi ini.")
    
    print("\n📝 Untuk demo ini, kita akan simulasikan voice input...")
    
    # Simulate some voice interactions
    simulated_inputs = [
        "Bagaimana cuaca hari ini?",
        "Ceritakan tentang teknologi AI",
        "Terima kasih!"
    ]
    
    for i, input_text in enumerate(simulated_inputs, 1):
        print(f"\n--- Voice Interaction {i} ---")
        print(f"👤 [Simulated Voice Input]: {input_text}")
        
        # Get bot response
        response = bot.get_response(input_text, stream=False)
        print(f"🤖 Bot Response: {response}")
        
        # Speak the response
        print("🔊 Bot mengucapkan respons...")
        bot.speak_response(response)
        
        time.sleep(2)

def main():
    """Main demo function"""
    print("🎭 DEMO: Voice Chatbot Features")
    print("Demonstrasi semua fitur chatbot dengan Azure OpenAI dan Azure Speech")
    print("=" * 70)
    
    try:
        # Initialize chatbot
        print("🚀 Menginisialisasi chatbot...")
        bot = SimpleChatbot()
        
        print("✅ Chatbot berhasil diinisialisasi!")
        
        if bot.speech_enabled:
            print("🎤 Speech services tersedia!")
        else:
            print("⚠️ Speech services tidak tersedia - demo terbatas pada text saja")
        
        # Demo 1: Text Chat
        demo_text_chat(bot)
        
        # Demo 2: Speech Features (if available)
        if bot.speech_enabled:
            demo_speech_features(bot)
            
            # Ask user if they want to try voice interaction
            print("\n" + "="*50)
            user_choice = input("🎤 Ingin mencoba voice interaction demo? (y/n): ").lower()
            if user_choice in ['y', 'yes', 'ya']:
                demo_voice_interaction(bot)
        
        print("\n" + "="*70)
        print("🎉 Demo selesai! Terima kasih telah mencoba Voice Chatbot!")
        print("🚀 Untuk penggunaan penuh, jalankan:")
        print("   • python voice_main.py (CLI dengan voice)")
        print("   • python web_app.py (Web interface dengan voice)")
        print("=" * 70)
        
    except Exception as e:
        print(f"❌ Error dalam demo: {e}")
        print("Pastikan Azure OpenAI dan Speech services sudah dikonfigurasi dengan benar.")

if __name__ == "__main__":
    main()