# TP2 – Analyse réseau d’un service HTTP

On observe maintenant ce qui se passe réellement sur le réseau.

Reprendre le projet du TP 1.

Modifier l’application :

```python
app.run(host="0.0.0.0", port=5000)
```

Relancer l’application.

```bash
python src/app.py
```

> Ne pas fermer ce terminal.

## 1. Capture avec Wireshark

Interface :

* Linux → `lo`
* Mac → Loopback lo0,
* Windows → Loopback / NPCAP Loopback Adapter.

Filtre :

```
tcp.port == 5000
```

Relancer :

```bash
curl http://127.0.0.1:5000/api/status
```

## 2. Observer le 3-way handshake TCP

Identifier (dans l'ordre) :

1. SYN
2. SYN/ACK
3. ACK

Puis :

4. Requête HTTP
5. Réponse HTTP

### Questions

1. IP source ?
2. IP destination ?
3. Port source ?
4. Port destination ?

<details>
<summary><strong>Réponses</strong>
</summary>

| Élément          | Valeur attendue           |
| ---------------- | ------------------------- |
| IP source        | 127.0.0.1                 |
| IP destination   | 127.0.0.1                 |
| Port source      | Port éphémère (ex: 53214) |
| Port destination | 5000                      |

</details>

5. Pourquoi le port source change-t-il à chaque requête ?

<details>
<summary><strong>Réponses</strong>
</summary>

Le système attribue un **port éphémère** pour chaque connexion client.

Un serveur écoute sur un port fixe.
Un client utilise un port temporaire.

</details>

## 3. Observer HTTP dans TCP

Utiliser l’option `-v` (verbose) :

```bash
curl -v http://127.0.0.1:5000/api/status
```

Identifier :

* La **méthode HTTP**
* Le **chemin**
* Le **protocole**

<details>
<summary><strong>Réponse</strong>
</summary>

On observe :

```
> GET /api/status HTTP/1.1
```

* **Méthode HTTP** : `GET`
* **Chemin demandé** : `/api/status`
* **Protocole utilisé** : `HTTP/1.1`

</details>

## 4. Forcer une autre méthode

```bash
curl -v -X POST http://127.0.0.1:5000/api/status
# OU
curl -X POST http://127.0.0.1:5000/api/status -v
```

### Question

Quel code HTTP est retourné ? Pourquoi ?

<details>
<summary><strong>Réponse</strong>
</summary>

**405 Method Not Allowed**

Pourquoi ?

La route Flask accepte uniquement GET.

| Code | Type d’erreur         |
| ---- | --------------------- |
| 404  | route inexistante     |
| 405  | méthode non autorisée |

</details>

## 5. Modèle OSI

HTTP fonctionne au-dessus de quel protocole ?

À quelles couches appartiennent :

| Protocole | Couche OSI |
| --------- | ---------- |
| HTTP      | ?          |
| TCP       | ?          |
| IP        | ?          |

<details>
<summary><strong>Réponse</strong>
</summary>

HTTP fonctionne au-dessus de : → **TCP**

| Protocole | Couche          |
| --------- | --------------- |
| HTTP      | 7 (Application) |
| TCP       | 4 (Transport)   |
| IP        | 3 (Réseau)      |

</details>

Pourquoi HTTP ne peut pas fonctionner sans TCP ?

<details>
<summary><strong>Réponse</strong>
</summary>

HTTP a besoin :

* d’un transport fiable
* d’un contrôle d’erreur
* d’une gestion de session

TCP fournit cela.

</details>

## Conclusion

Chaîne complète :

```
Application
↓
HTTP
↓
TCP
↓
IP
↓
Carte réseau
```
