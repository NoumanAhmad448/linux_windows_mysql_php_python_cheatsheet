<h1 align='center' style='color: green' >Python Cheatsheet</h1>                                                                                                     

## Huggingface
1. Enable large files <br/>
   Verify?
   ```
   git lfs version
   ```
   Install?
   ```
   git lfs install
   ```
   Enabling
   ```
   huggingface-cli lfs-enable-largefiles .
   ```
2. 
## Docker
1. Copy file(s)
   ```
   docker cp b4a34cd339de://app/saves/Llama-7B/lora/train_2024-11-16-12-13-34/training_loss.png D:\
   ```
2. show container
   ```
   docker ps -a
   ```

## Conda
### Enlist installed packages in the Env 
1. listing packages
   ```
   conda list
   ```
3. To list specific pkg
   ```
   conda list pkg_name
   ```

### Conda Activate/Deactivate Env
1. Open Anaconda Powershell Prompt 
2. Run
   ```
   Conda init bash
   ```
4. To activate
   ```
   conda activate env_name
   ```
6. To deactivate
   ```
   conda deactivate
   ```

### Conda Create Environment - CMD
1. To create
   ```
   conda create -n yourenvname python=x.x anaconda
   ```
3. To activate
   ```
   source activate yourenvname
   ```
5. pure pip deactivate
   ```
   source deactivate
   ```
6. To install
   ```
   conda install pkg_name
   ```

### Conda Create Environment - Manual
1. Go to Anaconda Navigator and Create An Env 
2. Go to Pycharm Setting and Search Interpreter
3. Choose Create new Interpreter
4. Select your Env 
5. on Main page, choose edit config
6. select your path 

### Conda change the python version 
1. Install python in conda
   ```
   conda install python=3.10
   ```

## PIP Cheatsheet 
1. pip list
   ```
   pip list
   ```
2. pip uninstall pkg_name
   ```
   pip uninstall pkg_name
   ```
3. pip show/list 【one specific installed package detail 】
   ```
   pip show pkg_name
   ```

### pip create packages file
1. pip freeze > requirements.txt
   ```
   pip freeze > requirements.txt
   ```
2. pip install -r requirements.txt
   ```
   pip install -r requirements.txt
   ```


## Nvidia 
1. Verify num of ```GPU```, their ```RAM``` , ```temp```
   ```
   nvidia-smi
   ```
3. Verify version
   ```
   !nvcc --version
   ```

## Git
1. Git show commits
   ```
   git log --oneline
   ```

2. git rebase/merge commit before push
   ```
   git reset HEAD~3
   ```
3. git merge after push
   ```
   git rebase -I HEAD~3
   ```
4. git delete all current changes before commit 
   ```
   git restore file_name
   ```
<BR/> follow the window and replace pick with ```squash``` and leave the first          ```pick``` work as it is

## Installation from Github
1. install mscoco python api
```!pip install git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI```
2. 
