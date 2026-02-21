
# Step 1 — Clone the Repo

```bash
git clone https://github.com/rititkbt01/secure-plant-diagnosis.git
cd secure-plant-diagnosis

```

# Step 2 - Create Virtual Environment

```bash
py -3.10 -m venv venv
venv\Scripts\activate

```

# Step 3 — All Libraries
```bash
pip install -r requirements.txt
```

# Step 4 — Set Up Kaggle all each members need to setup this :

    Create Kaggle account at https://www.kaggle.com
    Go to Settings → API → Create New Token
    Place kaggle.json at C:\Users\YourName\.kaggle\kaggle.json

# Download Dataset

```bash
cd data
kaggle datasets download -d abdallahalidev/plantvillage-dataset
tar -xf plantvillage-dataset.zip
cd ..

```


# Step 6 — Run Data Scripts in Order:

```bash

python data/prepare_data.py
python data/split_data.py
python data/verify_data.py

```

### Step 7 — Confirm It Worked
Last line should say:
```
✅ ALL CHECKS PASSED - Stage 1 Complete!



