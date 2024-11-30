# LangChain으로 Amazon Bedrock API 활용해보기
from langchain_aws import ChatBedrock
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate

bedrock_model_id = "anthropic.claude-3-sonnet-20240229-v1:0" #파운데이션 모델 설정
prompt = PromptTemplate.from_template("{country}에서 가장 큰 도시가 어디인가요?")

llm = ChatBedrock(
    model_id=bedrock_model_id,
    model_kwargs=dict(temperature=0),
    region_name="us-west-2"
)

print("======= OutputParser 사용 안함 =======")
input = {"country": "한국"}
chain = prompt | llm
msg = chain.invoke(input=input)
print(msg)

print("\n======= StrOutputParser 사용 =======")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
msg = chain.invoke(input=input)
print(msg)
