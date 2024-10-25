import nltk

CORPUS = ''.join(nltk.corpus.brown.words())[:10000]

from keyboard import colemak, qwerty, Layout

qwerty.set_fitness(CORPUS)
print(qwerty.fitness)

colemak.set_fitness(CORPUS)
print(colemak.fitness)

temp = Layout("""%k>3}9;&\*b$1]-?6~,_@#|4x"[fj'm=v`/uhg8z5lrc2ontisdeapw^(:y{)q+.<!70""")

temp.visualize()
