from transformers import pipeline

# Load lightweight model
model = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

def generate_single_question(text, index):
    prompt = f"""
    From the text below, generate ONE unique quiz question.
    The question must end with a question mark (?).

    Text:
    {text}
    """

    result = model(
        prompt,
        max_length=80,
        do_sample=True,
        temperature=0.9
    )

    return result[0]["generated_text"].strip()


def generate_quiz(text, num_questions):
    questions = []
    attempts = 0

    while len(questions) < num_questions and attempts < num_questions * 3:
        q = generate_single_question(text, len(questions))

        # accept only valid questions
        if "?" in q and q not in questions:
            questions.append(q)

        attempts += 1

    # Format output
    formatted = ""
    for i, q in enumerate(questions, 1):
        formatted += f"{i}. {q}\n"

    return formatted
