#from utils.function import add
from utils.count import count_word,word_count
if __name__ == '__main__':
    s = "hello world"
    print("e:",count_word(s,'e'))
    print("o:",count_word(s,'o'))
    print("l:",count_word(s,'l'))
    word_count(s,"aaa")

    #n = add(1,2)
    #print(n)
