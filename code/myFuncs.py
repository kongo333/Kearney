# 사용자 정의 함수를 모듈로 저장합니다.
def printValues3(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}은(는) {v}입니다.')
