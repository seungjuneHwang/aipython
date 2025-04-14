from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

console = Console()

# 텍스트 스타일링
console.print("Hello, [bold red]Rich[/bold red]!", "It's a [italic yellow]beautiful[/italic yellow] day.")

# 테이블 출력
table = Table(title="Star Wars Movies")

table.add_column("Title", style="cyan", no_wrap=True)
table.add_column("Director", style="magenta")
table.add_column("Year", justify="right", style="green")

table.add_row("Star Wars: A New Hope", "George Lucas", "1977")
table.add_row("Star Wars: The Empire Strikes Back", "Irvin Kershner", "1980")
table.add_row("Star Wars: Return of the Jedi", "Richard Marquand", "1983")

console.print(table)

# 진행률 표시줄
for step in track(range(10), description="Processing..."):
    time.sleep(0.5)

# 패널 사용
from rich.panel import Panel
console.print(Panel("This is a panel", style="blue", title="Panel Title"))

# 마크다운 출력
from rich.markdown import Markdown
markdown = """
# Rich Markdown

Rich can also render markdown.

- Bullet points
- bullet 2
- bullet 3

*italic* and **bold**
"""
console.print(Markdown(markdown))

# 트리 구조 출력
from rich.tree import Tree
tree = Tree("Files")
tree.add("README.md")
subtree = tree.add("src")
subtree.add("__init__.py")
subtree.add("main.py")
console.print(tree)

from rich import print

print("[sky_blue1]하늘색 글자[/sky_blue1]")
from rich import print

print("[sky_blue1]sky_blue1[/sky_blue1]")
print("[sky_blue2]sky_blue2[/sky_blue2]")
print("[sky_blue3]sky_blue3[/sky_blue3]")
from rich import print

print("[on sky_blue3]하늘색 배경에 흰색 글자[/on sky_blue3]")

from rich import print

print("[rgb(135,206,250)]하늘색 글자 (RGB)[/rgb(135,206,250)]")

from rich import print

def print_cat_ascii_art():
    """고양이 ASCII 아트를 출력하는 함수"""
    print("[sky_blue1]  /\\_/\\ [/sky_blue1]")
    print("[sky_blue1] ( o.o )[/sky_blue1]")
    print("[sky_blue1] > ^ <  [/sky_blue1]")

def print_dog_ascii_art():
    """강아지 ASCII 아트를 출력하는 함수"""
    print("[sky_blue1]   / \\__  [/sky_blue1]")
    print("[sky_blue1]  (    @\\___[/sky_blue1]")
    print("[sky_blue1]   /       O[/sky_blue1]")
    print("[sky_blue1]  /  (_____/[/sky_blue1]")
    print("[sky_blue1]  /_____/   U[/sky_blue1]")

def print_rabbit_ascii_art():
    """토끼 ASCII 아트를 출력하는 함수"""
    print("[sky_blue1]   (\\(\\[/sky_blue1]")
    print("[sky_blue1]  (='.') [/sky_blue1]")
    print("[sky_blue1]  (\")_(\")[/sky_blue1]")

def main():
    count = 0
    
    # 5번 반복하기 위한 반복문
    while count < 5:
        print(f"\n실행 {count + 1}/5")
        print("[bold]그림 출력 프로그램[/bold]")
        print("[bold]=====================[/bold]")
        print("1. 고양이")
        print("2. 강아지")
        print("3. 토끼")
        try:
            n = int(input("선택: "))

            if n == 1: 
                print("[bold]고양이 그림[/bold]")
                print_cat_ascii_art()
            elif n == 2: 
                print("[bold]강아지 그림[/bold]")
                print_dog_ascii_art()
            elif n == 3:
                print("[bold]토끼 그림[/bold]")
                print_rabbit_ascii_art()
            else:
                print("[red]1, 2, 3 중에서 선택해주세요.[/red]")
                continue  # 잘못된 입력이면 카운트 증가 없이 다시 시작
        except ValueError:
            print("[red]숫자를 입력해주세요.[/red]")
            continue  # 숫자가 아닌 입력이면 카운트 증가 없이 다시 시작
        
        count += 1  # 성공적으로 실행 후 카운트 증가

    print("\n프로그램을 종료합니다.")

if __name__ == "__main__":
    main()\


# pip install rich로 설치 필요
from rich import print
from rich.console import Console

console = Console()

# 기본 색상 텍스트
print("[red]빨간색 텍스트[/red]")
print("[green]녹색 텍스트[/green]")
print("[blue]파란색 텍스트[/blue]")
print("[yellow]노란색 텍스트[/yellow]")
print("[magenta]마젠타색 텍스트[/magenta]")
print("[cyan]청록색 텍스트[/cyan]")

# 다양한 스타일 조합
print("[bold red]굵은 빨간색 텍스트[/bold red]")
print("[italic green]이탤릭체 녹색 텍스트[/italic green]")
print("[underline blue]밑줄 있는 파란색 텍스트[/underline blue]")
print("[bold yellow on blue]파란 배경에 굵은 노란색 텍스트[/bold yellow on blue]")

# 복합 스타일 한 문장에 적용
print("[bold red]빨간색[/bold red] 텍스트와 [blue]파란색[/blue] 텍스트 [green]녹색[/green] 함께 사용")

# Console 객체로 좀 더 다양한 스타일링
console.print("다양한 색상의 텍스트를 출력합니다.", style="bold magenta")
console.print("중요한 알림입니다!", style="bold white on red")


# ANSI 코드를 이용한 무지개 텍스트
def rainbow_text(text):
    colors = ['\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m']
    reset = '\033[0m'
    rainbow = ""
    for i, char in enumerate(text):
        if char.strip():  # 공백이 아닌 경우에만 색상 적용
            rainbow += colors[i % len(colors)] + char + reset
        else:
            rainbow += char
    return rainbow

print(rainbow_text("무지개 색상으로 텍스트를 출력합니다! Python은 정말 재미있습니다."))

from textual.app import App
from textual.widgets import Header, Footer, Button, Static

class SimpleApp(App):
    async def on_mount(self):
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")
        
        # 메인 영역에 내용 추가
        await self.view.dock(Static("안녕하세요! 텍스츄얼 앱입니다."), edge="top")
        
        # 버튼 추가
        grid = await self.view.dock_grid(edge="left", name="buttons")
        grid.add_column("col", fraction=1)
        grid.add_row("row1", fraction=1)
        grid.add_row("row2", fraction=1)
        grid.add_areas(
            area1="col,row1",
            area2="col,row2",
        )
        grid.place(
            area1=Button("버튼 1", name="btn1"),
            area2=Button("버튼 2", name="btn2"),
        )

# 앱 실행
app = SimpleApp()
app.run()


from rich import print
from rich.console import Console

console = Console()

def print_colored_ascii_art(ascii_art, color="sky_blue1"):
    """
    rich 라이브러리를 사용하여 ASCII 아트에 색상을 적용하여 출력하는 함수

    Args:
        ascii_art (str): 출력할 ASCII 아트 문자열
        color (str, optional): 적용할 색상. 기본값은 "sky_blue1".
    """
    lines = ascii_art.splitlines()
    for line in lines:
        console.print(f"[{color}]{line}[/{color}]")

def print_cat_ascii_art():
    """색상이 적용된 고양이 ASCII 아트를 출력하는 함수"""
    ascii_art = """
      /\\_/\\
     ( o.o )
      > ^ <
    """
    print_colored_ascii_art(ascii_art, color="light_coral")

def print_dog_ascii_art():
    """색상이 적용된 강아지 ASCII 아트를 출력하는 함수"""
    ascii_art = """
       / \\__
      (    @\\___
       /       O
      /  (_____/
      /_____/   U
    """
    print_colored_ascii_art(ascii_art, color="deep_sky_blue1")

def print_rabbit_ascii_art():
    """색상이 적용된 토끼 ASCII 아트를 출력하는 함수"""
    ascii_art = """
        (\\(\\
       (='.')
      (\")_(\")
    """
    print_colored_ascii_art(ascii_art, color="light_green")

def main():
    count = 0

    while count < 5:
        console.print(f"\n실행 {count + 1}/5")
        console.print("[bold]그림 출력 프로그램[/bold]")
        console.print("[bold]=====================[/bold]")
        console.print("1. 고양이")
        console.print("2. 강아지")
        console.print("3. 토끼")

        try:
            n = int(input("선택: "))

            if n == 1:
                console.print("[bold]고양이 그림[/bold]")
                print_cat_ascii_art()
            elif n == 2:
                console.print("[bold]강아지 그림[/bold]")
                print_dog_ascii_art()
            elif n == 3:
                console.print("[bold]토끼 그림[/bold]")
                print_rabbit_ascii_art()
            else:
                console.print("[red]1, 2, 3 중에서 선택해주세요.[/red]")
                continue
        except ValueError:
            console.print("[red]숫자를 입력해주세요.[/red]")
            continue

        count += 1

    console.print("\n프로그램을 종료합니다.")

if __name__ == "__main__":
    main()