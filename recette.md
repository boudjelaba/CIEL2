# 📄 Fiche Recette Fonctionnelle — **EXEMPLE**

## 1. Informations Générales

| Élément                | Détail                           |
|-------------------------|----------------------------------|
| **Nom du projet**       | Projet Générateur de QR Code Événementiel |
| **Version testée**      | v1.0.0-beta |
| **Date**                | 28/04/2025 |
| **Testeur**             | Charles Carnus |
| **Objectif**            | Vérifier la génération, l'affichage, et la fonctionnalité du QR code pour ajout d’événement à un calendrier |

---

## 2. Environnement de Test

- **Navigateur(s)** : Chrome, Firefox, Safari
- **Mobile(s)** : iPhone 15, Pixel 7 ou autre
- **Applications Calendrier testées** : Google Calendar, Apple Calendar
- **Connexion** : Wi-Fi stable, tests 4G/5G en complément
- **Lecteur QR code** : Appareil photo natif + "QRbot" app dédiée

---

## 3. Pré-requis

- QR code généré et affiché dans la page

---

## 4. Cas de Test

| ID | Intitulé | Étapes | Résultat Attendu | Statut | Commentaires |
|----|----------|--------|------------------|--------|--------------|
| CT-001 | Affichage QR code | Créer un événement "JPO CIEL", 30/04/2025 12h-13h, lieu "Salle 215" > Générer | QR code affiché en 3 secondes max, visuellement lisible | 🟩 Succès | |
| CT-002 | Lecture QR code - Google Calendar | Scanner avec Pixel 7 > Proposer ajout dans Google Calendar | Titre, date, heure, lieu OK, description vide | 🟩 Succès | |
| CT-003 | Lecture QR code - Apple Calendar | Scanner avec iPhone 15 > Ajouter dans Apple Calendar | Titre, date, heure, lieu OK | 🟩 Succès | |
| CT-004 | Robustesse saisie minimale | Créer un événement avec juste "JPO" + date/heure > Générer | QR généré, événement reconnu sans crash | 🟩 Succès | |
| CT-005 | Gestion texte long | Événement avec titre de 300 caractères + grande description > Générer | QR généré, scannable, quelques troncatures visibles en description sur vieux Google Calendar | 🟥 Partiellement réussi | À limiter description en prod |
| CT-006 | Scan après impression papier | Impression du QR sur A4 > Scan avec iPhone 15 | Lecture sans souci, ajout événement OK | 🟩 Succès | |
| CT-007 | Résistance mauvaise connexion | Scanner sous 3G limitée > Tentative de création d'événement | Scan lisible, ajout local proposé si pas de synchronisation immédiate | 🟩 Succès | |

---

## 5. Résultats Globaux

| Résumé                   | Détail                           |
|---------------------------|----------------------------------|
| Nombre de cas testés       | 7 |
| Nombre de cas réussis      | 6 |
| Nombre de cas échoués      | 1 |
| Taux de réussite           | 85,7% |

---

## 6. Anomalies Observées

| ID Anomalie | Description | Niveau Criticité | Statut (Ouvert/Clos) |
|-------------|-------------|------------------|---------------------|
| BUG-001 | Description événement trop longue tronquée dans Google Calendar Mobile (> 1000 caractères) | Mineur | Ouvert (demande de limiter la description à 500 caractères) |

---

## 7. Conclusion

✅ La fonctionnalité de génération et de lecture du QR code est globalement **conforme aux attentes**.  
❗ Une **limitation sur la longueur de la description** est à prévoir pour assurer une compatibilité totale, surtout avec des outils un peu capricieux.

**Recommandation** :

- Mettre en place une validation sur longueur max des champs.
- Retester après correction sur environnements réels imprimés (affiche, flyer).
- Prévoir un contrôle de qualité visuel du QR code (taille minimum, contraste).
