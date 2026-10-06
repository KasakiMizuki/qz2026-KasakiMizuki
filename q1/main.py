import json
import os
def analyze_log(filepath):
    base_dir=os.path.dirname(os.path.abspath(__file__))
    full_path=os.path.join(base_dir, filepath)
    total=0
    by_level={}
    by_user={}
    last_error=None
    try :
        with open(full_path,"r",encoding="utf-8") as f:
            for line in f:
                line=line.strip()
                if not line:
                    continue
                try:
                    info=json.loads(line)
                except json.decoder.JSONDecodeError:
                    continue
                total+=1
                by_level[info["level"]]=by_level.get(info["level"],0)+1
                by_user[info["user"]]=by_user.get(info["user"],0)+1
                if info["level"] == "ERROR":
                    last_error = info["message"]
    except FileNotFoundError:
        pass
    return {"total":total,"by_level":dict(sorted(by_level.items(),key=lambda kv:kv[1],reverse=True)),"by_user":dict(sorted(by_user.items(),key=lambda kv:kv[1],reverse=True)),"last_error":last_error}