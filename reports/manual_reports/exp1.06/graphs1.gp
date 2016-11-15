
experiment_dir='../../../experiments/exp1.06-indels/'

set x2lab "FDR in mapping {{/:Italic(#wrongly mapped reads / #mapped reads)}} "
set log x
set log x2

set format x "10^{%L}"
set format x2 "10^{%L}"
set xran [.0008:.15]
set x2ran [.0008:.15]
set x2tics
unset xtics


set ylab "Part of all reads (%)"

set format y "%g %%"
set yran [85:100]
set y2ran [85:100]

set pointsize 1.5

set grid ytics lc rgb "#777777" lw 1 lt 0 front
set grid x2tics lc rgb "#777777" lw 1 lt 0 front

set datafile separator "\t"
set palette negative

set termin svg size 500,500 enhanced

set key off


#experiment_dir."3_evaluation.itref/roc/00000.roc" using (( (($3+$4)/($2+$3+$4)) )):(($6+$7+$8+$9+$5+$4+$10+$3+$2)*100/$11) lt rgb "#ee82ee" with filledcurve x1 title "Unmapped correctly", \
#experiment_dir."3_evaluation.itref/roc/00000.roc" using (( (($3+$4)/($2+$3+$4)) )):(($8+$9+$5+$4+$10+$3+$2)*100/$11) lt rgb "#00ff00" with filledcurve x1 title "Thresholded correctly", \

#set title "{/:Bold Static mapping}"
set out "sm.svg"
plot \
experiment_dir."3_evaluation.itref/roc/00000.roc" using (( (($3+$4)/($2+$3+$4)) )):(($7+$8+$9+$5+$4+$10+$3+$2)*100/$11) lt rgb "#ff0000" with filledcurve x1 title "Unmapped incorrectly", \
experiment_dir."3_evaluation.itref/roc/00000.roc" using (( (($3+$4)/($2+$3+$4)) )):(($9+$5+$4+$10+$3+$2)*100/$11) lt rgb "#008800" with filledcurve x1 title "Thresholded incorrectly", \
experiment_dir."3_evaluation.itref/roc/00000.roc" using (( (($3+$4)/($2+$3+$4)) )):(($5+$4+$10+$3+$2)*100/$11) lt rgb "#ffff00" with filledcurve x1 title "Multimapped", \
experiment_dir."3_evaluation.itref/roc/00000.roc" using (( (($3+$4)/($2+$3+$4)) )):(($4+$10+$3+$2)*100/$11) lt rgb "#7f7f7f" with filledcurve x1 title "Mapped, should be unmapped", \
experiment_dir."3_evaluation.itref/roc/00000.roc" using (( (($3+$4)/($2+$3+$4)) )):(($3+$2)*100/$11) lt rgb "#000000" with filledcurve x1 title "Mapped to wrong position", \
experiment_dir."3_evaluation.itref/roc/00000.roc" using (( (($3+$4)/($2+$3+$4)) )):(($2)*100/$11) lt rgb "#0000ff" with filledcurve x1 title "Mapped correctly", \


#experiment_dir."3_evaluation.dyn/roc/00019.roc" using (( (($3+$4)/($2+$3+$4)) )):(($6+$7+$8+$9+$5+$4+$10+$3+$2)*100/$11) lt rgb "#ee82ee" with filledcurve x1 title "Unmapped correctly", \
#experiment_dir."3_evaluation.dyn/roc/00019.roc" using (( (($3+$4)/($2+$3+$4)) )):(($8+$9+$5+$4+$10+$3+$2)*100/$11) lt rgb "#00ff00" with filledcurve x1 title "Thresholded correctly", \

#set title "{/:Bold Dynamic mapping with remapping}"
set out "dm.svg"
plot \
experiment_dir."3_evaluation.dyn/roc/00019.roc" using (( (($3+$4)/($2+$3+$4)) )):(($7+$8+$9+$5+$4+$10+$3+$2)*100/$11) lt rgb "#ff0000" with filledcurve x1 title "Unmapped incorrectly", \
experiment_dir."3_evaluation.dyn/roc/00019.roc" using (( (($3+$4)/($2+$3+$4)) )):(($9+$5+$4+$10+$3+$2)*100/$11) lt rgb "#008800" with filledcurve x1 title "Thresholded incorrectly", \
experiment_dir."3_evaluation.dyn/roc/00019.roc" using (( (($3+$4)/($2+$3+$4)) )):(($5+$4+$10+$3+$2)*100/$11) lt rgb "#ffff00" with filledcurve x1 title "Multimapped", \
experiment_dir."3_evaluation.dyn/roc/00019.roc" using (( (($3+$4)/($2+$3+$4)) )):(($4+$10+$3+$2)*100/$11) lt rgb "#7f7f7f" with filledcurve x1 title "Mapped, should be unmapped", \
experiment_dir."3_evaluation.dyn/roc/00019.roc" using (( (($3+$4)/($2+$3+$4)) )):(($3+$2)*100/$11) lt rgb "#000000" with filledcurve x1 title "Mapped to wrong position", \
experiment_dir."3_evaluation.dyn/roc/00019.roc" using (( (($3+$4)/($2+$3+$4)) )):(($2)*100/$11) lt rgb "#0000ff" with filledcurve x1 title "Mapped correctly", \


set key bottom right
set key spacing 0.8 opaque width -5
set key box

#experiment_dir."3_evaluation.itref/roc/00004.roc" using (( (($3+$4)/($2+$3+$4)) )):(($6+$7+$8+$9+$5+$4+$10+$3+$2)*100/$11) lt rgb "#ee82ee" with filledcurve x1 title "Unmapped correctly", \
#experiment_dir."3_evaluation.itref/roc/00004.roc" using (( (($3+$4)/($2+$3+$4)) )):(($8+$9+$5+$4+$10+$3+$2)*100/$11) lt rgb "#00ff00" with filledcurve x1 title "Thresholded correctly", \

#set title "{/:Bold Iterative referencing}"
set out "ir.svg"
plot \
experiment_dir."3_evaluation.itref/roc/00004.roc" using (( (($3+$4)/($2+$3+$4)) )):(($7+$8+$9+$5+$4+$10+$3+$2)*100/$11) lt rgb "#ff0000" with filledcurve x1 title "Unmapped incorrectly", \
experiment_dir."3_evaluation.itref/roc/00004.roc" using (( (($3+$4)/($2+$3+$4)) )):(($9+$5+$4+$10+$3+$2)*100/$11) lt rgb "#008800" with filledcurve x1 title "Thresholded incorrectly", \
experiment_dir."3_evaluation.itref/roc/00004.roc" using (( (($3+$4)/($2+$3+$4)) )):(($5+$4+$10+$3+$2)*100/$11) lt rgb "#ffff00" with filledcurve x1 title "Multimapped", \
experiment_dir."3_evaluation.itref/roc/00004.roc" using (( (($3+$4)/($2+$3+$4)) )):(($4+$10+$3+$2)*100/$11) lt rgb "#7f7f7f" with filledcurve x1 title "Mapped, should be unmapped", \
experiment_dir."3_evaluation.itref/roc/00004.roc" using (( (($3+$4)/($2+$3+$4)) )):(($3+$2)*100/$11) lt rgb "#000000" with filledcurve x1 title "Mapped to wrong position", \
experiment_dir."3_evaluation.itref/roc/00004.roc" using (( (($3+$4)/($2+$3+$4)) )):(($2)*100/$11) lt rgb "#0000ff" with filledcurve x1 title "Mapped correctly", \
