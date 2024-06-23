# Production Optimization Project

This project is designed to optimize the production schedule for a factory that manufactures five different products (P1, P2, P3, P4, and P5). The goal is to maximize the total profit while considering the constraints related to resource availability and production capacities.

## Structure

- **production_optimization**: Contains the main code for the optimization model.
- **tests**: Contains unit tests for the optimization model.
- **docs**: Documentation files including this README and the user guide.
- **.github/workflows**: GitHub Actions workflow files for CI/CD.
- **environment.yml**: Conda environment configuration.
- **requirements.txt**: Python package dependencies.
- **setup.py**: Setup script for installing the package.

## Getting Started

### Prerequisites

- Python 3.10
- Conda (optional)

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/Assignment_AIDDM.git
    cd Assignment_AIDDM
    ```

2. **Create a virtual environment**:

    Using Conda:

    ```sh
    conda env create -f environment.yml
    conda activate production_optimization_env
    ```

    Using pip:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Run the optimization**:

    ```sh
    python -m production_optimization.main
    ```

4. **Run the tests**:

    ```sh
    pytest
    ```

## Usage

For detailed usage instructions, refer to the [User Guide](user_guide.md).
