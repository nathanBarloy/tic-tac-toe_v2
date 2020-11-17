# tic-tac-toe_v2

This is the source code of a learning AI for the tic-tac-toe game.

## How to use it

To create the .py file equivalent to a .ui file, run this :
```batch
pyuic5 <file_name>.ui -o <file_name>.py
```

To update the translation files :
```batch
pylupdate5 <file_name>.pro
```
or if you want to specify only one file :
```batch
pylupdate5 <file_name>.py -ts <file_name>.ts
```

After the translations are done, run this to create the wanted .qm files :
```batch
lrelease <file_name>.ts
```
