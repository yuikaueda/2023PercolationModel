import numpy as np
import matplotlib.pyplot as plt

# パラメータ
N_total = 250  # Nの総数
Ns_0 = 10      # Nsの初期値
A = 0.1        # 定数A

# 時間パラメータ
t_start = 0
t_end = 100  # t=100までプロット
dt = 0.1
t_values = np.arange(t_start, t_end, dt)

# 初期 (kon, koff) と変更後の (kon, koff) の組み合わせ
initial_kon_koff = (0.8, 0.2)
changed_kon_koff = (0.2, 0.8)

# プロット
plt.figure(figsize=(10, 6))

Ns_values1 = [Ns_0]
Ns_values2 = [Ns_0]

for i, t in enumerate(t_values[:-1]):
    if t == 60:
        initial_kon_koff = changed_kon_koff

    kon, koff = initial_kon_koff

    # 微分方程式1: ∂Ns/∂t = -koff/(kon+koff)*Ns + kon/(kon+koff)*(N-Ns)
    dNs_dt1 = -koff / (kon + koff) * Ns_values1[-1] + kon / (kon + koff) * (N_total - Ns_values1[-1])
    Ns_new1 = Ns_values1[-1] + dNs_dt1 * dt
    Ns_values1.append(Ns_new1)

    # 微分方程式2: ∂Ns/∂t = -koff/(kon+koff)*Ns + A*(N-Ns)
    dNs_dt2 = -koff / (kon + koff) * Ns_values2[-1] + A * (N_total - Ns_values2[-1])
    Ns_new2 = Ns_values2[-1] + dNs_dt2 * dt
    Ns_values2.append(Ns_new2)

   # if t == 60:
   #     plt.axvline(x=t, color='red', linestyle='--', label='kon, koff change')

plt.plot(t_values, Ns_values1, label="∂Nb/∂t = -ko'ff/(k'on+k'off)*Nb + k'on/(k'on+k'off)*Nu")
plt.plot(t_values, Ns_values2, label='∂Nb/∂t = -koff/(kon+koff)*Nb + A*Nu', linestyle='--')

plt.xlabel('Time',fontsize=15)
plt.ylabel('Nb',fontsize=15)
plt.legend()
#plt.title(f'Comparison of Two Equations with Parameter Changes (N_total={N_total}, A={A})')
#plt.grid(True)

# グラフを保存
plt.savefig('2model_hikaku_houkai_a0.1_syokiKon08Koff02.png')

plt.show()

