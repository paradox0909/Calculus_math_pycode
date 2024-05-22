# a부터 b까지의 구간을 심볼로 정의
a, b = sp.symbols('a b')

# T(t)의 정적분 계산 (예: 0부터 10까지)
total_traffic = sp.integrate(T, (t, a, b))

# 결과 출력
print(f'T(t)의 {a}부터 {b}까지 정적분: {total_traffic}')
