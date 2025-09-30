from flask import Flask, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# 模擬的法規資料
laws = [
    {
        "title": "交通新制-酒駕加重罰則",
        "effective_date": "2025-10-01",
        "summary": "酒駕罰鍰加倍，並加強吊銷駕照機制。"
    },
    {
        "title": "機車安全帽新規範",
        "effective_date": "2025-11-15",
        "summary": "安全帽需符合新型 CNS 標準，違者處以新台幣 600 元罰鍰。"
    },
    {
        "title": "國道超速新罰則",
        "effective_date": "2026-01-01",
        "summary": "超速 40 公里以上直接吊扣駕照。"
    }
]

@app.route("/")
def home():
    return "法規查詢 API 已啟動 ?"

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
