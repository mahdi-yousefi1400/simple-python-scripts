# یک رشته را از کاربر بگیر ید و سپس تعداد جمله ها، تعداد کلمه ها، تعداد کل کاراکتر ها ) مثال حروف، فاصله، نقطه، ویرگول
# تعداد حروف انگلیسی مثل a، b، c و... را چاپ کند.
string_user = input("Enter string =")

string_user_count = string_user.count('.') + string_user.count('!') + string_user.count('?') + string_user.count('؟')
word = string_user.split()
word_count = len(word)
char_count = len(string_user)
alpa_count = (
    string_user.count('a') + string_user.count('b') + string_user.count('c') + string_user.count('d') +
    string_user.count('e') + string_user.count('f') + string_user.count('g') + string_user.count('h') +
    string_user.count('i') + string_user.count('j') + string_user.count('k') + string_user.count('l') +
    string_user.count('m') + string_user.count('n') + string_user.count('o') + string_user.count('p') +
    string_user.count('q') + string_user.count('r') + string_user.count('s') + string_user.count('t') +
    string_user.count('u') + string_user.count('v') + string_user.count('w') + string_user.count('x') +
    string_user.count('y') + string_user.count('z') +
    string_user.count('A') + string_user.count('B') + string_user.count('C') + string_user.count('D') +
    string_user.count('E') + string_user.count('F') + string_user.count('G') + string_user.count('H') +
    string_user.count('I') + string_user.count('J') + string_user.count('K') + string_user.count('L') +
    string_user.count('M') + string_user.count('N') + string_user.count('O') + string_user.count('P') +
    string_user.count('Q') + string_user.count('R') + string_user.count('S') + string_user.count('T') +
    string_user.count('U') + string_user.count('V') + string_user.count('W') + string_user.count('X') +
    string_user.count('Y') + string_user.count('Z')
)
print(word)
print(word_count)
print(char_count)
print(alpa_count)


