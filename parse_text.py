def parse(filename):
    valid_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','?',',','\'',':','!',';']

    # load ascii text and covert to lowercase
    raw_text = open(filename).read().lower().replace("--",";")

    wordlist = []
    s = ""

    # split the raw text into valid "words" (punctuation are words in this case)
    for i in range(0,len(raw_text)):
        x = i
        # space or return -> store word
        if raw_text[x] == ' ' or raw_text[x] == '\n':
            if len(s) > 0:
                wordlist.append(s)
            s = ""
        # include only valid characters
        elif raw_text[x] in valid_chars:
            if raw_text[x].isalpha():
                s += raw_text[x]
            else:
                # for I'll, don't, alice's, etc...
                if raw_text[x] == '\'' and ( raw_text[x+1] == 's' or raw_text[x+1] == 't' or raw_text[x+1] == 'm' or raw_text[x+1] == 'l' ):
                    s += raw_text[x]
                else:
                    if len(s) > 0:
                        wordlist.append(s)
                    wordlist.append(raw_text[x])
                    s = ""
    return wordlist