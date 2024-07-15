# 'Breathe (In The Air)' by Pink Floyd

text = """Breathe breathe in the air
Don't be afraid to care
Leave but don't leave me
Look around and choose your own ground

For long you live and high you fly
And smiles you'll give and tears you'll cry
And all you touch and all you see
Is all your life will ever be

Run rabbit run
Dig that hole forget the sun
And when at last the work is done
Don't sit down it's time to dig another one

For long you live and high you fly
But only if you ride the tide
And balanced on the biggest wave
You race towards an early grave
"""

# Splitting the lyrics into individual words and the length of the list of words
print(len(text.split()))

word_count = {}

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

