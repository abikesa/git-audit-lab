Yaas indeed. 🪩🧠 Here's **both**—your internship-ready **`report_template.md`** *and* a slick little **SHA256 integrity checker** for tampering detection. Drop these straight into your repo.

---

## 📄 `report_template.md`

````markdown
# 🕵️‍♂️ Forensic Audit Report

**Intern Name**: `_____________`  
**Date**: `_____________`  
**Repo Version Audited**: `git-audit-lab/study`  
**Tag/Commit**: `_____________`

---

## 1. 🧬 Chain of Evidence

### 📅 Git Log Summary

```bash
git log --oneline --graph
````

> *Paste or summarize the commit history here.*

---

## 2. 🔍 Diff Analysis

### What changed between the commits?

```bash
git diff HEAD~1 HEAD
```

> *Describe the nature of changes: what was modified in the data, scripts, or figures?*

---

## 3. 🐛 Suspect Files

* [ ] `data/manipulated_data.csv`
* [ ] `analysis/analyze.py`
* [ ] `figures/result_plot.png`
* [ ] Other: `_____________`

> *Mark any file that shows signs of manipulation. Explain why.*

---

## 4. 💡 Hypothesis

> *What kind of fraud was attempted? Fabrication? Falsification? Selective reporting?*

---

## 5. ✅ Reproduction Attempt

### Did the data and plot reproduce before manipulation?

* [ ] Yes
* [ ] No
* [ ] Partially

> *Explain what you did to check this. Include code snippets or screenshots if needed.*

---

## 6. 🧠 Final Assessment

### Verdict:

* [ ] No fraud detected
* [ ] Minor anomalies
* [x] Confirmed manipulation

> *Summarize your audit findings. Include moral or methodological insights.*

---

## 7. 🔐 Optional: SHA Integrity Check

```bash
shasum -a 256 data/raw_data.csv
```

> *Paste the hash and compare against original.*

---

# ✍️ Signature: `_____________`

````

Save as: `report_template.md` in the root of your repo.

---

## 🔐 `sha_check.py` — Automated SHA256 Integrity Verifier

```python
import hashlib

def sha256sum(filename):
    with open(filename, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

files = [
    "study/data/raw_data.csv",
    "study/data/manipulated_data.csv",
    "study/analysis/analyze.py"
]

for file in files:
    try:
        hash = sha256sum(file)
        print(f"{file}: {hash}")
    except FileNotFoundError:
        print(f"{file}: [Not Found]")
````

Save as: `sha_check.py`
Run with:

```bash
python sha_check.py
```

> **Use Case**: Students run this **before and after manipulation**. If hashes change, tampering is proven.

---

Let me know if you'd like a `Makefile` to wrap all of this into a `make audit`, `make verify`, `make reset` suite. You’re dangerously close to running an elite training lab on epistemic forensics.
