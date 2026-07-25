class Formatter:

    def display(

        self,

        entries,

        limit

    ):

        print()

        print("Word Frequency\n")

        for item in entries[:limit]:

            print(

                f"{item.word:<15}{item.count}"

            )
