from pyscript import document

def Gyaru(event):
    # Gets the value from the options
    ado = document.getElementById("adoSong").value

    # Determines what result to display depending on the song
    if ado == "Usseewa":
        result = "You love an old classic. You really can't go wrong with some good ol' fashioned rebellion style music!"
    elif ado == "Backlight":
        result = "You love that feeling of rebellion within you! Just let loose!"
    elif ado == "Readymade":
        result = "You love the smoothness of jazz, but also the roughness of rock!"
    elif ado == "Odo":
        result = "You wanna dance and dance, forgetting about all your worries in the process"
    elif ado == "Show":
        result = "You love the theatrics; putting on a Show, if you will, for other people"
    elif ado == "New Genesis":
        result = "You wanna feel free, like a bird in the wind or a boat on the open ocean. You wanna start anew, start more free."
    elif ado == "Gira Gira":
        result = "You love the feels. Perhaps you have an insecurity have trouble accepting it as part of your beauty?"
    elif ado == "Ashura-chan":
        result = "You are as authentic as they come. You live your life with extreme sincerity and authenticity, disregarding all acts to remain true."
    else:
        result = "Please select a song"

    #Displays result
    document.getElementById("result").innerText = result
