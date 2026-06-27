import os
import argparse

import pandas as pd
import torch
import numpy as np
from transformers import CLIPProcessor, CLIPTextModelWithProjection


parser = argparse.ArgumentParser()
parser.add_argument("--save_dir", type=str, required=True)
parser.add_argument("--train_csv", type=str, required=True)
parser.add_argument("--test_csv", type=str, required=True)
parser.add_argument("--reports_csv", type=str, required=True)
args = parser.parse_args()


processor = CLIPProcessor.from_pretrained("vinid/plip")
tokenizer = processor.tokenizer
text_model = CLIPTextModelWithProjection.from_pretrained("vinid/plip").cuda()

save_dir = args.save_dir
os.makedirs(save_dir, exist_ok=True)


def split_text(caption):
    tokens = tokenizer(caption, return_tensors="pt", add_special_tokens=False)['input_ids'][0]

    # Step 2: Split tokens into segments of maximum length (e.g., 77 tokens)
    max_length = 77
    token_batches = [tokens[i:i + max_length] for i in range(0, len(tokens), max_length)]

    # Step 3: Convert token segments back into text and prepare batches
    text_batches = [tokenizer.decode(batch, skip_special_tokens=True) for batch in token_batches]

    return text_batches


train_data_mmp = pd.read_csv(args.train_csv)
test_data_mmp = pd.read_csv(args.test_csv)
complete_data = pd.concat([train_data_mmp, test_data_mmp], axis=0, ignore_index=True)

tcga_reports = pd.read_csv(args.reports_csv, sep=',')
tcga_reports['case_id'] = tcga_reports['patient_filename'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')


common_ids = set(complete_data['case_id']).intersection(set(tcga_reports['case_id']))
tcga_reports = tcga_reports.set_index('case_id')

for case_id in common_ids:
    # self.data_df.loc[self.get_sample_id(idx)]
    unprocessed_text = tcga_reports.loc[case_id, 'text']
    text_batches = split_text(unprocessed_text)

    text = processor(text_batches, return_tensors="pt", padding=True, truncation=True, max_length=77)

    text = {key: value.cuda() for key, value in text.items()}

    with torch.no_grad():
        outputs = text_model(**text)
        text_embeds_gpu = outputs.text_embeds

    text_embeds = text_embeds_gpu.cpu()
    # Save the concatenated embeddings to a .pt file
    embedding_path = os.path.join(save_dir, f"{case_id}.pt")
    torch.save(text_embeds, embedding_path)

    print(f"Saved embeddings for ID: {case_id} of shape {text_embeds.shape} at {embedding_path} with number of batches {len(text_batches)}")
