# 📚 CurricuForge

**AI-Powered Personalized Curriculum Generator** - Create tailored learning pathways using artificial intelligence.

## Overview

CurricuForge is a web application that generates personalized curricula based on:
- **Learning Topic**: What you want to learn
- **Skill Level**: Your current proficiency (Beginner, Intermediate, Advanced)
- **Duration**: Program length in weeks
- **Learning Style**: How you prefer to learn (Visual, Auditory, Kinesthetic, Reading/Writing)

The application uses AI models (Google Gemini, HuggingFace) to generate comprehensive, personalized learning plans tailored to your preferences.

## Project Structure

```
CurricuForge/
├── backend/                    # FastAPI Application
│   ├── main.py                # Entry point & API routes
│   ├── ai_engine.py           # AI logic for HuggingFace & Gemini
│   ├── requirements.txt       # Python dependencies
│   └── .env                   # API Keys (keep private)
│
├── frontend/                  # Web Interface
│   ├── index.html            # UI structure & layout
│   ├── style.css             # Academic-themed styling
│   └── script.js             # API integration & DOM manipulation
│
└── README.md                 # This file
```

## Features

✨ **AI-Powered Generation**
- Integrates with Google Gemini and HuggingFace APIs
- Fallback template generator if APIs unavailable

🎯 **Personalization**
- Customizable learning levels
- Multiple learning style options
- Flexible program duration

📱 **Responsive Design**
- Works on desktop, tablet, and mobile
- Academic-themed UI with smooth animations
- Accessibility-focused design

🔒 **Secure**
- API keys stored in `.env` file (not committed to version control)
- CORS enabled for safe frontend-backend communication

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js (optional, for serving frontend locally)
- Git

### Installation

#### 1. Clone the Repository

```bash
git clone <repository-url>
cd CurricuForge
```

#### 2. Setup Backend

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Configure API Keys

Edit `backend/.env` with your API keys:

```env
GEMINI_API_KEY=your_gemini_key_here
HUGGINGFACE_API_KEY=your_huggingface_key_here
IBM_API_KEY=your_ibm_key_here
```

**How to get API keys:**

- **Google Gemini**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- **HuggingFace**: Sign up at [HuggingFace](https://huggingface.co) and create a token

#### 4. Start Backend Server

```bash
cd backend
python main.py
```

Server runs at `http://localhost:8000`

#### 5. Open Frontend

Open `frontend/index.html` in your browser or serve it:

```bash
# Using Python
cd frontend
python -m http.server 8001

# Using Node.js (if installed)
npx http-server frontend -p 8001
```

Then navigate to `http://localhost:8001`

## API Documentation

### Endpoints

#### `POST /generate-curriculum`

Generate a personalized curriculum.

**Request:**
```json
{
  "topic": "Machine Learning",
  "level": "beginner",
  "duration_weeks": 12,
  "learning_style": "visual"
}
```

**Response:**
```json
{
  "curriculum": "# Machine Learning Curriculum...",
  "status": "success"
}
```

#### `GET /health`

Check API health status.

**Response:**
```json
{
  "status": "healthy",
  "service": "CurricuForge API"
}
```

#### `GET /`

Welcome endpoint.

**Response:**
```json
{
  "message": "CurricuForge API is running"
}
```

## Usage

1. **Open the web interface** in your browser
2. **Fill in the form** with your learning details:
   - Topic you want to learn
   - Your skill level
   - Program duration in weeks
   - Your preferred learning style
3. **Click "Generate Curriculum"**
4. **Review your personalized curriculum**
5. **Export or print** if needed

## Technologies Used

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI web server
- **Pydantic** - Data validation
- **Google Generative AI** - Gemini integration
- **HuggingFace Hub** - Model access

### Frontend
- **HTML5** - Structure
- **CSS3** - Modern styling with gradients and animations
- **JavaScript (Vanilla)** - DOM manipulation and API calls
- **Fetch API** - HTTP requests

## Environment Setup

### Development

```bash
# Backend with auto-reload
uvicorn backend.main:app --reload

# Frontend with live server
npx live-server frontend/
```

### Production

Update `main.py` server configuration:

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Troubleshooting

### Backend not connecting
- Ensure backend is running: `http://localhost:8000/health`
- Check CORS settings in `main.py`
- Verify frontend API_BASE_URL in `script.js`

### API key errors
- Verify `.env` file has correct keys
- Check API key is active in service provider dashboard
- Try fallback template by not providing API keys

### Module not found errors
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Future Enhancements

- 📊 Progress tracking dashboard
- 💾 Save and manage multiple curricula
- 👥 Community sharing features
- 📱 Mobile app version
- 🎓 Integration with learning platforms
- 📈 AI-powered progress assessment
- 🌍 Multi-language support

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: support@curricuforge.com

## Acknowledgments

- Google Generative AI (Gemini)
- HuggingFace Community
- FastAPI Documentation
- Open-source contributors

---

**Made with ❤️ for Learners Everywhere**

Last Updated: February 2024
