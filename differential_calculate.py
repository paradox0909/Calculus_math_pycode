import sympy as sp

# 시간(t)을 심볼로 정의
t = sp.symbols('t')

# T(t) 함수를 정의 (예: t^2 + 2t + 1)
T = t**2 + 2*t + 1

# T(t)의 미분 계산
dT_dt = sp.diff(T, t)

# 결과 출력
print(f'T(t)의 미분: {dT_dt}')
