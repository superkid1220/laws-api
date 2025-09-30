from flask import Flask, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# �������k�W���
laws = [
    {
        "title": "��q�s��-�s�r�[���@�h",
        "effective_date": "2025-10-01",
        "summary": "�s�r�@��[���A�å[�j�Q�P�r�Ӿ���C"
    },
    {
        "title": "�����w���U�s�W�d",
        "effective_date": "2025-11-15",
        "summary": "�w���U�ݲŦX�s�� CNS �зǡA�H�̳B�H�s�x�� 600 ���@��C"
    },
    {
        "title": "��D�W�t�s�@�h",
        "effective_date": "2026-01-01",
        "summary": "�W�t 40 �����H�W�����Q���r�ӡC"
    }
]

@app.route("/")
def home():
    return "�k�W�d�� API �w�Ұ� ?"

@app.route("/laws")
def get_laws():
    today = datetime.today()
    three_months_later = today + timedelta(days=90)

    upcoming_laws = [
        law for law in laws
        if today <= datetime.strptime(law["effective_date"], "%Y-%m-%d") <= three_months_later
    ]
    return jsonify(upcoming_laws)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
