
class Smartphone:

    def __init__(self, memory):
        self.memory = memory
        self.memory_taken = 0
        self.apps = []
        self.is_on = False

    def power(self):
        if not self.is_on:
            self.is_on = True
        else:
            self.is_on = False

    def install(self, app, app_memory):
        if self.get_memory_left() < app_memory:
            return f"Not enough memory to install {app}"
        elif self.get_memory_left() >= app_memory and not self.is_on:
            return f"Turn on your phone to install {app}"
        elif self.get_memory_left() >= app_memory and self.is_on:
            self.apps.append(app)
            self.memory_taken += app_memory
            return f"Installing {app}"

    def get_memory_left(self):
        return self.memory - self.memory_taken

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.get_memory_left()}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
