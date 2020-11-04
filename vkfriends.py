import requests

VK_TOKEN = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'
FRIENDS_GET_URL = 'https://api.vk.com/method/friends.get'
V = '5.124'


class VkClient:

    def __init__(self, user_id):
        self.user_id = user_id
        self.link = f'https://vk.com/id{user_id}'

    def get_friends(self):
        response = requests.get(
            FRIENDS_GET_URL,
            params={
                'access_token': VK_TOKEN,
                'user_id': self.user_id,
                'v': V
            })
        return response.json()

    def set_friends(self):
        friends_list = self.get_friends()['response']['items']
        return set(friends_list)

    def __and__(self, other):
        result = self.set_friends() & other.set_friends()
        return list(result)


if __name__ == '__main__':
    user_1 = VkClient(input('Введите id для первого пользователя: '))
    user_2 = VkClient(input('Введите id для второго пользователя: '))
    print(user_1 & user_2)
    print(user_1.link)
    print(user_2.link)