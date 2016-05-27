# Numbers of reads in several categories in dependence
# on the applied threshold on mapping quality q
# 
# Categories:
#        M: Mapped correctly.
#        w: Mapped to a wrong position.
#        m: Mapped but should be unmapped.
#        P: Multimapped.
#        U: Unmapped and should be unmapped.
#        u: Unmapped but should be mapped.
#        T: Thresholded correctly.
#        t: Thresholded incorrectly.
#        x: Unknown.
#
# q	M	w	m	P	U	u	T	t	x	all
0	524	1	0	0	0	181	0	0	0	706
1	508	1	0	0	0	181	0	16	0	706
2	507	0	0	0	0	181	0	18	0	706
4	489	0	0	0	0	181	0	36	0	706
8	488	0	0	0	0	181	0	37	0	706
9	444	0	0	0	0	181	0	81	0	706
24	352	0	0	0	0	181	0	173	0	706
25	255	0	0	0	0	181	0	270	0	706
41	80	0	0	0	0	181	0	445	0	706
43	0	0	0	0	0	181	0	525	0	706
