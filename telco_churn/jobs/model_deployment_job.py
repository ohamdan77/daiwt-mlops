from telco_churn.common import Job
from telco_churn.model_deployment import ModelDeployment


class ModelDeploymentJob(Job):

    def launch(self):
        ModelDeployment(mlflow_params=self.conf['mlflow_params'],
                        reference_data=self.conf['data_input']['table_name'],
                        label_col=self.conf['data_input']['label_col'],
                        comparison_metric=self.conf['model_comparison_params']['metric'],
                        higher_is_better=self.conf['model_comparison_params']['higher_is_better']).run()


if __name__ == "__main__":
    job = ModelDeploymentJob()
    job.launch()