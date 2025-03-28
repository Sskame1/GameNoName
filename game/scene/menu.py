from engine.core import *

class MenuScene(Scene):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont('Arial', 32)
        self.button = pygame.Rect(300, 200, 200, 50)
    
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.collidepoint(event.pos):
                self.next_scene = "game"
    
    def update(self, dt):
        pass
    
    def render(self, surface):
        pygame.draw.rect(surface, (70, 130, 180), self.button)
        text = self.font.render("Start Game", True, (255, 255, 255))
        surface.blit(text, (self.button.x + 20, self.button.y + 10))
        
        title = self.font.render("Game", True, (255, 255, 255))
        surface.blit(title, (350, 100))