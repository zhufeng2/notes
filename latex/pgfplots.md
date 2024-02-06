```latex
\begin{tikzpicture}
        \begin{axis}[
            title=在不同温度下的速率分布曲线,
            xmin=0,ymin=0,
            ymax=1.5,
            xlabel={$v$},
            ylabel={$f(v)$},
            samples=201,
            % axis lines=left,
        ]
        \addplot[color=blue,very thick]{4*pi*(1/(0.4*pi))^1.5*x^2*exp(-x^2/0.4)};
        \addplot[color=green,very thick]{4*pi*(1/(pi))^1.5*x^2*exp(-x^2)};
        \addplot[color=orange,very thick]{4*pi*(1/(2*pi))^1.5*x^2*exp(-x^2/2)};
\end{axis}
\end{tikzpicture}
```
