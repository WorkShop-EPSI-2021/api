import json
from spellchecker import SpellChecker
from langdetect import detect
import sys
from feelingAnalyzer import FeelingAnalyzer


def Mail_ML (mail_recup):

    # print(sys.argv)

    '''
    La fonction prends en paramètre un Json avec ce que l'on récupère de l'utilisateur 
    Elle rends un json avec les scores calculés pendant le machine learning sur la probabilité que le mail soit un faux 
    On prends en compte :
        - Les fautes d'orthographes présentent dans le mail 
    '''
    # parse json:
    text = json.loads(mail_recup)


    #Objet a corriger
    corps_mail=text["text"]

    '''
        ANALYSE ORTHOGRAPHE
    '''


    new_str=""
    foundForbiddenChar = False
    for i in range(0, len(corps_mail)-1, 1):
        # end of corps_mail
        if (i+1 == len(corps_mail)):
            new_str = new_str + corps_mail[i]
           
        if (corps_mail[i+1]!="'" and corps_mail[i+1]!=","):
            if not foundForbiddenChar :
                new_str += corps_mail[i]
                foundForbiddenChar = False
            else :
                foundForbiddenChar = False
        else :
            foundForbiddenChar = True


    # print(new_str)

        
    if (detect(corps_mail)=='fr'):
        spell = SpellChecker(language='fr')
        # print(spell.correction("bojour"))

        all_words=new_str.split()

        corrected_all_words=[]
        for i in range (0,len(all_words),1):

            #print(spell.correction(l[i]))
            corrected_all_words.append(spell.correction(all_words[i]))

    if (detect(corps_mail)=='en'):
        spell = SpellChecker(language='en')
        # print(spell.correction("bojour"))

        all_words=new_str.split()

        corrected_all_words=[]
        for i in range (0,len(all_words),1):

            #print(spell.correction(l[i]))
            corrected_all_words.append(spell.correction(all_words[i]))


    # print (corrected_all_words)

    count_errors=0
    for i in range (0,len(corrected_all_words),1):
        if (corrected_all_words[i]!=all_words[i]):
            count_errors+=1


    
    if(len(corps_mail)<150 and count_errors>6):
        pourcentage_faute=80

    if(len(corps_mail)<150 and count_errors<=6):
        pourcentage_faute=20
    
    if(150<len(corps_mail)<450 and count_errors<=8):
        pourcentage_faute=20

    if(150<len(corps_mail)<450 and 8<count_errors<=10):
        pourcentage_faute=50

    if(150<len(corps_mail)<450 and count_errors>10):
        pourcentage_faute=80
    
    if(len(corps_mail)>450 and count_errors<=10):
        pourcentage_faute=20
    
    if(len(corps_mail)>450 and 10<count_errors<=15):
        pourcentage_faute=50
    
    if(len(corps_mail)>450 and count_errors>15):
        pourcentage_faute=80
    

    #print('{"Erreur":'+ str(pourcentage_faute)+"%"'}')



    '''
        ANALYSE SENTIMENTS (Positivity, engaging, alarming)
    '''


    resultPositivity = FeelingAnalyzer.predictMailFeeling_Positivity(
    verbose= False,
    mailToAnalyse = corps_mail
    )
    #print(resultPositivity)
    scorePositivity = 15
    if resultPositivity[0] == "positive" : scorePositivity += 35
    if resultPositivity[1] == "positive" : scorePositivity += 35
    #print("scorePositivity = ", scorePositivity)


    resultEngaging = FeelingAnalyzer.predictMailFeeling_Engaging(
        verbose= False,
        mailToAnalyse = corps_mail
    )
    #print(resultEngaging)
    scoreEngaging = 15
    if resultEngaging[0] == "engaging" : scoreEngaging += 35
    if resultEngaging[1] == "engaging" : scoreEngaging += 35
    #print("scoreEngaging = ", scoreEngaging)


    resultAlarming = FeelingAnalyzer.predictMailFeeling_Alarming(
        verbose= False,
        mailToAnalyse = corps_mail
    )
    #print(resultAlarming)
    scoreAlarming = 15
    if resultAlarming[0] == "alarming" : scoreAlarming += 35
    if resultAlarming[1] == "alarming" : scoreAlarming += 35
    #print("scoreAlarming = ", scoreAlarming)

    stringResult = {
        "scoreOrthographe": pourcentage_faute,
        "scorePositivity": scorePositivity, 
        "scoreEngaging": scoreEngaging,
        "scoreAlarming": scoreAlarming
    }

    print('{"orthographe":'+ str(pourcentage_faute)+',"positivite":'+str(scorePositivity)+',"engagement":'+str(scoreEngaging)+',"alarmant":'+str(scoreAlarming)+'}')

# print("-------------------------------------------------BAD MAILS-----------------------------------------------------")

# print("--------------------1-----------------------")
# our_mail1='{"objet" : "Support NETFLIX", "text": "Bonjour, Nous n\'avons pas pu autoriser votre paiement pour le prochain cycle de facturation de votre abonnement. Nous serions bien évidemment très heureux de vous compter à nouveau parmi nous. cliquez simplement sur, réactivez simplement votre abonnement pour profiter des meilleurs films et séries TV sans interruption. RÉACTIVER L\'ABONNEMENT. Nous sommes là pour vous aider. Pour plus d\'informations, consultez le Centre d\'aide ou contactez-nous. L\'équipe Netflix"}'
our_mail1=sys.argv[1]
Mail_ML(our_mail1)