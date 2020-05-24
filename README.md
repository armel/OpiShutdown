# OpiShutdown
Extinction de l'OrangePI Zero à partir d'un bouton physique.

# Installation

## Récupération des paquets

Depuis la console SSH, entrez les commandes suivantes :

```
cd /opt
git clone https://github.com/nvl1109/orangepi_zero_gpio.git
cd orangepi_zero_gpio
sudo python3 setup.py install
```

Puis,

```
cd /opt
git clone https://github.com/armel/OpiShutdown.git
```

> Modifier éventuellement la ligne 14 afin de pointer vers le GPIO utilisé (par défaut PA14).


## Automatisation du lancement au démarrage

Afin d'automatiser le lancement du script au démarrage, éditer le fichier `/etc/rc.local` et ajouter la ligne :

`nohup /usr/bin/python3 /OpiShutdown/shutdown.py &`

> Attention à bien insérer cette ligne avant la toute dernière ligne qui contient `exit O`


