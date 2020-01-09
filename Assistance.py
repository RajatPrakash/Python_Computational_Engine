import wolframalpha
import wikipedia


user_input = input('Type Your Query! ')
app_id = 'Q3K2GK-2E37H9ERUE'
client = wolframalpha.Client(app_id)
answer = client.query(user_input)
result = next(answer.results).text
print(result)
