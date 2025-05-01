import os
# disable wandb logging
os.environ["WANDB_DISABLED"] = "true"

import json
from datasets import Dataset
from transformers import (
    GPT2Tokenizer,
    GPT2LMHeadModel,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
)

# 1. Load QA pairs and build prompt–completion examples
with open('dataset.json') as f:
    qa = json.load(f)
examples = []
for item in qa:
    prompt = f"Q: {item['question']}\nA:"
    completion = " " + item['answer']
    examples.append({"text": prompt + completion})

# 2. Create Hugging Face Dataset
dataset = Dataset.from_list(examples)

# 3. Tokenizer & model
tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')
tokenizer.pad_token = tokenizer.eos_token
def tokenize(ex):
    return tokenizer(ex['text'], truncation=True, padding='max_length', max_length=128)
tokenized = dataset.map(tokenize, batched=True, remove_columns=['text'])

model = GPT2LMHeadModel.from_pretrained('distilgpt2')

# 4. TrainingArguments (disable all trackers)
training_args = TrainingArguments(
    output_dir='./model',
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_total_limit=2,
    report_to=[]              # disable wandb & other loggers
)

# 5. Trainer
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized,
    data_collator=data_collator,
)

trainer.train()
trainer.save_model('./model')
