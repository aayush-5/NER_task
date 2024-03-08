**Objective:**
The objective of this repo is to fine tune a Large Language Model (LLM) for performing named entity recognition (NER) task on an automotive dataset. NER task involves processing unstructured text data to extract useful entities. 

**Dataset Info:**
Dataset consist of text file having information about the car manufacturers who determine that a product or piece of original equipment either has a safety defect, or is not in compliance with federal safety standards. There is one supportive file “RCL.txt” that has the description of all the columns in the main file.

**Task-1:**
In the first task, I analyse the data and identifying what are some entities that can be
extracted from this data which are related to the automotive domain like “component”, “failure issue”, “brand”, “corrective action”. 

**Task-2:**
In the second task, we used “LLaMA 2 7b” and “Mistral 7b”  LLM for the extraction of the automotive domain entities from the given dataset. We also used the techniques like zero shot, few shot and COT (Chain-of-Thoughts) for prompting. 

**Task-3:**
In the final task, we fine tune the “LLaMa 2 7b” on the subset of the data.  We used QLORA to reduce the memory requirements of fine tuning LLMs. 
Comparison report of the fine-tuned model against zero shot/few shot on the testing dataset has been attached.

Repo also contains the test.py file which  take text paragraph as input and return all the entities and their types as output

Hugging face repo screenshot for the fine-tuned model on LLaMa 2 7b:

![image](https://github.com/aayush-5/NER_task/assets/32955085/cca5fc12-f051-4651-9673-fd2785809cb5)

