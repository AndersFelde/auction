from django.contrib.auth import authenticate, login
from django.contrib import messages


class Verify():
    def isInt(self, input):
        try:
            int(input)
            return True
        except:
            return False

    def authenticateUser(self, request, email, password):
        user = authenticate(request, username=email, password=password)
        if user is not None:
            return user
        else:
            return False

    def logUserIn(self, request, email, password):
        user = self.authenticateUser(request, email, password)
        if user:
            login(request, user)
            print(f"Logged in {email}")
            messages.add_message(request, messages.INFO,
                                 f'Logget inn som {email}')
            return True
        else:
            return False
