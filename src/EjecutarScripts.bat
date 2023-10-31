echo. ##############TEST PATH #############
cd "./Tests"
python -m pytest test_001.py test_002.py --html=../Results/CocaRochaGonzalo.html --self-contained-html
pause
