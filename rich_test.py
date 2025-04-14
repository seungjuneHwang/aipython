# rich 라이브러리에서 필요한 기능들을 가져옵니다.
from rich import print  # 내장 print 대신 rich의 print 함수를 사용합니다.
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# 1. 기본 print 기능 활용 (색상, 스타일, 이모지)
print("--- [bold cyan]Rich 기본 출력[/bold cyan] ---")
print("안녕하세요! :wave:")
print("[bold red]굵은 빨간색[/bold red] 텍스트입니다.")
print("[italic green]기울임꼴 초록색[/italic green] 텍스트입니다.")
print("[underline blue]밑줄 친 파란색[/underline blue] 텍스트입니다.")
print("혼합 스타일: [bold yellow on magenta]굵은 노란색 (자주색 배경)[/bold yellow on magenta]")
print("-" * 40) # 구분선

# 2. Panel 사용하기 (텍스트 블록 강조)
print("\n--- [bold green]Panel 예제[/bold green] ---")
panel_content = Text.assemble(
    ("이것은 ", "white"),
    ("Panel", "bold blue"),
    (" 예제입니다.\n", "white"),
    ("텍스트를 ", "white"),
    ("테두리", "underline red"),
    ("로 감싸서 강조할 수 있습니다. :framed_picture:", "white")
)
print(Panel(panel_content, title="[yellow]정보[/yellow]", border_style="blue", padding=(1, 1)))
print("-" * 40) # 구분선

# 3. Table 사용하기 (표 데이터 출력)
print("\n--- [bold magenta]Table 예제[/bold magenta] ---")

# 테이블 객체 생성
table = Table(title="간단한 사용자 목록", show_header=True, header_style="bold cyan")

# 테이블 컬럼(열) 정의
table.add_column("ID", style="dim", width=6, justify="center") # 흐리게, 폭 6, 가운데 정렬
table.add_column("이름", style="magenta", min_width=10)        # 자홍색, 최소 폭 10
table.add_column("상태", justify="right", style="green")     # 오른쪽 정렬, 초록색

# 테이블 로우(행) 추가
table.add_row("1", "Alice", "활성")
table.add_row("2", "Bob", "[yellow]비활성[/yellow]") # 특정 셀 스타일 변경 가능
table.add_row("3", "Charlie", "활성")

# 테이블 출력
print(table)
print("-" * 40) # 구분선

print("\n[bold]Rich[/bold]를 사용하면 터미널 출력이 훨씬 보기 좋아집니다! :sparkles:")

print("[sky_blue3]이것은 하늘색 (sky_blue3) 글자입니다.[/sky_blue3]")