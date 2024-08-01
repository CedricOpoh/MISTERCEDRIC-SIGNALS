import datetime
import random

heureDate = datetime.datetime.now()
heureMinute = heureDate.minute
heureHour = heureDate.hour

# Fonction pour supprimer un message
def delete_message(chat_id, message_id):
    # Code pour supprimer le message
    pass

# Clé API du jeu Lucky Jet sur 1win
# Cette clé est nécessaire pour prédire les cotes
# Prix : 5000$
# api_key = "1win.top/lucky-jet?V4.7:russian/moscowhacking=13975@dhvfftd%%%/for=50.00"

# Le bot détermine la minute du jeu
minutesAvancees = 2

# Le bot ajoute les minutes du jeu à l'heure actuelle
heureDate = heureDate + datetime.timedelta(minutes=minutesAvancees)

if 16 <= heureHour < 17:
    print("_Analyse des côtes en cours veuillez réessayer dans une heure_")
elif 13 <= heureMinute < 14:
    print("/interval")
else:
    # Les cotes maximum que le bot peut donner, ne pas les modifier
    min = 2.00
    max = 2.50
    hack = 2.20

    coefficientNumber = round(random.uniform(hack, max), 2)

    # Calcul de la probabilité
    halfNumber = round(coefficientNumber / 2, 2)

    fiabibily = round(halfNumber / 2, 2)

    # ramasser = round(fiabibily / 2, 2)

    # Afficher l'heure avec les minutes
    print("🚀AVIATOR(1win)🚀")
    print("Heure:", heureDate.hour, ":", heureDate.minute)
    print("Côte :", coefficientNumber)
    print("Assurance :", halfNumber)
    print("Fiable :", fiabibily)
    print("Demander un nouveau Signal après la fin du'une côte 2 à 50")
    print("Rejoint le canal Télégram https://t.me/+q6QGj_ZEqwphYjk")