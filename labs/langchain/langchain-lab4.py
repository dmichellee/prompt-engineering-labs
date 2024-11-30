# LangChain이 제공하는 라이브러리로 PDF 파일을 로드해서 청킹해보기
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyMuPDFLoader("../../files/lpoint.pdf")
pages = loader.load_and_split()

# Split
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)
texts = text_splitter.split_documents(pages)

print(texts[9])
