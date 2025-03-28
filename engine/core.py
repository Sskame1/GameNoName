import pygame
from typing import Dict, Optional
from abc import ABC, abstractmethod

class Scene(ABC):
    def __init__(self):
        self.next_scene = None
    
    @abstractmethod
    def handle_events(self, event: pygame.event.Event) -> None:
        pass
    
    @abstractmethod
    def update(self, dt: float) -> None:
        pass
    
    @abstractmethod
    def render(self, surface: pygame.Surface) -> None:
        pass

class GameCore:
    def __init__(self, title: str, width: int, height: int, target_fps: int = 60):
        pygame.init()
        
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        
        self.scenes: Dict[str, Scene] = {}
        self.current_scene: Optional[Scene] = None
        
        self.clock = pygame.time.Clock()
        self.target_fps = target_fps
        self.dt = 0.0 
        
        self.running = False
    
    def add_scene(self, name: str, scene: Scene) -> None:
        self.scenes[name] = scene
    
    def switch_scene(self, name: str) -> None:
        if name in self.scenes:
            self.current_scene = self.scenes[name]
    
    def run(self) -> None:
        self.running = True
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if self.current_scene:
                    self.current_scene.handle_events(event)
            
            if self.current_scene:
                self.current_scene.update(self.dt)
            
            self.screen.fill((0, 0, 0))
            if self.current_scene:
                self.current_scene.render(self.screen)
            
            pygame.display.flip()
            
            self.dt = self.clock.tick(self.target_fps) / 1000.0 

pygame.quit()