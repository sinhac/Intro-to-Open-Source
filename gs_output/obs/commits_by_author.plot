set terminal png transparent size 640,240
set size 1.0,1.0

set terminal png transparent size 640,480
set output 'commits_by_author.png'
set key left top
set yrange [0:]
set xdata time
set timefmt "%s"
set format x "%Y-%m-%d"
set grid y
set ylabel "Commits"
set xtics rotate
set bmargin 6
plot 'commits_by_author.dat' using 1:2 title "Aaron Gunderson" w lines, 'commits_by_author.dat' using 1:3 title "Severin Ibarluzea" w lines, 'commits_by_author.dat' using 1:4 title "Kiana McNellis" w lines, 'commits_by_author.dat' using 1:5 title "jfucci" w lines, 'commits_by_author.dat' using 1:6 title "kmcnellis" w lines, 'commits_by_author.dat' using 1:7 title "seveibar" w lines, 'commits_by_author.dat' using 1:8 title "Zaran" w lines, 'commits_by_author.dat' using 1:9 title "vkr96" w lines, 'commits_by_author.dat' using 1:10 title "Istyatur" w lines, 'commits_by_author.dat' using 1:11 title "nickkoul" w lines, 'commits_by_author.dat' using 1:12 title "Cole Baxter" w lines, 'commits_by_author.dat' using 1:13 title "Nathan Bernard" w lines, 'commits_by_author.dat' using 1:14 title "haoxinLuo" w lines, 'commits_by_author.dat' using 1:15 title "bennyty" w lines, 'commits_by_author.dat' using 1:16 title "Francesca Huber" w lines, 'commits_by_author.dat' using 1:17 title "matthewmawby" w lines, 'commits_by_author.dat' using 1:18 title "leej42" w lines, 'commits_by_author.dat' using 1:19 title "gitcole" w lines, 'commits_by_author.dat' using 1:20 title "Tae Park" w lines, 'commits_by_author.dat' using 1:21 title "Joshua Lu" w lines
