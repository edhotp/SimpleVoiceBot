#!/usr/bin/env python3
"""
Voice Chatbot CLI Application
Aplikasi chatbot dengan fitur voice menggunakan Azure OpenAI dan Azure Speech

Author: Edhot Purwoko - Microsoft Indonesia
License: MIT - Free to use
Disclaimer: Provided "as is" without warranty. Use at your own risk.
"""

from chatbot import SimpleChatbot
import sys

def main():
    print("=" * 60)
    print("🎤 Selamat datang di Voice Chatbot!")
    print("💬 Powered by Azure OpenAI + Azure Speech")
    print("=" * 60)
    print("Perintah yang tersedia:")
    print("• 'voice' - Mode voice chat (bicara dan dengar)")
    print("• 'listen' - Hanya dengarkan input suara")
    print("• 'speak <text>' - Ucapkan teks")
    print("• 'test' - Test speech services")
    print("• 'language <code>' - Ubah bahasa (id-ID, en-US)")
    print("• 'voice-list' - Lihat daftar suara tersedia")
    print("• 'voice-set <name>' - Ubah suara")
    print("• 'clear' - Hapus riwayat percakapan")
    print("• 'quit', 'exit', 'keluar' - Keluar dari aplikasi")
    print("-" * 60)
    
    # Initialize chatbot
    try:
        bot = SimpleChatbot()
        print("✅ Chatbot berhasil diinisialisasi!")
        
        if bot.speech_enabled:
            print("🎤 Speech services aktif!")
        else:
            print("⚠️ Speech services tidak tersedia - hanya mode teks")
            
    except Exception as e:
        print(f"❌ Error saat menginisialisasi chatbot: {e}")
        return

    while True:
        try:
            # Get user input
            user_input = input("\n👤 Anda: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'keluar', 'q']:
                print("\n👋 Terima kasih telah menggunakan voice chatbot! Sampai jumpa!")
                break
            
            # Check for clear command
            if user_input.lower() == 'clear':
                bot.clear_history()
                print("🗑️ Riwayat percakapan telah dihapus!")
                continue
            
            # Voice chat mode
            if user_input.lower() == 'voice':
                if not bot.speech_enabled:
                    print("❌ Speech services tidak tersedia")
                    continue
                
                print("\n🎤 Mode Voice Chat - Silakan berbicara!")
                result = bot.voice_chat(speak_response=True)
                
                if result and isinstance(result, dict):
                    print(f"👤 Anda: {result['user_input']}")
                    print(f"🤖 Bot: {result['bot_response']}")
                elif result:
                    print(f"❌ {result}")
                continue
            
            # Listen only mode
            if user_input.lower() == 'listen':
                if not bot.speech_enabled:
                    print("❌ Speech services tidak tersedia")
                    continue
                
                print("🎤 Mendengarkan...")
                speech_text = bot.listen_for_input()
                if speech_text:
                    print(f"👤 Terdeteksi: {speech_text}")
                    # Get response normally
                    response = bot.get_response(speech_text, stream=False)
                    print(f"🤖 Bot: {response}")
                continue
            
            # Speak text command
            if user_input.lower().startswith('speak '):
                if not bot.speech_enabled:
                    print("❌ Speech services tidak tersedia")
                    continue
                
                text_to_speak = user_input[6:]  # Remove 'speak ' prefix
                if text_to_speak:
                    success = bot.speak_response(text_to_speak)
                    if success:
                        print(f"🔊 Mengucapkan: {text_to_speak}")
                    else:
                        print("❌ Gagal mengucapkan teks")
                else:
                    print("⚠️ Silakan masukkan teks yang ingin diucapkan")
                continue
            
            # Test speech services
            if user_input.lower() == 'test':
                if not bot.speech_enabled:
                    print("❌ Speech services tidak tersedia")
                    continue
                
                print("🧪 Testing speech services...")
                success = bot.test_speech_services()
                if success:
                    print("✅ Semua speech services berfungsi dengan baik!")
                else:
                    print("❌ Ada masalah dengan speech services")
                continue
            
            # Change language
            if user_input.lower().startswith('language '):
                if not bot.speech_enabled:
                    print("❌ Speech services tidak tersedia")
                    continue
                
                lang_code = user_input[9:]  # Remove 'language ' prefix
                if lang_code:
                    success = bot.set_speech_language(lang_code)
                    if success:
                        print(f"🌐 Bahasa diubah ke: {lang_code}")
                    else:
                        print(f"❌ Gagal mengubah bahasa ke: {lang_code}")
                else:
                    print("⚠️ Contoh: language id-ID atau language en-US")
                continue
            
            # List available voices
            if user_input.lower() == 'voice-list':
                if not bot.speech_enabled:
                    print("❌ Speech services tidak tersedia")
                    continue
                
                voices = bot.get_available_voices()
                print("🗣️ Daftar suara tersedia:")
                for language, voice_list in voices.items():
                    print(f"\n{language}:")
                    for voice_code, voice_name in voice_list.items():
                        print(f"  • {voice_code}: {voice_name}")
                continue
            
            # Set voice
            if user_input.lower().startswith('voice-set '):
                if not bot.speech_enabled:
                    print("❌ Speech services tidak tersedia")
                    continue
                
                voice_name = user_input[10:]  # Remove 'voice-set ' prefix
                if voice_name:
                    success = bot.set_speech_voice(voice_name)
                    if success:
                        print(f"🗣️ Suara diubah ke: {voice_name}")
                    else:
                        print(f"❌ Gagal mengubah suara ke: {voice_name}")
                else:
                    print("⚠️ Contoh: voice-set id-ID-ArdiNeural")
                continue
            
            # Skip empty input
            if not user_input:
                print("⚠️ Silakan masukkan pesan Anda.")
                continue
            
            # Regular text chat
            print("\n🤖 Bot: ", end="")
            response = bot.get_response(user_input, stream=False)
            print(response)
                
        except KeyboardInterrupt:
            print("\n\n👋 Program dihentikan. Sampai jumpa!")
            break
        except Exception as e:
            print(f"\n❌ Terjadi error: {e}")
            print("Silakan coba lagi.")

if __name__ == "__main__":
    main()