import re

class Tokenizer:

    def tokenize(

        self,

        text

    ):

        text = text.lower()

        text = re.sub(

            r"[^a-z0-9 ]",

            " ",

            text

        )

        return [

            word

            for word in text.split()

            if word

        ]
