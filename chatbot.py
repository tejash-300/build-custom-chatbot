import json
from difflib import get_close_matches
from transformers import GPT2Tokenizer, GPT2LMHeadModel, pipeline

# Load dataset
with open('dataset.json') as f:
    qa_pairs = json.load(f)

# Load fine-tuned model
model_dir = 'model'
tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
model = GPT2LMHeadModel.from_pretrained(model_dir)
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

def get_response(user_input):
    user = user_input.strip()
    # Exact match
    for qa in qa_pairs:
        if user.lower() == qa['question'].lower():
            return qa['answer']
    # Fuzzy match
    questions = [q['question'] for q in qa_pairs]
    matches = get_close_matches(user, questions, n=1, cutoff=0.6)
    if matches:
        return next(q['answer'] for q in qa_pairs if q['question']==matches[0])
    # GPT-2 generation
    out = generator(f"Q: {user}\nA:", max_length=50, num_return_sequences=1)
    return out[0]['generated_text'].split('A:')[-1].strip()

if __name__=='__main__':
    print("ChatBot ready! Type 'exit' to quit.")
    while True:
        msg = input("You: ")
        if msg.lower()=='exit': break
        print("Bot:", get_response(msg))
