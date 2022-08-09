from accounts.models import User


class CustomUser(User):
    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username