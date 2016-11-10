#! /usr/bin/env gnuplot

set log x
set log x2

set format x "10^{%L}"
set format x2 "10^{%L}"

set termin svg size 400,400 enhanced
set out par_file.'.svg'
set key spacing 0.8 opaque

set title par_title
set key bottom right
set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
set ylab "#correctly mapped reads / #reads which should be mapped"

#set xran [par_x1:par_x2]
#set x2ran [par_x1:par_x2]

#set yran [par_y1:par_y2]
#set y2ran [par_y1:par_y2]

set autoscale x
set autoscale y

set style line 1 lt 1 pt 1 lc rgb "#00cc00"
set style line 2 lt 1 pt 1 lc rgb "#ff0000"
set style line 3 lt 1 pt 1 lc rgb "#0000ff"

plot \
par_dir."/static.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 1 ps 0.5 title "static mapping" noenhanced,\
par_dir."/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 2 ps 0.5 title "dynamic mapping" noenhanced,\
par_dir."/itref.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 3 ps 0.5 title "iterative referencing" noenhanced,\
