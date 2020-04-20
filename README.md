# MontyLingua
### A Free, Commonsense-Enriched Natural Language Understander for English
http://alumni.media.mit.edu/~hugo/montylingua/


I was looking for ways to do word conjugation/tense variation and stumbled across this old language processing toolkit from 2004. 
I ran `2to3.py -w` on the extracted zip and then...
```
import sys
import re
from pathlib import Path

for py_file in Path(path).glob('**/*.py'):
    print(f"converting {py_file}")
    py_text = re.sub(r'[\t]', '    ', py_file.read_text())
    py_file.write_text(py_text)
```
... to fix some of the indentation issues. After that, some Python2 methods needed to be transcribed/adjusted to their Python3 equivalents. Some of the file organization/logic was weird so I've changed it so things can be imported and used more easily. I wanted MontyLingua to behave more like a usual package you'd have in your site-packages folder.

## From Hugo Liu's site:

Recent bugfixes

Version 2.1 (6 Aug 2004)
- includes new MontyNLGenerator component generates sentences and summaries

Version 2.0.1
- fixes API bug in version 2.0 which prevents java api from being callable

What is MontyLingua?

MontyLingua is a free*, commonsense-enriched, end-to-end natural language understander for English. Feed raw English text into MontyLingua, and the output will be a semantic interpretation of that text. Perfect for information retrieval and extraction, request processing, and question answering. From English sentences, it extracts subject/verb/object tuples, extracts adjectives, noun phrases and verb phrases, and extracts people's names, places, events, dates and times, and other semantic information. MontyLingua makes traditionally difficult language processing tasks trivial!

Version 2.0 is substantially FASTER, MORE ACCURATE, and MORE RELIABLE than version 1.3.1. It has now been tested across Windows, many flavors of UNIX, and Mac OS X, and several flavors of Java, and is in use by several university research projects and under several commercial settings.

MontyLingua differs from other natural language processing tools because:

    it is complete end-to-end.. input raw_text; output semantic interpretation
    not many dated tools and implementations sewn together; it is one well-integrated implementation
    it does not require "training" and other fidgetting, and will work right out-of-the-box
    it is enriched with "common sense" knowledge about the everyday world, allowing it to escape many stupid interpretive mistakes. e.g.:
        "(NX the/DT mosquito/NN bit/NN NX) (NX the/DT boy/NN NX)" ==corrected==>
        "(NX the/DT mosquito/NN NX) (VX bit/VBD VX) (NX the/DT boy/NN NX)"
    it is lightweight and portable across platforms, written in portable Python and also available as a compiled Java library
    it is easy to customize by allowing for a user lexicon

MontyLingua performs the following tasks over text:

    MontyTokenizer - Tokenizes raw English text (sensitive to abbreviations), and resolve contractions, e.g. "you're" ==> "you are"
    MontyTagger - Part-of-speech tagging based on Brill94, enriched with common sense.
    MontyChunker - Lightning fast regular expression chunker
    MontyExtractor - Extracts phrases and subject/verb/object triplets from sentences
    MontyLemmatiser - Strips inflectional morphology, i.e. changes verbs to infinitive form and nouns to singular form
    MontyNLGenerator - Uses MontyLingua's concise predicate-arg representation to generate naturalistic English sentences and text summaries

* free for non-commercial use. please see MontyLingua Version 2.0 License

Terms of Use [top]

Author: Hugo Liu <hugo@media.mit.edu>
Project Page: <http://web.media.mit.edu/~hugo/montylingua/>

Terms of Use

Copyright (c) 2002-2004 by Hugo Liu, MIT Media Lab
All rights reserved.

Non-commercial use is free, as provided in the MontyLingua version 2.0 License. By downloading and using MontyLingua, you agree to abide by the additional copyright and licensing information in "license.txt", included in this distribution.

If you use this software in your research, please acknowledge MontyLingua and its author, and link to back to the project page http://web.media.mit.edu/~hugo/montylingua.

Please cite montylingua in academic publications as:

Liu, Hugo (2004). MontyLingua: An end-to-end natural
language processor with common sense. Available
at: web.media.mit.edu/~hugo/montylingua.
