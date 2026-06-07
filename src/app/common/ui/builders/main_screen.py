from app.common.ui.blocks import BlockPanel

def build_main_menu_screen()->BlockPanel:
    panel = BlockPanel(
        message="Добро пожаловать в панель управления 3x-ui",
        title="Entry",
        text_colour="bold green",
        panel_border_colour="blue",
    ).build_panel()
    return panel