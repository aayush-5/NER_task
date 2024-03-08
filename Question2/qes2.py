import ollama
import pandas as pd

# Initialize lists to store data
data = []
column_names = [
    "RECORD_ID",
    "CAMPNO",
    "MAKETXT",
    "MODELTXT",
    "YEARTXT",
    "MFGCAMPNO",
    "COMPNAME",
    "MFGNAME",
    "BGMAN",
    "ENDMAN",
    "RCLTYPECD",
    "POTAFF",
    "ODATE",
    "INFLUENCED_BY",
    "MFGTXT",
    "RCDATE",
    "DATEA",
    "RPNO",
    "FMVSS",
    "DESC_DEFECT",
    "CONEQUENCE_DEFECT",
    "CORRECTIVE_ACTION",
    "NOTES",
    "RCL_CMPT_ID",
    "MFR_COMP_NAME",
    "MFR_COMP_DESC",
    "MFR_COMP_PTNO"
]
# Read the text file line by line
with open("FLAT_RCL.txt", "r") as file:
    for line in file:
        # Split each line by tabs and append to data list
        row = line.strip().split("\t")
        data.append(row)

# Create DataFrame
df = pd.DataFrame(data, columns=column_names)

# Displaying the DataFrame
# print(df)
# df.to_csv("formated_data.csv")

df = df[[ "DESC_DEFECT","CONEQUENCE_DEFECT","CORRECTIVE_ACTION","NOTES"]]
data = df.to_dict()

for i in range(len(data['DESC_DEFECT'])):
    row = data["DESC_DEFECT"][i] + " " +  data["CONEQUENCE_DEFECT"][i] + " " + data["CORRECTIVE_ACTION"][i] + " "+ data["NOTES"][i]
    
    prompt = 'Paragraph: {row}'+' In above paragraph, find the entity like : component, failure issue, vehicle model, corrective action and give the output as json like {"Entity": "amplification of the stress", "Label": "Failure Issue"}, ONLY GIVE JSON AS OUTPUT'
    response = ollama.chat(model='mistral', messages=[
    {
        'role': 'user',
        'content': prompt
    },
    ])

    print(response['message']['content'])