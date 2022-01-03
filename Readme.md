# Guide pour le lancement de l'application

## Description rapide du principe de l'application
Notre application est une application de gestion de produits d'une base de données
Elle permet à partir d'un client, d'interagir avec un serveur (qui sert de base de données)
et propose les fonctionnalités classiques d'une base de données :
- Accéder aux produits stockés dans la base
- Ajouter / modifier / supprimer un produit existant

## Récupération du projet 

Cloner le projet avec git avec la commande : 
```git clone https://github.com/Hoz73/devOps.git```

Tous les fichiers concernant le TP sont stockés dans le dossier "tp1".

## Lancement de l'application

### Avec docker compose :

- Se rendre dans le dossier "server_rest_python".
- Pour télécharger les images docker, et lancer l'image du client et du serveur dans un même network, entrer la commande :
```docker-compose up```
- Récupérer l'id  du conteneur client avec la commande: 
```docker ps```
- Accéder au bash du client / interagir avec le conteneur du client avec la commande :
```docker exec -it ID  bash``` avec ID l'id du conteneur client récupéré dans l'étape précédente
- Lancer le client avec la commande :
``` python main.py```
- Il est mintenant possible d'interagir avec le conteneur du serveur à partir du conteneur du client en utilisant les
différentes commandes proposées dans le menu maintenant affiché dans le bash du client lancé à l'étape précédente.

### Avec kubernetes :

- Se rendre dans le dossier "tp1".
- Démarrer minikube avec la commande (peut prendre un certain temps) :
```minikube start```
- Déployer les 2 fichiers de déploiement afin de déployer à la fois le client et le serveur avec les commandes :
```kubectl apply -f deploiment.yml``` et ```kubectl apply -f deploiment2.yml```
- Vérifier que les pods sont bien en mode Running et récupérer le nom d'un des 2 clients avec la commande :
```kubectl get pods```
- Exécuter le client en mode interactif avec la commande :
```kubectl exec -it NOM -- sh``` où NOM est le nom du pod client récupéré à l'étape précédente
- Lancer le client avec la commande :
``` python main.py```
- Il est mintenant possible d'interagir avec le conteneur du serveur à partir du conteneur du client en utilisant les
différentes commandes proposées dans le menu maintenant affiché dans le bash du client lancé à l'étape précédente.

## Auteurs:
AL RASHEED Hamze
BOUVIER Rémi

M2 INFO - Introduction DevOps