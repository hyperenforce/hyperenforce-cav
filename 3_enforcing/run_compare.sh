#!/bin/bash

PROJECTNAME="implicit1"
# PROJECTNAME="implicit2"
# PROJECTNAME="login_ni"
# PROJECTNAME="gps_dni"
# PROJECTNAME="gps_dninf"
# PROJECTNAME="printer_ci"
# PROJECTNAME="m-log_ci"



ENFORCER="hyperenforce_cases/${PROJECTNAME}/${PROJECTNAME}_enforcer.js"
# ENFORCEDJS="hyperenforce_cases/${PROJECTNAME}/${PROJECTNAME}_enforced.js"
COMPAREJS="hyperenforce_cases/${PROJECTNAME}/${PROJECTNAME}_enforced_compare.js"
# ORIGINALJS="hyperenforce_cases/${PROJECTNAME}/${PROJECTNAME}.js"
# ENFORCEDOUT="hyperenforce_cases/${PROJECTNAME}/${PROJECTNAME}_out.txt"

# touch ${ENFORCEDOUT}

echo -e "(start running ${COMPAREJS}.)"

node src/js/commands/jalangi.js --inlineIID --inlineSource --analysis ${ENFORCER} ${COMPAREJS}

echo -e "(finished.)\n"
