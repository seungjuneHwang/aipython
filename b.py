from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from rich.spinner import Spinner
import time
import random

console = Console()

candidates = ["이재명", "윤석열", "심상정"]

text = """대선 주자 기호 1번 [black on blue]더불어민주당 이재명[/black on blue]
대선 주자 기호 2번 [black on red]국민의 힘 윤석열[/black on red]
대선 주자 기호 3번 [black on bright_yellow]정의당 심상정[/black on bright_yellow]
"""

console.print(Panel(
    text,
    title="제20대 대선 후보",
    border_style="red",
    padding=(1, 2),
    box=box.ROUNDED,
    expand=True 
))

table = Table(title="제 20대 대통령 선거 후보 리스트📝")

table.add_column("이름", style="cyan", no_wrap=True)
table.add_column("소속 정당", style="magenta")
table.add_column("기호", justify="right", style="green")

table.add_row("🟦 이재명", "더불어민주당", "1번")
table.add_row("🟥 윤석열", "국민의힘", "2번")
table.add_row("🟨 심상정", "정의당", "3번")

console.print(table)

spinner = Spinner("dots", text="로딩중...", style="bold green")

console.print(spinner, end="")

time.sleep(3)

selected_candidate = random.choice(candidates)

console.clear()

text = "대선 후보를 선택하는 게임을 시작합니다...\n"
for char in text:
    console.print(char, end="")
    time.sleep(0.1)

time.sleep(0.5)

for _ in range(5):
    selected_candidate = random.choice(candidates)
    console.print(f"[bold cyan]선택된 후보: {selected_candidate}[/bold cyan]", end="\r")
    time.sleep(0.5)

console.print(f"\n[bold green]게임 끝! 최종 선택된 후보는 {selected_candidate}입니다![/bold green]")

