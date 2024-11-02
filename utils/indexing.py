from llama_index.core import SummaryIndex
# from .chunking import Chunker


class Indexer:
    def __init__(self) -> None:
        pass

    def index(self, nodes):
        return SummaryIndex(nodes)

        