#! /usr/bin/env gnuplot

load "_init.gp"

set out 'manual_exp2.svg'
set title "Experiment 2"

par_x1=0.01
par_x2=0.1

par_y1=80
par_y2=100

set xran [par_x1:par_x2]
set x2ran [par_x1:par_x2]

set yran [par_y1:par_y2]
set y2ran [par_y1:par_y2]


plot \
"../../_rocs/exp2.04__Borrelia_dipl__0.07-ococo16/static.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 1 title "SM" noenhanced,\
"../../_rocs/exp2.04__Borrelia_dipl__0.07-ococo16-noremap/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 2 title "DM (noremap)" noenhanced,\
"../../_rocs/exp2.04__Borrelia_dipl__0.07-ococo16/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 3 title "DM" noenhanced,\
"../../_rocs/exp2.04__Borrelia_dipl__0.07-dels/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 4 title "DM (dels)" noenhanced,\
"../../_rocs/exp2.04__Borrelia_dipl__0.07-indels/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 5 title "DM (indels)" noenhanced,\
"../../_rocs/exp2.04__Borrelia_dipl__0.07-ococo16/itref.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 6 title "IR" noenhanced,\
"../../_rocs/exp2.04__Borrelia_dipl__0.07-indels/itref.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 8 title "IR (indels)" noenhanced,\

#"../../_rocs/exp2.08__Tuberculosis__0.07-dels/itref.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 7 title "IR (dels)" noenhanced,\
