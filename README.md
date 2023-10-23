# bitcoin-key-printer

_Bitcoin Key Printer_ est un programme Python qui offre une interface conviviale pour la gestion des clés cryptographiques dans l'écosystème Bitcoin. Ce programme Python simplifie la génération de clés, améliore la sécurité grâce au cryptage et facilite le partage sans effort via des codes QR. En tirant parti de bibliothèques puissantes telles que `base58`, `hashlib` et `ecdsa`, Bitcoin Key Printer assure une gestion sécurisée et efficace des clés. 

## Caractéristiques du Code

### 1. Génération de Clé

   _Génération de Clés:_ La fonction 'generate_keypair' renvoie trois valeurs: clé privée, clé publique compressée et adresse Bitcoin. Le processus de génération de clés est amélioré grâce à une source d'entropie sécurisée. La génération d'adresses Bitcoin suit les étapes de hachage SHA-256 et RIPEMD-160. Les fonctions de cryptage utilisent une fonction de dérivation de clé (PBKDF2) pour la génération de clés sécurisées, et la clé privée est cryptée à l'aide du cryptage Fernet. Cependant, il est important de noter qu'une adresse Bitcoin n'est pas dérivée directement de la clé publique, mais plutôt de la clé publique hachée.

### 2. Chiffrement & Déchiffrement

   _L'encodage Base58:_ Dans notre programme, 'Generate_keypair()' utilise l'encodage Base58 pour l'adresse Bitcoin finale afin de s'assurer qu'elle est dans un format convivial. Le 'extended_public_key_checksum' est encodé à l'aide de Base58 pour générer l'adresse Bitcoin, qui est la représentation finale avec laquelle l'utilisateur interagit.
   
   _Encodage Base64:_ Dans notre programme, 'Encrypt_private_key(private_key, encryption_key)' utilise 'base64' pour s'assurer que la clé de cryptage dérivée de l'entrée de l'utilisateur est représentée dans un format adapté aux opérations cryptographiques. La représentation Base64 garantit que la clé de chiffrement est correctement gérée par des fonctions cryptographiques. 

En tirant parti des deux encodages, notre programme maintient un équilibre entre l'expérience utilisateur (avec des adresses lisibles) et l'intégrité cryptographique (avec des clés codées efficacement), assurant une interaction transparente et sécurisée avec les clés et adresses Bitcoin.

   _Chiffrement Fernet:_ Pour le chiffrement des clés privées, nous utilisons le schéma de chiffrement symétrique Fernet, qui garantit la confidentialité de votre clé privée. C'est un choix sécurisé pour protéger votre clé lors de son stockage. La classe Fernet de la bibliothèque 'cryptography' requiert que la clé soit une chaîne d'octets codée base64 à sécurité URL de 32 octets. Cette exigence est spécifique au schéma de cryptage 'Fernet'.

Puisque nous utilisons l'encodage base58, nous devons nous assurer que la clé passée au constructeur Fernet soit une chaîne d'octets codée en base64.

### 3. Génération de Code QR

   _Code QR pour la Clé Publique:_ Les clés publiques sont encodées en codes QR pour faciliter le partage et l'utilisation dans les transactions Bitcoin. Cela offre un moyen rapide et fiable de faire des transactions avec d'autres utilisateurs dans l'écosystème Bitcoin.

### Pourquoi 'base64' dans 'encryption.py'

Dans le fichier `encryption.py`, 'base64' est utilisé pour gérer la clé de chiffrement des clés privées. Alors que l'écosystème Bitcoin utilise principalement l'encodage `Base58` ou `Base58Check` pour les données liées à Bitcoin, les processus de cryptage utilisent généralement l'encodage 'base64'.

Ce choix est fait parce que le codage `base64` est un codage standard pour les clés et les données cryptographiques. L'encodage est bien pris en charge dans diverses bibliothèques de programmation, ce qui garantit la compatibilité et l'interopérabilité avec les outils et bibliothèques cryptographiques courants.
De nombreuses applications, bibliothèques et protocoles liés à Bitcoin utilisent l'encodage `base64` pour l'échange de données. En adoptant cette norme, le programme 'bitcoin_key_printer' assure la compatibilité avec d'autres outils et services Bitcoin. Cette interopérabilité est vitale pour les utilisateurs qui pourraient utiliser plusieurs applications liées à Bitcoin simultanément.

### 4. Intégration à l'Écosystème Bitcoin

   _Simplification de la Gestion des Clés:_ Ce programme simplifie la génération de paires de clés, le chiffrement des clés et le partage des clés, le rendant plus accessible aux utilisateurs dans l'écosystème Bitcoin.

   _Amélioration de la Sécurité:_ En permettant le stockage sécurisé des clés privées chiffrées et le partage facile des clés publiques, 'Bitcoin Key Printer' améliore la sécurité et le maintien des clés.

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
## Utilisation

   - Générer une paire de clés

Cette option génère une paire aléatoire de clés privée, compressée et publique Bitcoin et l'affiche.

```vbnet
python3 main.py
1. Generate Key Pair
2. Encrypt and Store Private Key
3. Generate QR Code
4. Exit
Enter your choice: 1
Private Key:
Compressed Public Key:
Bitcoin Address:
```
   - Chiffrer et stocker la clé privée:

Chiffre une clé privée pour un stockage sécurisé et génère une version cryptée.

```vbnet
$ python3 main.py
1. Generate Key Pair
2. Encrypt and Store Private Key
3. Generate QR Code
4. Exit
Enter your choice: 2
Enter your private key: <enter your private key>
Encrypted Private Key: <encrypted private key>
```
   - Générer un QRCode:

Génère un code QR pour une clé publique Bitcoin, utile pour les transactions et le partage.

```vbnet
$ python3 main.py
1. Generate Key Pair
2. Encrypt and Store Private Key
3. Generate QR Code
4. Exit
Enter your choice: 3
Enter your public key: <enter your public key>
QR code generated and saved as qrcode.png.
```
## Contribution

Si vous trouvez un bug, avez une suggestion de fonctionnalité ou souhaitez contribuer de quelque manière que ce soit, vous êtes le bienvenue! 
