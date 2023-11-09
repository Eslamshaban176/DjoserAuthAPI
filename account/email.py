from djoser import email

class ActivationEmail(email.ActivationEmail):
    template_name = 'account/email/activation.html'

class ConfirmationEmail(email.ConfirmationEmail):
    template_name = 'account/email/confirmation.html'

class PasswordResetEmail(email.PasswordResetEmail):
    template_name = 'account/email/password_reset.html'

class PasswordChangedConfirmationEmail(email.PasswordChangedConfirmationEmail):
    template_name = 'account/email/password_changed_confirmation.html'
