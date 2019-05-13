import dash_html_components as html
import pickle
import pandas as pd
import requests

loadModel = pickle.load(open('rfc_pokemon.sav','rb'))
encoderType1 = pickle.load(open('le_type1.sav','rb'))
encoderType2 = pickle.load(open('le_type2.sav','rb'))

def callbackpredict(n_clicks,name,type1,type2,generation,total,hp,attack,defense,spatk,spdef,speed):

    inputdata = [name,type1,type2,generation,total,hp,attack,defense,spatk,spdef,speed]
    if '' in inputdata:
        return [html.H2('Please fill all inputs!')]
    else :
        type1en = encoderType1.transform([type1])
        type2en = encoderType2.transform([type2])
        data = [[type1en[0],type2en[0],int(total),int(hp),int(attack),int(defense),int(spatk),int(spdef),int(speed),int(generation)]]
        predictProba = loadModel.predict_proba(data)
        predictions = ''
        predictSave = 0
        if(predictProba[0,1] > 0.15):
            predictions = 'Legendary'
            predictSave = 1
        else:
            predictions = 'Normal Pokemon'
            predictSave = 0

        data = {
            'name' : name,
            'type1' : type1,
            'type2' : type2,
            'total' : int(total),
            'hp' : int(hp),
            'attack' : int(attack),
            'defense' : int(defense),
            'spatk' : int(spatk),
            'spdef' : int(spdef),
            'speed' : int(speed),
            'generation' : int(generation),
            'legendary' : predictSave,
            'legendaryProba' : predictProba[0,1],
            'createdby' : 'Diast'
        }

        res = requests.post('http://api-pokemon-baron.herokuapp.com/saveprediction', data=data)
        print(res.content)

        return [
            html.H2('Probability of your Pokemon is Legendary : {}%'.format(predictProba[0,1]*100)),
            html.H2('so we predict {} is a {}'.format(name, predictions))
        ]
    
    
