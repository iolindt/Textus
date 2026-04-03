import re
from collections import Counter
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class AnalysisResult:
    word_count: int
    unique_words: int
    char_count: int
    sentence_count: int
    most_common_words: List[tuple]


class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text
        self.cleaned_text = self._clean_text()

    def _clean_text(self) -> str:
        return re.sub(r"[^\w\s]", "", self.text.lower())

    def get_words(self) -> List[str]:
        return self.cleaned_text.split()

    def word_count(self) -> int:
        return len(self.get_words())

    def unique_words(self) -> int:
        return len(set(self.get_words()))

    def char_count(self) -> int:
        return len(self.text)

    def sentence_count(self) -> int:
        sentences = re.split(r"[.!?]+", self.text)
        return len([s for s in sentences if s.strip()])

    def most_common_words(self, n=5) -> List[tuple]:
        return Counter(self.get_words()).most_common(n)

    def analyze(self) -> AnalysisResult:
        return AnalysisResult(
            word_count=self.word_count(),
            unique_words=self.unique_words(),
            char_count=self.char_count(),
            sentence_count=self.sentence_count(),
            most_common_words=self.most_common_words()
        )


class CLI:
    @staticmethod
    def run():
        print("=== Advanced Text Analyzer ===")
        text = input("Enter text: ")

        analyzer = TextAnalyzer(text)
        result = analyzer.analyze()

        CLI.display(result)

    @staticmethod
    def display(result: AnalysisResult):
        print("\n--- Analysis Result ---")
        print(f"Total words: {result.word_count}")
        print(f"Unique words: {result.unique_words}")
        print(f"Characters: {result.char_count}")
        print(f"Sentences: {result.sentence_count}")
        print("Most common words:")

        for word, count in result.most_common_words:
            print(f"  {word}: {count}")


if __name__ == "__main__":
    CLI.run()
