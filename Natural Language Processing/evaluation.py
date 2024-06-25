from nltk.tokenize import word_tokenize
from nltk.translate.meteor_score import meteor_score
# import nltk
# nltk.download('wordnet')

def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().strip()

def tokenize_text(text):
    return word_tokenize(text)

# Read reference translation from a text file
reference_path = "tgt-val.txt"
reference_translation = read_text_file(reference_path)
reference_tokens = tokenize_text(reference_translation)

# Read hypothesis translation from a text file
hypothesis_path = "pred_1000.txt"
hypothesis_translation = read_text_file(hypothesis_path)
hypothesis_tokens = tokenize_text(hypothesis_translation)

# Compute METEOR score
meteor_score_value = meteor_score([reference_tokens], hypothesis_tokens)

# Print METEOR score
print("METEOR score:", meteor_score_value)



import sacrebleu
with open('tgt-val.txt', 'r', encoding="utf-8") as f:
    references = [line.strip() for line in f]
with open('pred_1000.txt', 'r',encoding="utf-8") as f:
    predictions = [line.strip() for line in f]

bleu = sacrebleu.corpus_bleu(predictions, [references])
print(f'BLEU score: {bleu.score}')