import string

asciilist = list(string.ascii_lowercase)
# shortcut_mapper = {
#     'a': {
#         'ctrl': None,
#         'ctrl+shift': None,
#         'ctrl+alt': None,
#         'ctrl+shift+alt': None,
#     },
#     'b': {
#         'ctrl': None,
#         'ctrl+shift': None,
#         'ctrl+alt': None,
#         'ctrl+shift+alt': None,
#     },
#     'c': {
#         'ctrl': None,
#         'ctrl+shift': None,
#         'ctrl+alt': None,
#         'ctrl+shift+alt': None,
#     },
# }
# list ( zip(asciilist, map(lambda a: {'ctrl':f'ctrl for {a}'},asciilist)) )
# [
# ('a', {'ctrl': 'ctrl for a'}),
# ('b', {'ctrl': 'ctrl for b'}),
# ('c', {'ctrl': 'ctrl for c'}),
# ('d', {'ctrl': 'ctrl for d'}),
# ('e', {'ctrl': 'ctrl for e'}), ('f', {'ctrl': 'ctrl for f'}), ('g', {'ctrl': 'ctrl for g'}), ('h', {'ctrl': 'ctrl for h'}), ('i', {'ctrl': 'ctrl for i'}), ('j', {'ctrl': 'ctrl for j'}), ('k', {'ctrl': 'ctrl for k'}), ('l', {'ctrl': 'ctrl for l'}), ('m', {'ctrl': 'ctrl for m'}), ('n', {'ctrl': 'ctrl for n'}), ('o', {'ctrl': 'ctrl for o'}), ('p', {'ctrl': 'ctrl for p'}), ('q', {'ctrl': 'ctrl for q'}), ('r', {'ctrl': 'ctrl for r'}), ('s', {'ctrl': 'ctrl for s'}), ('t', {'ctrl': 'ctrl for t'}), ('u', {'ctrl': 'ctrl for u'}), ('v', {'ctrl': 'ctrl for v'}), ('w', {'ctrl': 'ctrl for w'}), ('x', {'ctrl': 'ctrl for x'}), 
# ('y', {'ctrl': 'ctrl for y'}),
# ('z', {'ctrl': 'ctrl for z'})
# ]
# di awal semua kosong
initializer = {'ctrl':None,'ctrl+shift':None,'ctrl+alt':None,'ctrl+shift+alt':None}
shortcut_mapper = dict ( zip(asciilist, map(lambda _: initializer, asciilist)) )
