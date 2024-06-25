# from onmt.bin.train import main
#
# if __name__ == "__main__":
#     config_path = "config.yaml"
#     main(config_path)
# import sacrebleu
# with open('tgt-test.txt', 'r') as f:
#     references = [line.strip() for line in f]
# with open('pred_1000.txt', 'r') as f:
#     predictions = [line.strip() for line in f]
#
# bleu = sacrebleu.corpus_bleu(predictions, [references])
# print(f'BLEU score: {bleu.score}')
#
# from mlmorph import Analyser
# analyser = Analyser()
# print(analyser.analyse("കിഴക്ക്"))

from indicnlp import common
from indicnlp.morph import unsupervised_morph

# Initialize IndicNLP resources
common.INDIC_RESOURCES_PATH = ""

# Initialize unsupervised morphological analyzer
analyzer = unsupervised_morph.UnsupervisedMorphAnalyzer('ml')

# Path to the input Kannada text file
kannada_file_path = "tgt-train.txt"

# Open the Kannada text file
with open(kannada_file_path, "r", encoding="utf-8") as file:
    # Read each line (sentence) from the file
    with open("morph/tgt-train.txt", "w", encoding="utf-8") as output_file:
        for line in file:
            # Remove leading and trailing whitespace
            line = line.strip()
            # Perform morphological analysis on the line
            morph_analyzed_tokens = analyzer.morph_analyze_document(line.split(' '))
            # Display the morphological analysis
            # print(f"Kannada Sentence: {line}")
            # print(" ".join(morph_analyzed_tokens))
            output_file.write(" ".join(morph_analyzed_tokens))
            output_file.write("\n")
        # for token, analysis in zip(line.split(), morph_analyzed_tokens):
        #     print(f"Token: {token}")
        #     print(morph_analyzed_tokens)
            # for morph in analysis:
            #     print(f"Lemma: {morph['lemma']}, Morphemes: {morph['morphemes']}")
            # print("---------------")


# from indicnlp.morph import unsupervised_morph
# from indicnlp import common
#
# common.INDIC_RESOURCES_PATH=""
#
# analyzer=unsupervised_morph.UnsupervisedMorphAnalyzer('kn')
#
# indic_string="ಇವರು ಸಂಶೋಧಕ ಸ್ವಭಾವದವರು"
#
# analyzes_tokens=analyzer.morph_analyze_document(indic_string.split(' '))
# print(analyzes_tokens)
