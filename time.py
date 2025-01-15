from datetime import datetime, timedelta
import time

# 指定する日時を設定 (例: 2025年1月15日15時30分)
target_datetime = datetime(2025, 1, 15, 15, 30, 0)  # 年, 月, 日, 時, 分, 秒

# 現在時刻を取得
current_time = datetime.now()

# もし指定日時が過去の場合はエラー表示
if target_datetime < current_time:
    pass
else:
    # 指定日時まで待機
    while datetime.now() < target_datetime:
        time.sleep(1)  # 1秒ごとにチェック（CPU負荷を軽減）

    # 指定日時に到達したらメッセージを表示
    print("指定した日時になりました！")
