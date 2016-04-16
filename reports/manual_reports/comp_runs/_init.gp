set log x
set log x2

set key bottom right
set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
set ylab "#correctly mapped reads / #reads which should be mapped"

set key spacing 0.8 opaque

set format x "10^{%L}"
set format x2 "10^{%L}"

set termin svg size 400,400 enhanced

set style line 1 lt 1 pt 1 ps 0.5 lc rgb "#FF0000" lw 1;
set style line 2 lt 1 pt 2 ps 0.5 lc rgb "#00C000" lw 1;
set style line 3 lt 1 pt 3 ps 0.5 lc rgb "#0080FF" lw 1;
set style line 4 lt 1 pt 4 ps 0.5 lc rgb "#C000FF" lw 1;
set style line 5 lt 1 pt 5 ps 0.5 lc rgb "#00EEEE" lw 1;
set style line 6 lt 1 pt 6 ps 0.5 lc rgb "#C04000" lw 1;
set style line 7 lt 1 pt 7 ps 0.5 lc rgb "#C8C800" lw 1;
set style line 8 lt 1 pt 8 ps 0.5 lc rgb "#FF80FF" lw 1;
set style line 9 lt 1 pt 9 ps 0.5 lc rgb "#4E642E" lw 1;
set style line 10 lt 1 pt 10 ps 0.5 lc rgb "#800000" lw 1;
set style line 11 lt 1 pt 11 ps 0.5 lc rgb "#67B7F7" lw 1;
set style line 12 lt 1 pt 12 ps 0.5 lc rgb "#FFC127" lw 1;
set style line 13 lt 1 pt 13 ps 0.5 lc rgb "#000000" lw 1;
set style line 14 lt 1 pt 14 ps 0.5 lc rgb "#9F0000" lw 1;
