# Summary

CINTIL-UDep is a dependency bank of Portuguese that is treebanked with Universal Dependencies.
It contains over 38K annotated sentences (and 476K tokens), of mostly newspaper text.


# Introduction

CINTIL-UDep is a dependency bank of Portuguese with 38,400 sentences (and nearly 476,000 tokens), that is treebanked with Universal Dependencies (UD).

CINTIL-UDep was obtained through the merger and automatic conversion to UD of two non-UD dependency banks, [CINTIL-DependencyBank](https://hdl.handle.net/21.11129/0000-000B-D31C-8) and [CINTIL DependencyBank PREMIUM](https://hdl.handle.net/21.11129/0000-000B-D378-0).

* CINTIL-DependencyBank was manually annotated with the support of the LXGram deep computational grammar (Costa and Branco, 2010). For each sentence, a parse forest is generated by the grammar with all possible grammatical analyses for that sentence. The human annotator is then tasked with picking the correct analysis from those in the forest. This method ensures precise and highly consistent analyses throughout the treebank.
* CINTIL DependencyBank PREMIUM was created through a different process, though it adheres to the same guidelines as the previous treebank. In CINTIL DependencyBank PREMIUM, human annotators manually corrected the output of a statistical dependency parser. Since this treebank was initially annotated with a statistical parser, it contains sentences that instantiate linguistic phenomena that may not be present in the previous, grammar-based treebank, as computational grammars, albeit precise, have suboptimal coverage.

For more details, refer to (Branco _et al._, 2022), the canonical reference given below.

# Acknowledgments

This work was partly supported by [PORTULAN CLARIN Research Infrastructure for the Science and Technology of Language](https://portulanclarin.net), funded by Lisboa 2020, Alentejo 2020, and FCT-Fundação para a Ciência e Tecnologia under the grant PINFRA/22117/2016; by FCT-Fundação para a Ciência e Tecnologia through the Portuguese project DP4LT (PTDC/EEI-SII/1940/2012); and by the European Commission through the European project QTLeap (EC/FP7/610516).

# References

CINTIL-UDep is described in the following article

* Branco, António, João Ricardo Silva, Luís Gomes, and João Rodrigues, 2022. Universal Grammatical Dependencies for Portuguese with CINTIL Data, LX Processing and CLARIN support. In _Proceedings of the 13th Conference on Language Resources and Evaluation (LREC 2022)_.

which should be used as its canonical citation, and which interested users are referred to for detailed information.

The source treebanks for CINTIL-UDep dependency bank were [CINTIL-DependencyBank](https://hdl.handle.net/21.11129/0000-000B-D31C-8) and [CINTIL DependencyBank PREMIUM](https://hdl.handle.net/21.11129/0000-000B-D378-0), which were initially manually annotated with different guidelines, as described in:

* de Carvalho, Rita, Andreia Querido, Marisa Campos, Rita Pereira, João Silva, and António Branco, 2016. CINTIL DependencyBank PREMIUM: A corpus of grammatical dependencies for Portuguese. In _Proceedings of the 10th International Conference on Language Resources and Evaluation (LREC 2016)_.
* Branco, António, Francisco Costa, João Silva, Sara Silveira, Sérgio Castro, Mariana Avelãs, Clara Pinto, and João Graça, 2010. Developing a deep linguistic databank supporting a collection of treebanks: the CINTIL DeepGramBank. In _Proceedings of the 7th International Conference on Language Resources and Evaluation (LREC 2010)_.

Other relevant references are:

* Costa, Francisco, and António Branco, 2010. LXGram: A deep linguistic grammar processing grammar for Portuguese. In _Proceedings of the International Conference and Computational Processing of the Portuguese Language (PROPOR 2010)_.

# Changelog

* 2022-11-15 v2.11
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.11
License: CC BY-NC-ND 4.0
Includes text: yes
Genre: news fiction
Lemmas: automatic with corrections
UPOS: converted from manual
XPOS: automatic with corrections
Features: converted from manual
Relations: converted from manual
Contributors: Silva, João Ricardo
Contributing: elsewhere
Contact: jrsilva@fc.ul.pt
===============================================================================
</pre>