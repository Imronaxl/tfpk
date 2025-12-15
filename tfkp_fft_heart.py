import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных
H = np.loadtxt('H (2.2).txt')
Vp = np.loadtxt('Vp (2.2).txt')

# Расчет закона "глубина-время"
# 1. Вычисляем интервалы глубины
dH = np.diff(H)

# 2. Средняя скорость для каждого интервала
Vp_avg = (Vp[:-1] + Vp[1:]) / 2

# 3. Интервальное время (в секундах)
dt = dH / Vp_avg

# 4. Накопленное время (закон глубина-время)
T = np.zeros(len(H))
T[0] = 0  # На поверхности время = 0
T[1:] = np.cumsum(dt)

# Последнее значение
last_value = T[-1]

print(f"Последнее значение закона глубина-время: {last_value:.3f} с")
print(f"В формате e-3: {last_value*1000:.3f}e-3")
print(f"Или в формате 0.000: {last_value:.3f}")

# Визуализация
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 10))

# График Vp от глубины
ax1.plot(Vp, H, 'b-', linewidth=2)
ax1.invert_yaxis()
ax1.set_title('Скорость Vp', fontsize=20)
ax1.set_ylabel('Глубина, м', fontsize=16)
ax1.set_xlabel('Скорость, м/с', fontsize=16)
ax1.grid(True)

# График закона глубина-время
ax2.plot(T, H, 'r-', linewidth=2)
ax2.invert_yaxis()
ax2.set_title('Закон глубина-время', fontsize=20)
ax2.set_ylabel('Глубина, м', fontsize=16)
ax2.set_xlabel('Время, с', fontsize=16)
ax2.grid(True)

plt.tight_layout()
plt.show()
