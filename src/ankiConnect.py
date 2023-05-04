import requests
import json


def buildRequest(action, params):
    return {
        "action": action,
        "params": params,
        "version": 6
    }

def addNote(deckName, front, back):
    params = {
        "note": {
            "deckName": deckName,
            "modelName": "Einfach (beide Richtungen)",
            "fields": {
                "Vorderseite": front,
                "Rückseite": back
            },
            "options": {
                "allowDuplicate": True,
                "duplicateScope": "deck"
            }
        }
    }

    response = requests.post("http://localhost:8765", json=buildRequest("addNote", params))
    print(response.text)