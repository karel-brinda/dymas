#! /usr/bin/env gnuplot

set log x
set log x2

set key bottom right
set x2lab "FDR {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
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

#set autoscale x
#set autoscale y


do for [it=1:2] {
	set output sprintf('manual_exp%d.svg',it)
	set title sprintf('Experiment %d',it)


	set xran [0.00001:0.5]
	set yran [70:100]

	if (it>2){
		if (it<5){
			set xran [0.00001:0.5]
			set yran [40:100]
		}
	}

	prefix=sprintf('../../_rocs/exp%d.',it)

	#"../../_rocs/exp1.08__0.07-dels/itref.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 7 title "IR (dels)" noenhanced,\

	plot \
	prefix."04-ococo16/static.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 1 title "SM" noenhanced,\
	prefix."11-ococo16-noremap/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 2 title "DM (noremap)" noenhanced,\
	prefix."04-ococo16/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 3 title "DM" noenhanced,\
	prefix."08-dels/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 4 title "DM (dels)" noenhanced,\
	prefix."06-indels/dynamic.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 5 title "DM (indels)" noenhanced,\
	prefix."04-ococo16/itref.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 6 title "IR" noenhanced,\
	prefix."06-indels/itref.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 8 title "IR (indels)" noenhanced,\


}
