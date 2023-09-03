class StarCookie:
    milk = 0.5
    def __init__(self,color, weight=0) -> None:
        self.color = color
        self.weight = weight
    
    
    def __str__(self) -> str:
        return f'star cookie is the color {self.color} and weighs {self.weight}'
        
 
star_cookie = StarCookie('red')
print(star_cookie)


class Youtube: 

    def __init__(self, username, subscribers = 0,subscriptions = 0) -> None:
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self, user):
        user.subscribers +=1
        self.subscriptions +=1


user1 = Youtube('Abu')
user2 = Youtube('Mohamed')

user1.subscribe(user2)
