import pandas as pd


with open('One.txt') as mytext:
    world_one = mytext.read().lower().split()
    uni_world_one = set(world_one)

with open('Two.txt') as mytext:
    world_two = mytext.read().lower().split()
    uni_world_two = set(world_two)

all_uni_worlds = set()
all_uni_worlds.update(uni_world_one)
all_uni_worlds.update(uni_world_two)

full_vocab = dict()
i = 0
for world in all_uni_worlds:
    full_vocab[world] = i
    i = i +1

one_freq = [0]*len(full_vocab)
two_freq = [0]*len(full_vocab)
all_worlds = ['']*len(full_vocab)

with open('One.txt') as t:
    one_text = t.read().lower().split()
for word in one_text:
    word_ind = full_vocab[word]
    one_freq[word_ind] +=1

with open('Two.txt') as t:
    two_text = t.read().lower().split()
for word in two_text:
    word_ind = full_vocab[word]
    two_freq[word_ind] +=1

for word in full_vocab:
    word_ind = full_vocab[word]
    all_worlds[word_ind] = word


bow = pd.DataFrame(data=[one_freq, two_freq], columns=all_worlds)



# print(uni_world_one)
# print(uni_world_two)
#print(all_uni_worlds)
#print(full_vocab)
print(one_freq)
print(two_freq)
print(all_worlds)
print(bow)
