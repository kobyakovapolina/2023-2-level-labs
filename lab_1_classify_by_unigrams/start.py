"""
Language detection starter
"""
#from lab_1_classify_by_unigrams.main import create_language_profile
import lab_1_classify_by_unigrams.main


def main() -> None:
    """
    Launches an implementation
    """
    with open("assets/texts/en.txt", "r", encoding="utf-8") as file_to_read_en:
        en_text = file_to_read_en.read()
        en_tokens = lab_1_classify_by_unigrams.main.tokenize(en_text)
        print(en_tokens)
        language_profile = lab_1_classify_by_unigrams.main.create_language_profile('en', en_text)
        print(language_profile)
    with open("assets/texts/de.txt", "r", encoding="utf-8") as file_to_read_de:
        de_text = file_to_read_de.read()
    with open("assets/texts/unknown.txt", "r", encoding="utf-8") as file_to_read_unk:
        unknown_text = file_to_read_unk.read()
    #print(tokenize(en_text))
    #print(calculate_frequencies(tokenize(en_text)))
    #print(create_language_profile('en', en_text))

    #result = None
    #assert result, "Detection result is None"

if __name__ == "__main__":
    main()
