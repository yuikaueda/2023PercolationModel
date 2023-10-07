import numpy as np
import matplotlib.pyplot as plt

# パラメータ
N_total = 250  # Nの総数
Ns_0 = 50      # Nsの初期値
A = 0.1       # 定数A

# 時間パラメータ
t_start = 0
t_end = 100
dt = 0.1
t_values = np.arange(t_start, t_end, dt)

# 各(koff, kon)の組み合わせ
parameter_combinations = [(0.5, 0.5), (0.8, 0.2), (0.2, 0.8)]

# プロット
plt.figure(figsize=(10, 6))

for koff, kon in parameter_combinations:
    Ns_values = [Ns_0]
    N_values = [N_total]

    for t in t_values[:-1]:
        dNs_dt = -koff / (kon + koff) * Ns_values[-1] + A * (N_total - Ns_values[-1])
        Ns_new = Ns_values[-1] + dNs_dt * dt
        Ns_values.append(Ns_new)
        N_values.append(N_total)

    plt.plot(t_values, Ns_values, label=f'(koff, kon) = ({koff}, {kon})')

plt.xlabel('Time')
plt.ylabel('Ns')
plt.legend()
plt.title(f'Ns vs. Time (Initial Ns={Ns_0}, N_total={N_total}, A={A})')
plt.grid(True)

plt.savefig('kokoff_vs_Time.png')
plt.show()

