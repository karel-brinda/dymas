#! /usr/bin/env gnuplot

set log x
set log x2

set format x "10^{%L}"
set format x2 "10^{%L}"

set termin svg size 400,400 enhanced
set out 'report.svg'
set key spacing 0.8 opaque

set title "Comparison of runs Exp2"
set key bottom right
set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
set ylab "#correctly mapped reads / #reads which should be mapped"

par_x1=0.01
par_x2=0.1

par_y1=80
par_y2=100

set xran [par_x1:par_x2]
set x2ran [par_x1:par_x2]

set yran [par_y1:par_y2]
set y2ran [par_y1:par_y2]

#set style line 1 lt 1 pt 1 lc rgb "#00cc00"
#set style line 2 lt 1 pt 1 lc rgb "#ff0000"
#set style line 3 lt 1 pt 1 lc rgb "#0000ff"
#set style line 4 lt 1 pt 1 lc rgb "#aa00aa"
#set style line 5 lt 1 pt 1 lc rgb "#00aaaa"
#set style line 6 lt 1 pt 1 lc rgb "#aaaa00"
#set style line 7 lt 1 pt 1 lc rgb "#ff33dd"
#set style line 8 lt 1 pt 1 lc rgb "#33ddff"

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

plot \
"../../_rocs/exp2.04__Tuberculosis__0.07-ococo16/static.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 1 title "SM" noenhanced,\
"../../_rocs/exp2.11__Tuberculosis__0.07-ococo16-noremap/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 2 title "DM (noremap)" noenhanced,\
"../../_rocs/exp2.04__Tuberculosis__0.07-ococo16/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 3 title "DM" noenhanced,\
"../../_rocs/exp2.08__Tuberculosis__0.07-dels/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 4 title "DM (dels)" noenhanced,\
"../../_rocs/exp2.06__Tuberculosis__0.07-indels/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 5 title "DM (indels)" noenhanced,\
"../../_rocs/exp2.04__Tuberculosis__0.07-ococo16/itref.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 6 title "IR" noenhanced,\
"../../_rocs/exp2.08__Tuberculosis__0.07-dels/itref.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 7 title "IR (dels)" noenhanced,\
"../../_rocs/exp2.06__Tuberculosis__0.07-indels/itref.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 8 title "IR (indels)" noenhanced,\
