from ...config.config_loader import load_config, AppConfig
import pandas as pd

def load_data(data_config: DataConfig) -> pd.DataFrame:
    """Load data from the specified file path in the configuration.

    Args:
        data_config (DataConfig): The data configuration with file paths.

    Returns:
        pd.DataFrame: The loaded dataset.
    """
    if data_config.csv_path:
        return pd.read_csv(data_config.csv_path)
    elif data_config.json_path:
        return pd.read_json(data_config.json_path)
    elif data_config.parquet_path:
        return pd.read_parquet(data_config.parquet_path)
    else:
        raise ValueError("No valid data path configuration found.")

def main():
    config = load_config('config.yaml')
    # Example of loading data based on the configuration
    data = load_data(config.data)
    print(data.head())

if __name__ == "__main__":
    main()
