
set log x
set log x2


#set format x "10^{{%L}}"
set format x2 "10^{{%L}}"
set x2tics
unset xtics

set style line 1 lt 1 pt 1 lc rgb "#0000FF"
set style line 2 lt 1 pt 1 lc rgb "#3F00C0"
set style line 3 lt 1 pt 1 lc rgb "#7F0080"
set style line 4 lt 1 pt 1 lc rgb "#BF0040"
set style line 5 lt 1 pt 1 lc rgb "#FF0000"

set format y "%g %%"
set ytics

set pointsize 1.5

set grid ytics lc rgb "#777777" lw 1 lt 0 front
set grid x2tics lc rgb "#777777" lw 1 lt 0 front

set datafile separator "\t"
set palette negative

set termin svg size 640,640 enhanced
set out "3_evaluation.itref/graphics/_combined_0.svg"
set key spacing 0.8 opaque
##################################################
set title "{/:Bold Mapped reads in all reads}"
set key bottom right
set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
set ylab "#mapped reads / #reads"
set xran [0.0001000000:0.1000000000]
set x2ran [0.0001000000:0.1000000000]
set yran [60.0000000000:100.0000000000]
set y2ran [60.0000000000:100.0000000000]

plot \
"3_evaluation.itref/roc/00000.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 1 ps 0.8 title "  00000" noenhanced,\
"3_evaluation.itref/roc/00001.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 2 ps 0.8 title "  00001" noenhanced,\
"3_evaluation.itref/roc/00002.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 3 ps 0.8 title "  00002" noenhanced,\
"3_evaluation.itref/roc/00003.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 4 ps 0.8 title "  00003" noenhanced,\
"3_evaluation.itref/roc/00004.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 5 ps 0.8 title "  00004" noenhanced,\


set termin svg size 640,640 enhanced
set out "3_evaluation.itref/graphics/_combined_1.svg"
set key spacing 0.8 opaque
##################################################
set title "{/:Bold Correctly mapped reads in all mapped reads}"
set key bottom right
set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
set ylab "#correctly mapped reads / #mapped reads"
set xran [0.0001000000:0.1000000000]
set x2ran [0.0001000000:0.1000000000]
set yran [60.0000000000:100.0000000000]
set y2ran [60.0000000000:100.0000000000]

plot \
"3_evaluation.itref/roc/00000.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 1 ps 0.8 title "  00000" noenhanced,\
"3_evaluation.itref/roc/00001.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 2 ps 0.8 title "  00001" noenhanced,\
"3_evaluation.itref/roc/00002.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 3 ps 0.8 title "  00002" noenhanced,\
"3_evaluation.itref/roc/00003.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 4 ps 0.8 title "  00003" noenhanced,\
"3_evaluation.itref/roc/00004.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 5 ps 0.8 title "  00004" noenhanced,\


set termin svg size 640,640 enhanced
set out "3_evaluation.itref/graphics/_combined_2.svg"
set key spacing 0.8 opaque
##################################################
set title "{/:Bold Correctly mapped reads in all reads which should be mapped}"
set key bottom right
set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
set ylab "#correctly mapped reads / #reads which should be mapped"
set xran [0.0001000000:0.1000000000]
set x2ran [0.0001000000:0.1000000000]
set yran [60.0000000000:100.0000000000]
set y2ran [60.0000000000:100.0000000000]

plot \
"3_evaluation.itref/roc/00000.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 1 ps 0.8 title "  00000" noenhanced,\
"3_evaluation.itref/roc/00001.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 2 ps 0.8 title "  00001" noenhanced,\
"3_evaluation.itref/roc/00002.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 3 ps 0.8 title "  00002" noenhanced,\
"3_evaluation.itref/roc/00003.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 4 ps 0.8 title "  00003" noenhanced,\
"3_evaluation.itref/roc/00004.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 5 ps 0.8 title "  00004" noenhanced,\


set termin svg size 640,640 enhanced
set out "3_evaluation.itref/graphics/_combined_3.svg"
set key spacing 0.8 opaque
##################################################
set title "{/:Bold Correctly unmapped reads in all unmapped reads}"
set key bottom right
set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
set ylab "#correctly unmapped reads / #unmapped reads"
set xran [0.0001000000:0.1000000000]
set x2ran [0.0001000000:0.1000000000]
set yran [60.0000000000:100.0000000000]
set y2ran [60.0000000000:100.0000000000]

plot \
"3_evaluation.itref/roc/00000.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 1 ps 0.8 title "  00000" noenhanced,\
"3_evaluation.itref/roc/00001.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 2 ps 0.8 title "  00001" noenhanced,\
"3_evaluation.itref/roc/00002.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 3 ps 0.8 title "  00002" noenhanced,\
"3_evaluation.itref/roc/00003.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 4 ps 0.8 title "  00003" noenhanced,\
"3_evaluation.itref/roc/00004.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 5 ps 0.8 title "  00004" noenhanced,\


set termin svg size 640,640 enhanced
set out "3_evaluation.itref/graphics/_combined_4.svg"
set key spacing 0.8 opaque
##################################################
set title "{/:Bold Correctly unmapped reads in all reads which should be unmapped}"
set key bottom right
set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
set ylab "#correctly unmapped reads / #reads which should be unmapped"
set xran [0.0001000000:0.1000000000]
set x2ran [0.0001000000:0.1000000000]
set yran [60.0000000000:100.0000000000]
set y2ran [60.0000000000:100.0000000000]

plot \
"3_evaluation.itref/roc/00000.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 1 ps 0.8 title "  00000" noenhanced,\
"3_evaluation.itref/roc/00001.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 2 ps 0.8 title "  00001" noenhanced,\
"3_evaluation.itref/roc/00002.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 3 ps 0.8 title "  00002" noenhanced,\
"3_evaluation.itref/roc/00003.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 4 ps 0.8 title "  00003" noenhanced,\
"3_evaluation.itref/roc/00004.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 5 ps 0.8 title "  00004" noenhanced,\

