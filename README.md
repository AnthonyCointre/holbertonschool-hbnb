# Projet HBnB Evolution : Guide de la première partie
Bienvenue dans la première étape de notre passionnant voyage : créer notre propre application Web, HBnB Evolution, calquée sur AirBnB à l'aide de Python et Flask !


### Qu’est-ce qui se passe dans la première partie ?
1. Esquisse avec UML : vous commencerez par dessiner l'épine dorsale de notre application à l'aide d'UML (Unified Modeling Language). Pensez-y comme si vous créiez le plan architectural d’un bâtiment. C’est là que vous décidez de la manière dont vos classes et composants interagiront.

2. Tester notre logique : après avoir établi notre plan, il est temps de s'assurer que tout fonctionne comme prévu. Vous créerez des tests pour l’API et la logique métier. C’est comme s’assurer que tous les engrenages tournent sans à-coups dans une machine.

3. Construire l'API : Passons maintenant à la vraie affaire : implémenter l'API. C’est là que votre plan prend vie. Vous utiliserez Flask pour créer une API qui fonctionne bien avec notre logique métier et notre persistance basée sur les fichiers (pour l'instant).

4. Stockage de données basé sur des fichiers : nous commençons simplement avec un système basé sur des fichiers pour stocker nos données. Choisissez votre format – texte, JSON, XML – vous le nommez. Gardez à l’esprit que nous passerons à une base de données plus tard, alors construisez-la intelligemment !

5. Packaging avec Docker : Enfin, vous envelopperez le tout dans une image Docker soignée. C’est comme emballer votre application dans un conteneur qui peut être facilement déplacé et déployé n’importe où.


### Les trois couches de notre gâteau API :
- Couche de services : c'est là que notre API accueille le monde. Il gère toutes les demandes et réponses.
- Couche de logique métier : le cerveau de l’opération. C’est là que se déroulent tous les traitements et prises de décision.
- Couche de persistance : pour l'instant, il s'agit de notre humble système de fichiers, mais nous passerons à une base de données à l'avenir.


## Le modèle de données : entités clés
1. Lieux : ce sont le cœur de notre application. Chaque lieu (comme une maison, un appartement ou une chambre) possède des caractéristiques telles que le nom, la description, l'adresse, la ville, la latitude, la longitude, l'hôte, le nombre de chambres, de salles de bains, le prix par nuit, le nombre maximum de voyageurs, les équipements et les avis. 

2. Utilisateurs : les utilisateurs sont soit des propriétaires (hôtes), soit des évaluateurs (commentateurs) de lieux. Ils ont des attributs tels que l'e-mail, le mot de passe, le prénom et le nom. Un utilisateur peut héberger plusieurs lieux et peut également rédiger des avis sur des lieux qui ne lui appartiennent pas.

3. Avis : représentent les commentaires et les évaluations des utilisateurs pour un lieu. C'est ici que les utilisateurs partagent leurs expériences.

4. Équipements : il s'agit de fonctionnalités de lieux, comme le Wi-Fi, les piscines, etc. Les utilisateurs peuvent choisir dans un catalogue ou en ajouter de nouveaux.

5. Pays et ville : Chaque lieu est lié à une ville, et chaque ville appartient à un pays. Ceci est important pour catégoriser et rechercher des lieux.


### Logique métier : règles à respecter
1. Utilisateurs uniques : Chaque utilisateur est unique et identifié par son email.

2. Un hôte parlieu : chaque lieu doit avoir exactement un hôte. Hébergement flexible : un utilisateur peut héberger plusieurs emplacements, voire aucun.

3. Révision ouverte : les utilisateurs peuvent rédiger des avis sur des lieux qui ne leur appartiennent pas.

4. Options d'équipements : les lieux peuvent disposer de plusieurs équipements d'un catalogue et les utilisateurs peuvent en ajouter de nouveaux.

5. Structure ville-pays : un lieu appartient à une ville, les villes appartiennent à des pays et un pays peut avoir plusieurs villes.


Au fur et à mesure que vous concevez et implémentez ces fonctionnalités, n'oubliez pas que notre application va croître. Les choix que vous faites maintenant devraient permettre des ajouts et des modifications faciles plus tard, en particulier lorsque nous passons du stockage basé sur des fichiers au stockage sur base de données.

Dans notre quête de création d'une application robuste et efficace, il est essentiel que chaque entité de notre modèle de données, à l'exception du pays, comprenne les attributs suivants :

1. ID unique (UUID4) : chaque objet - qu'il s'agisse d'un lieu, d'un utilisateur, d'un avis, d'un équipement ou d'une ville - doit avoir un identifiant unique. Cet identifiant doit être généré à l'aide de l'UUID4 pour garantir l'unicité globale. Ceci est essentiel pour identifier et gérer de manière cohérente les entités dans notre application.

2. Date de création (created_at) : cet attribut enregistrera la date et l'heure de création d'un objet. C’est essentiel pour suivre la durée de vie de nos données et comprendre les modèles d’utilisation.

3. Date de mise à jour (updated_at) : De même, chaque objet doit avoir un attribut pour enregistrer la dernière mise à jour effectuée. Cela aide à maintenir l’exactitude historique de nos données et est essentiel pour toute modification ou piste d’audit.


Pourquoi ces attributs sont importants ?

- Unicité : L'UUID4 garantit que chaque entité est distincte, éliminant ainsi toute confusion ou chevauchement, particulièrement crucial lors d'une mise à l'échelle. 

- Traçabilité : avec Create_at et Updated_at, nous pouvons suivre le cycle de vie de chaque entité, ce qui est inestimable pour le débogage, l'audit et la compréhension des interactions des utilisateurs au fil du temps.

- Lors de la conception de vos classes et schémas de base de données (dans les étapes ultérieures), assurez-vous que ces attributs sont inclus en tant que partie standard de chaque entité.

- Utilisez le module uuid de Python pour générer des identifiants UUID4.

- Tirez parti du module datetime de Python pour enregistrer les horodatages pour la création et les mises à jour.
