from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QFont
from qgis.utils import iface

def openProject():
    pass

def saveProject():
    pass

def closeProject():
    pass

def show_project_info():
    # Création de la fenêtre flottante
    dialog = QDialog(iface.mainWindow())
    dialog.setWindowTitle("Informations du Projet")
    dialog.setWindowModality(Qt.NonModal)  # Permet de continuer à utiliser QGIS
    dialog.setMinimumWidth(400)

    # Création du layout et du texte d'information
    layout = QVBoxLayout()
    label = QLabel(
        "Ce projet est en lecture seule (consultation uniquement). L'édition géométrique et attributaire doit s'effectuer depuis le projet QWAT.\n"
        "\n"
        "⚠ Veuillez consulter les notes sur chaque couche de ce projet pour savoir comment effectuer l'édition géométrique ou attributaire depuis QWAT."
    )
    label.setWordWrap(True)
    
    # Changer la police pour agrandir la taille
    font = QFont()
    font.setPointSize(10)  # Définir la taille de la police (12 points ici, ajustez selon votre besoin)
    label.setFont(font)

    # Bouton de fermeture
    close_button = QPushButton("Fermer")
    close_button.clicked.connect(dialog.close)

    # Ajout des widgets au layout
    layout.addWidget(label)
    layout.addWidget(close_button)
    dialog.setLayout(layout)

    # Positionner la fenêtre au centre de l'écran QGIS
    screen_geometry = iface.mainWindow().geometry()
    dialog.move(screen_geometry.center() - dialog.rect().center())

    # Afficher la fenêtre
    dialog.show()

# Exécuter la fonction au démarrage
show_project_info()
