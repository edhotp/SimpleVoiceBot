# Contributing to Voice Chatbot

## 👨‍💻 Author & Maintainer
**Edhot Purwoko**  
Microsoft Indonesia  
Solutions Architect & AI Enthusiast  

## 🤝 Contributing Guidelines

Terima kasih atas minat Anda untuk berkontribusi pada project Voice Chatbot ini! 

### How to Contribute

1. **Fork** repository ini
2. **Create** branch baru untuk fitur/perbaikan Anda:
   ```bash
   git checkout -b feature/nama-fitur-anda
   ```
3. **Make** perubahan yang diperlukan
4. **Test** perubahan Anda secara menyeluruh
5. **Commit** perubahan dengan pesan yang jelas:
   ```bash
   git commit -m "Add: fitur baru untuk xyz"
   ```
6. **Push** ke branch Anda:
   ```bash
   git push origin feature/nama-fitur-anda
   ```
7. **Create** Pull Request

### 📋 Contribution Areas

Kami menyambut kontribusi dalam berbagai area:

- 🐛 **Bug fixes**
- ✨ **New features** 
- 📚 **Documentation improvements**
- 🎨 **UI/UX enhancements**
- 🔧 **Performance optimizations**
- 🧪 **Testing improvements**
- 🌍 **Localization/translation**

### 🎯 Priority Areas

1. **Voice Quality Improvements**
   - Better noise cancellation
   - Multi-language voice support
   - Voice emotion detection

2. **Security Enhancements**
   - Better API key management
   - Input validation
   - Rate limiting

3. **User Experience**
   - Better error handling
   - Mobile responsiveness
   - Accessibility features

### 📝 Code Standards

- Follow **PEP 8** untuk Python code
- Add **docstrings** untuk functions dan classes
- Include **type hints** where appropriate
- Write **clear commit messages**
- Add **comments** untuk complex logic

### 🧪 Testing

- Test fitur baru secara menyeluruh
- Pastikan existing tests masih pass
- Add tests untuk fitur baru jika memungkinkan
- Test di berbagai browser untuk web interface

### 📖 Documentation

- Update README.md jika ada perubahan usage
- Add docstrings untuk new functions
- Include examples untuk fitur baru
- Update comments jika ada perubahan logic

### ⚠️ Important Notes

- **Security**: Jangan commit API keys atau credentials
- **Dependencies**: Hati-hati menambah dependencies baru
- **Compatibility**: Pastikan compatible dengan existing code
- **Performance**: Perhatikan impact terhadap performance

### 🚀 Development Setup

1. Clone repository:
   ```bash
   git clone <repository-url>
   cd SampleVoicebot
   ```

2. Setup virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Setup environment variables:
   ```bash
   cp .env.example .env
   # Edit .env dengan credentials Anda
   ```

5. Test installation:
   ```bash
   python demo.py
   ```

### 📞 Contact

Jika ada pertanyaan atau butuh bantuan:
- Create **GitHub Issue** untuk bug reports atau feature requests
- Mention **@edhot** dalam pull requests
- Email untuk pertanyaan private

### 🙏 Recognition

All contributors akan diakui dalam:
- README.md contributors section
- Release notes
- Project documentation

---

**Happy Contributing!** 🚀

*Remember: Code with ❤️, test with 🧪, and document with 📚*