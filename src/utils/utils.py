from pathlib import Path


class Root:

    @staticmethod
    def get_project_root():
        return str(Path(__file__).parent.parent.parent)