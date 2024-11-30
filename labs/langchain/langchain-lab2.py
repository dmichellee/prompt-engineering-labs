# LangChain으로 Amazon Bedrock API 활용해보기
from langchain_aws import ChatBedrock

bedrock_model_id = "anthropic.claude-3-sonnet-20240229-v1:0" #파운데이션 모델 설정

llm = ChatBedrock(
    model_id=bedrock_model_id,
    model_kwargs=dict(temperature=0),
    region_name="us-west-2"
)
prompt = "한국에서 가장 큰 도시가 어디인가요?" #모델에 보낼 프롬프트 설정
msg = llm.invoke(input=prompt)
print(msg.content)

