from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_prompt():
    task = request.form['task']
    category = request.form['category']
    tone = request.form['tone']

    prompt_templates = {
        'Blog Writing': f"You are an expert blog writer. Write a blog post about: {task}. Keep it {tone}.",
        'Caption Writing': f"You are a creative social media strategist. Write a catchy caption for: {task}. Make it {tone}.",
        'Code Debugging': f"You are a senior software developer. Debug the following code issue: {task}. Explain the bug and provide a corrected version.",
        'Marketing Ad Copy': f"You are a marketing expert. Write an engaging ad copy for: {task}. Keep the tone {tone}.",
        'Interview Q&A Generator': f"You are an experienced interviewer. Generate interview questions and answers for: {task}. Keep them {tone}."
    }

    prompt = prompt_templates.get(category, "Invalid category.")

    return jsonify({'prompt': prompt})

if __name__ == '__main__':
    app.run(debug=True)
