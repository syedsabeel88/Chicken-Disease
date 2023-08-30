from dataclasses import dataclass
from pathlib import Path

# dataclasses are immutable, so they can't be changed
@dataclass(frozen=True) # frozen=True means that the dataclass can't be changed
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path