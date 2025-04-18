import pygame

from client.scenes.base import BaseScene, Scenes
from client.services.matchmaking import MatchmakingService


class MatchmakingScene(BaseScene):
    """Simplified matchmaking scene: waits for a single match_found event."""

    def __init__(self, app) -> None:
        super().__init__(app)
        self.matchmaking: MatchmakingService = app.matchmaking_service
        self.match_id: str | None = None
        self.opponent_id: str | None = None

        # Font for messages
        self.font = pygame.font.SysFont(None, 48)

        # Register callback and start matchmaking
        self.matchmaking.add_match_found_listener(self._on_match_found)
        self.matchmaking.start()

    def _on_match_found(self, match_id: str, opponent_id: str) -> None:
        """Called when the server pairs us with an opponent."""
        self.match_id = match_id
        self.opponent_id = opponent_id

    def handle_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self.matchmaking.stop()
            self.app.running = False

        elif event.type == pygame.KEYDOWN:
            # Allow user to cancel matchmaking
            if event.key == pygame.K_ESCAPE:
                self.matchmaking.stop()
                self.app.current_scene = Scenes.START

    def update(self) -> None:
        # On match, transition immediately to game scene
        if self.match_id:
            self.matchmaking.stop()
            self.app.game_service.start(self.match_id)
            self.app.current_scene = Scenes.GAME
        super().update()

    def render(self) -> None:
        screen = self.app.screen
        screen.fill((0, 0, 0))

        if not self.match_id:
            # Waiting message with simple dot animation
            ticks = pygame.time.get_ticks()
            dots = "." * ((ticks // 500) % 4)
            text = self.font.render(f"Waiting for opponent{dots}", True, (255, 255, 255))
        else:
            text = self.font.render("Match found! Connecting...", True, (255, 255, 255))

        rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, rect)

        # Hint to cancel
        if not self.match_id:
            small = pygame.font.SysFont(None, 24)
            hint = small.render("Press ESC to cancel", True, (180, 180, 180))
            screen.blit(hint, (20, screen.get_height() - 40))
