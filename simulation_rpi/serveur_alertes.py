# serveur_alertes.py
# Serveur de surveillance recevant les alertes d'urgence
# Utilise Flask pour créer une API REST simple
# Affiche les alertes reçues dans la console et sur une page web
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
alertes = []

@app.route('/')
def accueil():
    return f"""
    <h1>Centre de Surveillance</h1>
    <p><strong>Alertes reçues :</strong> {len(alertes)}</p>
    <p><a href="/alertes">Voir toutes les alertes</a></p>
    <hr>
    <p><em>Serveur en attente d'alertes...</em></p>
    """
    # return redirect("/alertes")

@app.route('/alerte', methods=['POST'])
def recevoir_alerte():
    try:
        data = request.get_json()
        alerte = {
            'timestamp_reception': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'donnees': data
        }
        alertes.append(alerte)
        print(f"\n=== ALERTE #{len(alertes)} ===")
        print(f"Reçue : {alerte['timestamp_reception']}")
        print(f"Source : {data.get('source')}")
        print(f"Message : {data.get('message')}")
        return jsonify({"status": "OK", "alerte_id": len(alertes)}), 200
    except Exception as e:
        return jsonify({"status": "ERREUR", "message": str(e)}), 400

@app.route('/alertes')
def lister_alertes():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="refresh" content="3">
        <title>Historique des alertes</title>
    </head>
    <body>
    <h1>Historique des Alertes</h1>
    """
    if not alertes:
        html += "<p>Aucune alerte reçue.</p>"
    else:
        for i, alerte in enumerate(alertes, 1):
            html += f"""
            <div style='border: 1px solid red; margin: 10px; padding: 10px;'>
                <h3>Alerte #{i}</h3>
                <p><strong>Reçue :</strong> {alerte['timestamp_reception']}</p>
                <p><strong>Données :</strong> {alerte['donnees']}</p>
            </div>
            """
    html += "</body></html>"
    return html

if __name__ == '__main__':
    print("Serveur de surveillance démarré sur http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)