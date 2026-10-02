import json
class UserManager:
    def __init__(self):
        self.users= []
        self.id=1
    def add_user(self,name,age):
        self.users.append({"id":self.id,"name":name,"age":age})
        self.id += 1
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
um=UserManager()
