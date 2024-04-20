import rtx_api.rtx_api_3_5 as rtx_api
import python_interface
import datetime
import time
import re
import os

def write_section(book_title, chapter, section_desc):
    prompt = "You are writing a book about: " + book_title + "." +\
        "You are writing chapter about: " + chapter + "." +\
        " Write a section title for: " + section_desc + ". Add double quotes around the new title."
    title_tmp = rtx_api.send_message(prompt)
    match = re.search(r'"(.*?)"', title_tmp)
    title = ""
    if match:
        title = match.group(1)

    prompt = "You are writing a book about: " + book_title + "." +\
            "You are writing chapter about: " + chapter + "." +\
            " Write a section about " + section_desc + "."
    section_text = rtx_api.send_message(prompt)
    lines = section_text.split('. ')
    if "section" in lines[0]:
        lines = lines[1:]
    section_text = ". ".join(lines)
    return title, section_text

def write_a_book(book_title):
    start_time_unix_ms = int(time.time() * 1000)
    res = []
    chapters = python_interface.generate_list("Write list of chapters for book about " + book_title)
    # chapters = chapters[:2]
    res.append("# " + book_title)
    for c in chapters:
        res.append("## " + c)
        sections = python_interface.generate_list("You are writing a book about: " + book_title + ". Write list of sections for book chapter about " + c)
        # sections = sections[:2]
        print(c)
        print("\t", sections)
        for s in sections:
            section_title, section_text = write_section(book_title, c, s)
            res.append("### " + section_title)
            res.append(section_text)
            print(section_text)

    end_time_unix_ms = int(time.time() * 1000)
    formatted_time = str(datetime.timedelta(seconds=int(end_time_unix_ms - start_time_unix_ms) / 1000))[:-7]
    time_str = "# Chat with RTX Llama 2 took " + formatted_time + " to write this book"
    res = [time_str] + res
    res.append(time_str)
    if not os.path.exists("books"):
        os.makedirs("books")
    book_str = "\n".join(res)
    book_filename = book_title.replace(' ', '_') + ".md"
    with open("books/" + book_filename, 'w', encoding='utf-8') as file:
        file.write(book_str)

if __name__ == '__main__':
    write_a_book("C programming language")
    write_a_book("CIA tactics")
    write_a_book("How to fly a 747")
    write_a_book("Modern radio link stack")
    write_a_book("Fall of the Roman Empire")

    write_a_book("Developing a scramjet (supersonic combustion ramjet) engine")
    write_a_book("Developing an external pulsed plasma propulsion engine")
    write_a_book("Developing a liquid-fuel rocket engine")
    write_a_book("Developing a super heavy-lift launch vehicle")
    write_a_book("Orbital mechanics")
    write_a_book("Spacecraft atmospheric re-entry")

    write_a_book("How to become a master yapper")
    write_a_book("How to write a book")
