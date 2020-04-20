from MontyLingua import MontyNLGenerator
from MontyLingua import RunMontyLingua


"""conjugate verbs"""
monty = MontyNLGenerator.MontyNLGenerator()
# print(dir(monty))
# print(monty.conjugate_verb.__doc__)

verb_lemma = 'run'
print(f"{verb_lemma=}")
print(f"conjugated={monty.conjugate_verb(verb_lemma, 'VBD')}")


"""play with text"""
monty = RunMontyLingua.MontyLingua()
# print(dir(monty))

text = "This is a sentence for testing the functionality of these modules. I really hope this doesn't fail."
print(f"{text=}\n")

tokenized_text = monty.tokenize(text)
print(f"{tokenized_text=}\n")

tag_tokenized_text = monty.tag_tokenized(tokenized_text)
print(f"{tag_tokenized_text=}\n")

lemmatised_text = monty.lemmatise_tagged(tag_tokenized_text)
print(f"{lemmatised_text=}\n")