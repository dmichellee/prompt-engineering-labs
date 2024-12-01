import boto3

def read_file(file_name):
    with open(file_name, "r") as f:
        text = f.read()
     
    return text


def get_context_list():
    return ["Prompt engineering 기초", "요약", "질의응답", "번역", "감정 분석", "코딩"]


def get_context(lab):
    if lab == "Prompt engineering 기초":
        return read_file("data/basics.txt")
    if lab == "요약":
        return read_file("data/summarization_content.txt")
    elif lab == "질의응답":
        return read_file("data/qa.txt")
    elif lab == "리뷰 분석":
        return read_file("data/review_analysis.txt")
    elif lab == "번역":
        return read_file("data/qa.txt")
    elif lab == "Prompt 최적화":
        return ""


def get_prompt(template, context=None):
    
    if "{context}" not in template:
        prompt = template
    else:
        prompt = template.format(context=context)
    
    return prompt


def get_text_response(model_id, temperature, system_prompt, user_prompt, context=None):

    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')

    prompt = get_prompt(user_prompt, context)
    
    message = {
        "role": "user",
        "content": [ 
            # { "text": "Image:" },
            # {
            #     "image": {
            #         "format": file_format,
            #         "source": {
            #             "bytes": file_content
            #         }
            #     }
            # },
            { "text": prompt } 
        ]
    }
    
    response = bedrock.converse(
        modelId=model_id,
        system=[{"text": system_prompt}],
        messages=[message],
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": temperature,
            "topP": 0.9,
            "stopSequences": []
        },
    )
    
    return response['output']['message']['content'][0]['text']
