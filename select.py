import os
from glob import glob
import random
import re

def convert_file_name(file_name):
    # 첫 번째 경우: 숫자로 시작하고 "_" 뒤에 내용이 있는 파일
    if re.match(r"^\d+_\S+$", file_name):  # ".cpp" 확장자 없이도 동작하도록 수정
        base = file_name.split("_")[0]  # 첫 번째 "_" 이전의 숫자 부분 추출
        return base
    # 두 번째 경우: "_"로 구분된 문자열 포함된 파일
    elif "_" in file_name:
        base = file_name.split("_", 1)[1].split(".")[0]  # 첫 번째 "_" 이후의 문자열 추출
        return base
    else:
        return file_name  # 변환 조건에 맞지 않으면 원래 이름 반환

target="initial"
problems=glob("./problem/*.cpp")
while target=="initial" or target in glob("*"):
    target=random.choice(problems).lstrip("./problem/").rstrip(".cpp")
    target=convert_file_name(target)
print(target)

