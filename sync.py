import os
import json
import requests
from datetime import datetime

# 直接讀取 GitHub Secrets
API_KEY = os.getenv('INTERVALS_API_KEY')
ATHLETE_ID = os.getenv('INTERVALS_ATHLETE_ID')

if not API_KEY or not ATHLETE_ID:
    print("❌ 錯誤: 找不到 Secrets。請檢查 GitHub Settings > Secrets > Actions")
    exit(1)

def fetch_data():
    auth = ('API_KEY', API_KEY)
    url = f"https://intervals.icu/api/v1/athlete/{ATHLETE_ID}"
    
    print(f"正在抓取運動員 {ATHLETE_ID} 的數據...")
    
    try:
        # 1. 抓取最近一次活動 (最新數據)
        res_act = requests.get(f"{url}/activities?limit=1", auth=auth)
        activity = res_act.json()[0] if res_act.status_code == 200 and res_act.json() else {}

        # 2. 抓取體能指標 (Fitness)
        res_fit = requests.get(f"{url}/stats", auth=auth)
        stats = res_fit.json()[-1] if res_fit.status_code == 200 else {}

        # 3. 抓取健康數據 (Wellness)
        res_well = requests.get(f"{url}/wellness", auth=auth)
        wellness = res_well.json()[-1] if res_well.status_code == 200 else {}

        # 組合 snapshot
        snapshot = {
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "athlete_id": ATHLETE_ID,
            "metrics": {
                "ctl": stats.get('ctl'),
                "atl": stats.get('atl'),
                "tsb": stats.get('tsb'),
                "fitness": stats.get('fitness')
            },
            "wellness": {
                "hrv": wellness.get('hrv'),
                "rhr": wellness.get('restingHR'),
                "sleep_score": wellness.get('sleepScore')
            },
            "latest_activity": {
                "name": activity.get('name'),
                "type": activity.get('type'),
                "average_watts": activity.get('icu_average_watts'),
                "decoupling": activity.get('pwr_hr_dr_pct')
            }
        }

        with open('latest.json', 'w', encoding='utf-8') as f:
            json.dump(snapshot, f, indent=4, ensure_ascii=False)
        print("✅ 成功生成 latest.json!")

    except Exception as e:
        print(f"❌ 發生錯誤: {e}")
        exit(1)

if __name__ == "__main__":
    fetch_data()
