import rtx_api.rtx_api_3_5 as rtx_api
import python_interface
import datetime
import time
import os

def write_an_episode(show_title, show_description, episode_title, episode_description):
    scene_list = python_interface.generate_list("You are a Professional screenwriter for a TV show called: " + show_title + ". " +\
        show_description + " Write a list of scenes for the episode called: " + episode_title +\
        ". Here is the episode description: " + episode_description
    )
    res = []
    # scene_list = scene_list[:2]
    for scene_idx, scene_desc in enumerate(scene_list):
        res.append("### Scene " + str(scene_idx + 1) + ", " + episode_description)
        scene_script = rtx_api.send_message("You are a Professional screenwriter for a TV show called: " + show_title + ". " +\
            show_description + ". You are writing an episode about" + episode_description + " Write the screenplay to this scene: " + scene_desc)
        res.append(scene_script)
        print(scene_script)
    return res

def write_a_tv_show(show_title, show_description):
    start_time_unix_ms = int(time.time() * 1000)
    res = []

    res.append("# " + show_title)
    episodes = python_interface.generate_list("You are a Professional TV show writer. Give all characters a name. Be creative. " +\
                        "Write a long list of episode descriptions for a tv show about " + show_description)
    # episodes = episodes[:2]
    for episode_idx, c in enumerate(episodes):
        print(c)
        episode_title = ""
        desc = c.split(':')
        if len(desc) >= 2:
            desc[0].replace('"', '')
            episode_desc = desc[1]
        else:
            episode_desc = desc[0]
        res.append("## Episode " + str(episode_idx + 1) + " " + episode_title)
        print(episode_title)
        print("\t" + episode_desc)
        ep = write_an_episode(show_title, show_description, episode_title, episode_desc)
        res += ep

    end_time_unix_ms = int(time.time() * 1000)
    formatted_time = str(datetime.timedelta(seconds=int(end_time_unix_ms - start_time_unix_ms) / 1000))[:-7]
    time_str = "# Chat with RTX Mistral took " + formatted_time + " to write this tv show"
    res = ["# Inteded as parody and/or educational on generative llms"] + res
    res = [time_str] + res
    res.append(time_str)
    if not os.path.exists("tv_shows"):
        os.makedirs("tv_shows")
    show_str = "\n".join(res)
    show_filename = show_title.replace(' ', '_') + ".md"
    with open("tv_shows/" + show_filename, 'w', encoding='utf-8') as file:
        file.write(show_str)

if __name__ == '__main__':
    write_a_tv_show("Matrices", "Series that revolves around a dystopian future where humanity is unknowingly trapped inside a simulated reality called the Matrices, created by sentient machines to distract humans while using their bodies as an energy source. The protagonist, One, is awakened to the real world by rebels who try to end the war between humans and machines. Throughout the series, One improves his hacking skills and confronts the robots in explosive action gunfigts. The narrative explores themes of fate, choice, and the nature of consciousness. Support characters include morphed and triangle")
    write_a_tv_show("Band of UAV Brothers", "Series that follows a parachute infantry regiment in the 42nd Airborne Division of the US Army, Drone attack company, during World War 3. Series convers their drone flying training, battles and drone operations in Europe. The series highlights leadership and sacrifices made by the soldiers.")
    write_a_tv_show("Goat of Wall Street", "Series about Wall Street in the 1990s. A beginner stockbroker who ath the end of the show becomes notorious for his excessive lifestyle and fraudulent activities. Pump and dump schemes, drug use, excessive partying, and extravagant purchases. Greed, corruption, and unchecked excess.")
    write_a_tv_show("LAPD", "The series follows LAPD officers, while they navigate their career, prove themselves to younger colleagues and superiors, while also dealing with the physical and emotional demands of the job. Blend of drama, humor, and action.")
