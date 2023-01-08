import ast
import argparse
import re
def remove_comments(src):
    src = re.sub('#.*', '', src)
    f = []
    for i in src:
        if i != '\n' and i != ' ':
            f.append(i)
    return ''.join(f)


def levenshtein(text1, text2):
    return min(levenshtein(text1[1:], text2[1:])+(text1[0] != text2[0]),
               levenshtein(text1[1:], text2)+1,
               levenshtein(text1, text2[1:])+1)

parser = argparse.ArgumentParser(description='Levenshtein_distance_plagiarism')
parser.add_argument('Input', type=str, help='Input dir')
parser.add_argument('Output', type=str, help='Output dir')
args = parser.parse_args()
out_data = []
with open(args.Input) as load_data:
    for data in load_data:
        data = data.split()
        with open(data[0]) as text1:
            text1 = text1.read()
        with open(data[1]) as text2:
            text2 = text2.read()
        text1 = remove_comments(text1)
        text2 = remove_comments(text2)
        score = levenshtein(text1, text2) / len(text1)
        out_data.append(score)
with open(args.Output, 'w') as data:
    for score in out_data:
        data.write(score, '\n')
