from llama_index.core import Document
from llama_index.core.node_parser import TokenTextSplitter


class Chunker:
    def __init__(self) -> None:
        pass

    def chunk(self, text: str):
        doc = Document(text=text)
        splitter = TokenTextSplitter(
            chunk_size=512,
            chunk_overlap=128,
            separator= "\n"
        )
        return splitter.get_nodes_from_documents([doc])
        