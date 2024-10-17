# SAE Cryptographie - Partie 1

## Auteurs

Amin EL MELLOUKI -  Groupe 23A<br>David DEFLANDRE - Groupe 21B<br>Fahed BOUAMRANI - Groupe 21A<br>Arthur JOUAN - Groupe 21B

## Description
Ce projet fait partie de la première étape de la SAE cryptographie. La première partie comprend les trois premières méthodes de chiffrement: le chiffrement César, le chiffrement de Vigenère, et le chiffrement ADFGVX. Chaque message fourni est chiffré avec l'une de ces techniques, et le projet fournit les scripts nécessaires pour détecter le type de chiffrement utilisé et déchiffrer automatiquement les messages.

## Utilisation
### Lancement d'un déchiffrement

Pour déchiffrer, placez vous à la racine du projet et exécutez la commande suivante:

```python
python3 src/main.py message/<fichier_contenant_chiffré>
```

### Règles de déchiffrement

- Selon le message chiffré passé dans la commande, différents types de déchiffrement sont exécutés:
    - **message1_chiffre.txt** : lance un déchiffrement césar automatiquement
    - **message2_chiffre.txt** : lance un déchiffrement de **Vigenère** automatiquement avec la **clé "CINQ"**
    - **message3_chiffre.txt** : lance un déchiffrement **ADFGVX** automatiquement avec la **clé "CRYPTO"** et la **matrice de taille 6*6 suivante : "AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M"**