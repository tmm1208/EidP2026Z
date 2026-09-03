# Aufgabe 07-Z2: Default-Werte und Docstrings
# Musterlösung

def erstelle_email(empfaenger, betreff, signatur="Mit freundlichen Grüßen"):
    """
    Erstellt eine formatierte E-Mail als String.

    Parameter:
        empfaenger (str): Die E-Mail-Adresse des Empfängers.
        betreff (str): Der Betreff der E-Mail.
        signatur (str): Die Signatur. Standard: 'Mit freundlichen Grüßen'.

    Rückgabe:
        str: Die formatierte E-Mail.
    """
    email = f"An: {empfaenger}\n"
    email += f"Betreff: {betreff}\n"
    email += f"\nHallo!\n"
    email += f"\n{signatur}"
    return email

print(erstelle_email("max.mustermann@example.com", "Testmail"))
print()
print(erstelle_email("erika.muster@example.com", "Hallo!", "Viele Grüße"))
