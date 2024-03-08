from transformers import AutoTokenizer
import transformers
import torch

model = "jarvis05/Llama-2-7b-chat-finetune"
para = input("Enter the Paragraph :")
para = f"""{para}"""

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device=0,
)

prompt = f"""paragraph:
{para}

find out entities like (component, failure issue, vehicle model, corrective action) from this above paragraph ,output should be in json format only:

output format:
{"Entity": "bottoming out the suspension", "Label": "Failure Issue"}
"""

sequences = pipeline(
    f'<s>[INST] {prompt} [/INST]',
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=2048,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")



