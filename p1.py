import json
def analyze_log(filepath):
    total=0
    by_level=0
    by_user={}
    last_error=None
    try :
        with open(filepath,"r",encoding="utf-8") as f:
            data=json.load(f)
            if not data:
                return {"total":total,"by_level":by_level,"by_user":by_user,"last_error":last_error}
            for info in data:
                if type(info) is not dict:
                    continue
                if info!={"timestamp","level","message","user"}:
                    continue

    except FileNotFoundError:
        return {"total":total,"by_level":by_level,"by_user":by_user,"last_error":last_error}
    return {"total":total,"by_level":by_level,"by_user":by_user,"last_error":last_error}
