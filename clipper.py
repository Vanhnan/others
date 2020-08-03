import sys
import pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?""",
        'отвали': """СЛЫШЬ ОТВАЛИ !!!! """
}

if len(sys.argv) < 2:
    print('HOw to use: python clipper.py keyphrase')
    sys.exit()

keyphrase = sys.argv[1] 
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("succesfully copied")
else:
    print("couldn't find that keyword (")
