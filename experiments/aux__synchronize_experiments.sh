#! /usr/bin/env bash

set -x
set -o pipefail

rm -fr exp2* exp3* exp4* exp5*

./aux__duplicate_experiment.py exp1 exp2
rename 's/Borrelia/Tuberculosis/' exp2.*

./aux__duplicate_experiment.py exp1 exp3
rename 's/Borrelia/Meningitidis/' exp3.*

./aux__duplicate_experiment.py exp1 exp4
rename 's/Borrelia/Solibacter/' exp4.*
