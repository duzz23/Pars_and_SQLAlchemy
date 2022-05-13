import json



def addcategories():
    with open("tiktok.json", encoding='utf-8') as read_file:
        js = json.load(read_file)

    parser = {
        'search': [],
    }

    input_name = 'redbullrussia'
    # input_name = input('Напиши Ник: ')
    for result in js:
        if input_name == result['username']:
            avatar_link = result['avatar_link']
            name = result['name']
            username = result['username']
            description = result['description']
            following_count = result['following_count']
            # 'Список подписок': '0',
            followers_count = result['followers_count']
            # 'Список подписчиков': 'где взять список',
            # 'Кол-во лайков': 'имеется в виду всех со всех видео ',
            # 'Cписок лайкеров': 'как узнать список лайкеров',
            # Хэштэги
            comments_count = 0
            plays_count = 0
            shares_count = 0
            # Список комментаторов
            videos_date = []
            verified = result['verified']
            # в чем разница Количество комментариев поста и Кол-во комментариев  (блогер)
            # Упоминания брендов в постах (из описания сслыки на акк )

            for video in result['videos']:
                videos_date.append(
                    {
                        'comment_count': video['comment_count'],
                        'comment': video['comments'],
                        'share_count': video['share_count'],
                        'hashtags': [word for word in video['description'].split() if word.startswith('#')],
                        'play_count': video['play_count'],
                        'created_time': video['created_time'],
                        'description': video['description'],
                        'likes_count': video['likes_count'],

                    }
                )
                comments_count += video['comment_count'] or 0
                plays_count += video['play_count']
                shares_count += video['share_count']

            avatar = {
                'avatar_link': avatar_link,
                'name': name,
                'username': username,
                'description': description,
                'following_count': following_count,
                # 'Список подписок': '0',
                'followers_count': followers_count,
                # 'Список подписчиков': '0',
                # 'Кол-во лайков': '0',
                # 'Cписок лайкеров': '0',
                'comments_count': comments_count,
                'plays_count': plays_count,
                'shares_count': shares_count,
                'verified': verified,
                'videos': videos_date,

            }

            parser['search'].append(avatar)


    return json.dumps(parser, indent=2)

print(addcategories())