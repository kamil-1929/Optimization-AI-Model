# Production Optimization

This project aims to optimize the production schedule for a factory that manufactures five different products (P1, P2, P3, P4, P5). Each product requires different amounts of three resources: labor, machine time, and raw materials. The goal is to maximize the total profit while considering the constraints related to resource availability and production capacities.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [License](#license)

## Installation

### Using `requirements.txt`
1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
2. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Using `environment.yml`
1. Create and activate the environment using conda:
    ```sh
    conda env create -f environment.yml
    conda activate production-optimization
    ```

## Usage

To run the optimization script:
```sh
python -m production_optimization.main
```

## Testing
To run the tests, use:
```sh
pytest
```
## License
This project is licensed under the MIT License - see the LICENSE file for details.
