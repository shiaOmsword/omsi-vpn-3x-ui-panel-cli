from app.application.facades.panel_facade import PanelFacade


class AppFacade:
    def __init__(self, panel: PanelFacade) -> None:
        self.panel = panel