# Weighted Least Squares - Signal Denoising

In this project, we denoise a signal with an iteratively reweighted least squares algorithm, using different regularisation parameters. Without these weights, when the regularisation parameter is large, the objective function would be too sensitive to sudden jumps in the dataset that are clearly not caused by noise, resulting in a denoised signal that is very smooth but does not fit the data. The algorithm terminates after 100 iterations. 

Noisy signal:
![image](https://github.com/danielzml/Signal-Denoising/assets/107761315/37188bba-70ad-40a7-b761-eb8ac36817aa)

Denoised signals:
![image](https://github.com/danielzml/Signal-Denoising/assets/107761315/23fac22b-d4b3-438f-90b6-2027a57027cf)

Coursework graded at 95%.
