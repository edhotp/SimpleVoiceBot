#!/usr/bin/env python3
"""
Simple Chatbot CLI Application
Aplikasi chatbot sederhana menggunakan Azure OpenAI

Author: Edhot Purwoko - Microsoft Indonesia
License: MIT - Free to use
Disclaimer: Provided "as is" without warranty. Use at your own risk.
"""

from chatbot import SimpleChatbot

def main():
    print("=" * 50)
    print("🤖 Selamat datang di Simple Chatbot!")
    print("💬 Powered by Azure OpenAI")
    print("=" * 50)
    print("Ketik 'quit', 'exit', atau 'keluar' untuk mengakhiri percakapan")
    print("Ketik 'clear' untuk menghapus riwayat percakapan")
    print("Ketik 'stream' untuk toggle streaming mode")
    print("-" * 50)
    
    # Initialize chatbot
    try:
        bot = SimpleChatbot()
        print("✅ Chatbot berhasil diinisialisasi!")
    except Exception as e:
        print(f"❌ Error saat menginisialisasi chatbot: {e}")
        return
    
    streaming_mode = False
    
    while True:
        try:
            # Get user input
            user_input = input("\n👤 Anda: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'keluar', 'q']:
                print("\n👋 Terima kasih telah menggunakan chatbot! Sampai jumpa!")
                break
            
            # Check for clear command
            if user_input.lower() == 'clear':
                bot.clear_history()
                print("🗑️ Riwayat percakapan telah dihapus!")
                continue
            
            # Check for stream toggle
            if user_input.lower() == 'stream':
                streaming_mode = not streaming_mode
                status = "ON" if streaming_mode else "OFF"
                print(f"🔄 Streaming mode: {status}")
                continue
            
            # Skip empty input
            if not user_input:
                print("⚠️ Silakan masukkan pesan Anda.")
                continue
            
            print("\n🤖 Bot: ", end="")
            
            if streaming_mode:
                # Streaming response
                for chunk in bot.get_response(user_input, stream=True):
                    print(chunk, end="", flush=True)
                print()  # New line after streaming
            else:
                # Regular response
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