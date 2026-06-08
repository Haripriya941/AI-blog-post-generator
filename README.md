# AI Blog Post Generator

An AI-powered Blog Post Generator built using **Streamlit** and **Google Gemini AI**. This application generates complete blog articles from a user-provided topic, including a title, introduction, headings, detailed content, and conclusion.

## Features

- Generate blog posts instantly using AI
- Attractive blog title generation
- Well-structured content with headings and subheadings
- Professional and informative writing style
- Simple and user-friendly Streamlit interface

## Technologies Used

- Python 3.13
- Streamlit
- Google Generative AI (Gemini API)

## Project Structure

```
AI-Blog-Post-Generator/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Blog-Post-Generator.git
cd AI-Blog-Post-Generator
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Requirements

Create a `requirements.txt` file with:

```txt
streamlit
google-generativeai
```

Or install manually:

```bash
pip install streamlit google-generativeai
```

## Configure Gemini API Key

Replace the API key in the code:

```python
genai.configure(api_key="YOUR_API_KEY")
```

You can obtain an API key from Google AI Studio.

## Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

## How It Works

1. Enter a blog topic.
2. Click **Generate Blog**.
3. Gemini AI creates:
   - Blog Title
   - Introduction
   - Headings & Subheadings
   - Detailed Content
   - Conclusion
4. The generated blog is displayed on the page.

## Example

### Input

```
Artificial Intelligence in Healthcare
```

### Output

- Attractive Blog Title
- Introduction
- Multiple Sections
- Detailed Explanations
- Conclusion

## Future Enhancements

- Download blog as PDF
- Download blog as DOCX
- Multiple writing styles
- SEO-optimized blog generation
- Word count selection
- Blog history storage

## Screenshots

Add screenshots of the application here.

## License

This project is licensed under the MIT License.

## Author

Haripriya G

---

⭐ If you found this project useful, consider giving it a star on GitHub.
