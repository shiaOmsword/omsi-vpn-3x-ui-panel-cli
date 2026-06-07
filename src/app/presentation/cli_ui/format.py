from rich.panel import Panel
from rich.table import Table

def format_users_table(headers:list[str], table: Table)-> Table:
    for field in headers:
        if field=="id":
            table.add_column(field, justify="right", style="cyan")
            continue
        
        if field=="email":
            table.add_column(field, style="magenta")
            continue
        if field=="created_at":
            table.add_column(field, overflow="fold", style="blue")
            continue
        # if field=="sub_id":
        #     table.add_column(field, overflow="crop", style="bold red")
        #     continue        
        if field=="sub_url":
            table.add_column(field, overflow="fold" , style="bold red")
            continue
        
        table.add_column(field, style="green")
        
    return Table
    