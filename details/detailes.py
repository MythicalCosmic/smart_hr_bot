
import json

with open("./data/data_labels.json", "r", encoding="utf-8") as f:
    DATA_LABELS = json.load(f)

with open("./data/job_positions.json", "r", encoding="utf-8") as f:
    POSITION_DETAILS = json.load(f)

with open("./data/job_roles.json", "r", encoding="utf-8") as f:
    JOB_ROLES = json.load(f)