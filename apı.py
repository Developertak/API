from flask import Flask, request, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/api/transcript', methods=['POST'])
def save_transcript():
    data = request.json
    # Dosya adı: transcript-ticketType-channelId-tarih.txt
    ticket_type = data.get("ticket_type", "unknown")
    channel_id = data.get("channel_id", "unknown")
    username = data.get("username", "unknown")
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"transcript-{ticket_type}-{username}-{now}.txt"
    # Mesajları dosyaya yaz
    with open(filename, "w", encoding="utf-8") as f:
        for msg in data.get("messages", []):
            f.write(msg + "\n")
    return jsonify({"status": "ok", "filename": filename})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)