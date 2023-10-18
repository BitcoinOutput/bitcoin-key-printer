# bitcoin-key-printer

_Bitcoin Key Printer_ est un programme Python qui offre une interface conviviale pour la gestion des clés cryptographiques dans l'écosystème Bitcoin. Ce README explique les caractéristiques fondamentales du code et la logique derrière nos choix d'implémentation.

## Caractéristiques du Code

### 1. Génération de Clé

   _Génération de Paire de Clés ECDSA:_ Bitcoin Key Printer utilise l'algorithme de signature numérique à courbe elliptique (ECDSA) pour générer des paires de clés privées-publiques sécurisées. ECDSA est un standard largement accepté pour la génération de clés Bitcoin et offre un haut niveau de sécurité.

### 2. Chiffrement & Déchiffrement

   _Encodage Base58:_ Nous avons choisi l'encodage Base58 pour le chiffrement de clés privées et la représentation de clés publiques. Base58 est préféré dans Bitcoin pour sa lisibilité et l'évitement de caractères qui pourraient être confondus (comme 0 et O, ou I et l).

   _Chiffrement Fernet:_ Pour le chiffrement des clés privées, nous utilisons le schéma de chiffrement symétrique Fernet, qui garantit la confidentialité de votre clé privée. C'est un choix sécurisé pour protéger votre clé lors de son stockage.

### 3. Génération de Code QR

   _Code QR pour la Clé Publique:_ Les clés publiques sont encodées en codes QR pour faciliter le partage et l'utilisation dans les transactions Bitcoin. Cela offre un moyen rapide et fiable de faire des transactions avec d'autres utilisateurs dans l'écosystème Bitcoin.

### 4. Intégration à l'Écosystème Bitcoin

   _Simplification de la Gestion des Clés:_ Ce programme simplifie la génération de paires de clés, le chiffrement des clés et le partage des clés, le rendant plus accessible aux utilisateurs dans l'écosystème Bitcoin.

   _Amélioration de la Sécurité:_ En permettant le stockage sécurisé des clés privées chiffrées et le partage facile des clés publiques, Bitcoin Key Printer améliore la sécurité et la convivialité des clés Bitcoin.

### 5. Bibliothèques Python et Exigences

   _ECDSA:_ Nous utilisons la bibliothèque ECDSA pour générer des paires de clés et pour diverses opérations cryptographiques.

   _Base58:_ La bibliothèque base58 est utilisée pour gérer l'encodage et le décodage Base58.

   _Fernet (Cryptography):_ Fernet, faisant partie de la bibliothèque Cryptography, offre un chiffrement sécurisé et simple pour les clés privées.

   _qrcode:_ La bibliothèque qrcode est utilisée pour générer des codes QR pour les clés publiques.

## Aperçu des Fichiers

   - **code_generation.py:** Gère la génération des codes QR pour les clés publiques.

   - **main.py:** Le point d'entrée du programme, qui offre une interface utilisateur pour sélectionner les actions de gestion des clés.

   - **key_generation.py:** Gère la génération de paires de clés ECDSA.

   - **encryption.py:** Gère le chiffrement et le déchiffrement des clés privées pour un stockage sécurisé.

   - **storage.py:** Fournit des fonctions pour stocker et charger des clés privées chiffrées.

## Installation

Pour exécuter Bitcoin Key Printer, suivez ces étapes:

   - Clonez le dépôt:
```bash
git clone https://github.com/Ferrerkomi/bitcoin-key-printer.git
cd bitcoin-key-printer
```
   - Installez les bibliothèques requises:
```bash
pip install -r requirements.txt
```
   - Exécutez le programme:
```bash
python3 main.py
```
## Contribution

Si vous trouvez un bug, avez une suggestion de fonctionnalité ou souhaitez contribuer de quelque manière que ce soit, vous êtes le bienvenue! 
