import customtkinter as ctk
import tkinter as tk 
import speech_recognition as sr 
import pyttsx3
from youtube_search import YoutubeSearch
import webbrowser
          
# initialiser la reconnaissance vocale et la synthese vocale
 
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Fonction pour (synthese vocale)
 
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Fonction pour ecouter et reconnaitre la voix

def recognizer_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Parlez maintenant")

        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="fr-FR")
            print(f"vous avez dit: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("je n'ai pas compris")
            return ""
        except sr.RequestError:
            speak("Erreur de connexion")
            return ""
        

# fonction pour executer des commandes vocales
        
def execute_command():
    command = recognizer_speech()

    if "joue" in command:
        song_name = command.replace("joue","").strip()
        speak(f"Recherche de {song_name} sur Youtube.")

        # Recherche Youtube
        results = YoutubeSearch(song_name, max_results=1).to_dict()
        if results:
            video_url = f"https://www.youtube.com/watch?v={results[0]['id']}"
            speak(f"Lecture de {results[0]['titlte']}.")
            webbrowser.open(video_url)
        else:
            speak("Aucune video trouvee.")
    elif "ouvre Youtube" in command:
        speak("ouverture de Youtube.")
        webbrowser.open("https://www.youtube.com")

    elif "ferme" in command:
        speak("Fermeture de l'application")
        app.quit()

    else:
        speak("commande non reconnue")


#initialiser l'application

# ctk.set_appearence_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("assitance vocal")
app.geometry("500x400")

# label d'instruction

label = ctk.CTkLabel(app, text="Cliquez sur le bouton pour une commande", font=("helvertica",16))
label.pack(pady=30)

#bouton pour activer la reconnaissance vocale

ecoute_bouton = ctk.CTkButton(app, text="Ecouter", command=execute_command , font = ("Helvetica", 14),height=50,width=200)
ecoute_bouton.pack(pady=20)

#bouton pour quitter l'application

quitter_bouton = ctk.CTkButton(app, text="Quitter", command=app.quit() ,font = ("Helvetica", 14),height=50,width=200, fg_color="red")
quitter_bouton.pack(pady=20)

app.mainloop()
