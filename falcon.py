from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

import os
import sys

model = "tiiuae/falcon-7b-instruct"

# Save the original stdout
original_stdout = sys.stdout
original_stderr = sys.stderr

# Open a null file for writing
null_file = open(os.devnull, 'w')

# Redirect stdout to the null file
sys.stdout = null_file
sys.stderr = null_file

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)

# Restore the original stdout
sys.stdout = original_stdout
sys.stderr = original_stderr

prompt = input("Falcon: Hello! What do you want to ask?\nYou: ")

sys.stdout = null_file
sys.stderr = null_file

preprompt = "This is a conversation between a programmer using an AI assistant to write code. The AI assistant always answers with fully working code and puts the code inside a Markdown code block. Before starting the code block, the assistant will always add the name of the file before the code block."

sequences = pipeline(
   f"{preprompt}\nUser: {prompt}\nAssistant: ",
    max_length=2000,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)

sys.stdout = original_stdout
sys.stderr = original_stderr

for seq in sequences:
    print(f"Result: {seq['generated_text']}")
