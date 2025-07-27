<img width="1918" height="871" alt="image" src="https://github.com/user-attachments/assets/6b655312-aac7-420d-90aa-ee6e0e1a9270" /># PDF Compressor Web Application

A modern, responsive web application for compressing PDF files using multiple compression methods.

## 🌟 Features

- **Beautiful Web Interface**: Modern, responsive design with drag-and-drop functionality
- **Multiple Compression Methods**: Choose between Ghostscript and PyPDF2
- **Quality Control**: Adjustable compression levels for optimal file size vs quality balance
- **Large File Support**: Handle files up to 50MB
- **Secure Processing**: Automatic file cleanup and secure handling
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📷 Features

- **Main Interface
<img width="1918" height="871" alt="image" src="https://github.com/user-attachments/assets/465c4c0a-4f46-48c7-b01e-365398310a5e" />

-**File Uploaded
<img width="1919" height="868" alt="image" src="https://github.com/user-attachments/assets/df3ff1ec-c8b6-4598-b521-bcd47803091f" />

-**Success
<img width="1907" height="860" alt="image" src="https://github.com/user-attachments/assets/31e6850c-534c-4d9b-b7ce-24b24d4bf49a" />

## 🛠️ Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Ghostscript** (for advanced compression):
   - Ubuntu/Debian: `sudo apt-get install ghostscript`
   - macOS: `brew install ghostscript`
   - Windows: Download from [ghostscript.com](https://www.ghostscript.com/download.html)

3. **Run the application**:
   ```bash
   python src/main.py
   ```

4. **Open your browser** and go to `http://localhost:5000`

## 📋 Compression Methods

### Ghostscript (Recommended)
- **Screen**: Lowest quality, smallest file size (72 dpi)
- **E-book**: Balanced quality for screen viewing (150 dpi)
- **Printer**: High quality for printing (300 dpi)
- **Prepress**: Highest quality for commercial printing

### PyPDF2
- Basic optimization and stream compression
- Good for simple PDF cleanup

## 🏗️ Project Structure

```
src/
├── main.py              # Flask application entry point
├── routes/
│   └── pdf_compress.py  # PDF compression API
├── static/
│   └── index.html       # Web interface
└── models/              # Database models (if needed)
```

## 🔧 Configuration

The application can be configured through environment variables:

- `PORT`: Server port (default: 5000)
- `SECRET_KEY`: Flask secret key
- `MAX_CONTENT_LENGTH`: Maximum upload size (default: 50MB)

## 📚 API Documentation

### POST /api/pdf/compress
Upload and compress a PDF file.

**Parameters:**
- `file`: PDF file (required)
- `method`: `ghostscript` or `pypdf2` (default: ghostscript)
- `quality`: `screen`, `ebook`, `printer`, or `prepress` (default: ebook)

### GET /api/pdf/info
Get available compression methods and quality levels.

## 🚀 Deployment

See `DEPLOYMENT_GUIDE.md` for detailed deployment instructions including:
- Local development setup
- Cloud platform deployment (Heroku, Railway, Render)
- VPS/Server deployment with Gunicorn and Nginx
- Security considerations

## 📦 Dependencies

- Flask 3.1.1
- Flask-CORS 6.0.0
- PyPDF2 3.0.1
- Ghostscript (system dependency)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🐛 Issues

If you encounter any issues:
1. Check that Ghostscript is properly installed
2. Verify all Python dependencies are installed
3. Ensure file permissions are correct
4. Check the application logs for detailed error messages

---

Built with ❤️ using Flask and modern web technologies.

