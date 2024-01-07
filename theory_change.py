import numpy as np
import matplotlib.pyplot as plt

# パラメータ
N_total = 250  # Nの総数
Ns_0 = 1      # Nsの初期値
A = 5e-2      # 定数A

# 時間パラメータ
t_start = 0
t_end = 100  # t=100までプロット
dt = 0.1
t_values = np.arange(t_start, t_end, dt)

# 各(kon, koff)の組み合わせと初期値
parameter_combinations = [(0.8, 0.2), (0.7, 0.3)]
initial_kon_koff = [(0.8, 0.2), (0.7, 0.3)]

# プロット
plt.figure(figsize=(10, 6))

for i, (initial_kon, initial_koff) in enumerate(initial_kon_koff):
    Ns_values = [Ns_0]

    for t in t_values[:-1]:
        dNs_dt = -initial_koff / (initial_kon + initial_koff) * Ns_values[-1] + A * (N_total - Ns_values[-1]) 
        Ns_new = Ns_values[-1] + dNs_dt * dt
        Ns_values.append(Ns_new)

        if t == 60:
            # 初期 (kon, koff) を変更
            initial_kon, initial_koff = (0.2, 0.8)

    plt.plot(t_values, Ns_values, label=f'Initial (kon, koff) = ({parameter_combinations[i][0]}, {parameter_combinations[i][1]})')

plt.xlabel('Time',fontsize=15)
plt.ylabel('Nd',fontsize=15)
plt.legend()
#plt.title(f'Ns vs. Time with Parameter Changes (N_total={N_total}, A={A})')
#plt.grid(True)

# グラフを保存
plt.savefig('0107_houkai_Ns_vs_Time_with_Parameter_Changes.png')

plt.show()

