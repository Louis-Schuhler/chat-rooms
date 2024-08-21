#!/usr/bin/env python
"""
Utilitaire en ligne de commande de Django pour les tâches administratives.
"""

import os
import sys

def main():
    """Exécute les tâches administratives."""
    # Définit le module de paramètres par défaut pour Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatrooms.settings')
    
    try:
        # Tente d'importer l'utilitaire execute_from_command_line de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Gère l'ImportError avec un message plus informatif
        raise ImportError(
            "Impossible d'importer Django. Assurez-vous qu'il est installé et "
            "disponible dans votre variable d'environnement PYTHONPATH. "
            "Vous avez peut-être oublié d'activer votre environnement virtuel."
        ) from exc

    # Exécute l'utilitaire en ligne de commande de Django avec les arguments fournis
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # Exécute la fonction principale lorsque le script est lancé directement
    main()
