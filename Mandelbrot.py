import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

class MandelbrotSet:
   
    def __init__(self, width=800, height=800):
        self.width = width
        self.height = height
        
    def compute(self, x_min, x_max, y_min, y_max, max_iterations):
        """
        Вычисление множества Мандельброта для заданной области и итераций
        """
        x = np.linspace(x_min, x_max, self.width)
        y = np.linspace(y_min, y_max, self.height)
        c = x[:, np.newaxis] + 1j * y[np.newaxis, :]
        
        # Итерационный процесс: z_{n+1} = z_n^2 + c
        z = np.zeros(c.shape, dtype=complex)
        divergence_time = np.zeros(c.shape, dtype=int)
        
        for iteration in range(max_iterations):
            # Вычисляем новые значения z
            z = z**2 + c
            
            # Проверяем, какие точки разбежались
            diverged = (np.abs(z) > 2) & (divergence_time == 0)
            divergence_time[diverged] = iteration
            
            z[diverged] = 0
            
        return divergence_time
    
    def plot(self, divergence_map, x_min, x_max, y_min, y_max, title, filename=None):
        plt.figure(figsize=(10, 8))
        plt.imshow(divergence_map.T, 
                  extent=[x_min, x_max, y_min, y_max],
                  cmap='hot', 
                  origin='lower',
                  interpolation='bilinear')
        
        plt.title(title, fontsize=14, fontweight='bold')
        plt.xlabel('Re(c)')
        plt.ylabel('Im(c)')
        plt.colorbar(label='Скорость расходимости')
        
        if filename:
            plt.savefig(filename, dpi=300, bbox_inches='tight')
        
        plt.show()

