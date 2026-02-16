import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Try to import required libraries
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

try:
    from huggingface_hub import InferenceApi
    HUGGINGFACE_AVAILABLE = True
except ImportError:
    HUGGINGFACE_AVAILABLE = False

def generate_curriculum(topic: str, level: str, duration_weeks: int, learning_style: str) -> str:
    """
    Generate a personalized curriculum using Gemini or HuggingFace AI models.
    
    Args:
        topic: Subject or topic to learn
        level: Learning level (beginner, intermediate, advanced)
        duration_weeks: Total duration in weeks
        learning_style: Preferred learning style
    
    Returns:
        Generated curriculum as string
    """
    
    # Create the prompt
    prompt = f"""Create a comprehensive {duration_weeks}-week curriculum for learning {topic}.
    
    Student Level: {level}
    Learning Style: {learning_style}
    
    Please structure the curriculum as follows:
    1. Learning Objectives
    2. Weekly Breakdown (with topics, resources, and exercises)
    3. Assessment Methods
    4. Recommended Resources
    5. Tips for {learning_style} learners
    
    Make it engaging and tailored to a {learning_style} learning style."""
    
    # Try Gemini first
    if GEMINI_AVAILABLE:
        try:
            api_key = os.getenv("GEMINI_API_KEY")
            if api_key:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-pro")
                response = model.generate_content(prompt)
                return response.text
        except Exception as e:
            print(f"Gemini error: {e}")
    
    # Try HuggingFace as fallback
    if HUGGINGFACE_AVAILABLE:
        try:
            api_key = os.getenv("HUGGINGFACE_API_KEY")
            if api_key:
                api = InferenceApi(repo_id="gpt2", token=api_key)
                response = api(inputs=prompt)
                return response[0]["generated_text"]
        except Exception as e:
            print(f"HuggingFace error: {e}")
    
    # Fallback: Return a template curriculum if no AI is available
    return generate_template_curriculum(topic, level, duration_weeks, learning_style)

def generate_template_curriculum(topic: str, level: str, duration_weeks: int, learning_style: str) -> str:
    """
    Generate a template curriculum when AI services are unavailable.
    """
    return f"""
# {topic} Curriculum ({duration_weeks} Weeks)

## Student Level: {level}
## Learning Style: {learning_style}

### Learning Objectives
- Understand fundamental concepts of {topic}
- Apply knowledge to practical projects
- Develop proficiency in {topic}

### Weekly Breakdown

#### Week 1-2: Foundations
- Introduction to {topic}
- Key concepts and terminology
- Resources: Online tutorials, documentation
- Exercises: Practice problems and quizzes

#### Week 3-4: Core Concepts
- Deep dive into core principles
- Hands-on projects
- Resources: Books, video tutorials
- Exercises: Mini-projects and case studies

#### Week 5-{duration_weeks}: Advanced Topics & Application
- Advanced concepts and techniques
- Real-world applications
- Resources: Research papers, advanced courses
- Exercises: Capstone project

### Assessment Methods
- Weekly quizzes
- Practical assignments
- Peer review
- Final project

### Recommended Resources
- Online courses
- Books and documentation
- Community forums
- Mentorship opportunities

### Tips for {learning_style} Learners
- Customize learning approach based on preferred style
- Use interactive tools and platforms
- Engage with community
- Regular practice and feedback
"""
