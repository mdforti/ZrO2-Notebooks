datavol.dat: tkens.sh
	bash tkens.sh

more_useful_data.txt: alldata.txt
	bash get_usefull_data.sh > more_useful_data.txt

alldata.txt: get_all_sumo.sh
	bash get_all_sumo.sh

make_valenceband_wall.pdf: make_valenceband_wall.tex detail_bands_hole.sh
	pdflatex make_valenceband_wall.tex

detail
