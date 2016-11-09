#! /usr/bin/env gnuplot

load "_init.gp"

set out 'manual_exp1.svg'
set title "Experiment 1"

plot \
"../../_rocs/exp1.04__0.07-ococo16/static.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 1 title "SM" noenhanced,\
"../../_rocs/exp1.11__0.07-ococo16-noremap/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 2 title "DM (noremap)" noenhanced,\
"../../_rocs/exp1.04__0.07-ococo16/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 3 title "DM" noenhanced,\
"../../_rocs/exp1.08__0.07-dels/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 4 title "DM (dels)" noenhanced,\
"../../_rocs/exp1.06__0.07-indels/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 5 title "DM (indels)" noenhanced,\
"../../_rocs/exp1.04__0.07-ococo16/itref.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 6 title "IR" noenhanced,\
"../../_rocs/exp1.06__0.07-indels/itref.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 8 title "IR (indels)" noenhanced,\

#"../../_rocs/exp1.08__0.07-dels/itref.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 7 title "IR (dels)" noenhanced,\
