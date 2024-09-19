import os
import pandas as pd

def generate_csv_files(path):
    data = {"phrase": [], "sentiment": []}
    
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r") as f:
                    data["phrase"].append(f.read())
                    data["sentiment"].append(os.path.basename(root))

    df = pd.DataFrame(data) 
    output_file = f"{os.path.basename(path)}_dataset.csv"
    df.to_csv(output_file, index=False)

folders = ["train", "test"]

for folder in folders:
    generate_csv_files(folder)