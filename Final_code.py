import wolframalpha
import wikipedia

while True:
    user_input = input('Type Your Query! ')
    try:
        app_id = 'Q3K2GK-2E3XXXXXXX'
        client = wolframalpha.Client(app_id)
        answer = client.query(user_input)
        result = next(answer.results).text
        print(result)
    except:
        print(wikipedia.summary(user_input))
