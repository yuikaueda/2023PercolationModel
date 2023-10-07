import numpy as np
import matplotlib.pyplot as plt

# パラメータ
N_total = 250  # Nの総数
A = 0.1        # 定数A
parameter_combinations = [(0.9, 0.1)]  # (kon, koff)の組み合わせ

# Ns(0) の異なる初期値
initial_Ns_values = [0, 25, 50]

# 時間パラメータ
t_start = 0
t_end = 50
dt = 0.1
t_values = np.arange(t_start, t_end, dt)

# プロット
plt.figure(figsize=(10, 6))

for initial_Ns in initial_Ns_values:
    for kon, koff in parameter_combinations:
        Ns_values = [initial_Ns]
        N_values = [N_total]

        for t in t_values[:-1]:
            dNs_dt = -koff / (kon + koff) * Ns_values[-1] + A * (N_total - Ns_values[-1])
            Ns_new = Ns_values[-1] + dNs_dt * dt
            Ns_values.append(Ns_new)
            N_values.append(N_total)

        plt.plot(t_values, Ns_values, label=f'Ns(0) = {initial_Ns}')

plt.xlabel('Time')
plt.ylabel('Ns')
plt.legend()
plt.title(f'Ns vs. Time (kon={0.5}, koff={0.5}, N_total={N_total}, A={A})')
plt.grid(True)

# グラフを画像ファイルとして保存
plt.savefig('seisei_Ns0_vs_Time.png')

# グラフを表示
plt.show()

