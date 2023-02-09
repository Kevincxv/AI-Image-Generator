import openai as openai

openai.api_key = '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'

openai.Model.list()

response = openai.Image.create(
  prompt = "Cat",
  n=1,
  size = "1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)