from engine.core import GameCore
from game.scene.menu import MenuScene

if __name__ == "__main__":
    game = GameCore("Hello World", 800, 600)

    game.add_scene("menu", MenuScene())

    game.switch_scene("menu")

    game.run()