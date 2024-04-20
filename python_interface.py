import rtx_api.rtx_api_3_5 as rtx_api
import re

def boolean_question(prompt):
    prompt = prompt + "?"
    # maybe like ask the question in 5 different ways
    res = rtx_api.send_message(
        "Answer with yes or no. Is the following statement true: " + prompt
        # "Determine if the given statement is true or false, and write boolean string true or false. nothing else. " +\
        # "Your first word has to be false or true. Here is the question: " + prompt
    )
    res = res.lower()
    if res.startswith("yes"):
        return True
    return False

def generate_list(prompt):
    def remove_duplicates(lst):
        seen = []
        for item in lst:
            if item not in seen:
                seen.append(item)
        return seen

    def remove_leading_number(s):
        return re.sub(r'^\d+\.?\d*', '', s)

    res = rtx_api.send_message(prompt)
    res = res.split("\n")
    res = [s.strip() for s in res]
    res = [s for s in res if s]
    res = [s[1:] if s.startswith('*') else s for s in res]

    res = [s.strip() for s in res]
    res = [s for s in res if "exhaustive list" not in s.lower()]
    res = [s for s in res if "let me know" not in s.lower()]
    res = [s for s in res if "hope this" not in s.lower()]
    res = [s for s in res if "please note" not in s.lower()]
    res = [s for s in res if "subject to change" not in s.lower()]
    res = [remove_leading_number(s) for s in res]
    res = [s.strip() for s in res]
    res = [s for s in res if s]
    if res[0][-1] == ':':
        res = res[1:]

    res = remove_duplicates(res)

    # for s in res[:]:
    #     if not boolean_question("I have a list of" + prompt + ". Does this belong to the list: " + s + " Here is the full list: " + str(res)):
    #         print("!!! Removing: " + s)
    #         res.remove(s)

    return res

def generate_code(prompt):
    # return ''' this '''
    pass

def improve_sentence_grammar(prompt):
    text = rtx_api.send_message(
        "Please correct and enhance the following sentence to improve its grammar, punctuation, spelling, vocabulary, coherence, and cohesion. " +\
        "The sentece: " + prompt + ". Add double quotes around the new sentence."
    )
    match = re.search(r'"(.*?)"', text)
    if match:
        content = match.group(1)
        return content
    else:
        return prompt

def improve_text_grammar(prompt):
    res = []
    sentences = prompt.split('. ')
    for s in sentences:
        res.append(improve_sentence_grammar(s + '.'))
    res_str = " ".join(res)
    return res_str


# #true
# print(boolean_question("1 + 1 = 2"))
# print(boolean_question("5 * 5 = 25"))
# print(boolean_question("234 / 10 = 23.4"))
# print(boolean_question("cherry and crimson are both red colors"))
# print(boolean_question("cherry and crimson are similar colors"))
# print(boolean_question("""The following text contains only code:
#     res = []
#     sentences = prompt.split('. ')
#     for s in sentences:
# """))

# print("")
# #false
# print(boolean_question("red and blue are similar colors"))
# print(boolean_question("c is slower than python"))

# print(generate_list("Write a list of planets"))
# print(generate_list("Write a list of car brands"))
# print(generate_list("Write a list of most sold videogames"))

# print(improve_sentence_grammar("git sybmodule add"))
# print(improve_sentence_grammar("Solidfuel rcket engines are the simplest and most reliable type ofrpcket engine."))
# print(improve_text_grammar("Solidfuel rcket engines are the simplest and most reliable type of rocket engine. They conist of a solid ful that is burned to produce thrust. The main advantage of solid-fual rocket engines is their simplicity and reliability. They are easy to manufacture and maintain, and they do not require any complx plumbing or fuel systems. However, they have limited control over the thrust and direction of the ricket, and they cannot be shut down once they have been ignited."))

