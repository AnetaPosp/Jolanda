import openai
import random
import re
from lists import signs, general_topics, fch_topics, elements, sentiment

# reading OpenAI API key. The key is available on https://beta.openai.com/account/api-keys after registration (free trial available)
# save it to my_key.txt file to make this script work
with open("my_key.txt") as file: 
  openai.api_key = file.read()

def write_prophecy(my_prompt, topic):
  """
  my_prompt: str, instruction in natural language. Must contain {} - to fill in the topic. example: "write a sentence about {}" 
  language seems unimportant (tested on English and Czech). If the output should be in other language than English, it's better to specify it. 
  For example, using my_prompt = "napiš větu o {} v češtině", the function returns output in Czech, but with my_prompt = "napiš větu o {}" often returns English
  topic: str
  returns: str
  """
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt= my_prompt.format(topic),
    temperature=0.7,
    max_tokens=348,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  output = response["choices"][0]["text"]
  output = re.sub("\s+", " ", output) #removal of empty lines, because OpenAI is obsessed with writing them
  return output

# generating horoscope topics for each sign
selected_general_topics = random.sample(general_topics, 12)
selected_fch_topics = random.sample(fch_topics, 12)
selected_elements = random.sample(elements, 12)

# creation of horoscope sentences (in Czech)
prompt = 'napiš ' + random.choice(sentiment) + ' věštbu na příští měsíc v češtině, která bude mít jednu větu a bude na téma {}'
with open("horoskop.txt", "w", encoding="utf-8") as horoscope:
  for i in range(12):
    horoscope.write(signs[i] + "\n")
    horoscope.write(write_prophecy(prompt, selected_general_topics[i]))
    horoscope.write(write_prophecy(prompt, selected_fch_topics[i]))
    horoscope.write(f' Tvůj prvek bude {selected_elements[i]}. ')
    horoscope.write(write_prophecy("napiš v jedné české větě, jak člověka ve znamení " + signs[i] + " ovlivní {}", selected_elements[i]))
    horoscope.write("\n\n")