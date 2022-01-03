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

- se rendre dans le dossier "server_rest_python"
- entrer la comande : docker-compose up (téléchargement des images, lancement image client + server dans même network)
- récupérer id conteneur client : docker ps
- docker exec -it ID  bash -> accéder bash client / terragir conteneur du client
- lancer le client : python main.py
- possible d'interagir avec le serveur en utilisant les différentes commandes proposées dans le menu

### Avec kubernetes :

run minikube : 
minikube start
déployer les deux fichiers de déploiment afin de déployer le client et le serveur (modifié)
kubectl apply -f deploiment.yml
kubectl apply -f deploiment2.yml
vérifier que les pods sont en mode Running et puis récupérer le nom du client
avec la commande : kubectl get pods
puis, exécuter le client en mode interactif
kubectl exec -it "le nom du client"  -- sh

## Auteurs:
AL RASHEED Hamze
BOUVIER Rémi
M2 INFO - Introduction DevOps

```
```