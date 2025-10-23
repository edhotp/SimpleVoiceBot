#!/usr/bin/env python3
"""
Text-to-Speech Chatbot CLI
Chatbot yang menerima input text dan merespons dengan suara
"""

import os
from dotenv import load_dotenv
from chatbot import SimpleChatbot

def main():
    """Main function untuk Text-to-Speech chatbot CLI"""
    # Load environment variables
    load_dotenv()
    
    # Inisialisasi chatbot
    print("🤖 Initializing Text-to-Speech Chatbot...")
    bot = SimpleChatbot()
    
    if not bot.speech_enabled:
        print("❌ Speech services tidak tersedia!")
        print("Pastikan Azure Speech Service sudah dikonfigurasi dengan benar.")
        return
    
    print("✅ Text-to-Speech Chatbot siap!")
    print("💡 Ketik pesan Anda, dan bot akan merespons dengan suara")
    print("💡 Ketik 'quit', 'exit', atau 'bye' untuk keluar")
    print("💡 Ketik 'clear' untuk menghapus history percakapan")
    print("-" * 50)
    
    try:
        while True:
            # Input text dari user
            user_input = input("\n👤 Anda: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'keluar']:
                print("👋 Terima kasih! Sampai jumpa!")
                break
            
            # Check for clear command
            if user_input.lower() in ['clear', 'hapus']:
                bot.clear_history()
                print("✅ History percakapan telah dihapus!")
                continue
            
            # Skip empty input
            if not user_input:
                continue
            
            try:
                print("🤖 Menggenerate respons...")
                
                # Get text response
                response = bot.get_response(user_input, stream=False)
                
                if response:
                    print(f"🤖 Bot: {response}")
                    
                    # Speak the response
                    print("🔊 Berbicara...")
                    success = bot.speak_response(response)
                    
                    if success:
                        print("✅ Respons telah diucapkan!")
                    else:
                        print("❌ Gagal mengucapkan respons")
                else:
                    print("❌ Tidak mendapat respons dari bot")
                    
            except KeyboardInterrupt:
                print("\n⏸️  Proses dihentikan oleh user")
                continue
            except Exception as e:
                print(f"❌ Error: {e}")
                continue
                
    except KeyboardInterrupt:
        print("\n👋 Program dihentikan. Sampai jumpa!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()