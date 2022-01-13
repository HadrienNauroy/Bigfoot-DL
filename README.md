# Bigfoot-DL 🦍⬇️
 

Tu vas bientôt perdre tes identifiants Bigfoot car tu es trop vieux, tu regardes des miliers de films, tu as tout simplement la flemme ? Voici l'outil qu'il te faut. Bigfoot DL te permet d'autaumatiser le telechargement de tes films (Séries incomming).

## Dépendances

Pour utiliser Bigfoot DL tu as besoin de :

 - [Google Chrome](https://www.google.fr/chrome/?brand=XXVF&gclid=Cj0KCQiAuP-OBhDqARIsAD4XHpfUlBlHR4vMvEuMn6YFdDIM0KkWBrDN96cVsCMXeW898k1WhzsovoQaAj8zEALw_wcB&gclsrc=aw.ds)
 - [Python](https://www.python.org/downloads/)
 - [selenium](https://selenium-python.readthedocs.io/) que tu  peux installer en lancant la commande `pip install selenium`.
 - [webdriver_manager](https://pypi.org/project/webdriver-manager/) que tu  peux installer en lancant la commande `pip install webdriver-manager`

## Utilisation

Voici la marche a suivre pour utiliser le programme:

Premièrement il te faut modifier le fichier `config.py` pour y placer tes identifiants Cascad ansi que le fichier où tu veux que les films soient rangés. Voilà à quoi devrait ressembler le fichier après la manoeuvre. Plus besoin de refaire cette étape les prochaines fois.

``` 
"""C'est le fichier que vous devez modifier avant d'executer le bot"""


# indentifiants cascad
username = "Dupont"
password = "m0t2Passe"

# Là où ranger les films
destination = "D:\\films"

# Ne pas toucher sauf si votre connection est trop lente !
WAIT_TIME = 5
```

Ensuite il faut remplire le fichier `watch_list.txt` avec les films que tu veux telecharger. Voila un exemple avec les 5 meilleurs films de tout les temps selon allo-ciné :

```
Forrest Gump
La Liste de Schindler
La Ligne verte
12 hommes en colère
Le Parrain
```

Enfin pour lancer le programme, place toi dans le repertoir où il se situe et lance la commande suivante : 


```
PS D:\Projets\Bigfoot DL> python3 main.py
```

Et voilà tu peux suivre l'évolution de tes telechargements dans le terminal qui s'est ouvert ! 

## Connection trop lente

Il peut arriver que le programme soulève une erreur du type `increase 'WAIT_TIME'`. Il est possible que ce soit a cause d'une connexion trop lente ou d'un PC qui rame. Rends toi alors dans le fichier `config.py` et augmente legèrement la valeur de cette variable. 

## Plus d'informations

1. Pas besoin de retirer les films déjà telechargés du fichier `watch_list.txt` le programme s'en souviens même si tu as déplacé les films. 
2. Pour stopper le programme avant qu'il n'ai telechargé tous les films tu peux presser la commande suivante `CTRL + C` ce qui ne devrait pas poser de problème. Le telechargement reprendra là où il s'est arrété.
3. Si tus as une autre question où que tu veux reporter un bug tu peux ouvrir une [issue](https://github.com/HadrienNauroy/Bigfoot-DL/issues), je tacherais d'y répondre. 




 
 
