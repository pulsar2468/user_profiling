import copy

import merge_concept


entity_list=[['trump', 'san francisco', 'illegal immigration','second world war']]
mashup=[['second', 'world', 'war', 'francisco', 'san', 'shoot', 'woman', 'san', 'francisco', 'second', 'world', 'war', 'row', 'illegal', 'immigration']]
final=merge_concept.to_singular_concept(copy.deepcopy(entity_list),copy.deepcopy(mashup))
print(entity_list)
print(mashup)
print(final)


