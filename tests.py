from jolanda import *

#test of write_prophecy function, to evaluate how it responds to different instructions
prompt_1 = 'napiš ' + random.choice(sentiment) + ' českou větu v druhé osobě v budoucím čase na téma {}'
prompt_2 = 'napiš dvě ' + random.choice(sentiment) + ' české věty v druhé osobě v budoucím čase na téma {}'
prompt_3 = 'napiš ' + random.choice(sentiment) + ' věštbu v češtině, která bude mít dvě věty a bude na téma {}'
[print(write_prophecy(prompt, "vodík")) for prompt in [prompt_1, prompt_2, prompt_3]]
