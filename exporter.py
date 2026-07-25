class Exporter:

    def save(

        self,

        entries,

        filename

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            for item in entries:

                file.write(

                    f"{item.word}: {item.count}\n"

                )
