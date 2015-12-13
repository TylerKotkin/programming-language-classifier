# <div align="center">Programming Language Classifier </div>

The Programming Language Classifier is designed to take a snippet of code and identify the programming language used.

Two IPython notebooks are included in the repository:
* programming_language_classifier.ipynb uses a MultinomialNB classifier
* custom_programming_language_classifier.ipynb uses a custom classifier

The test data used was downloaded from the [Computer Language Benchmarks Game](http://benchmarksgame.alioth.debian.org/). It can be downloaded [here](https://alioth.debian.org/snapshots.php?group_id=100815).

### <div align="center">Compatible Languages </div>
* C (.gcc, .c)
* C#
* Common Lisp (.sbcl)
* Clojure
* Haskell
* Java
* JavaScript
* OCaml
* Perl
* PHP (.hack, .php)
* Python
* Ruby (.jruby, .yarv)
* Scala
* Scheme (.racket)

## <div align="center">Instructions</div>

* The Programming Language Classifier notebooks can be viewed on GitHub or downloaded to the users computer.
* Before the user can open the Programming Language Classifier notebooks on their computer, the user must first clone the `programming-language-classifier` repo onto their computer. The user must have Python 3 installed.
* To properly run the notebook, the contents of requirements.txt must be installed.
  * After navigating to the folder containing `programming_language_classifier.ipynb` and `custom_programming_language_classifier.ipynb`, enter `pip install -r requirements.txt` on the command-line to download the contents of requirements.txt.
* The user can enter `ipython notebook programming_language_classifier.ipynb` on the command-line to open the MultinomialNB classifier notebook or `ipython notebook custom_programming_language_classifier.ipynb` to open the custom classifier.
