🧠 AI Quiz Generator

An AI-powered Quiz Generator that automatically creates quiz questions from any given topic or study material using Generative AI and NLP.
Built with Python, Streamlit, and Transformer models.

📌 Project Overview

The AI Quiz Generator allows users to:

Enter any topic or study text

Select the number of questions

Automatically generate quiz questions using AI

The project demonstrates the practical use of Generative AI, prompt engineering, and model control.

🚀 Features

✅ Generates quiz questions automatically

✅ Uses Transformer-based AI model

✅ User-friendly web interface (Streamlit)

✅ Handles AI limitations using iterative generation

✅ Lightweight & runs on normal laptops

✅ Suitable for college projects & resumes

🛠️ Tech Stack
Category	Technology
Programming Language	Python
AI / NLP	Hugging Face Transformers
Model Used	google/flan-t5-small
Web Framework	Streamlit
Environment	Virtual Environment (venv)
📂 Project Structure
AI_Quiz_Generator/
│
├── app.py                 # Streamlit web app
├── quiz_generator.py      # AI quiz logic
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── venv/                  # Virtual environment

⚙️ Installation & Setup
1️⃣ Clone or Download the Project
git clone https://github.com/your-username/AI_Quiz_Generator.git
cd AI_Quiz_Generator

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
streamlit run app.py


Open browser:

http://localhost:8501

🧪 How It Works

User enters topic or study material

User selects number of questions

AI model generates one question at a time

Questions are validated and formatted

Final quiz is displayed to the user

🧠 AI Logic Used

Text-to-Text Generation

Prompt Engineering

Iterative Question Generation

Duplicate Removal

AI Output Validation

This approach ensures reliable multiple questions, even with small models.

📸 Sample Output
1. What is Artificial Intelligence?
2. What do AI systems learn from?
3. What tasks can AI systems perform?

🎓 Viva / Interview Explanation

Q: Why did you generate questions one by one?
👉 Small transformer models may not reliably generate multiple structured outputs, so iterative generation ensures correctness.

Q: Which AI model is used?
👉 google/flan-t5-small from Hugging Face Transformers.

Q: Why Streamlit?
👉 It allows rapid development of interactive web apps using Python only.

🔮 Future Enhancements

🔹 MCQ generation with options

🔹 Automatic quiz scoring

🔹 Difficulty levels (easy/medium/hard)

🔹 PDF upload support

🔹 Download quiz as PDF

🔹 User login & result tracking

👩‍💻 Author

Sara Shitole
Computer Engineering Student

⭐ Conclusion

This project demonstrates a practical implementation of Generative AI in education, showcasing how AI can automate content creation and improve learning experiences.
