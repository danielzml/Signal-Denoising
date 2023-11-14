# Linear Least Squares - Signal Denoising

In this project, we denoise a signal by applying an iterative least squares algorithm, using different regularisation parameters and a set of weights which are also updated iteratively. Without these weights, the objective function would be too sensitive to sudden jumps in the dataset that are clearly not caused by noise, for higher values of the regularisation parameter.

Noisy signal:
![image](https://github.com/danielzml/Linear-Least-Squares---Denoising/assets/107761315/0933cbf4-ed83-4228-b8d4-0c365fa4f8a3)

Denoised signals:
![image](https://github.com/danielzml/Linear-Least-Squares-Signal-Denoising/assets/107761315/c75ddb7e-704f-4114-aca1-32d33422b0e5)
