from collections import Counter

from models import WordEntry

class Analyzer:

    def analyze(

        self,

        words

    ):

        counter = Counter(words)

        return [

            WordEntry(

                word,

                count

            )

            for word, count

            in counter.most_common()

        ]
