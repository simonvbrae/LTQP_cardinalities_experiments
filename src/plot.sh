#!/bin/bash
# This file was used to create different types of plots via the psbr library.

# Requires local psbr: https://github.com/rubensworks/process-sparql-benchmark-results.js/
psbrInstallationDirectory=/home/simon/Documents/Unief/Thesis/process-sparql-benchmark-results.js/bin/psbr

# Plotting dieff of all configurations 23.6.12
inputDir=/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12

queries=("interactive-discover-1-0" "interactive-discover-1-1" "interactive-discover-1-2" "interactive-discover-1-3" "interactive-discover-1-4" "interactive-discover-2-0" "interactive-discover-2-1" "interactive-discover-2-2" "interactive-discover-2-3" "interactive-discover-2-4" "interactive-discover-3-0" "interactive-discover-3-1" "interactive-discover-3-2" "interactive-discover-3-3" "interactive-discover-3-4" "interactive-discover-4-0" "interactive-discover-4-1" "interactive-discover-4-2" "interactive-discover-4-3" "interactive-discover-4-4" "interactive-discover-5-0" "interactive-discover-5-1" "interactive-discover-5-2" "interactive-discover-5-3" "interactive-discover-5-4" "interactive-discover-6-0" "interactive-discover-6-1" "interactive-discover-6-2" "interactive-discover-6-3" "interactive-discover-6-4" "interactive-discover-7-0" "interactive-discover-7-1" "interactive-discover-7-2" "interactive-discover-7-3" "interactive-discover-7-4" "interactive-discover-8-0" "interactive-discover-8-1" "interactive-discover-8-2" "interactive-discover-8-3" "interactive-discover-8-4" "interactive-short-1-0" "interactive-short-1-1" "interactive-short-1-2" "interactive-short-1-3" "interactive-short-1-4" "interactive-short-2-0" "interactive-short-2-1" "interactive-short-2-2" "interactive-short-2-3" "interactive-short-2-4" "interactive-short-3-0" "interactive-short-3-1" "interactive-short-3-2" "interactive-short-3-3" "interactive-short-3-4" "interactive-short-4-0" "interactive-short-4-1" "interactive-short-4-2" "interactive-short-4-3" "interactive-short-4-4" "interactive-short-5-0" "interactive-short-5-1" "interactive-short-5-2" "interactive-short-5-3" "interactive-short-5-4" "interactive-short-6-0" "interactive-short-6-1" "interactive-short-6-2" "interactive-short-6-3" "interactive-short-6-4" "interactive-short-7-0" "interactive-short-7-1" "interactive-short-7-2" "interactive-short-7-3" "interactive-short-7-4")
for q in ${queries[@]};
do
    NAME="8_may_dieff_$q"

    $psbrInstallationDirectory tex queryTimes $q --name "$NAME" --svg \
    --color Dark2 \
    --overrideCombinationLabels 'base_zero','index_card','count','count+index'\
    --inputName "result-psbrtitle-qtimes.csv"\
    $inputDir/baseline/baseline-zero $inputDir/index/index-card $inputDir/timeout/timeout-noindex-card $inputDir/timeout/timeout-index-card

    texliveonfly "$NAME.tex"
    # mv $NAME.pdf 7_may_diefficiency
    sleep 1
    rm "$NAME.csv"
    rm $NAME.aux
    rm $NAME.log
    rm $NAME.synctex.gz
done

# Plotting results of all configurations 23.6.12
# inputDir=/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12

# subsetFileSuffixes=("disc1-3" "disc4-6" "disc7-8" "short1-3" "short4-6" "short7")
# queryLabels=("1.0,1.1,1.2,1.3,1.4,2.0,2.1,2.2,2.3,2.4,3.0,3.1,3.2,3.3,3.4" "4.0,4.1,4.2,4.3,4.4,5.0,5.1,5.2,5.3,5.4,6.0,6.1,6.2,6.3,6.4" "7.0,7.1,7.2,7.3,7.4,8.0,8.1,8.2,8.3,8.4" "1.0,1.1,1.2,1.3,1.4,2.0,2.1,2.2,2.3,2.4,3.0,3.1,3.2,3.3,3.4" "4.0,4.1,4.2,4.3,4.4,5.0,5.1,5.2,5.3,5.4,6.0,6.1,6.2,6.3,6.4" "7.0,7.1,7.2,7.3,7.4")
# for i in 0 1 2 3 4;
# do
#     subsetFileSuffix=${subsetFileSuffixes[$i]}
#     echo $subsetFileSuffix
#     NAME="4_jul_all_compare_$subsetFileSuffix"
#     /home/simon/Documents/Unief/Thesis/process-sparql-benchmark-results.js/bin/psbr tex query --name $NAME --svg --legendPos '1.4,0.9' --relative \
#         --color Paired-12 \
#         --inputName "result-psbrtitle-$subsetFileSuffix.csv"\
#         --overrideQueryLabels ${queryLabels[$i]}\
#         --overrideCombinationLabels 'baseline - zero','baseline - cardinality','index - zero','index - card','timeout - noindex - card','timeout - index - card'\
#         $inputDir/baseline/baseline-zero $inputDir/baseline/baseline-card $inputDir/index/index-zero $inputDir/index/index-card $inputDir/timeout/timeout-noindex-card $inputDir/timeout/timeout-index-card
#     texliveonfly $NAME.tex
#     sleep 1
#     rm $NAME.csv
#     rm $NAME.aux
#     rm $NAME.log
#     rm $NAME.synctex.gz
# done

# # Plotting results of all configurations 23.5.31
# inputDir=/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.5.31

# subsetFileSuffixes=("disc1-3" "disc4-6" "disc7-8" "short1-3" "short4-6" "short7")
# queryLabels=("1.0,1.1,1.2,1.3,1.4,2.0,2.1,2.2,2.3,2.4,3.0,3.1,3.2,3.3,3.4" "4.0,4.1,4.2,4.3,4.4,5.0,5.1,5.2,5.3,5.4,6.0,6.1,6.2,6.3,6.4" "7.0,7.1,7.2,7.3,7.4,8.0,8.1,8.2,8.3,8.4" "1.0,1.1,1.2,1.3,1.4,2.0,2.1,2.2,2.3,2.4,3.0,3.1,3.2,3.3,3.4" "4.0,4.1,4.2,4.3,4.4,5.0,5.1,5.2,5.3,5.4,6.0,6.1,6.2,6.3,6.4" "7.0,7.1,7.2,7.3,7.4")
# for i in 0 1 2 3 4;
# do
#     subsetFileSuffix=${subsetFileSuffixes[$i]}
#     echo $subsetFileSuffix
#     NAME="8_jun_all_compare_$subsetFileSuffix"
#     /home/simon/Documents/Unief/Thesis/process-sparql-benchmark-results.js/bin/psbr tex query --name $NAME --svg --legendPos '1.4,0.9' --relative \
#         --color Paired-12 \
#         --inputName "result-psbrtitle-$subsetFileSuffix.csv"\
#         --overrideQueryLabels ${queryLabels[$i]}\
#         --overrideCombinationLabels 'baseline - zero','baseline - cardinality','callback - zero','callback - card','timeout - noindex','timeout - index'\
#         $inputDir/baseline/baseline-zero $inputDir/baseline/baseline-card $inputDir/callback/callback-zero-zero $inputDir/callback/callback-card-card $inputDir/timeout/timeout-noextract2-card $inputDir/timeout/timeout-extract2-card
#     texliveonfly $NAME.tex
#     sleep 1
#     rm $NAME.csv
#     rm $NAME.aux
#     rm $NAME.log
#     rm $NAME.synctex.gz
# done

# Plotting results of all configurations above 1000
# inputDir=/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.5.31

# subsetFileSuffixes=("timeAbove1000-0" "timeAbove1000-1" "timeAbove1000-2" "timeAbove1000-3")
# queryLabels=("d1.0,d1.3,d1.4,d2.0,d2.3,d2.4,d3.1,d3.3,d5.0,d5.3,d5.4,d6.0,d6.3,d6.4" "d7.0,d7.3,d7.4,d8.0,d8.1,d8.2,d8.3,d8.4,s1.0,s1.1,s1.2,s1.3,s1.4" "s2.0,s2.1,s2.2,s2.3,s2.4,s3.0,s3.1,s3.2,s3.3,s3.4" "s6.0,s6.1,s6.2,s6.3,s6.4,s7.0,s7.1,s7.2,s7.3,s7.4")
# for i in 0 1 2 3;
# do
#     subsetFileSuffix=${subsetFileSuffixes[$i]}
#     oNAME="8_may_all_extimes_above1000-$subsetFileSuffix"
#     /home/simon/Documents/Unief/Thesis/process-sparql-benchmark-results.js/bin/psbr tex query --name $oNAME --svg --legendPos '1.4,0.9' --relative \
#         --color Paired-12 \
#         --inputName "result-psbrtitle-$subsetFileSuffix.csv"\
#         --overrideQueryLabels ${queryLabels[$i]}\
#         --overrideCombinationLabels 'baseline - zero','baseline - cardinality','callback - zero','callback - card','timeout - noindex','timeout - index'\
#         $inputDir/baseline/baseline-zero $inputDir/baseline/baseline-card $inputDir/callback/callback-zero-zero $inputDir/callback/callback-card-card $inputDir/timeout/timeout-noextract2-card $inputDir/timeout/timeout-extract2-card
#     texliveonfly $oNAME.tex
#     sleep 1
#     rm $oNAME.csv
#     rm $oNAME.aux
#     rm $oNAME.log
#     rm $oNAME.synctex.gz
# done

# Plotting dieff of each query of all configurations
# resultDir=/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.5.31
# queries=("interactive-discover-1-0" "interactive-discover-1-1" "interactive-discover-1-2" "interactive-discover-1-3" "interactive-discover-1-4" "interactive-discover-2-0" "interactive-discover-2-1" "interactive-discover-2-2" "interactive-discover-2-3" "interactive-discover-2-4" "interactive-discover-3-0" "interactive-discover-3-1" "interactive-discover-3-2" "interactive-discover-3-3" "interactive-discover-3-4" "interactive-discover-4-0" "interactive-discover-4-1" "interactive-discover-4-2" "interactive-discover-4-3" "interactive-discover-4-4" "interactive-discover-5-0" "interactive-discover-5-1" "interactive-discover-5-2" "interactive-discover-5-3" "interactive-discover-5-4" "interactive-discover-6-0" "interactive-discover-6-1" "interactive-discover-6-2" "interactive-discover-6-3" "interactive-discover-6-4" "interactive-discover-7-0" "interactive-discover-7-1" "interactive-discover-7-2" "interactive-discover-7-3" "interactive-discover-7-4" "interactive-discover-8-0" "interactive-discover-8-1" "interactive-discover-8-2" "interactive-discover-8-3" "interactive-discover-8-4" "interactive-short-1-0" "interactive-short-1-1" "interactive-short-1-2" "interactive-short-1-3" "interactive-short-1-4" "interactive-short-2-0" "interactive-short-2-1" "interactive-short-2-2" "interactive-short-2-3" "interactive-short-2-4" "interactive-short-3-0" "interactive-short-3-1" "interactive-short-3-2" "interactive-short-3-3" "interactive-short-3-4" "interactive-short-4-0" "interactive-short-4-1" "interactive-short-4-2" "interactive-short-4-3" "interactive-short-4-4" "interactive-short-5-0" "interactive-short-5-1" "interactive-short-5-2" "interactive-short-5-3" "interactive-short-5-4" "interactive-short-6-0" "interactive-short-6-1" "interactive-short-6-2" "interactive-short-6-3" "interactive-short-6-4" "interactive-short-7-0" "interactive-short-7-1" "interactive-short-7-2" "interactive-short-7-3" "interactive-short-7-4")
# for q in ${queries[@]};
# do
#     NAME="8_may_dieff_$q"

#     psbr tex queryTimes $q --name "$NAME" --svg \
#     --color Paired-12 \
#     --overrideCombinationLabels 'baseline - zero','baseline - cardinality','callback - zero','callback - card','timeout - noindex','timeout - index'\
#     --inputName "result-psbrtitle-qtimes.csv"\
#     $resultDir/baseline/baseline-zero $resultDir/baseline/baseline-card $resultDir/callback/callback-zero-zero $resultDir/callback/callback-card-card $resultDir/timeout/timeout-extract2-card $resultDir/callback/callback-card-card

#     texliveonfly "$NAME.tex"
#     # mv $NAME.pdf 7_may_diefficiency
#     sleep 1
#     rm "$NAME.csv"
#     rm $NAME.aux
#     rm $NAME.log
#     rm $NAME.synctex.gz
# done


# NAME="6_may_baseline_compare"
# psbr tex query --name $NAME --legendPos '1.4,0.9' --relative \
#     --color Paired-12 \
#     --inputName "result-psbrtitle-disc1-3.csv"\
#     --overrideQueryLabels 1 2 3\
#     --overrideCombinationLabels 'baseline - zero'\
#     experiment-results/23.5.31/baseline/baseline-card #TODO <- zet terug op zero #experiment-results/23.5.31/baseline/baseline-card experiment-results/23.5.31/callback/callback-zero-zero experiment-results/23.5.31/callback/callback-card-card
# texliveonfly $NAME.texsubsetFile
# exit()
# echo 'HI'
# # 6 may plot baseline
# subsetFileAdds=("disc1-3") # "disc4-6") #"disc7-8" "short1-3" "short4-6" "short7")
# queryLabels=("1.0,1.1,1.2,1.3,1.4,2.0,2.1,2.2,2.3,2.4,3.0,3.1,3.2,3.3,3.4") # "4.0,4.1,4.2,4.3,4.4,5.0,5.1,5.2,5.3,5.4,6.0,6.1,6.2,6.3,6.4")
# for i in 0;# 2 3 4 5;
# do
#     NAME="6_may_baseline_compare_${subsetFileAdds[$i]}"
#     psbr tex query --name $NAME --legendPos '1.4,0.9' --relative \
#         --color Paired-12 \
#         --inputName "result-psbrtitle-${subsetFileAdds[$i]}.csv"\
#         --overrideQueryLabels ${queryLabels[$i]}\
#         --overrideCombinationLabels 'baseline - zero'\
#         experiment-results/23.5.31/baseline/baseline-card #TODO <- zet terug op zero #experiment-results/23.5.31/baseline/baseline-card experiment-results/23.5.31/callback/callback-zero-zero experiment-results/23.5.31/callback/callback-card-card
#     texliveonfly $NAME.tex
#     sleep 1
#     rm $NAME.csv
#     rm $NAME.aux
#     rm $NAME.log
#     rm $NAME.synctex.gz
# done



# NAME='6_may_baseline_compare'
# psbr tex query --name $NAME --svg --legendPos '1.4,0.9' --relative \
#     --color Paired-12 \
#     --inputName result-psbrtitle.csv\
#     --overrideQueryLabels D1,2,3,4,5,6,7,8,S1,.2,.3,.4,.5,.6,.7 \
#     --overrideCombinationLabels 'baseline - zero','baseline - cardinality','callback - zero','callback - card' \
#     experiment-results/23.5.31/baseline/baseline-zero experiment-results/23.5.31/baseline/baseline-card experiment-results/23.5.31/callback/callback-zero-zero experiment-results/23.5.31/callback/callback-card-card
# texliveonfly $NAME.tex
# sleep 1
# rm $NAME.csv
# rm $NAME.aux
# rm $NAME.log
# rm $NAME.synctex.gz
