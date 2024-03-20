import os 
import mlflow 
import argparse 
import time 




def eval(p1, p2):
    output_metric = p1**2 + p2**2
    return output_metric

def main(inp1, inp2):
    mlflow.set_experiment("Demo_Experiment_Example")
    # with mlflow.start_run(run_name='Demo Run Example'):
    with mlflow.start_run():
        mlflow.set_tag('version','0.0.5')
        mlflow.log_param('param1', inp1)
        mlflow.log_param('param2', inp2)
        metric = eval(p1 = inp1, p2 = inp2)
        mlflow.log_metric("Eval_metric", metric)
        os.makedirs("mlfolder", exist_ok=True)
        with open("mlfolder/example.txt", "wt") as f:
            f.write(f"Artifact created at {time.asctime()}")
        mlflow.log_artifacts("mlfolder")





if __name__ == '__main__' :
    args = argparse.ArgumentParser()
    args.add_argument("--param1","-p1", type=int, default=5)
    args.add_argument("--param2","-p2", type=int, default=10)
    parsed_args = args.parse_args()
    
    main(parsed_args.param1, parsed_args.param2)