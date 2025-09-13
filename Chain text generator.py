#AI chatbot

import random

def build_markov_chain(text, n=2):
    words = text.split()
    chain = {}
    for i in range(len(words)-n):
        key = tuple(words[i:i+n])
        next_word = words[i+n]
        chain.setdefault(key, []).append(next_word)
    return chain

def generate_text(chain, length=20):
    key = random.choice(list(chain.keys()))
    result = list(key)
    for _ in range(length):
        next_words = chain.get(key)
        if not next_words:
            break
        word = random.choice(next_words)
        result.append(word)
        key = tuple(result[-2:])
    return " ".join(result)

sample_text = "I love to eat food. Food is crazy good."
chain = build_markov_chain(sample_text)
print("Generated:", generate_text(chain))
