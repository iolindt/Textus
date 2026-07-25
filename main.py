from config import TOP_WORDS
from config import OUTPUT_FILE

from repository import Repository
from reader import Reader
from tokenizer import Tokenizer
from analyzer import Analyzer
from formatter import Formatter
from exporter import Exporter
from statistics import Statistics

text = Repository().load()

text = Reader().read(

    text

)

words = Tokenizer().tokenize(

    text

)

entries = Analyzer().analyze(

    words

)

Formatter().display(

    entries,

    TOP_WORDS

)

stats = Statistics().build(

    words,

    entries

)

Statistics().print(

    stats

)

Exporter().save(

    entries,

    OUTPUT_FILE

)
