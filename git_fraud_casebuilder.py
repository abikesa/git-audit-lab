import os

# Directory and file blueprint
structure = {
    "study/data": ["raw_data.csv", "manipulated_data.csv"],
    "study/analysis": ["analyze.py"],
    "study/figures": ["result_plot.png"],
    "study": ["README.md"]
}

# Optional: placeholder contents
file_contents = {
    "study/data/raw_data.csv": "id,value\n1,10\n2,15\n3,12\n",
    "study/data/manipulated_data.csv": "id,value\n1,20\n2,25\n3,22\n",
    "study/analysis/analyze.py": "# analysis script placeholder\n",
    "study/figures/result_plot.png": "",  # empty file
    "study/README.md": "# Study Directory\n\nUse this space to explain your project."
}

# Create structure and files
for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for filename in files:
        path = os.path.join(folder, filename)
        with open(path, 'w') as f:
            f.write(file_contents.get(path, ""))

print("✅ Directory structure created under ./study")
