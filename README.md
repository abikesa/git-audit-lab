 
## ✅ Recommended GitHub Repo Layout

```
git-audit-lab/
├── study/                    # The actual Git repo with commits and tag
│   ├── .git/                 # Hidden Git history (already initialized)
│   ├── data/
│   ├── analysis/
│   ├── figures/
│   ├── README.md
│   └── ... (tag v1.0 exists here)
├── directory_structure.py    # Scaffolding-only script
├── git_fraud_casebuilder.py  # Full fraud simulation & Git commits
├── .gitignore                # Optional: ignore .pyc, __pycache__/
└── README.md                 # Instructions for interns (see below)
```

---

## 🧳 What to Push

You only need to push the **outer repo** (not the inner `.git/` from `study/`). Here's how:

### 1. Create a New GitHub Repo

Call it something like `git-audit-lab` or `ethical-research-lab`.

### 2. From Terminal, in your `Documents`:

```bash
cd ~/Documents
mkdir git-audit-lab
mv study git-audit-lab/
mv git_fraud_casebuilder.py git-audit-lab/
mv directory_structure.py git-audit-lab/
cd git-audit-lab
touch README.md .gitignore
```

### 3. Initialize a *new* outer repo (not the one inside `study/`):

```bash
git init
git add .
git commit -m "Initial setup with study case and setup scripts"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/git-audit-lab.git
git push -u origin main
```

> 🔐 Be careful **not** to push `study/.git/` — it’ll confuse things and may violate student repo expectations. This inner repo is meant to be explored, not versioned recursively.

---

## 🪧 Suggested `README.md` (outer repo)

````markdown
# Git Audit Lab 🧪

This training kit teaches version control as an ethical tool, using a real-world inspired case of data manipulation.

## 🔍 Files

- `directory_structure.py`: Builds an empty research directory structure.
- `git_fraud_casebuilder.py`: Simulates data fraud and commits changes to a Git repo inside `/study`.

## 📁 study/

This is a Git repo **within** the folder—interns should `cd study/` and run forensic audits using:

```bash
git log
git diff HEAD~1
git checkout HEAD~1
````

They can analyze data and explore what changed, when, and why it matters.

## 🧠 Learning Goals

* Practice Git forensically (not just for versioning)
* Spot dishonest commit patterns
* Reproduce analysis before and after data tampering

## 🚀 Setup

```bash
python git_fraud_casebuilder.py
cd study
python analysis/analyze.py
```

 