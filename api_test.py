import requests

post_id = input("Enter a post ID (1-100): ")
response = requests.get("https://jsonplaceholder.typicode.com/posts/" + post_id)
data = response.json()

print("title:", data["title"])
print("body:", data["body"])