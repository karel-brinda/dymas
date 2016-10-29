
set log x
set log x2


#set format x "10^{{%L}}"
set format x2 "10^{{%L}}"
set x2tics
unset xtics

set style line 1 lt 1 pt 1 lc rgb "#0000FF"
set style line 2 lt 1 pt 1 lc rgb "#0D00F2"
set style line 3 lt 1 pt 1 lc rgb "#1A00E5"
set style line 4 lt 1 pt 1 lc rgb "#2800D7"
set style line 5 lt 1 pt 1 lc rgb "#3500CA"
set style line 6 lt 1 pt 1 lc rgb "#4300BC"
set style line 7 lt 1 pt 1 lc rgb "#5000AF"
set style line 8 lt 1 pt 1 lc rgb "#5D00A2"
set style line 9 lt 1 pt 1 lc rgb "#6B0094"
set style line 10 lt 1 pt 1 lc rgb "#780087"
set style line 11 lt 1 pt 1 lc rgb "#860079"
set style line 12 lt 1 pt 1 lc rgb "#93006C"
set style line 13 lt 1 pt 1 lc rgb "#A1005E"
set style line 14 lt 1 pt 1 lc rgb "#AE0051"
set style line 15 lt 1 pt 1 lc rgb "#BB0044"
set style line 16 lt 1 pt 1 lc rgb "#C90036"
set style line 17 lt 1 pt 1 lc rgb "#D60029"
set style line 18 lt 1 pt 1 lc rgb "#E4001B"
set style line 19 lt 1 pt 1 lc rgb "#F1000E"
set style line 20 lt 1 pt 1 lc rgb "#FF0000"

set format y "%g %%"
set ytics

set pointsize 1.5

set grid ytics lc rgb "#777777" lw 1 lt 0 front
set grid x2tics lc rgb "#777777" lw 1 lt 0 front

set datafile separator "\t"
set palette negative

set termin svg size 640,640 enhanced
set out "3_evaluation.dyn/graphics/_combined_0.svg"
set key spacing 0.8 opaque
##################################################
set title "{/:Bold Mapped reads in all reads}"
set key bottom right
set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
set ylab "#mapped reads / #reads"
set xran [0.0030000000:0.3000000000]
set x2ran [0.0030000000:0.3000000000]
set yran [60.0000000000:100.0000000000]
set y2ran [60.0000000000:100.0000000000]

plot \
"3_evaluation.dyn/roc/00000.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 1 ps 0.8 title "  00000" noenhanced,\
"3_evaluation.dyn/roc/00001.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 2 ps 0.8 title "  00001" noenhanced,\
"3_evaluation.dyn/roc/00002.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 3 ps 0.8 title "  00002" noenhanced,\
"3_evaluation.dyn/roc/00003.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 4 ps 0.8 title "  00003" noenhanced,\
"3_evaluation.dyn/roc/00004.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 5 ps 0.8 title "  00004" noenhanced,\
"3_evaluation.dyn/roc/00005.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 6 ps 0.8 title "  00005" noenhanced,\
"3_evaluation.dyn/roc/00006.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 7 ps 0.8 title "  00006" noenhanced,\
"3_evaluation.dyn/roc/00007.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 8 ps 0.8 title "  00007" noenhanced,\
"3_evaluation.dyn/roc/00008.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 9 ps 0.8 title "  00008" noenhanced,\
"3_evaluation.dyn/roc/00009.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 10 ps 0.8 title "  00009" noenhanced,\
"3_evaluation.dyn/roc/00010.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 11 ps 0.8 title "  00010" noenhanced,\
"3_evaluation.dyn/roc/00011.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 12 ps 0.8 title "  00011" noenhanced,\
"3_evaluation.dyn/roc/00012.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 13 ps 0.8 title "  00012" noenhanced,\
"3_evaluation.dyn/roc/00013.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 14 ps 0.8 title "  00013" noenhanced,\
"3_evaluation.dyn/roc/00014.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 15 ps 0.8 title "  00014" noenhanced,\
"3_evaluation.dyn/roc/00015.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 16 ps 0.8 title "  00015" noenhanced,\
"3_evaluation.dyn/roc/00016.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 17 ps 0.8 title "  00016" noenhanced,\
"3_evaluation.dyn/roc/00017.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 18 ps 0.8 title "  00017" noenhanced,\
"3_evaluation.dyn/roc/00018.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 19 ps 0.8 title "  00018" noenhanced,\
"3_evaluation.dyn/roc/00019.roc" using (($3+$4)/($2+$3+$4)):((($2+$3+$4+$5+$10)/$11)*100) with lp ls 20 ps 0.8 title "  00019" noenhanced,\


set termin svg size 640,640 enhanced
set out "3_evaluation.dyn/graphics/_combined_1.svg"
set key spacing 0.8 opaque
##################################################
set title "{/:Bold Correctly mapped reads in all mapped reads}"
set key bottom right
set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
set ylab "#correctly mapped reads / #mapped reads"
set xran [0.0030000000:0.3000000000]
set x2ran [0.0030000000:0.3000000000]
set yran [60.0000000000:100.0000000000]
set y2ran [60.0000000000:100.0000000000]

plot \
"3_evaluation.dyn/roc/00000.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 1 ps 0.8 title "  00000" noenhanced,\
"3_evaluation.dyn/roc/00001.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 2 ps 0.8 title "  00001" noenhanced,\
"3_evaluation.dyn/roc/00002.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 3 ps 0.8 title "  00002" noenhanced,\
"3_evaluation.dyn/roc/00003.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 4 ps 0.8 title "  00003" noenhanced,\
"3_evaluation.dyn/roc/00004.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 5 ps 0.8 title "  00004" noenhanced,\
"3_evaluation.dyn/roc/00005.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 6 ps 0.8 title "  00005" noenhanced,\
"3_evaluation.dyn/roc/00006.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 7 ps 0.8 title "  00006" noenhanced,\
"3_evaluation.dyn/roc/00007.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 8 ps 0.8 title "  00007" noenhanced,\
"3_evaluation.dyn/roc/00008.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 9 ps 0.8 title "  00008" noenhanced,\
"3_evaluation.dyn/roc/00009.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 10 ps 0.8 title "  00009" noenhanced,\
"3_evaluation.dyn/roc/00010.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 11 ps 0.8 title "  00010" noenhanced,\
"3_evaluation.dyn/roc/00011.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 12 ps 0.8 title "  00011" noenhanced,\
"3_evaluation.dyn/roc/00012.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 13 ps 0.8 title "  00012" noenhanced,\
"3_evaluation.dyn/roc/00013.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 14 ps 0.8 title "  00013" noenhanced,\
"3_evaluation.dyn/roc/00014.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 15 ps 0.8 title "  00014" noenhanced,\
"3_evaluation.dyn/roc/00015.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 16 ps 0.8 title "  00015" noenhanced,\
"3_evaluation.dyn/roc/00016.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 17 ps 0.8 title "  00016" noenhanced,\
"3_evaluation.dyn/roc/00017.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 18 ps 0.8 title "  00017" noenhanced,\
"3_evaluation.dyn/roc/00018.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 19 ps 0.8 title "  00018" noenhanced,\
"3_evaluation.dyn/roc/00019.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$3+$4+$5+$10))*100) with lp ls 20 ps 0.8 title "  00019" noenhanced,\


set termin svg size 640,640 enhanced
set out "3_evaluation.dyn/graphics/_combined_2.svg"
set key spacing 0.8 opaque
##################################################
set title "{/:Bold Correctly mapped reads in all reads which should be mapped}"
set key bottom right
set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
set ylab "#correctly mapped reads / #reads which should be mapped"
set xran [0.0030000000:0.3000000000]
set x2ran [0.0030000000:0.3000000000]
set yran [60.0000000000:100.0000000000]
set y2ran [60.0000000000:100.0000000000]

plot \
"3_evaluation.dyn/roc/00000.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 1 ps 0.8 title "  00000" noenhanced,\
"3_evaluation.dyn/roc/00001.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 2 ps 0.8 title "  00001" noenhanced,\
"3_evaluation.dyn/roc/00002.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 3 ps 0.8 title "  00002" noenhanced,\
"3_evaluation.dyn/roc/00003.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 4 ps 0.8 title "  00003" noenhanced,\
"3_evaluation.dyn/roc/00004.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 5 ps 0.8 title "  00004" noenhanced,\
"3_evaluation.dyn/roc/00005.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 6 ps 0.8 title "  00005" noenhanced,\
"3_evaluation.dyn/roc/00006.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 7 ps 0.8 title "  00006" noenhanced,\
"3_evaluation.dyn/roc/00007.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 8 ps 0.8 title "  00007" noenhanced,\
"3_evaluation.dyn/roc/00008.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 9 ps 0.8 title "  00008" noenhanced,\
"3_evaluation.dyn/roc/00009.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 10 ps 0.8 title "  00009" noenhanced,\
"3_evaluation.dyn/roc/00010.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 11 ps 0.8 title "  00010" noenhanced,\
"3_evaluation.dyn/roc/00011.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 12 ps 0.8 title "  00011" noenhanced,\
"3_evaluation.dyn/roc/00012.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 13 ps 0.8 title "  00012" noenhanced,\
"3_evaluation.dyn/roc/00013.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 14 ps 0.8 title "  00013" noenhanced,\
"3_evaluation.dyn/roc/00014.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 15 ps 0.8 title "  00014" noenhanced,\
"3_evaluation.dyn/roc/00015.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 16 ps 0.8 title "  00015" noenhanced,\
"3_evaluation.dyn/roc/00016.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 17 ps 0.8 title "  00016" noenhanced,\
"3_evaluation.dyn/roc/00017.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 18 ps 0.8 title "  00017" noenhanced,\
"3_evaluation.dyn/roc/00018.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 19 ps 0.8 title "  00018" noenhanced,\
"3_evaluation.dyn/roc/00019.roc" using (($3+$4)/($2+$3+$4)):(($2/($2+$4+$10+$7+$9+$5))*100) with lp ls 20 ps 0.8 title "  00019" noenhanced,\


set termin svg size 640,640 enhanced
set out "3_evaluation.dyn/graphics/_combined_3.svg"
set key spacing 0.8 opaque
##################################################
set title "{/:Bold Correctly unmapped reads in all unmapped reads}"
set key bottom right
set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
set ylab "#correctly unmapped reads / #unmapped reads"
set xran [0.0030000000:0.3000000000]
set x2ran [0.0030000000:0.3000000000]
set yran [60.0000000000:100.0000000000]
set y2ran [60.0000000000:100.0000000000]

plot \
"3_evaluation.dyn/roc/00000.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 1 ps 0.8 title "  00000" noenhanced,\
"3_evaluation.dyn/roc/00001.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 2 ps 0.8 title "  00001" noenhanced,\
"3_evaluation.dyn/roc/00002.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 3 ps 0.8 title "  00002" noenhanced,\
"3_evaluation.dyn/roc/00003.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 4 ps 0.8 title "  00003" noenhanced,\
"3_evaluation.dyn/roc/00004.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 5 ps 0.8 title "  00004" noenhanced,\
"3_evaluation.dyn/roc/00005.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 6 ps 0.8 title "  00005" noenhanced,\
"3_evaluation.dyn/roc/00006.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 7 ps 0.8 title "  00006" noenhanced,\
"3_evaluation.dyn/roc/00007.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 8 ps 0.8 title "  00007" noenhanced,\
"3_evaluation.dyn/roc/00008.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 9 ps 0.8 title "  00008" noenhanced,\
"3_evaluation.dyn/roc/00009.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 10 ps 0.8 title "  00009" noenhanced,\
"3_evaluation.dyn/roc/00010.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 11 ps 0.8 title "  00010" noenhanced,\
"3_evaluation.dyn/roc/00011.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 12 ps 0.8 title "  00011" noenhanced,\
"3_evaluation.dyn/roc/00012.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 13 ps 0.8 title "  00012" noenhanced,\
"3_evaluation.dyn/roc/00013.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 14 ps 0.8 title "  00013" noenhanced,\
"3_evaluation.dyn/roc/00014.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 15 ps 0.8 title "  00014" noenhanced,\
"3_evaluation.dyn/roc/00015.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 16 ps 0.8 title "  00015" noenhanced,\
"3_evaluation.dyn/roc/00016.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 17 ps 0.8 title "  00016" noenhanced,\
"3_evaluation.dyn/roc/00017.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 18 ps 0.8 title "  00017" noenhanced,\
"3_evaluation.dyn/roc/00018.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 19 ps 0.8 title "  00018" noenhanced,\
"3_evaluation.dyn/roc/00019.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($7+$6+$9+$8))*100) with lp ls 20 ps 0.8 title "  00019" noenhanced,\


set termin svg size 640,640 enhanced
set out "3_evaluation.dyn/graphics/_combined_4.svg"
set key spacing 0.8 opaque
##################################################
set title "{/:Bold Correctly unmapped reads in all reads which should be unmapped}"
set key bottom right
set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}}  "
set ylab "#correctly unmapped reads / #reads which should be unmapped"
set xran [0.0030000000:0.3000000000]
set x2ran [0.0030000000:0.3000000000]
set yran [60.0000000000:100.0000000000]
set y2ran [60.0000000000:100.0000000000]

plot \
"3_evaluation.dyn/roc/00000.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 1 ps 0.8 title "  00000" noenhanced,\
"3_evaluation.dyn/roc/00001.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 2 ps 0.8 title "  00001" noenhanced,\
"3_evaluation.dyn/roc/00002.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 3 ps 0.8 title "  00002" noenhanced,\
"3_evaluation.dyn/roc/00003.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 4 ps 0.8 title "  00003" noenhanced,\
"3_evaluation.dyn/roc/00004.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 5 ps 0.8 title "  00004" noenhanced,\
"3_evaluation.dyn/roc/00005.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 6 ps 0.8 title "  00005" noenhanced,\
"3_evaluation.dyn/roc/00006.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 7 ps 0.8 title "  00006" noenhanced,\
"3_evaluation.dyn/roc/00007.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 8 ps 0.8 title "  00007" noenhanced,\
"3_evaluation.dyn/roc/00008.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 9 ps 0.8 title "  00008" noenhanced,\
"3_evaluation.dyn/roc/00009.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 10 ps 0.8 title "  00009" noenhanced,\
"3_evaluation.dyn/roc/00010.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 11 ps 0.8 title "  00010" noenhanced,\
"3_evaluation.dyn/roc/00011.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 12 ps 0.8 title "  00011" noenhanced,\
"3_evaluation.dyn/roc/00012.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 13 ps 0.8 title "  00012" noenhanced,\
"3_evaluation.dyn/roc/00013.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 14 ps 0.8 title "  00013" noenhanced,\
"3_evaluation.dyn/roc/00014.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 15 ps 0.8 title "  00014" noenhanced,\
"3_evaluation.dyn/roc/00015.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 16 ps 0.8 title "  00015" noenhanced,\
"3_evaluation.dyn/roc/00016.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 17 ps 0.8 title "  00016" noenhanced,\
"3_evaluation.dyn/roc/00017.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 18 ps 0.8 title "  00017" noenhanced,\
"3_evaluation.dyn/roc/00018.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 19 ps 0.8 title "  00018" noenhanced,\
"3_evaluation.dyn/roc/00019.roc" using (($3+$4)/($2+$3+$4)):((($6+$8)/($6+$8+$3))*100) with lp ls 20 ps 0.8 title "  00019" noenhanced,\

