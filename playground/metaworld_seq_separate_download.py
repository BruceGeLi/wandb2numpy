from wandb2numpy.config_loader import load_config
from wandb2numpy.export import export_data
from wandb2numpy.save_experiment import create_output_dirs, save_matrix

if __name__ == "__main__":
    default_config = "/home/lige/Codes/seq_rl/wandb2numpy/example_configs/metaworld_seq.yaml"
    env_name_list = [
        "metaworld_ProDMP_TCE/assembly-v2",
        "metaworld_ProDMP_TCE/pick-out-of-hole-v2",
        "metaworld_ProDMP_TCE/plate-slide-v2",
        "metaworld_ProDMP_TCE/plate-slide-back-v2",
        "metaworld_ProDMP_TCE/plate-slide-side-v2",
        "metaworld_ProDMP_TCE/plate-slide-back-side-v2",
        "metaworld_ProDMP_TCE/bin-picking-v2",
        "metaworld_ProDMP_TCE/hammer-v2",
        "metaworld_ProDMP_TCE/sweep-into-v2",
        "metaworld_ProDMP_TCE/box-close-v2",
        "metaworld_ProDMP_TCE/button-press-v2",
        "metaworld_ProDMP_TCE/button-press-wall-v2",
        "metaworld_ProDMP_TCE/button-press-topdown-v2",
        "metaworld_ProDMP_TCE/button-press-topdown-wall-v2",
        "metaworld_ProDMP_TCE/coffee-button-v2",
        "metaworld_ProDMP_TCE/coffee-pull-v2",
        "metaworld_ProDMP_TCE/coffee-push-v2",
        "metaworld_ProDMP_TCE/dial-turn-v2",
        "metaworld_ProDMP_TCE/disassemble-v2",
        "metaworld_ProDMP_TCE/door-close-v2",
        "metaworld_ProDMP_TCE/door-lock-v2",
        "metaworld_ProDMP_TCE/door-open-v2",
        "metaworld_ProDMP_TCE/door-unlock-v2",
        "metaworld_ProDMP_TCE/hand-insert-v2",
        "metaworld_ProDMP_TCE/drawer-close-v2",
        "metaworld_ProDMP_TCE/drawer-open-v2",
        "metaworld_ProDMP_TCE/faucet-open-v2",
        "metaworld_ProDMP_TCE/faucet-close-v2",
        "metaworld_ProDMP_TCE/handle-press-side-v2",
        "metaworld_ProDMP_TCE/handle-press-v2",
        "metaworld_ProDMP_TCE/handle-pull-side-v2",
        "metaworld_ProDMP_TCE/handle-pull-v2",
        "metaworld_ProDMP_TCE/lever-pull-v2",
        "metaworld_ProDMP_TCE/peg-insert-side-v2",
        "metaworld_ProDMP_TCE/pick-place-wall-v2",
        "metaworld_ProDMP_TCE/reach-v2",
        "metaworld_ProDMP_TCE/push-back-v2",
        "metaworld_ProDMP_TCE/push-v2",
        "metaworld_ProDMP_TCE/pick-place-v2",
        "metaworld_ProDMP_TCE/peg-unplug-side-v2",
        "metaworld_ProDMP_TCE/soccer-v2",
        "metaworld_ProDMP_TCE/stick-push-v2",
        "metaworld_ProDMP_TCE/stick-pull-v2",
        "metaworld_ProDMP_TCE/push-wall-v2",
        "metaworld_ProDMP_TCE/reach-wall-v2",
        "metaworld_ProDMP_TCE/shelf-place-v2",
        "metaworld_ProDMP_TCE/sweep-v2",
        "metaworld_ProDMP_TCE/window-open-v2",
        "metaworld_ProDMP_TCE/window-close-v2",
        "metaworld_ProDMP_TCE/basketball-v2"
    ]

    list_doc = load_config(default_config)
    root_output_path = list_doc['experiment1']['output_path']
    for env_name in env_name_list:
        list_doc['experiment1']['config']['sampler.args.env_id']['values'][
            0] = env_name
        list_doc['experiment1'][
            'output_path'] = root_output_path + "/" + env_name
        experiment_data_dict, config_list = export_data(list_doc)
        for i, experiment in enumerate(experiment_data_dict.keys()):
            experiment_dir = create_output_dirs(config_list[i], experiment)
            print(experiment_dir)

            for field in experiment_data_dict[experiment]:
                save_matrix(experiment_data_dict[experiment], experiment_dir,
                            field, True, config_list[i])
