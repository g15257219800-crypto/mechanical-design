# 单位圆盘的 100 圆覆盖：一个可核验的精确上界

本文给出 \(r_D(100)\) 的夹逼

\[
\frac{1}{10} < r_D(100) \le \frac{1}{\sqrt{67}},
\]

其中右端由一组完全显式的圆心实现，覆盖性用有限次 \(\mathbb{Q}(\sqrt{3})\) 算术核验。左端是面积下界的严格形式。题目所要求的**全局最优性**（即 \(r_D(100)=\frac{1}{\sqrt{67}}\)）在 \(n=100\) 时仍是未解决问题：文献中等圆覆盖单位圆盘的最优性仅对 \(n\le 10\) 有证明。下文不假设任何未经证明的对称限制。

## 记号

单位圆盘 \(D=\{x\in\mathbb{R}^2:\lVert x\rVert_2\le 1\}\)。对 \(C=(c_1,\dots,c_{100})\in(\mathbb{R}^2)^{100}\)，

\[
R_D(C)=\max_{x\in D}\min_{1\le i\le 100}\lVert x-c_i\rVert_2,\qquad
r_D(100)=\inf_C R_D(C).
\]

六角格 \(\Lambda=\{m(1,0)+n(\tfrac12,\tfrac{\sqrt3}{2}):m,n\in\mathbb{Z}\}\)。范数

\[
N(m,n)=m^2+mn+n^2=\lVert p(m,n)\rVert_2^2,
\]

其中 \(p(m,n)=(m+\tfrac n2,\, n\tfrac{\sqrt3}2)\)。

## 1. 精确半径（多项式与隔离区间）

取整系数多项式

\[
P(t)=67t^2-1
\]

（系数表：常数项 \(-1\)，一次项 \(0\)，二次项 \(67\)），以及有理端点 \(a=\dfrac{3}{25}\)、\(b=\dfrac18\)。

\(P'(t)=134t\)，故 \(P\) 在 \([0,\infty)\) 上严格递增，在 \(\mathbb{R}\) 上恰有两个实根 \(\pm\alpha\)，其中 \(\alpha>0\)。又

\[
P\Bigl(\frac{3}{25}\Bigr)=\frac{603}{625}-1=-\frac{22}{625}<0,\qquad
P\Bigl(\frac18\Bigr)=\frac{67}{64}-1=\frac{3}{64}>0,
\]

因此 \(P\) 在 \((a,b)\) 内恰有一个实根 \(\alpha=\dfrac{1}{\sqrt{67}}\)。

下文证明 \(r_D(100)\le\alpha\)。不能把 \(\alpha\) 写成 \(r_D(100)\) 本身，除非再证任意构型的覆盖半径 \(\ge\alpha\)；第 4 节只给出面积下界。

## 2. 具体构型 \(C_*\)

令

\[
S_0=\bigl\{(m,n)\in\mathbb{Z}^2:N(m,n)\le 27\bigr\},
\]

以及 \(120^\circ\) 格旋转 \(\rho(m,n)=(-m-n,\,m)\)。令

\[
S_{28}=\bigl\{(4,2),\,\rho(4,2),\,\rho^2(4,2)\bigr\}=\bigl\{(4,2),\,(-6,4),\,(2,-6)\bigr\},
\]

\[
S=S_0\cup S_{28}.
\]

\(S_0\) 有 97 个点（对 \(|m|,|n|\le 6\) 穷举即可，因为 \(N(m,n)\ge\min(|m|,|n|)^2\) 且 \(N(m,n)\le 27\) 蕴含 \(\lvert m\rvert,\lvert n\rvert\le 6\)），\(S_{28}\) 三点两两不同，故 \(\lvert S\rvert=100\)。

\(S_{28}\) 是壳 \(N=28\)（共 12 点）上唯一包含 \((4,2)\) 的三阶轨道，因此 \(S\) 由有限整数数据唯一确定。

缩放比 \(s=\sqrt{3/67}\)。圆心

\[
c_{m,n}=s\,p(m,n)
=\Biggl(\frac{(2m+n)\sqrt{201}}{134},\;
\frac{3n\sqrt{67}}{134}\Biggr),\qquad (m,n)\in S.
\]

记 \(C_*=(c_{m,n})_{(m,n)\in S}\)。全部 \((m,n)\) 见 `data/centers_mn.txt`。

## 3. 覆盖性

先在未缩放坐标中工作。令 \(\Delta=\{x:\lVert x\rVert_2\le R\}\)，\(R=\sqrt{67/3}\)。只需证明

\[
\Delta\subset\bigcup_{(m,n)\in S} \overline{B}\bigl(p(m,n),\,1/\sqrt3\bigr),
\]

再以 \(s\) 缩放：\(sR=1\)，\(s/\sqrt3=1/\sqrt{67}=\alpha\)。

### 3.1 无限六角格的覆盖半径

\(\Lambda\) 的 Voronoi 胞腔是正六边形，外接半径等于边长为 1 的正三角形外接半径。该三角形高 \(\sqrt3/2\)，外接半径 \(\frac23\cdot\frac{\sqrt3}2=\frac1{\sqrt3}\)。因此对任意 \(x\in\mathbb{R}^2\)，存在 \(\lambda\in\Lambda\) 使 \(\lVert x-\lambda\rVert_2\le 1/\sqrt3\)。相邻三点 \((0,0),(1,0),(0,1)\) 的外心到顶点距离平方为 \(1/3\)，见 `src/verify_covering.py`。

### 3.2 远离原点的胞腔不进入 \(\Delta\)

Voronoi 胞腔 \(\mathrm{Vor}(u)\subset\overline{B}(u,1/\sqrt3)\)，故

\[
\mathrm{dist}(0,\mathrm{Vor}(u))\ge \lVert u\rVert_2-\frac1{\sqrt3}.
\]

若 \(N(u)\ge 31\)，则 \(\lVert u\rVert_2\ge\sqrt{31}\)。不等式 \(\sqrt{31}-1/\sqrt3>\sqrt{67/3}\) 等价于（两边为正）

\[
3\sqrt{31}-\sqrt3>\sqrt{201}.
\]

两边平方：\(282-6\sqrt{93}>201\Leftrightarrow 81>6\sqrt{93}\Leftrightarrow \frac{27}2>\sqrt{93}\Leftrightarrow \frac{729}4>93\Leftrightarrow 729>372\)，成立。因此 \(N\ge 31\) 的胞腔与 \(\Delta\) 不交。\(N\) 在 28 与 31 之间无格点。

### 3.3 内部格点已在 \(S\) 中

\(N\le 27\) 的全体格点属于 \(S_0\subset S\)。若 \(x\in\Delta\) 的最近格点 \(u\) 满足 \(N(u)\le 27\)，则 \(u\in S\)，且 \(\lVert x-u\rVert_2\le 1/\sqrt3\)。

### 3.4 壳 \(N=28\) 的九个未选点

\(N=28\) 共 12 个格点，其中 3 个属于 \(S_{28}\)。对其余 9 个点 \(u\)，`src/verify_covering.py` 用 \(\mathbb{Q}(\sqrt3)\) 精确算术核验下列有限命题（每个 \(u\) 的 Voronoi 六顶点是 \(u\) 与两个相邻邻居的外心，坐标在 \(\mathbb{Q}(\sqrt3)\) 中）：

1. 六个顶点中恰有一个 \(V\) 满足 \(\lVert V\rVert_2^2=67/3\)（即 \(V\in\partial\Delta\)），没有顶点落在 \(\Delta\) 内部。
2. \(V\) 由 \(u\) 与两个邻居 \(a,b\in S\) 生成，且 \(\lVert V-a\rVert_2^2=\lVert V-b\rVert_2^2=\lVert V-u\rVert_2^2=1/3\)。
3. 该六边形的每个顶点 \(W\) 满足 \(W\cdot V\ge 67/3\)。由凸性，\(\mathrm{Vor}(u)\subset\{x:x\cdot V\ge R^2\}\)。

由 Cauchy–Schwarz：若 \(\lVert x\rVert_2\le R\) 且 \(x\cdot V\ge R^2=\lVert V\rVert_2^2\)，则 \(x\cdot V\le\lVert x\rVert_2\lVert V\rVert_2\le R^2\)，故等号成立，从而 \(x\) 与 \(V\) 同向且 \(\lVert x\rVert_2=R\)，即 \(x=V\)。因此

\[
\Delta\cap\mathrm{Vor}(u)=\{V\}.
\]

点 \(V\) 到 \(a,b\in S\) 的距离为 \(1/\sqrt3\)，故被覆盖。

### 3.5 结论

任取 \(x\in\Delta\)，设 \(u\in\Lambda\) 为最近格点。则 \(\lVert x-u\rVert_2\le 1/\sqrt3\)。\(N(u)\ge 31\) 时 \(x\notin\mathrm{Vor}(u)\)，矛盾。\(N(u)\le 27\) 时 \(u\in S\)。\(N(u)=28\) 且 \(u\in S_{28}\) 时同样 \(u\in S\)。\(N(u)=28\) 且 \(u\notin S\) 时 \(x=V\) 仍被两个 \(S\) 中邻居覆盖。故 \(\Delta\) 被半径 \(1/\sqrt3\) 的 100 个闭圆盘覆盖。缩放后

\[
\forall x\in D\ \exists i,\qquad \lVert x-c_i^*\rVert_2\le\alpha=\frac1{\sqrt{67}}.
\]

特别地 \(R_D(C_*)=\alpha\)：内部正三角形外心达到距离 \(\alpha\)，且 \(\partial D\) 上的上述 \(V\) 的缩放像也达到 \(\alpha\)。

## 4. 下界（非匹配的全局估计）

**面积下界。** 设 \(R_D(C)=r\)。则 \(D\subset\bigcup_i B(c_i,r)\)，于是

\[
\pi=\mathrm{area}(D)
\le\sum_{i=1}^{100}\mathrm{area}\bigl(B(c_i,r)\cap D\bigr)
\le 100\pi r^2,
\]

故 \(r\ge 1/10\)。从而 \(r_D(100)\ge 1/10\)。

**严格性。** 等号要求 \(\{B(c_i,r)\cap D\}\) 几乎不交、每个 \(B(c_i,r)\subset D\)、并且它们填满 \(D\)。此时 \(D\) 被剖成 100 个半径 \(1/10\) 的闭圆盘。这与圆盘不能剖分成更小等圆相矛盾（三圆交界处出现正曲率空隙，边界处同样无法无重叠填满）。因此 \(r_D(100)>1/10\)。

该下界与上界 \(1/\sqrt{67}\) 并不相等。平面六角覆盖密度给出启发式 \(\sqrt{2\pi/(100\sqrt{27})}\approx 0.110\)，位于 \(1/10\) 与 \(1/\sqrt{67}\approx 0.12217\) 之间，但不能代替对任意构型的证明。题目禁止把未经证明的对称或组合限制当作最优性依据；本文不把六角格子集说成全局最优。

## 5. 计算机核验材料

允许计算机辅助证明。精确核验代码是 `src/verify_covering.py`：

- 输入：`data/centers_mn.txt`（100 个整数对）。
- 检查：点数、\(S_0\) 与 \(S_{28}\) 的唯一描述、\(P\) 在 \((3/25,1/8)\) 内恰一根、\(N\ge 31\) 的平方比较、九个未选胞腔的外心坐标、支撑半平面、格覆盖半径。
- 全部比较在 `sympy` 的精确代数中进行，不依赖浮点覆盖抽样。

运行：

```
python3 src/verify_covering.py
python3 src/plot_covering.py
```

图 `figures/covering_100.png` 只供示意，不是覆盖性证明。

## 6. 与题目四项要求的对照

| 要求 | 本文给出的 |
|------|------------|
| 1. 精确半径 | \(P(t)=67t^2-1\)，区间 \((3/25,1/8)\)，单根 \(\alpha=1/\sqrt{67}\) 是**上界**，不是已证的 \(r_D(100)\) |
| 2. 具体构型 | 六角格指数 \(S\) 与缩放 \(\sqrt{3/67}\)，坐标在 \(\mathbb{Q}(\sqrt{67},\sqrt{3})\) |
| 3. 覆盖性 | 第 3 节对整个 \(D\) 的证明（不是有限点抽样） |
| 4. 全局最优性 | 仅证 \(r_D(100)>1/10\)；**未证**对一切 \(C\) 有 \(R_D(C)\ge\alpha\) |

已知结果：\(n\le 4\) 与 \(n=7\) 平凡；\(n=5,6\) 由 Bezdek；\(n=8,9,10\) 由 G. Fejes Tóth。\(n=100\) 的精确最优值仍开放。
