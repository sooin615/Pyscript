import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.instagram.com/so._.in/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["red", "blue"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "천수인")
write("description", "안녕! 난 대소고 7기")
write("button", "My instagram")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "My hobby 1": "Guitar",
  "My hobby 2": "book",
  "My hobby 3": "bike",
  "My hobby 4": "ios development"
}
information(informations)
