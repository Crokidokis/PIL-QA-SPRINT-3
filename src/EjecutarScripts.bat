echo. ##############TEST PATH #############
cd "./Tests"
python -m pytest Test_001.py Test_002.py Test_003.py --html=../Results/CocaRochaGonzalo.html --self-contained-html
pause
