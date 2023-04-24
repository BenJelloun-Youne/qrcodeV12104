from flask import Flask, render_template, request
import pyqrcode
import os
import webbrowser

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/qrcode", methods=["POST"])
def qrcode_generator():
    # Collecter les informations de l'utilisateur
    nom = request.form["nom"]
    prenom = request.form["prenom"]
    email = request.form["email"]
    telephone = request.form["telephone"]
    site_web = request.form["site_web"]
    adresse = request.form["adresse"]
    ville = request.form["ville"]
    code_postal = request.form["code_postal"]

    # Générer le texte pour le code QR en fonction des informations fournies par l'utilisateur
    texte_qr = ""
    if nom:
        texte_qr += "Nom: {}\n".format(nom)
    if prenom:
        texte_qr += "Prénom: {}\n".format(prenom)
    if email:
        texte_qr += "E-mail: {}\n".format(email)
    if telephone:
        texte_qr += "Téléphone: {}\n".format(telephone)
    if site_web:
        texte_qr += "Site web: {}\n".format(site_web)
    if adresse:
        texte_qr += "Adresse: {}\n".format(adresse)
    if ville:
        texte_qr += "Ville: {}\n".format(ville)
    if code_postal:
        texte_qr += "Code postal: {}\n".format(code_postal)

    # Générer le code QR
    qr_code = pyqrcode.create(texte_qr)

    # Enregistrer le code QR en tant que fichier SVG
    nom_fichier = "{}_{}_QR.svg".format(prenom, nom)
    qr_code.svg(os.path.join("static", nom_fichier), scale=8)

    # Ouvrir le code QR dans le navigateur
    url = request.host_url + "static/" + nom_fichier

    chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'

    webbrowser.get('chrome').open_new_tab(url)

    return render_template("qrcode.html", nom_fichier=nom_fichier)

if __name__ == "__main__":
    app.run(debug=True)
