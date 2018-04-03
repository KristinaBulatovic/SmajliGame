import cx_Freeze

executables = [cx_Freeze.Executable("SmajliGame.py")]

cx_Freeze.setup(
    name = "Smajli Game",
    options = {"build_exe": {"packages":["pygame"],
                             "include_files": ["smajli.png","smajli1.png","A_Long_Cold.mp3","Crash.mp3","srce.png","high_score.txt"],}},
    executables = executables

    )
