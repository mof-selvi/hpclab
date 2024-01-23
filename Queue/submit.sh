#!/bin/bash
#
# CompecTA (c) 2018
#
#
# TODO:
#   - Set name of the job below changing "Keras" value.
#   - Set the requested number of tasks (cpu cores) with --ntasks parameter.
#   - Put this script and all the input file under the same directory.
#   - Set the required parameters, input and output file names below.
#   - If you do not want mail please remove the line that has --mail-type
#   - Put this script and all the input file under the same directory.
#   - Submit this file using:
#      sbatch keras_pulsar_submit.sh
#
# -= Resources =-
#
#SBATCH --job-name=MofDeep
#SBATCH --ntasks=1
#SBATCH --gres=gpu:2
#SBATCH --partition=longer
#SBATCH --output=./%j-deep.out

# #SBATCH --mail-user=your_mail@foo.com

################################################################################
#source /etc/profile.d/lmod.sh
################################################################################

# MODULES LOAD...
echo "Load Anaconda-3..."
module load anaconda/3

# conda init bash
# conda activate myenv
conda activate myenv
echo "Environment activated..."

################################################################################

echo ""
echo "============================== ENVIRONMENT VARIABLES ==============================="
env
echo "===================================================================================="
echo ""
echo ""

echo "Running Keras-Tensorflow command..."
echo "===================================================================================="
RET=$?

/cta/users/mselvi/.conda/envs/myenv/bin/python run.py
RET=$?

echo ""
echo "===================================================================================="
echo "Solver exited with return code: $RET"
exit $RET
