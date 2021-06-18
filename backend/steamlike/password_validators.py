from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re


class ComplexPasswordValidator:
    """
    Validate whether the password contains minimum one digit.
    """

    def validate(self, password, user=None):
        # if re.search('[A-Z]', password) is None \
        #         and and re.search('[^A-Za-z0-9]', password) is None
        if re.search('[0-9]', password) is None:
            raise ValidationError(
                _("Password must contain at least one number."),
                code='password_is_weak',
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 number.")
