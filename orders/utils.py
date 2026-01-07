from pathlib import Path
from django.conf import settings

def log_transaction(transaction_id):
    base = Path(settings.BASE_DIR) / "payments"
    base.mkdir(exist_ok=True)
    file_path = base / "transactions.txt"

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(transaction_id + "\n")