from collections import Counter
import re


hipster_lorem = """
Messenger bag excepteur anim mlkshk. Chillwave Tonx Shoreditch Carles. Ethical vero skateboard, mixtape you probably haven't heard of them lo-fi occaecat. Ad four loko nesciunt, letterpress Neutra salvia meh excepteur qui typewriter fixie bicycle rights Pitchfork banjo cillum. YOLO retro sunt Cosby sweater occaecat hoodie. Slow-carb incididunt Terry Richardson PBR tousled ex, bespoke ugh locavore farm-to-table hella. Non banh mi Banksy accusamus occaecat kitsch.

Bicycle rights Wes Anderson Marfa photo booth polaroid pork belly eu slow-carb. Forage jean shorts food truck, viral duis letterpress XOXO freegan. Church-key pour-over bicycle rights Truffaut Portland, small batch velit authentic narwhal sed roof party banh mi. Duis laboris pickled, fashion axe mumblecore deep v ea jean shorts. Skateboard Helvetica voluptate Terry Richardson sed, cornhole chambray lomo disrupt. Tonx chambray proident wayfarers Carles flexitarian, meh nostrud cliche Neutra Bushwick hella. 3 wolf moon trust fund gentrify, Williamsburg tousled culpa scenester roof party.

Nesciunt drinking vinegar forage in, yr post-ironic letterpress before they sold out fugiat tote bag. Kale chips pariatur PBR cillum umami, gentrify sunt iPhone Vice fashion axe Williamsburg Intelligentsia ut culpa post-ironic. Nesciunt slow-carb iPhone, esse you probably haven't heard of them butcher beard Terry Richardson actually cornhole fashion axe. Sriracha fugiat cillum, lo-fi occupy pour-over Tonx food truck hella gastropub Austin sint ennui. Anim ex post-ironic qui salvia bespoke, bitters eiusmod ethical mustache proident forage irure Pinterest. Qui bitters bicycle rights, non locavore PBR&B incididunt leggings slow-carb farm-to-table whatever Godard. Swag aliquip biodiesel, cornhole pour-over proident lo-fi ea PBR&B wolf.

Sriracha vegan cred, hoodie umami tousled cupidatat banh mi sapiente swag lomo irony skateboard. 90's tofu street art, semiotics post-ironic ex bicycle rights beard small batch consectetur. Tempor lo-fi incididunt kale chips. Pickled keffiyeh ullamco YOLO Bushwick vegan authentic quis. Brooklyn pork belly vero polaroid lomo. Duis officia Truffaut mixtape roof party aliqua. Master cleanse chillwave chia 3 wolf moon commodo, drinking vinegar vegan put a bird on it.
"""

stripped_lorem = re.sub(r'\.|,', '', hipster_lorem)
words = stripped_lorem.split()

counter = Counter(words)

s = sum(counter.values())
print("total words: {}".format(s))
print

print("most common:")
for word, count in counter.most_common(10):
    print("({}) {}".format(count, word))
print

print("least common:")
for word, count in counter.most_common()[-10:-1]:
    print("({}) {}".format(count, word))
print 

# list() will get only unique elements. can also use set() and dict()
as_list = list(counter)
print('unique count: {0}'.format(len(as_list)))

a = Counter(farms=5, tomatoes=1233)
b = Counter(farms=2, tomatoes=999)

print('a + b: {0}'.format(a + b))
print('a - b: {0}'.format(a - b))
# this results in an empty counter:
print('b - a: {0}'.format(b - a))
# intersection - min(a[x], b[x])
print('a & b: {0}'.format(a & b))
# union - max
print('a | b: {0}'.format(a | b))
