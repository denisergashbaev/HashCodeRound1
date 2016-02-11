from config import Config


def run():
    input_file_name = 'sample_input'
    output_file_name = input_file_name + "_output"
    config = Config(input_file_name)

    #outputting results
    with open(output_file_name, 'w') as f:
        all_drone_commands = []
        for drone in config.drones:
            all_drone_commands += drone.commands
        commands_count = str(len(all_drone_commands))
        cmds = "\n".join(all_drone_commands)
        f.write(commands_count)
        f.write(cmds)
        print commands_count
        print cmds


if __name__ == "__main__":
    run()