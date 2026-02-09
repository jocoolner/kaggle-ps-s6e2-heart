# EDA Summary — PS S6E2 Heart Disease

- Train rows: 630,000, Test rows: 270,000

- Baseline Presence rate: 0.4483

- Numeric cols: ['Age', 'BP', 'Cholesterol', 'Max HR', 'ST depression']

- Categorical cols: ['Sex', 'FBS over 120', 'Exercise angina', 'EKG results', 'Slope of ST', 'Thallium', 'Number of vessels fluro', 'Chest pain type']


## Strong numeric signals (mean differences)

- Max HR: mean_abs=160.415, mean_pre=143.467, diff=-16.948
- Cholesterol: mean_abs=242.499, mean_pre=248.104, diff=5.604
- Age: mean_abs=52.558, mean_pre=56.079, diff=3.521
- ST depression: mean_abs=0.348, mean_pre=1.169, diff=0.821
- BP: mean_abs=130.567, mean_pre=130.411, diff=-0.156

## High-risk categorical levels (largest lift vs baseline)

- Number of vessels fluro=3: presence_rate=0.900 (lift +0.451), count=22857
- Number of vessels fluro=2: presence_rate=0.897 (lift +0.449), count=54303
- Thallium=7: presence_rate=0.815 (lift +0.367), count=246748
- Exercise angina=1: presence_rate=0.806 (lift +0.358), count=172447
- Number of vessels fluro=1: presence_rate=0.729 (lift +0.281), count=106978
- Slope of ST=3: presence_rate=0.721 (lift +0.273), count=15492
- Chest pain type=4: presence_rate=0.697 (lift +0.249), count=329179
- Slope of ST=2: presence_rate=0.692 (lift +0.244), count=256215

## Low-risk categorical levels (most negative lift vs baseline)

- Chest pain type=1: presence_rate=0.108 (lift -0.340), count=28602
- Chest pain type=2: presence_rate=0.162 (lift -0.286), count=74941
- Sex=0: presence_rate=0.179 (lift -0.270), count=179717
- Chest pain type=3: presence_rate=0.191 (lift -0.258), count=197278
- Thallium=3: presence_rate=0.198 (lift -0.250), count=372286
- Slope of ST=1: presence_rate=0.262 (lift -0.186), count=358293
- Number of vessels fluro=0: presence_rate=0.303 (lift -0.145), count=445862
- Exercise angina=0: presence_rate=0.313 (lift -0.135), count=457553

## Train vs test categorical shift (L1 distance)

- Slope of ST: L1_shift=0.006179
- Number of vessels fluro: L1_shift=0.004420
- Chest pain type: L1_shift=0.004180
- EKG results: L1_shift=0.003236
- Sex: L1_shift=0.003160
- Exercise angina: L1_shift=0.001860
- Thallium: L1_shift=0.000621
- FBS over 120: L1_shift=0.000129