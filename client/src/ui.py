import pygame

pygame.init()
pygame.key.set_repeat(500, 50)


class App:

    def __init__(self, client):
        self.client = client
        pygame.display.set_caption("PyChat v2.0")

        self.screen = pygame.display.set_mode((1280, 720))

        self.update = pygame.USEREVENT + 1
        pygame.time.set_timer(self.update, 1000)

        self.font = pygame.font.Font("oxygen.ttf", 12)

        self.message = ''
        self.history = []

        self.is_running = True

    def __call__(self):
        pygame.event.set_blocked(None)
        pygame.event.set_allowed(
            (self.update, pygame.KEYDOWN, pygame.TEXTINPUT, pygame.QUIT)
        )

        while self.is_running:
            self.draw()
            self.handle_event(pygame.event.wait())

    def draw(self):
        self.screen.fill(0)

        text = self.font.render(f">>>   {self.message}", True, (255, 255, 255))
        self.screen.blit(text, (20, 680))

        history = self.history[-15:]
        length_history = len(history)

        c_gain = 255 // (length_history + 1)

        for c, message in enumerate(history):
            color = ((c + 1) * c_gain, (c + 1) * c_gain, (c + 1) * c_gain)

            info = self.font.render(message['author'], True, color)
            self.screen.blit(info, (20, (c + 1) * 40))

            text = self.font.render(message['content'], True, color)
            self.screen.blit(text, (20, (c + 1) * 40 + 15))

        pygame.display.update()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False
            return

        if event.type == self.update:
            new_messages = self.client.fetch_new_messages()

            if len(new_messages):
                for new_message in new_messages:
                    self.history.append(new_message)

            return

        if event.type == pygame.TEXTINPUT:
            self.message += event.text
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.message = self.message[:-1]

            if event.key == pygame.K_RETURN and len(self.message):
                self.client.send_message = self.message

                self.history.append({"author": "you", "content": self.message})
                self.message = ''