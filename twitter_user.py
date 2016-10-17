from twit_api import api

user = api.get_user('@protoskull')

print(user.screen_name)
print(user.followers_count)

for friend in user.friends():
    print
    print(friend.screen_name)
    print(friend.followers_count)