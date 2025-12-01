# hpclab
This repo is a document that shows how to run Python codes in an HPC Lab under Slurm.

There are 2 ways to run a Python code in a Slurm-based HPC Lab. Either put your script to the queue, or connect to a node and run it directly.

## Putting a script to the process queue ( [files](Queue) )
- Let's say, you have a file named "run.py".
- Then run [submit.sh](Queue/submit.sh) file:
  ```
  ./submit.sh
  ```
- This will queue your file (run.py) to process.
- When done, you fill find a file with a name like "1234-deep.out" in the working directory.
- To change gpu numbers, log file name etc., edit "submit.sh" file.

## Running a script directly ( [files](Straight) )
- If you need to run a .py file directly on Terminal, connect to one of the nodes:
  ```
  srun -p short -N1 -n1 --gres=gpu:1 --job-name=job01 --pty bash
  ```
  or a specific node:
  
  ```
  srun -p short -N1 -n1 --gres=gpu:1 --job-name=job02 --nodelist=ne02 --pty bash
  ```
  You can change the number of the GPU's by setting "--gres" parameter to something like "gpu:2".
- You were working under login previously:
  "(base) mselvi@login:~$"
- Now, you are working under one of the nodes:
  "(base) mselvi@ne03:~$"
  Note that the node name may differ time to time. You will be automatically logged in whichever of the nodes is available. It can be "ne02" or "ne01", depending on the busyness.
- Let's say you want to run "txt2img.py".
- You can now run this script using Python installed in a specific environment. Just choose one:

### activating the Anaconda environment
- First, activate conda module for Slurm:
  ```
  module load anaconda/3
  ```
- Then, activate your conda environment:
  ```
  conda activate myenv
  ```
- Run the script.
  ```
  python txt2img.py
  ```

### using the Anaconda environment path
- Find your python location and copy its path and type the name of the script file.
  ```
  /cta/users/mselvi/.conda/envs/myenv/bin/python txt2img.py
  ```
  Notice that you should have your own username in the Python path.

