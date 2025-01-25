from wandb2numpy.config_loader import load_config
from wandb2numpy.export import export_data
from wandb2numpy.save_experiment import create_output_dirs, save_matrix


if __name__=="__main__":
    # task = "Ant-v3"
    task = "Humanoid-v3"

    default_config = f"/home/lige/Codes/onur/wandb2numpy/example_configs/gym_tasks.yaml"

    list_doc = load_config(default_config)
    list_doc['experiment1']['output_path'] =f"/home/lige/Codes/onur/wandb2numpy/wandb_data/{task}"
    list_doc['experiment1']["config"]["env_name"]["values"] = [task]
    experiment_data_dict, config_list = export_data(list_doc)
    print(experiment_data_dict.keys())
    for i, experiment in enumerate(experiment_data_dict.keys()):
        experiment_dir = create_output_dirs(config_list[i], experiment)
        print(experiment_dir)

        for field in experiment_data_dict[experiment]:
            save_matrix(experiment_data_dict[experiment], experiment_dir, field, True, config_list[i])