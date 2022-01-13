# Bigfoot-DL
 
Tu vas bientôt perdre tes identifiants Bigfoot car tu es trop vieux, tu regardes des miliers de films ou tout simplement tu as la flemme ? Voici l'outil qu'il te faut. Bigfoot DL te permet d'autaumatiser le telechargement de tes films (Séries incomming).

## Dépendances

Pour utiliser Bigfoot DL tu as besoin de :

 - [Google Chrome](https://www.google.fr/chrome/?brand=XXVF&gclid=Cj0KCQiAuP-OBhDqARIsAD4XHpfUlBlHR4vMvEuMn6YFdDIM0KkWBrDN96cVsCMXeW898k1WhzsovoQaAj8zEALw_wcB&gclsrc=aw.ds)
 - [Python](https://www.python.org/downloads/)
 - [selenium](https://selenium-python.readthedocs.io/) que tu  peux installer en lancant la commande `pip install selenium`.
 - [webdriver_manager](https://pypi.org/project/webdriver-manager/) que tu  peux installer en lancant la commande `pip install webdriver-manager`

## Utilisation

Voici la marche a suivre pour utiliser le programe:

Premièrement il te faut modifier le fichier `config.py` pour y placer tes identifiants Cascad ansi que le fichier où tu veux que les films soient rangés. Voilà à quoi devrait ressembler le fichier après la manoeuvre. Plus besoin de refaire cette étape les prochaines fois.

``` 
"""C'est le fichier que vous devez modifier avant d'executer le bot"""


# indentifiants cascad
username = "Dupont"
password = "m0t2Passe"

# Là où ranger les films
destination = "D:\\films"
```

Ensuite il faut remplire le fichier `watch_list.txt` avec les films que tu veux telecharger. Voila un exemple avec les 5 meilleurs films de tout les temps selon allo-ciné :

```
Forrest Gump
La Liste de Schindler
La Ligne verte
12 hommes en colère
Le Parrain
```

Enfin pour lancer le programe, place toi dans le repertoir où se situe le programe et lance la commande suivante : 


```
PS D:\Projets\Bigfoot DL> python3 main.py
```

Et voilà tu peux suivre l'évolution de tes telechargement dans le terminal qui s'est ouvert ! 

## Connection trop lente

Il peut arriver que le programe soulève une erreur du type `increase 'WAIT_TIME'` rends toi alors dans le fichier config et augmente legèrement la valeur de cette variable. 





 
 
