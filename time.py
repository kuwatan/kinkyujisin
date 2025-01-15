from datetime import datetime, timedelta
import time

# 指定する時刻を設定 (例: 15時30分)
target_time = "15:30:00"  # 時刻は HH:MM:SS 形式で指定

# 現在の日付に指定の時刻を組み合わせる
today = datetime.now()
target_datetime = datetime.strptime(f"{today.date()} {target_time}", "%Y-%m-%d %H:%M:%S")

# もし指定時刻が過去の場合は翌日に設定
if target_datetime < today:
    target_datetime += timedelta(days=1)

# 指定時刻まで待機
while datetime.now() < target_datetime:
    time.sleep(1)  # 1秒ごとにチェック（CPU負荷を軽減）

# 指定時刻に到達したらメッセージを表示
print("指定した時間になりました！")
