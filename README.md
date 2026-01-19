# Laboratory TDD – Python

## 1. Objectif du tp

Développer une classe `Laboratory` capable de gérer des substances (dans notre cas on parlera plus d'ingrédients) et de fabriquer des produits à partir de réactions en Python, en suivant une approche **TDD**.

## 2. Les fonctionnalités implémentées

- Initialisation du laboratoire avec une liste de substances connues.
- Gestion des **stocks** des substances.
- Ajout de quantités avec la méthode `add`.
- Consultation des quantités en stock avec la méthode `getQuantity`, supportant les pluriels.
- Définition de **réactions** produisant de nouveaux produits à partir d’ingrédients.
- Fabrication de produits avec la méthode `make`, prenant en compte :
  - Paramètre `quantity` pour produire plusieurs unités.
  - Fabrication **partielle** si le stock des ingrédients est insuffisant.
  - Produits utilisés comme ingrédients pour d’autres produits.
- Retour de la quantité réellement produite par `make`.

## 3. Les ests TDD

- Les tests unitaires couvrent :
  - L’initialisation du laboratoire avec ou sans réactions.
  - L’ajout de substances et la gestion des erreurs de type ou de valeurs.
  - La fabrication de produits simples et en chaîne.
  - La fabrication partielle lorsque le stock est insuffisant.
  - L’utilisation de produits comme ingrédients.
  - La vérification du stock restant et des quantités produites.

## 4. Refactor

Pendant le refactor, le code a été amélioré pour :
- Ajouter des méthodes privées `_validate_reactions()` et `_get_stock()` pour rendre le code plus lisible.
- Assurer la cohérence du stock avec les substances et les produits.
- Maintenir la logique inchangée tout en rendant le code plus modulaire et facile à étendre.

