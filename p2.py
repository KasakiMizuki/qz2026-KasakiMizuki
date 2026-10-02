import json
class UserManager:
    def __init__(self):
        self.users= []
        self.maxid=1
    def add_user(self,name,age):
        self.users.append({"id":self.maxid,"name":name,"age":age})
        self.maxid += 1
        return self.users[-1]
    def get_user(self,target):
        for user in self.users:
            if user["id"]==target:
                return user
        return None
    def remove_user(self,id):
        user=self.get_user(id)
        if user==None:
            return False
        self.users.remove(user)
        return True
    def update_age(self,target,newage):
        user=self.get_user(target)
        if user==None:
            return False
        user["age"]=newage
        return True
    def list_users(self):
        inventory=[]
        for user in self.users:
            inventory.append(user)
        return inventory
    def save_to_json(self,fPath):
        with open(fPath,"w",encoding="utf-8") as f:
            json.dump(self.users,f,ensure_ascii=False)
    def load_from_json(self,fPath):
        with open(fPath,"r",encoding="utf-8") as f:
            data=json.load(f)
            self.users=data
            for user in self.users:
                self.maxid=max(self.maxid,user["id"])
            self.maxid+=1

um=UserManager()
um.add_user("Mortis",2)
um.add_user("Oblivious",18)
for user in um.users:
    print(user)
