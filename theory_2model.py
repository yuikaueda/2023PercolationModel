import numpy as np
import matplotlib.pyplot as plt

# パラメータ
N_total = 250  # Nの総数
Ns_0 = 100      # Nsの初期値
A = 0.1        # 定数A
kon = 0.2      # konの値
koff = 0.8     # koffの値

# 時間パラメータ
t_start = 0
t_end = 50
dt = 0.1
t_values = np.arange(t_start, t_end, dt)

# Nsの微分方程式1
def dNs_dt1(Ns, N):
    return -koff / (kon + koff) * Ns + kon / (kon + koff) * (N - Ns)

# Nsの微分方程式2
def dNs_dt2(Ns, N):
    return -koff / (kon + koff) * Ns + A * (N - Ns)

# 初期値
Ns_values1 = [Ns_0]
Ns_values2 = [Ns_0]

# プロット
plt.figure(figsize=(10, 6))

for t in t_values[:-1]:
    dNs1 = dNs_dt1(Ns_values1[-1], N_total)
    Ns_new1 = Ns_values1[-1] + dNs1 * dt
    Ns_values1.append(Ns_new1)

    dNs2 = dNs_dt2(Ns_values2[-1], N_total)
    Ns_new2 = Ns_values2[-1] + dNs2 * dt
    Ns_values2.append(Ns_new2)

plt.plot(t_values, Ns_values1, label='∂Ns/∂t = -koff/(kon+koff)*Ns + kon/(kon+koff)*(N-Ns)')
plt.plot(t_values, Ns_values2, label='∂Ns/∂t = -koff/(kon+koff)*Ns + A*(N-Ns)', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Ns')
plt.legend()
plt.title(f'Ns vs. Time (kon={kon}, koff={koff}, N_total={N_total}, A={A})')
plt.grid(True)

plt.savefig('houkai_2model.png')

plt.show()

