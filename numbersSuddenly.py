import re
from random import shuffle
import sys

def format(**kwargs):
    """
    words is a list of words
    length is the amount of words per page
    """
    s = open("base.html").read();
    return s.format(words=",".join(kwargs["words"]), length=kwargs["length"], total=len(kwargs['words']))
    
minlen = 3 #it's better this way
NUMBER_OF_WORDS = 50
subs = [
    #almost entirely senseless variation
    ('sics', '6'),
    ('nein', '9'),
    ('ue', '00'),
    ('ah', '44'),
    ('ew', '300'),
    ('owe', '0'),
    ('oh', '0'),
    ('oe', '0'),
    #numberHomophones:number
    ('won', '1'),
    ('too', '2'),
    ('to', '2'),
    ('for', '4'),
    #('fore', '4'), #fore is represented as 43
    ('ate', '8'),
    #number spelt in word:number(s) - Theoretically infinite
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9'),
    ('ten', '10'),
    #increase in complexity/bizzareness (don't actually do anything)
    #('eleven', '11'),
    #('twelve', '12'),
    #('thirteen', '13'),
    #('fourteen', '14'),
    #1:1 letter:number(s)
    ('b', '13'), #adds complication
    ('z', '2'),
    ('g', '6'),
    ('l', '1'),
    ('o', '0'),
    ('s', '5'),
    ('t', '7'),
    ('e', '3'),
    ('a', '4'),
]

reHexWord = re.compile("[0-9]*")
gue = re.compile("gue") #removing phonetically dissimlar 'ue's
if sys.platform == "win32":
    fWords = open("enable1.txt")
else:
    fWords = open('/usr/share/dict/words', 'r')
output = open("output.html", 'w')
if sys.version_info[0] >= 3:
    fWords.xreadlines = fWords.readlines
    xrange = range
end = []
for w in fWords.xreadlines():
    w = w.strip()
    z = w
    for old, new in subs:
        w = w.replace(old, new)
    if len(w) >= minlen:
        match = reHexWord.search(w)
        if match and match.group() == w and not gue.search(z):
            end.append(r""""<tr><td class=\"spoiler\" onclick=\"this.style.color='black'\">%s </td><td> %s </td></tr>"
            """ % (z,w))
shuffle(end) #If you've seen the list, it's no longer a game
output.write(format(words=end, length=NUMBER_OF_WORDS))