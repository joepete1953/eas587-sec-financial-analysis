import io
import zipfile
from pathlib import Path

import pandas as pd
import requests


# January 2026 SEC Financial Statement and Notes package
SEC_URL = (
    "https://www.sec.gov/files/dera/data/"
    "financial-statement-notes-data-sets/2026_01_notes.zip"
)

HEADERS = {
    "User-Agent": "Joebin Peter Soosairaj and Shreyas Aravind EAS587 project joebinpe@buffalo.edu"
}

SAMPLE_DIR = Path("data/samples")
SAMPLE_DIR.mkdir(parents=True, exist_ok=True)


print("Downloading January 2026 SEC sample package...")

response = requests.get(SEC_URL, headers=HEADERS, timeout=120)
response.raise_for_status()

print("Download complete.")

# Open ZIP directly from memory
with zipfile.ZipFile(io.BytesIO(response.content)) as z:

    print("\nFiles in SEC package:")
    print(z.namelist())

    # Load the four main tables we want to demonstrate
    sub = pd.read_csv(z.open("sub.tsv"), sep="\t", low_memory=False)
    num = pd.read_csv(z.open("num.tsv"), sep="\t", low_memory=False)
    txt = pd.read_csv(z.open("txt.tsv"), sep="\t", low_memory=False)
    tag = pd.read_csv(z.open("tag.tsv"), sep="\t", low_memory=False)

memory_bytes = sum(
    df.memory_usage(deep=True).sum()
    for df in [sub, num, txt, tag]
)

print(
    f"\nMemory used by the four January 2026 tables: "
    f"{memory_bytes / (1024**3):.2f} GiB"
)


print("\nOriginal table sizes:")
print("SUB:", sub.shape)
print("NUM:", num.shape)
print("TXT:", txt.shape)
print("TAG:", tag.shape)


# Small representative samples
sub_sample = sub.head(100)
num_sample = num.head(100)
tag_sample = tag.head(100)

# Use actual longer narrative disclosures for TXT
if "txtlen" in txt.columns:
    txt_sample = txt[txt["txtlen"] > 500].head(50)
else:
    txt_sample = txt.head(50)


# Save samples
sub_sample.to_csv(SAMPLE_DIR / "sub_sample.csv", index=False)
num_sample.to_csv(SAMPLE_DIR / "num_sample.csv", index=False)
txt_sample.to_csv(SAMPLE_DIR / "txt_sample.csv", index=False)
tag_sample.to_csv(SAMPLE_DIR / "tag_sample.csv", index=False)


print("\nRepresentative samples created:")
print("data/samples/sub_sample.csv")
print("data/samples/num_sample.csv")
print("data/samples/txt_sample.csv")
print("data/samples/tag_sample.csv")