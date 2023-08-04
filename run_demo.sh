#!/bin/sh

###################################
#  user defined, please change:)  #
###################################
# project names and it's location
# PROJECTNAME=mytest_suppress # we build a ${PROJECTNAME}.py as final plant for controller synthesis
# BENCHMARKLOCATION=benchmarks/mytests # this directory should inclide only two files: (1) a extended plant, (2) a hyperautomaton
#
# # sepecify file names
# ENTENDEDPLANT=mytest_suppress_extended.js
# HYPERAUTOMATON=hyperauto_test.txt

# PROJECTNAME=example
# BENCHMARKLOCATION=demo/example
# ENTENDEDPLANT=example_extended.js
# HYPERAUTOMATON=hyperauto_example.txt

PROJECTNAME=test
BENCHMARKLOCATION=demo/test
ENTENDEDPLANT=extended.js
HYPERAUTOMATON=hyperauto.txt

###################################################
#   tool parameters, please don't change below    #
###################################################
# tools #
EXPOSE=1_buildModel/ExpoSE
EXTRACTOR=1_buildModel/modelbuilder.py
SYNTHSISTOOL=2_synth_symbolic #up-to-date version

# JS programs #
JSPROGRAM=${BENCHMARKLOCATION}/${ENTENDEDPLANT}
HYPERAUTOFILE=${BENCHMARKLOCATION}/${HYPERAUTOMATON}
### read/write file names ###
OUTFOLDER=${BENCHMARKLOCATION}/hyperenforce_out
mkdir -p ${OUTFOLDER}
EXPOSEOUT=${OUTFOLDER}/output.txt
TRACESFILE=${OUTFOLDER}/traces.txt
MODELFILE=${OUTFOLDER}/model.txt
STATSFILE=${OUTFOLDER}/stats.txt
FINLAPLANT=${OUTFOLDER}/${PROJECTNAME}.py

############
#   MAIN   #
############
echo "======================================================="
echo " HyperEnforce! Runtime enforcement of hyperproperties "
echo "======================================================="
echo "- project name:       ${PROJECTNAME}"
echo "- benchmark location: ${BENCHMARKLOCATION}"
echo "- extended plant:     ${BENCHMARKLOCATION}/${ENTENDEDPLANT}"
echo "- hyperautomaton:     ${BENCHMARKLOCATION}/${HYPERAUTOMATON}"

echo "\n (hyperenforce starts.)"

echo "\n\`\` step 1: build formal model. \`\`"
echo "call expoSE to obtain information of a JS program..."
EXPOSE_PRINT_PATHS=1 EXPOSE_LOG_LEVEL=3 EXPOSE_MAX_CONCURRENT=1 ${EXPOSE} ${JSPROGRAM} > ${EXPOSEOUT}
echo "\n\`\` success! \`\`"

echo "\n\`\` use modelBuilder.py to obtain a well-formatted collection of traces and build model...\`\`"
python3 ${EXTRACTOR} ${JSPROGRAM} ${EXPOSEOUT} ${TRACESFILE} ${MODELFILE} ${HYPERAUTOFILE} ${STATSFILE} ${FINLAPLANT};
echo "\n\`\` success! \`\` "

echo "\n\`\` step 2: synthesis controller \`\`"
echo "\n\`\` call synthesis tool, using either symbolic or explicit automaton \`\`"


time(
mkdir -p ${SYNTHSISTOOL}/temp_container;
cp ${OUTFOLDER}/*.py ${SYNTHSISTOOL}/temp_container;
cd ${SYNTHSISTOOL};
poetry run python temp_container/${PROJECTNAME}.py;
)

echo "\n\`\` success! synthesis finished. \`\`"

echo "\n (hyperenforce ended.)"

# #
echo "\n(extra step:) save this file if it's a new run."
mkdir -p ${SYNTHSISTOOL}/previous_runs
mv ${SYNTHSISTOOL}/temp_container/*.py ${SYNTHSISTOOL}/previous_runs/
# rm ${SYNTHSISTOOL}/temp_container/*.py
