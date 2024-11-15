import subprocess
from decimal import Decimal

import yaml


def main():
    # Read the template catalog yaml file
    with open("rover_continuous.mcdplib/battery_catalogues/battery_catalogue_template.yaml", 'r', encoding="UTF-8") as file_stream:
        data = yaml.safe_load(file_stream)
        print(f"Template Catalogue Data schema: {data.keys()}")

        # see the first implementation of the template catalogue
        implementation_name = next(iter(data['implementations'].keys()))
        print(f"Implementation name: {implementation_name}")
        implementation = data['implementations'][implementation_name]
        print(f"Implementation: {implementation}")

        # write the implementation to the actual catalogue file
        with open("rover_continuous.mcdplib/battery_catalogues/battery_catalogue_1.yaml", 'w', encoding="UTF-8") as file_stream:
            yaml.dump(data, file_stream)

    # start the docker container
    container_id = subprocess.check_output("docker run --platform linux/amd64 -it --rm -v $PWD:$PWD -w $PWD -d zupermind/mcdp:2024 bash -l", shell=True).decode().strip()
    print(f"Container ID: {container_id}")

    # run mcdp solver for a specific query
    query = "rover_q"
    subprocess.run(f"docker exec {container_id} mcdp-solve-query {query}", shell=True, check=True)

    # read the output file and parse the results. Pay attention to which output file you are reading!
    with open("out/out-000/output.yaml", 'r', encoding="UTF-8") as file_stream:
        data = yaml.safe_load(file_stream)
        optimistic_antichain = eval(data['optimistic']['minimals'])
        print("Optimistic antichain:")
        print(optimistic_antichain)
        for resource_element in optimistic_antichain:
            print("Resource element:")
            print(resource_element)
            for single_resource in resource_element:
                print("Single resources in the resource antichain:")
                print(single_resource)
                if isinstance(single_resource, tuple):
                    print("The resource element is a Tuple (element in the product of posets)")
                    print(single_resource[0])
                    print(single_resource[1])

    # Do as many queries as you want!
    # if you want to supress the output when solving the queries, you can use the following command
    #By looking into "subprocess" of Python more carefully, you may find better solutions to supress the output.
    print("Solving the query again with suppressing the output.")
    subprocess.run(f"docker exec {container_id} mcdp-solve-query {query}", shell=True, check=True, capture_output=True)

    # stop the docker container
    subprocess.run(f"docker stop {container_id}", shell=True, check=True)

if __name__ == '__main__':
    main()
  
