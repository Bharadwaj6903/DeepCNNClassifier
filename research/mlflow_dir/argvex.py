import sys
alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
args = sys.argv
print(args)
print(alpha,l1_ratio)
#cd research/mlflow_dir
#python filename.py  argv[1]  argv[2] 

#args = sys.argv
#print(args)
#output
#python argvex.py 0.5 0.5 0.7
#['argvex.py', '0.5', '0.5', '0.7']
