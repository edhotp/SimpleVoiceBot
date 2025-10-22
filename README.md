# Simple Chatbot dengan Azure OpenAI

Aplikasi chatbot sederhana yang menggunakan Azure OpenAI API untuk memberikan respons yang cerdas dan natural.

## Fitur

- 💬 **Chat CLI**: Antarmuka command line untuk berinteraksi dengan chatbot
- 🌐 **Web Interface**: Antarmuka web yang user-friendly dengan Flask
- 🎤 **Voice Input**: Speech-to-Text menggunakan Azure Speech Service
- 🔊 **Voice Output**: Text-to-Speech dengan suara natural
- 🗣️ **Voice Chat**: Mode percakapan suara penuh (bicara & dengar)
- 🌍 **Multi-Language**: Mendukung Indonesia dan English
- 🔄 **Streaming Response**: Mendukung respons streaming untuk pengalaman yang lebih baik
- 📝 **Memory**: Menyimpan riwayat percakapan selama sesi berlangsung
- 🗑️ **Clear History**: Fitur untuk menghapus riwayat percakapan

## Persyaratan

- Python 3.8+
- Azure OpenAI API Key dan Endpoint
- Akses internet

## Instalasi

1. **Clone atau download project ini**
2. **Buat virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Konfigurasi environment variables:**
   - Edit file `.env` dan sesuaikan dengan kredensial Azure OpenAI Anda
   - Pastikan endpoint dan API key sudah benar

## Penggunaan

### 1. CLI Chatbot (Text Only)
Jalankan chatbot dalam mode command line:
```bash
python main.py
```

**Perintah yang tersedia:**
- `quit`, `exit`, `keluar` - Keluar dari aplikasi
- `clear` - Hapus riwayat percakapan
- `stream` - Toggle streaming mode

### 2. Voice Chatbot CLI
Jalankan chatbot dengan fitur voice:
```bash
python voice_main.py
# atau
run_voice.bat
```

**Perintah voice yang tersedia:**
- `voice` - Mode voice chat penuh (bicara dan dengar)
- `listen` - Hanya dengarkan input suara
- `speak <text>` - Ucapkan teks
- `test` - Test speech services
- `language <code>` - Ubah bahasa (id-ID, en-US)
- `voice-list` - Lihat daftar suara tersedia
- `voice-set <name>` - Ubah suara TTS
- `clear` - Hapus riwayat percakapan
- `quit`, `exit`, `keluar` - Keluar dari aplikasi

### 3. Web Chatbot (dengan Voice Features)
Jalankan chatbot dalam mode web:
```bash
python web_app.py
# atau
run_web.bat
```

Kemudian buka browser dan akses: `http://localhost:5000`

**Fitur web voice:**
- 🎤 **Voice Chat** - Bicara langsung ke chatbot
- 👂 **Listen** - Input suara ke text box
- 🔊 **Speak** - Ucapkan teks yang ada di input
- 🧪 **Test Voice** - Test speech services

## Struktur Project

```
45.SampleVoicebot/
├── main.py              # CLI chatbot application (text only)
├── voice_main.py        # Voice chatbot CLI application
├── web_app.py           # Web chatbot application (Flask) with voice
├── chatbot.py           # Core chatbot class
├── speech_service.py    # Azure Speech service integration
├── demo.py              # Demo script untuk semua fitur
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (jangan di-commit ke git)
├── run_cli.bat          # Script untuk menjalankan CLI text chatbot
├── run_voice.bat        # Script untuk menjalankan voice CLI chatbot
├── run_web.bat          # Script untuk menjalankan web chatbot
├── README.md           # Dokumentasi ini
└── templates/
    └── index.html      # HTML template untuk web interface with voice
```

## Konfigurasi

File `.env` berisi konfigurasi untuk Azure OpenAI dan Azure Speech:

```env
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4.1-mini

# Azure Speech Configuration
AZURE_SPEECH_KEY=your-speech-key-here
AZURE_SPEECH_REGION=your-region
AZURE_SPEECH_ENDPOINT=https://your-speech-endpoint.cognitiveservices.azure.com/
```

### Voice Configuration Options

**Bahasa yang Didukung:**
- `id-ID` - Bahasa Indonesia
- `en-US` - English (US)
- `en-GB` - English (UK)

**Suara Indonesia yang Tersedia:**
- `id-ID-ArdiNeural` - Suara laki-laki Indonesia
- `id-ID-GadisNeural` - Suara perempuan Indonesia

**Suara English yang Tersedia:**
- `en-US-JennyNeural` - Suara perempuan Amerika
- `en-US-GuyNeural` - Suara laki-laki Amerika
- `en-US-AriaNeural` - Suara perempuan Amerika
- `en-US-DavisNeural` - Suara laki-laki Amerika

## Keamanan

⚠️ **Penting**: 
- Jangan commit file `.env` ke repository
- Pastikan API key Anda aman dan tidak dibagikan
- Gunakan environment variables di production

## Troubleshooting

### Error: "Module not found"
Pastikan virtual environment sudah diaktifkan dan dependencies sudah diinstall:
```bash
pip install -r requirements.txt
```

### Error: "Authentication failed"
Periksa kembali:
- API Key di file `.env`
- Endpoint URL
- Deployment name

### Error: "Connection timeout"
Periksa koneksi internet dan pastikan endpoint Azure OpenAI dapat diakses.

## Demo & Testing

Untuk mencoba semua fitur sekaligus:
```bash
python demo.py
```

Demo script akan menunjukkan:
- ✅ Text chatting
- ✅ Text-to-Speech functionality  
- ✅ Voice changing capabilities
- ✅ Interactive voice conversation simulation

## Voice Features

### Speech-to-Text (STT)
- 🎤 Real-time speech recognition
- 🌍 Multi-language support (Indonesian, English)
- 🔄 Continuous listening mode
- 📝 One-time speech recognition

### Text-to-Speech (TTS)
- 🔊 Natural sounding voices
- 🗣️ Multiple voice options per language
- ⚡ Fast audio generation
- 🎛️ Configurable voice settings

### Voice Chat Features
- 🗨️ Full duplex voice conversation
- 🎯 Voice command recognition
- 🔄 Seamless voice-to-text-to-voice flow
- 🧪 Built-in voice service testing

## API Endpoints (Web)

Voice-related endpoints yang tersedia:

- `POST /voice/chat` - Full voice chat (listen + respond with voice)
- `POST /voice/listen` - Speech-to-text only
- `POST /voice/speak` - Text-to-speech only
- `POST /voice/test` - Test voice services
- `GET /voice/voices` - Get available voices
- `POST /voice/set-voice` - Change TTS voice
- `POST /voice/set-language` - Change STT language
- `GET /voice/status` - Check voice service status

## Pengembangan Lebih Lanjut

Fitur yang sudah tersedia:
- ✅ Speech-to-Text (Azure Speech)
- ✅ Text-to-Speech (Azure Speech)
- ✅ Voice Chat Mode
- ✅ Multi-language support
- ✅ Multiple voice options
- ✅ Web and CLI interfaces

Beberapa fitur yang bisa ditambahkan:
- 💾 Persistent storage untuk riwayat chat
- 🔐 User authentication
- 🎨 Customizable UI themes
- 📱 Mobile app integration
- 📊 Analytics dan logging
- �️ Advanced voice settings (speed, pitch)
- 🔀 Voice translation capabilities

## Lisensi

Project ini dibuat untuk tujuan pembelajaran dan dapat digunakan secara bebas.

---

## 👨‍💻 Author

**Dibuat oleh: Edhot Purwoko**  
📧 Microsoft Indonesia  
🚀 Solutions Architect & AI Enthusiast

---

## 📄 License & Disclaimer

**License**: MIT - Kode ini dapat digunakan secara bebas untuk tujuan pembelajaran dan pengembangan.

**Disclaimer**: 
⚠️ **PENTING**: Kode ini disediakan "sebagaimana adanya" tanpa jaminan atau garansi apapun. Penulis dan Microsoft Indonesia tidak bertanggung jawab atas segala kerusakan, kehilangan data, atau masalah lainnya yang mungkin timbul dari penggunaan kode ini.

**Penggunaan Risiko Sendiri**: 
- Pastikan untuk menguji secara menyeluruh sebelum digunakan dalam lingkungan produksi
- Selalu backup data Anda sebelum menggunakan aplikasi ini
- Gunakan API key dan kredensial dengan aman
- Ikuti best practices keamanan Azure

---

**Dibuat dengan ❤️ menggunakan Azure OpenAI & Azure Speech Services**