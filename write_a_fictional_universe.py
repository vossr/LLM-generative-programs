import rtx_api.rtx_api_july_2024 as rtx_api
import datetime
import time
import os
import re

def write_story(description):
    msg = f"For this world and setting description: {description}" +\
    "Write a high level narrative structure for a story taking place in the described setting. " +\
    "Leave some things mysterious, to extend the world past the story. " +\
    "Enrich the character background details. " +\
    "Most stories about ordinary people. " +\
    "Story has a message, a extrapolatable moral. " +\
    "People experiencing this story should see themselves enjoying living in it. "
    narrative = ""
    for i in range(2):
        narrative += rtx_api.send_message(msg + narrative)
        print("narrative", narrative)
        print("-------------------------------------\n")
    return narrative

def create_setting(description):
    msg = f"For this world description: {description}" +\
    " Create a setting where some stories can take place." +\
    " For the setting, describe its time period and duration. Are there any major conflicts (optional). Describe specific locations in detail. "

    setting = ""
    # for i in range(3):
    setting += rtx_api.send_message(msg + setting)
    print("setting", setting)
    print("-------------------------------------\n")

    return setting

def worldbuilding_start(og_description):
    worldbuilding_steps = [
"""
Foundation of the universe
        if relevant: write list of real world mythological or historical influences.
        if relevant: describe magical systems or elements, enchanted objects or artifacts.
        theme, underlying messages, moral questions and emotional tones.
""",
"Geography and environment of the described world",
"Culture, theology, races and society. Customs, traditions and norms, linguistic diversity and charasteristics of the described world",
"If relevant, write about magic technology and the supernatural of the described world"
"History, chronology, myth and religion of the described world. major historical changes in the world that impact the stories.",
]

    description = " "
    for i, step in enumerate(worldbuilding_steps):
        tmp = rtx_api.send_message(f"For this world description: {og_description + description} \nIn creative worldbuilding context, write about {step}")
        if description[-1] == '.':
            description += " "
        if description[-1] != ' ':
            description += ". "
        description += tmp
        print(description)
        print("-------------------------------------\n")
    
        if i and i < len(worldbuilding_steps) - 1:
            print("improve consistency")
            description = rtx_api.send_message(f"Improve consistency of this world description: {description} \nIn creative worldbuilding context, improve consistency of the text")
            # print(description)
            # print("-------------------------------------\n")
    return description

def name_universe(description):
    uname = rtx_api.send_message(f"For this world description: {description} \n Write a good name to describe this universe. name the universe. respond with a name for the universe")
    tmp = uname.split('"')
    if len(tmp) > 2:
        uname = tmp[1]
    uname = re.sub(r'[^a-zA-Z0-9 ]', '', uname)

    if not uname:
        tmp = description.split()
        uname = tmp[0] + tmp[1]
        uname = re.sub(r'[^a-zA-Z0-9 ]', '', uname)
    print("name", uname)
    print("-------------------------------------\n")
    return uname

def build_a_world(description):
    start_time_unix_ms = int(time.time() * 1000)
    description = worldbuilding_start(description)
    setting = create_setting(description)
    story = write_story(description + setting)
    res = "# World\n" + description + "\n\n\n\n\n# Setting\n" + setting + "\n\n\n\n\n# Story\n" + story + '\n'

    uname = name_universe(description)

    end_time_unix_ms = int(time.time() * 1000)
    formatted_time = str(datetime.timedelta(seconds=int(end_time_unix_ms - start_time_unix_ms) / 1000))[:-7]
    # time_str = "# Chat with RTX Llama 2 took " + formatted_time + " to write this book"
    time_str = "# Chat with RTX Mistral took " + formatted_time + " to build this world\n"
    message = "# Intended as parody and/or educational on generative llms\n"
    res = time_str + message + res + time_str + message
    if not os.path.exists("worlds"):
        os.makedirs("worlds")
    with open("worlds/" + uname + '.md', 'w', encoding='utf-8') as file:
        file.write(res)

    print("\n----------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------\n")

if __name__ == '__main__':
    build_a_world("18th century, Golden Age of Piracy.")
    build_a_world("Steampunk")
    build_a_world("Full galaxy wide warfare, exotic weapon systems, different factions, humanoid robot technology, cloning and accelerated growth of biological life.")
    build_a_world("In the late 21st century, as the decade began, a wave of technological optimism swept through society, reshaping its values and philosophical outlook. So a very rational and realistic scientific exploration.")
    build_a_world("Fantasy world where a clan of evil T-rex dinosaurs rule over the land. Humans compete for resources with all the other wild animals.")
    build_a_world("WW2 but gunpowder is not invented, only melee weapons. Otherwise a fully realistic historical violent description of 1940s")
