from django.core.exceptions import ValidationError


def validate_eventapp_email(value):
    """
    Validate the email passed is in the domain "@anulujkredyt.pl"
    """
    if not "@eventapp.pl" in value:
        raise ValidationError(
            "Sorry, the email submitted is invalid. All emails have to be registered on this domain only - @eventapp.pl",
            params={'value': value},
        )
