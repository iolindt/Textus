class Statistics:

    def build(

        self,

        words,

        entries

    ):

        return {

            "total_words": len(words),

            "unique_words": len(entries),

            "most_common": entries[0].word

        }

    def print(

        self,

        stats

    ):

        print()

        print("Statistics\n")

        print(

            f"Words: {stats['total_words']}"

        )

        print(

            f"Unique: {stats['unique_words']}"

        )

        print(

            f"Most common: {stats['most_common']}"

        )
