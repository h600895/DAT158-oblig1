nor_pattern = "versj"
eng_pattern = "versi"

nor_alphabet = "abcdefghijklmnopqrstuvwxyzæøå "
eng_alphabet = "abcdefghijklmnopqrstuvwxyz "


nor_text = "I motsetning til hva mange tror, er Lorem Ipsum ikke bare tilfeldig tekst. Den har røtter i et stykke klassisk latinsk litteratur fra 45 f.Kr., noe som gjør den over 2000 år gammel. Richard McClintock, en latinprofessor ved Hampden-Sydney College i Virginia, slo opp et av de mer obskure latinske ordene, consectetur, fra en Lorem Ipsum-passasje, og gikk gjennom sitatene til ordet i klassisk litteratur, og oppdaget den utvilsomme kilden. Lorem Ipsum kommer fra seksjonene 1.10.32 og 1.10.33 av de Finibus Bonorum et Malorum (The Extremes of Good and Evil) av Cicero, skrevet i 45 f.Kr. Denne boken er en avhandling om teorien om etikk, veldig populær under renessansen. Den første linjen i Lorem Ipsum, Lorem ipsum dolor sit amet.., kommer fra en linje i avsnitt 1.10.32."
eng_text = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32."


def removeSymbols(text):
    symbols = ",.-1234567890?!"

    for s in symbols:
        text = text.replace(s, "")
    return text
