
# függvény ami karaktereket,szavakat számol


def char_counter(a: str): return a.count("a")


print(char_counter("kugya"))


# beljebb viszi a szöveget

def word_pusher(a: str): return a.center(60)


print(word_pusher("kutya"))


# függvény ami karaktereket,szavakat, számokat egy listában
def list_thing_counter(a: list): return a.count(10)


print(list_thing_counter([10, 10, "kutya"]))


# függvény ami kitöröl mindent a listából
def list_killer(a: list): return a.clear()


print(list_killer([10,10,"kutya"]))



# függvény ami másolatot csinál egy listáról
def kak(a: list): return a.copy()


print(kak([10,10,"kutya"]))


