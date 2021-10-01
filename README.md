# Projet C'MAIL

## Objectif 

Le projet consiste en une extension web qui analyse le contenu du mail et retourne à l'utilisateur 
le résultat de l'analyse du texte sous différents aspects pour lui permettre de .

Le projet se décompose suivant les 5 parties suivantes :
* le front-end de l'extension, dont le code se trouve [ici](https://github.com/WorkShop-EPSI-2021/extension-new/tree/testronan), 
* le site web de présentation du projet, ainsi que des vidéos externes de sensibilisation à la sécurité des mails : le code se trouve [ici](https://github.com/WorkShop-EPSI-2021/front), 
* le back end qui prend le texte du mail, exécute les différentes analyses et retourne les résultats à l'API : code [ici](https://github.com/WorkShop-EPSI-2021/script)  
* l'API qui fait le pont entre le front-end et le back-end : le code est [ici](https://github.com/WorkShop-EPSI-2021/api)
* Une base de données enregistrant les résultats des analyses


## Installation et utilisation de l'extension Chrome

Les étapes à suivre sont les suivantes :
Pour installer et utiliser chrome://extensions
1. Télécharger le projet de l'extension qui se trouve [ici](https://github.com/WorkShop-EPSI-2021/extension-new/tree/testronan) 
puis dézipper le dossier
2. Ouvrir le navigateur Chrome et aller à l'URL suivante : `chrome://extensions`
3. Activer le mode développeur (bouton slide dans la barre juste au-dessus des extensions) 
4. Cliquer sur 'charger l'extension non empaquetée'
5. Sélectionner le dossier dézippé de l'extension  


## Site web d'informations

Le site web a été réalisé avec le framework REACT. Il est hébergé sur un serveur et accessible via ce 
[lien](https://tanjobi.fr/) 

## Suivi de l'activité

Afin de suivre l'activité et pouvoir générer des statistiques sur les résultats des analyses de mails,
une base de données enregistre les résultats obtenus par l'ananlyse.

## La sécurité et la RGPD

* Le projet tente en particulier d'apporter une solution à la technique de hameçonnage (ou phishing) par mail
en analysant le contenu du mail avant que l'utilisateur ne clique sur un lien malicieux
* Le site analyse uniquement le texte des mails que l'utilisateur souhaite faire analyser
* Aucune donnée identifiant directement ou indirectement l'utilisateur n'est stockée, seuls les résultats de l'analyse sont enregistrés
* Les données qui transitent sont chiffrées via le protocole https

# Auteurs

CORBIER Zoé, EBERST Emmanuel, MORIN Alexandre, SONZOGNI Dorian, THIEBAUT Ronan, WEHREY Alexy
